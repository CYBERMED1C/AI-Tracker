import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import update_dashboard as dashboard


class DashboardTests(unittest.TestCase):
    def test_parse_atom_feed(self):
        payload = b'''<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry><title>Claude 9 released</title><link href="https://example.test/release"/>
          <updated>2026-09-30T10:00:00Z</updated><summary>A safer model.</summary></entry>
        </feed>'''
        items = dashboard.parse_feed(payload, "Test Lab", "model")
        self.assertEqual(items[0]["title"], "Claude 9 released")
        self.assertEqual(items[0]["url"], "https://example.test/release")
        self.assertEqual(items[0]["date"], "2026-09-30")

    def test_parse_ai_gov_orders(self):
        page = b'''<h3>Executive Orders</h3>
        <a href="https://whitehouse.gov/a">Order A | 9/30/2026</a>
        <a href="https://whitehouse.gov/b">Order B | 8/1/2026</a>
        <h3>Fact Sheets</h3><a href="/not-an-order">Fact | 9/30/2026</a>'''
        original = dashboard.fetch
        dashboard.fetch = lambda *args, **kwargs: page
        try:
            orders = dashboard.collect_ai_gov_orders()
        finally:
            dashboard.fetch = original
        self.assertEqual([o["title"] for o in orders], ["Order A", "Order B"])

    def test_parse_sitemap_for_official_news(self):
        payload = b'''<?xml version="1.0"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url><loc>https://example.test/news/claude-opus-9</loc><lastmod>2026-09-30T10:00:00Z</lastmod></url>
          <url><loc>https://example.test/claude-sonnet-9</loc><lastmod>2026-09-29T10:00:00Z</lastmod></url>
          <url><loc>https://example.test/legal</loc><lastmod>2026-09-30</lastmod></url>
        </urlset>'''
        items = dashboard.parse_sitemap(payload, "Test Lab", "model-sitemap")
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["title"], "Claude Opus 9")

    def test_parse_meta_html(self):
        payload = b'''<a href="https://ai.meta.com/blog/muse/">Introducing Muse 2</a>
        <div class="date">September 30, 2026</div>'''
        items = dashboard.parse_meta_html(payload, "Meta AI", "model-html")
        self.assertEqual(items[0]["title"], "Introducing Muse 2")
        self.assertEqual(items[0]["date"], "2026-09-30")

    def test_parse_anthropic_html(self):
        payload = b'''<a href="/claude-opus-9"><time>Sep 29, 2026</time>
        <h2>Introducing Claude Opus 9</h2><p>A safer model.</p></a>'''
        items = dashboard.parse_anthropic_html(payload, "Anthropic", "model-anthropic-html")
        self.assertEqual(items[0]["title"], "Introducing Claude Opus 9")
        self.assertEqual(items[0]["date"], "2026-09-29")

    def test_rfc_date_and_diverse_selection(self):
        self.assertEqual(dashboard.parse_date("Tue, 29 Sep 2026 10:00:00 GMT"), "2026-09-29")
        items = [
            {"title": "A", "url": "a", "date": "2026-09-30", "source": "One"},
            {"title": "B", "url": "b", "date": "2026-09-29", "source": "One"},
            {"title": "C", "url": "c", "date": "2026-09-28", "source": "One"},
            {"title": "D", "url": "d", "date": "2026-09-27", "source": "Two"},
        ]
        self.assertEqual([item["title"] for item in dashboard.take_diverse(items)], ["A", "B", "D"])

    def test_known_exploitation_dominates_ranking(self):
        kev = {"risk": 70, "cvss": 7, "kev": True, "exploit": False}
        critical = {"risk": 85, "cvss": 10, "kev": False, "exploit": False}
        self.assertGreater(dashboard.advisory_score(kev), dashboard.advisory_score(critical))

    def test_replace_section_preserves_surrounding_text(self):
        text = "before\n<!-- dashboard:x:start -->old<!-- dashboard:x:end -->\nafter"
        rendered = dashboard.replace_section(text, "x", "new")
        self.assertIn("before", rendered)
        self.assertIn("new", rendered)
        self.assertIn("after", rendered)

    def test_headline_does_not_cut_a_long_description_mid_sentence(self):
        value = "Upgrade the affected service now. This second sentence is deliberately irrelevant."
        self.assertEqual(dashboard.headline(value), "Upgrade the affected service now")


if __name__ == "__main__":
    unittest.main()
