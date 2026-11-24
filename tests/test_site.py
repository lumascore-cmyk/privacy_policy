"""Check the static site as served from a GitHub Pages project subdirectory."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / "docs"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.feed(path.read_text())
        self.close()

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class SiteTests(unittest.TestCase):
    def test_links_assets_and_fragment_targets(self):
        pages = {p.name: Page(p) for p in ROOT.glob("*.html")}
        self.assertEqual(set(pages), {"index.html", "faq.html", "privacy.html"})
        for name, page in pages.items():
            ids = [a["id"] for _, a in page.tags if "id" in a]
            self.assertEqual(len(ids), len(set(ids)), name)
            for tag, attrs in page.tags:
                for field in ("href", "src"):
                    if field not in attrs:
                        continue
                    link = urlsplit(attrs[field])
                    if link.scheme:
                        self.assertIn(link.scheme, {"mailto", "https"})
                        if link.scheme == "mailto":
                            self.assertEqual(link.path, "lumascore@gmail.com")
                        continue
                    self.assertFalse(link.netloc or link.path.startswith("/"), attrs[field])
                    target = link.path or name
                    self.assertTrue((ROOT / target).is_file(), target)
                    if link.fragment:
                        self.assertIn(link.fragment, {a.get("id") for _, a in pages[target].tags})
        for asset in re.findall(r'url\("([^"]+)"\)', (ROOT / "styles.css").read_text()):
            self.assertTrue((ROOT / asset).is_file(), asset)

    def test_answers_and_support_contact_are_available_without_javascript(self):
        faq = Page(ROOT / "faq.html")
        tags = [tag for tag, _ in faq.tags]
        self.assertGreaterEqual(tags.count("details"), 6)
        self.assertEqual(tags.count("details"), tags.count("summary"))
        for name in ("index.html", "privacy.html"):
            self.assertTrue(any(a.get("href", "").startswith("mailto:lumascore@gmail.com")
                                for _, a in Page(ROOT / name).tags))
