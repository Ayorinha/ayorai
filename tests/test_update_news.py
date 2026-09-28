import importlib.util
from pathlib import Path


_MODULE_PATH = Path(__file__).parents[1] / "scripts" / "update_news.py"
_SPEC = importlib.util.spec_from_file_location("update_news", _MODULE_PATH)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

classify = _MODULE.classify
parse_feed = _MODULE.parse_feed


RSS = """<?xml version="1.0"?>
<rss version="2.0"><channel>
  <item>
    <title>New AI agent security research</title>
    <link>https://example.com/ai</link>
    <description>Researchers study machine learning agents.</description>
    <pubDate>Mon, 28 Sep 2026 12:00:00 GMT</pubDate>
  </item>
  <item>
    <title>Open source developer release</title>
    <link>https://example.com/dev</link>
    <description>A new GitHub developer tool is released.</description>
  </item>
</channel></rss>"""


def test_parse_feed_extracts_articles():
    articles = parse_feed(RSS, "Example")
    assert len(articles) == 2
    assert articles[0]["source"] == "Example"
    assert articles[0]["category"] == "ai"
    assert articles[1]["category"] == "dev"


def test_classify_defaults_to_dev():
    assert classify("A quiet story", "No matching topic") == "dev"
