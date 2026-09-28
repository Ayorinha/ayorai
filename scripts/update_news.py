#!/usr/bin/env python3
"""Build docs/news.json from public technology and AI RSS feeds."""

from __future__ import annotations

import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

FEEDS = (
    ("TechCrunch", "https://techcrunch.com/feed/"),
    ("The Verge", "https://www.theverge.com/rss/index.xml"),
    ("WIRED", "https://www.wired.com/feed/rss"),
    ("Ars Technica", "https://feeds.arstechnica.com/arstechnica/index"),
)

CATEGORIES = {
    "ai": ("ai", "artificial intelligence", "machine learning", "llm", "agent"),
    "security": ("security", "cybersecurity", "privacy", "hack", "vulnerability"),
    "hardware": ("chip", "gpu", "hardware", "device", "processor"),
    "startup": ("startup", "funding", "venture", "acquisition", "ipo"),
    "cloud": ("cloud", "aws", "azure", "google cloud", "infrastructure"),
    "dev": ("developer", "programming", "github", "open source", "software"),
}

TAG = "{http://www.w3.org/2005/Atom}"


def _text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return " ".join("".join(element.itertext()).split())


def _first(element: ET.Element, names: tuple[str, ...]) -> ET.Element | None:
    for name in names:
        child = element.find(name)
        if child is not None:
            return child
    return None


def classify(title: str, summary: str) -> str:
    haystack = f"{title} {summary}".lower()
    for category, terms in CATEGORIES.items():
        if any(re.search(rf"\b{re.escape(term)}\b", haystack) for term in terms):
            return category
    return "dev"


def parse_feed(xml_text: str, source: str, limit: int = 10) -> list[dict[str, str]]:
    root = ET.fromstring(xml_text)
    items = root.findall(".//item")
    atom_mode = not items
    if atom_mode:
        items = root.findall(f".//{TAG}entry")

    articles: list[dict[str, str]] = []
    for item in items[:limit]:
        if atom_mode:
            title = _text(item.find(f"{TAG}title"))
            summary = _text(item.find(f"{TAG}summary")) or _text(item.find(f"{TAG}content"))
            link_node = item.find(f"{TAG}link")
            url = link_node.get("href", "") if link_node is not None else ""
            published = _text(item.find(f"{TAG}published")) or _text(item.find(f"{TAG}updated"))
        else:
            title = _text(_first(item, ("title",)))
            summary = _text(_first(item, ("description", "content")))
            link = _first(item, ("link",))
            url = _text(link)
            published = _text(_first(item, ("pubDate", "date")))
        if not title or not url:
            continue
        articles.append(
            {
                "title": title,
                "source": source,
                "url": url,
                "time": published,
                "category": classify(title, summary),
                "summary": summary[:300],
            }
        )
    return articles


def fetch(url: str, timeout: int = 20) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ayorai-rss-feed/0.2"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def build_news(feeds: tuple[tuple[str, str], ...] = FEEDS, per_feed: int = 10) -> dict:
    articles: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for source, url in feeds:
        try:
            parsed = parse_feed(fetch(url), source, per_feed)
        except (OSError, ET.ParseError, ValueError):
            continue
        for article in parsed:
            if article["url"] in seen_urls:
                continue
            seen_urls.add(article["url"])
            articles.append(article)

    return {
        "title": "Ayorai Tech — Notícias de tecnologia",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "articles": articles[:40],
    }


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "docs" / "news.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_news(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
