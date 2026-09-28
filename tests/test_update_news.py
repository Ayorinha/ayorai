import importlib.util
import json
from pathlib import Path

_MODULE_PATH = Path(__file__).parents[1] / "scripts" / "update_news.py"
_SPEC = importlib.util.spec_from_file_location("update_news", _MODULE_PATH)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

build_news = _MODULE.build_news
classify = _MODULE.classify
parse_feed = _MODULE.parse_feed
write_news = _MODULE.write_news


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


def test_write_news_keeps_fallback_when_all_feeds_fail(tmp_path, monkeypatch):
    fallback = tmp_path / "news.json"
    fallback.write_text('{"articles": [{"title": "cached"}]}\n', encoding="utf-8")

    monkeypatch.setattr(_MODULE, "fetch", lambda _url: (_ for _ in ()).throw(OSError("offline")))

    assert write_news(fallback, (("Example", "https://example.com/rss"),)) is False
    assert json.loads(fallback.read_text(encoding="utf-8")) == {
        "articles": [{"title": "cached"}]
    }


def test_write_news_replaces_fallback_when_feed_has_articles(tmp_path, monkeypatch):
    fresh = tmp_path / "news.json"
    fresh.write_text('{"articles": [{"title": "cached"}]}\n', encoding="utf-8")

    monkeypatch.setattr(_MODULE, "fetch", lambda _url: RSS)

    assert write_news(fresh, (("Example", "https://example.com/rss"),)) is True
    payload = json.loads(fresh.read_text(encoding="utf-8"))
    assert payload["articles"][0]["title"] == "New AI agent security research"
