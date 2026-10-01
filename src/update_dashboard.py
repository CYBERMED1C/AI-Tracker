#!/usr/bin/env python3
"""Build the AI Security Intelligence dashboard in README.md.

The collector intentionally uses public, read-only endpoints and the Python
standard library. A failed source is reported and its last successful section
is retained from data/dashboard.json.
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA_FILE = ROOT / "data" / "dashboard.json"
USER_AGENT = "AI-Security-Intel-Dashboard/1.0 (+https://github.com/)"
TIMEOUT_SECONDS = 25

AI_TERMS = (
    "artificial intelligence", "machine learning", "generative ai", "llm",
    "pytorch", "tensorflow", "transformers", "hugging face", "langchain",
    "llamaindex", "vllm", "ollama", "mlflow", "kubeflow", "jupyter",
    "ray", "openai", "anthropic", "gemini", "llama", "mistral",
    "model serving", "prompt injection", "model poisoning",
)

MODEL_TERMS = (
    "gpt", "codex", "claude", "gemini", "gemma", "llama", "muse", "mistral",
    "mixtral", "deepseek", "grok", "phi", "command r", "nova", "qwen",
)

MODEL_RELEASE_TERMS = (
    "launch", "release", "introduc", "available", "preview", "upgrade",
    "update", "system card", "model card",
)

MODEL_STORY_EXCLUSIONS = (
    "adopts", "access to", "built with", "customer", "how ", "partner",
    "powered by", "using ", "uses ", "widens access", "with openai",
)

SECURITY_NEWS_TERMS = (
    "advisory", "alignment", "attack", "cyber", "defen", "eval", "exploit",
    "governance", "incident", "misuse", "risk", "safeguard", "safety",
    "secure", "security", "standard", "threat", "vulnerab",
)

ECHELON_ENDPOINT = "https://app.echelongraph.io/api/v1/public/cves"
CISA_KEV_ENDPOINT = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)
GITHUB_ADVISORIES_ENDPOINT = "https://api.github.com/advisories"
AI_GOV_URL = "https://www.ai.gov/"

FEEDS = (
    ("OpenAI", "https://openai.com/news/rss.xml", "model"),
    ("Anthropic", "https://www.anthropic.com/news", "model-anthropic-html"),
    ("Google DeepMind", "https://blog.google/rss/", "model"),
    ("Meta AI", "https://ai.meta.com/blog/", "model-html"),
    ("Microsoft AI", "https://blogs.microsoft.com/feed/", "news"),
    ("NIST", "https://www.nist.gov/news-events/cybersecurity/rss.xml", "news"),
    ("ModelScan", "https://github.com/protectai/modelscan/releases.atom", "project"),
    ("garak", "https://github.com/NVIDIA/garak/releases.atom", "project"),
    ("Fickling", "https://github.com/trailofbits/fickling/releases.atom", "project"),
)


@dataclass
class FetchResult:
    name: str
    ok: bool
    detail: str


def fetch(url: str, *, accept: str = "application/json, application/xml, text/html;q=0.9") -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": accept},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.read()


def fetch_json(url: str) -> Any:
    return json.loads(fetch(url, accept="application/json").decode("utf-8"))


def clean_text(value: Any, limit: int = 240) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", str(value or "")))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def headline(value: Any, limit: int = 150) -> str:
    text = clean_text(value, 1000)
    sentence = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)[0]
    return clean_text(sentence, limit).rstrip(".")


def md_escape(value: Any) -> str:
    return clean_text(value).replace("|", "\\|").replace("\n", " ")


def parse_date(value: Any) -> str:
    raw = clean_text(value, 80)
    if not raw:
        return "Unknown"
    raw = raw.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(raw).date().isoformat()
    except ValueError:
        pass
    try:
        parsed = email.utils.parsedate_to_datetime(raw)
        if parsed is not None:
            return parsed.date().isoformat()
    except (TypeError, ValueError, OverflowError):
        pass
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d", "%m/%d/%Y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    match = re.search(r"(20\d{2})[-/](\d{1,2})[-/](\d{1,2})", raw)
    return f"{match.group(1)}-{int(match.group(2)):02d}-{int(match.group(3)):02d}" if match else raw


def is_ai_related(*values: Any) -> bool:
    haystack = " ".join(clean_text(v, 4000).lower() for v in values)
    return any(re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", haystack) for term in AI_TERMS)


def contains_term(text: str, terms: Iterable[str]) -> bool:
    return any(re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) for term in terms)


def item_date(item: dict[str, Any]) -> str:
    value = str(item.get("date") or "")
    return value if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", value) else "0000-00-00"


def dedupe(items: Iterable[dict[str, Any]], key: str = "url") -> list[dict[str, Any]]:
    seen: set[str] = set()
    result = []
    for item in sorted(items, key=item_date, reverse=True):
        marker = clean_text(item.get(key) or item.get("title")).lower()
        if marker and marker not in seen:
            seen.add(marker)
            result.append(item)
    return result


def take_diverse(items: Iterable[dict[str, Any]], limit: int = 5, per_source: int = 2) -> list[dict[str, Any]]:
    counts: dict[str, int] = {}
    selected = []
    for item in dedupe(items):
        source = str(item.get("source") or "Unknown")
        if counts.get(source, 0) >= per_source:
            continue
        counts[source] = counts.get(source, 0) + 1
        selected.append(item)
        if len(selected) == limit:
            break
    return selected


def advisory_score(item: dict[str, Any]) -> float:
    score = float(item.get("risk") or 0)
    if not score:
        score = float(item.get("cvss") or 0) * 8
    if item.get("kev"):
        score += 25
    if item.get("exploit"):
        score += 10
    return min(score, 100)


def normalize_echelon(row: dict[str, Any]) -> dict[str, Any]:
    cve = row.get("cve_id") or row.get("id") or "Unassigned"
    description = row.get("description") or row.get("summary") or row.get("title") or "No summary supplied."
    severity = row.get("echelongraph_severity") or row.get("severity") or row.get("cvss_v3_severity") or "UNSCORED"
    cvss = row.get("echelongraph_score") or row.get("cvss_v4_score") or row.get("cvss_v3_score") or row.get("cvss_v2_score") or 0
    return {
        "id": cve,
        "title": f"{cve}: {headline(description)}",
        "summary": clean_text(description, 260),
        "severity": str(severity).upper(),
        "cvss": cvss,
        "risk": row.get("echelongraph_risk") or 0,
        "kev": bool(row.get("kev") or row.get("is_kev") or row.get("cisa_kev") or row.get("kev_listed")),
        "exploit": bool(row.get("exploit_poc_available")),
        "date": parse_date(row.get("published") or row.get("published_date") or row.get("modified")),
        "source": "EchelonGraph",
        "url": f"https://echelongraph.io/pulse/{urllib.parse.quote(str(cve))}",
    }


def collect_echelon() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    # Search individual ecosystem terms because the public API documents a
    # single full-text search expression, not OR syntax.
    for term in ("pytorch", "tensorflow", "transformers", "langchain", "llamaindex", "vllm", "ollama", "mlflow", "jupyter", "machine learning"):
        query = urllib.parse.urlencode({"search": term, "limit": 20, "sort": "published", "skip_count": 1})
        payload = fetch_json(f"{ECHELON_ENDPOINT}?{query}")
        candidates = payload.get("cves", payload if isinstance(payload, list) else [])
        rows.extend(normalize_echelon(row) for row in candidates if isinstance(row, dict))
    return dedupe(rows, "id")


def collect_cisa_kev() -> list[dict[str, Any]]:
    payload = fetch_json(CISA_KEV_ENDPOINT)
    result = []
    for row in payload.get("vulnerabilities", []):
        if not is_ai_related(row.get("vendorProject"), row.get("product"), row.get("vulnerabilityName"), row.get("shortDescription")):
            continue
        cve = row.get("cveID", "Unassigned")
        result.append({
            "id": cve,
            "title": f"{cve}: {clean_text(row.get('vulnerabilityName'), 135)}",
            "summary": clean_text(row.get("shortDescription"), 260),
            "severity": "KNOWN EXPLOITED",
            "cvss": 0,
            "risk": 100,
            "kev": True,
            "exploit": True,
            "date": parse_date(row.get("dateAdded")),
            "source": "CISA KEV",
            "url": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
        })
    return result


def collect_github_advisories() -> list[dict[str, Any]]:
    query = urllib.parse.urlencode({"per_page": 100, "type": "reviewed", "sort": "published", "direction": "desc"})
    payload = fetch_json(f"{GITHUB_ADVISORIES_ENDPOINT}?{query}")
    result = []
    for row in payload if isinstance(payload, list) else []:
        if not is_ai_related(row.get("summary"), row.get("description"), row.get("vulnerabilities")):
            continue
        ghsa = row.get("ghsa_id", "GitHub advisory")
        cvss = (row.get("cvss") or {}).get("score") or 0
        result.append({
            "id": ghsa,
            "title": f"{ghsa}: {clean_text(row.get('summary'), 135)}",
            "summary": clean_text(row.get("description") or row.get("summary"), 260),
            "severity": str(row.get("severity") or "UNSCORED").upper(),
            "cvss": cvss,
            "risk": float(cvss) * 8,
            "kev": False,
            "exploit": False,
            "date": parse_date(row.get("published_at")),
            "source": "GitHub Advisory Database",
            "url": row.get("html_url") or f"https://github.com/advisories/{ghsa}",
        })
    return result


def collect_advisories() -> tuple[list[dict[str, Any]], list[FetchResult]]:
    all_items: list[dict[str, Any]] = []
    health: list[FetchResult] = []
    for name, collector in (
        ("EchelonGraph", collect_echelon),
        ("CISA KEV", collect_cisa_kev),
        ("GitHub Advisories", collect_github_advisories),
    ):
        try:
            items = collector()
            all_items.extend(items)
            health.append(FetchResult(name, True, f"{len(items)} AI-related records"))
        except Exception as exc:  # a single upstream must not abort the dashboard
            health.append(FetchResult(name, False, clean_text(exc, 100)))
    ranked = sorted(dedupe(all_items, "id"), key=lambda i: (advisory_score(i), item_date(i)), reverse=True)
    return ranked[:5], health


def collect_ai_gov_orders() -> list[dict[str, Any]]:
    page = fetch(AI_GOV_URL, accept="text/html").decode("utf-8", errors="replace")
    # AI.gov renders the relevant cards in source order. Scope extraction to
    # the Executive Orders block so fact sheets do not leak into this list.
    matches = list(re.finditer(r"Executive Orders(?P<body>.*?)(?:Fact Sheets|Remarks)", page, flags=re.I | re.S))
    # Webflow may emit tab labels before the actual card collection. Choose the
    # candidate containing the most date-stamped content rather than the first.
    body = max((match.group("body") for match in matches), key=lambda value: len(re.findall(r"\d{1,2}/\d{1,2}/20\d{2}", value)), default=page)
    anchors = re.findall(r"<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", body, flags=re.I | re.S)
    orders = []
    for url, label in anchors:
        title = clean_text(label, 220)
        date_match = re.search(r"\b(\d{1,2}/\d{1,2}/20\d{2})\b", title)
        if not date_match or not title:
            continue
        title = re.sub(r"\s*\|\s*\d{1,2}/\d{1,2}/20\d{2}\s*$", "", title).strip()
        orders.append({"title": title, "date": parse_date(date_match.group(1)), "url": urllib.parse.urljoin(AI_GOV_URL, html.unescape(url)), "source": "AI.gov"})
    return dedupe(orders)[:3]


def xml_local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(node: ET.Element, names: set[str]) -> str:
    for child in node.iter():
        if xml_local(child.tag) in names and child.text:
            return child.text.strip()
    return ""


def parse_feed(content: bytes, source: str, category: str) -> list[dict[str, Any]]:
    root = ET.fromstring(content)
    nodes = [node for node in root.iter() if xml_local(node.tag) in {"item", "entry"}]
    result = []
    for node in nodes[:30]:
        title = child_text(node, {"title"})
        summary = child_text(node, {"description", "summary", "content"})
        date = child_text(node, {"pubdate", "published", "updated", "date"})
        url = child_text(node, {"link"})
        if not url:
            link_node = next((n for n in node.iter() if xml_local(n.tag) == "link" and n.attrib.get("href")), None)
            url = link_node.attrib.get("href", "") if link_node is not None else ""
        if title and url:
            result.append({"title": clean_text(title, 180), "summary": clean_text(summary, 240), "date": parse_date(date), "url": url, "source": source, "category": category})
    return result


def parse_sitemap(content: bytes, source: str, category: str) -> list[dict[str, Any]]:
    root = ET.fromstring(content)
    result = []
    for node in root.iter():
        if xml_local(node.tag) != "url":
            continue
        url = child_text(node, {"loc"})
        slug = urllib.parse.urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]
        slug_text = re.sub(r"[-_]", " ", slug).lower()
        is_model_page = contains_term(slug_text, MODEL_TERMS)
        if "/news/" not in url and not is_model_page:
            continue
        title = re.sub(r"[-_]", " ", slug).strip().title()
        date = child_text(node, {"lastmod"})
        result.append({"title": title, "summary": "Official announcement; open the source for release details.", "date": parse_date(date), "url": url, "source": source, "category": category})
    return sorted(result, key=item_date, reverse=True)[:100]


def parse_meta_html(content: bytes, source: str, category: str) -> list[dict[str, Any]]:
    page = content.decode("utf-8", errors="replace")
    pattern = re.compile(
        r'<a\b[^>]*href=["\'](?P<url>https://ai\.meta\.com/blog/[^"\']+)["\'][^>]*>'
        r'(?P<title>.*?)</a>(?P<after>.{0,1200})',
        flags=re.I | re.S,
    )
    result = []
    for match in pattern.finditer(page):
        title = clean_text(match.group("title"), 180)
        if not title or title.lower() in {"featured", "learn more"}:
            continue
        date_match = re.search(
            r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
            r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
            r"Dec(?:ember)?)\s+\d{1,2},\s+20\d{2}\b",
            clean_text(match.group("after"), 1200),
            flags=re.I,
        )
        result.append({
            "title": title,
            "summary": "Official Meta AI announcement; open the source for release details.",
            "date": parse_date(date_match.group(0)) if date_match else "Unknown",
            "url": html.unescape(match.group("url")),
            "source": source,
            "category": category,
        })
    return dedupe(result)


def parse_anthropic_html(content: bytes, source: str, category: str) -> list[dict[str, Any]]:
    page = content.decode("utf-8", errors="replace")
    result = []
    for match in re.finditer(
        r'<a\b[^>]*href=["\'](?P<url>[^"\']+)["\'][^>]*>(?P<body>.*?)</a>',
        page,
        flags=re.I | re.S,
    ):
        body = match.group("body")
        title_match = re.search(r"<h[1-6]\b[^>]*>(?P<title>.*?)</h[1-6]>", body, flags=re.I | re.S)
        date_match = re.search(r"<time\b[^>]*>(?P<date>.*?)</time>", body, flags=re.I | re.S)
        if not title_match or not date_match:
            continue
        summary_match = re.search(r"<p\b[^>]*>(?P<summary>.*?)</p>", body, flags=re.I | re.S)
        result.append({
            "title": clean_text(title_match.group("title"), 180),
            "summary": clean_text(summary_match.group("summary"), 240) if summary_match else "Official Anthropic announcement.",
            "date": parse_date(clean_text(date_match.group("date"), 80)),
            "url": urllib.parse.urljoin("https://www.anthropic.com/news", html.unescape(match.group("url"))),
            "source": source,
            "category": category,
        })
    return dedupe(result)


def collect_feeds() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[FetchResult]]:
    model_updates: list[dict[str, Any]] = []
    news_projects: list[dict[str, Any]] = []
    health: list[FetchResult] = []
    for name, url, category in FEEDS:
        try:
            content = fetch(url, accept="application/atom+xml, application/rss+xml, application/xml, text/html;q=0.8")
            if category.endswith("sitemap"):
                items = parse_sitemap(content, name, category)
            elif category.endswith("anthropic-html"):
                items = parse_anthropic_html(content, name, category)
            elif category.endswith("html"):
                items = parse_meta_html(content, name, category)
            else:
                items = parse_feed(content, name, category)
            if category.startswith("model"):
                for item in items:
                    title = item["title"].lower()
                    text = f"{title} {item['summary']}".lower()
                    has_model = contains_term(title, MODEL_TERMS)
                    has_release_shape = (
                        any(term in title for term in MODEL_RELEASE_TERMS)
                        or bool(re.match(r"^(?:claude|gpt|gemini|gemma|llama|muse|mistral|mixtral|deepseek|grok|phi|command r|nova|qwen)\b.*\b\d", title))
                    )
                    is_customer_story = any(term in title for term in MODEL_STORY_EXCLUSIONS)
                    if has_model and has_release_shape and not is_customer_story:
                        model_updates.append(item)
                    elif is_ai_related(text) and any(term in text for term in SECURITY_NEWS_TERMS):
                        news_projects.append(item)
            elif category == "news":
                news_projects.extend(
                    item for item in items
                    if is_ai_related(item["title"], item["summary"])
                    and any(term in f"{item['title']} {item['summary']}".lower() for term in SECURITY_NEWS_TERMS)
                )
            else:
                news_projects.extend(items)
            health.append(FetchResult(name, True, f"{len(items)} feed entries"))
        except Exception as exc:
            health.append(FetchResult(name, False, clean_text(exc, 100)))
    return take_diverse(model_updates), take_diverse(news_projects, per_source=1), health


def load_previous() -> dict[str, Any]:
    if not DATA_FILE.exists():
        return {}
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def retain_if_empty(new: list[dict[str, Any]], previous: dict[str, Any], key: str) -> list[dict[str, Any]]:
    return new or list(previous.get(key) or [])


def render_table(items: list[dict[str, Any]], columns: list[tuple[str, str]]) -> str:
    if not items:
        return "_No matching items were available from healthy sources in this run._"
    header = "| " + " | ".join(label for label, _ in columns) + " |"
    rule = "| " + " | ".join("---" for _ in columns) + " |"
    rows = []
    for item in items:
        cells = []
        for _, key in columns:
            if key == "linked_title":
                value = f"[{md_escape(item.get('title'))}]({item.get('url')})"
            elif key == "score":
                risk = advisory_score(item)
                value = f"{risk:.0f}/100"
            else:
                value = md_escape(item.get(key, ""))
            cells.append(value)
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, rule, *rows])


def replace_section(readme: str, name: str, content: str) -> str:
    start = f"<!-- dashboard:{name}:start -->"
    end = f"<!-- dashboard:{name}:end -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    replacement = f"{start}\n{content.rstrip()}\n{end}"
    if not pattern.search(readme):
        raise ValueError(f"README marker pair missing: {name}")
    return pattern.sub(lambda _: replacement, readme)


def render_readme(data: dict[str, Any]) -> str:
    readme = README.read_text(encoding="utf-8")
    advisories = render_table(data["advisories"], [
        ("Priority", "score"), ("Advisory", "linked_title"), ("Severity", "severity"),
        ("Published", "date"), ("Source", "source"),
    ])
    orders = render_table(data["executive_orders"], [
        ("Executive order", "linked_title"), ("Date", "date"), ("Source", "source"),
    ])
    models = render_table(data["model_updates"], [
        ("Major model update", "linked_title"), ("What changed", "summary"),
        ("Date", "date"), ("Official source", "source"),
    ])
    news = render_table(data["news_projects"], [
        ("News / project", "linked_title"), ("Why it matters", "summary"),
        ("Date", "date"), ("Source", "source"),
    ])
    health_lines = []
    for item in data["source_health"]:
        icon = "✅" if item["ok"] else "⚠️"
        health_lines.append(f"- {icon} **{md_escape(item['name'])}** — {md_escape(item['detail'])}")
    readme = replace_section(readme, "updated", f"**Last refreshed:** {data['generated_at']} (America/Los_Angeles) · **Next scheduled refresh:** 10:00 a.m. Pacific")
    readme = replace_section(readme, "advisories", advisories)
    readme = replace_section(readme, "orders", orders)
    readme = replace_section(readme, "models", models)
    readme = replace_section(readme, "news", news)
    readme = replace_section(readme, "health", "\n".join(health_lines))
    return readme


def build_dashboard(now: datetime | None = None) -> dict[str, Any]:
    previous = load_previous()
    advisories, advisory_health = collect_advisories()
    health = advisory_health
    try:
        orders = collect_ai_gov_orders()
        health.append(FetchResult("AI.gov", True, f"{len(orders)} executive orders"))
    except Exception as exc:
        orders = []
        health.append(FetchResult("AI.gov", False, clean_text(exc, 100)))
    models, news, feed_health = collect_feeds()
    health.extend(feed_health)
    instant = now or datetime.now().astimezone()
    return {
        "schema_version": 1,
        "generated_at": instant.isoformat(timespec="seconds"),
        "advisories": retain_if_empty(advisories, previous, "advisories"),
        "executive_orders": retain_if_empty(orders, previous, "executive_orders"),
        "model_updates": retain_if_empty(models, previous, "model_updates"),
        "news_projects": retain_if_empty(news, previous, "news_projects"),
        "source_health": [result.__dict__ for result in health],
    }


def write_outputs(data: dict[str, Any]) -> bool:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    readme = render_readme(data)
    previous_hash = hashlib.sha256((DATA_FILE.read_bytes() if DATA_FILE.exists() else b"") + README.read_bytes()).digest()
    DATA_FILE.write_text(payload, encoding="utf-8")
    README.write_text(readme, encoding="utf-8")
    current_hash = hashlib.sha256(DATA_FILE.read_bytes() + README.read_bytes()).digest()
    return previous_hash != current_hash


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="collect and render without writing")
    args = parser.parse_args(argv)
    try:
        data = build_dashboard()
        if args.check:
            render_readme(data)
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            changed = write_outputs(data)
            print(f"Dashboard updated ({'changed' if changed else 'unchanged'}).")
        return 0
    except Exception as exc:
        print(f"Dashboard update failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
