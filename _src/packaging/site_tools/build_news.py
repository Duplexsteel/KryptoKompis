"""Crypto news page for kryptokompis.no: the latest headlines from a few large crypto news sites.

Only the headline, source, time and a link are shown - never the article text - and every item links to
the original. The daily site build (public repo, .github/workflows/daily-site.yml) runs this every
morning. If a feed cannot be fetched, the headlines from the last good run (assets/news.json) are kept.

Run:  python packaging/site_tools/build_news.py <site dir>     (after build_site.py: uses its head/nav/footer)"""
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import escape
from pathlib import Path
from xml.etree import ElementTree as ET

import build_site as B

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
CACHE = SITE / "assets" / "news.json"
FEEDS = [("Cointelegraph", "https://cointelegraph.com/rss"),
         ("Decrypt", "https://decrypt.co/feed"),
         ("CoinDesk", "https://www.coindesk.com/arc/outboundfeeds/rss/"),
         ("Bitcoin Magazine", "https://bitcoinmagazine.com/.rss/full/")]
KEEP_DAYS, MAX_ITEMS = 4, 60

L = {
    "nb": dict(file="kryptonytt.html", other="crypto-news.html", h1="Kryptonytt",
               lead="De siste overskriftene fra store kryptomedier, samlet ett sted og oppdatert hver morgen. Artiklene er på engelsk.",
               note="Overskriftene hentes automatisk fra kildene, og lenkene går til den opprinnelige artikkelen. Kryptokompis står ikke bak innholdet, og ingenting her er investeringsråd.",
               empty="Ingen overskrifter akkurat nå - prøv igjen senere.", updated="Oppdatert",
               days=["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"],
               months=["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]),
    "en": dict(file="crypto-news.html", other="kryptonytt.html", h1="Crypto news",
               lead="The latest headlines from large crypto news sites, in one place and updated every morning.",
               note="Headlines are fetched automatically from the sources, and the links go to the original article. Kryptokompis is not behind the content, and nothing here is investment advice.",
               empty="No headlines right now - try again later.", updated="Updated",
               days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
               months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]),
}

CSS = """<style>
.news{max-width:860px;padding-top:56px;padding-bottom:72px}.news h1{font-size:clamp(32px,5vw,46px);margin-bottom:12px}
.news h2{font-size:18px;color:var(--ink2);margin:34px 0 8px;font-weight:600}
.nl{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.nl li{display:grid;grid-template-columns:52px 1fr;gap:14px;padding:13px 0;border-bottom:1px solid var(--line)}
.nl time{color:var(--ink2);font-size:14px;padding-top:2px}.nl a{color:var(--ink);text-decoration:none;font-weight:600}
.nl a:hover{color:var(--spruce-d);text-decoration:underline}.nl small{display:block;color:var(--ink2);font-size:13.5px;margin-top:2px}
</style>"""


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Kryptokompis news page (+https://kryptokompis.no)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


def parse(source: str, xml: bytes) -> list:
    out = []
    for it in ET.fromstring(xml).iter("item"):
        title, link, date = [(it.findtext(k) or "").strip() for k in ("title", "link", "pubDate")]
        if not (title and link.startswith("http") and date):
            continue
        try:
            when = parsedate_to_datetime(date).astimezone(timezone.utc)
        except (TypeError, ValueError):
            continue
        out.append({"title": title, "link": link, "source": source, "at": when.isoformat()})
    return out


def collect(fetcher=fetch) -> list:
    old = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else []
    items = []
    for source, url in FEEDS:
        try:
            items += parse(source, fetcher(url))
        except Exception as e:  # noqa: BLE001 - one feed down must not stop the page
            print(f"{source}: {e} - keeping its headlines from last time")
            items += [i for i in old if i["source"] == source]
    cutoff = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS)
    seen, keep = set(), []
    for i in sorted(items, key=lambda i: i["at"], reverse=True):
        if i["link"] in seen or datetime.fromisoformat(i["at"]) < cutoff:
            continue
        seen.add(i["link"])
        keep.append(i)
    return keep[:MAX_ITEMS]


def render(items: list) -> None:
    from zoneinfo import ZoneInfo
    oslo = ZoneInfo("Europe/Oslo")
    for lang, t in L.items():
        groups, cur = [], None
        for i in items:
            at = datetime.fromisoformat(i["at"]).astimezone(oslo)
            day = (f"{t['days'][at.weekday()]} {at.day}. {t['months'][at.month - 1]}" if lang == "nb"
                   else f"{t['days'][at.weekday()]} {at.day} {t['months'][at.month - 1]}")
            if day != cur:
                groups.append((day, []))
                cur = day
            groups[-1][1].append(f'<li><time>{at:%H:%M}</time><div><a href="{escape(i["link"])}" target="_blank" rel="noopener nofollow">'
                                 f'{escape(i["title"])}</a><small>{escape(i["source"])}</small></div></li>')
        body = "".join(f'<h2>{d}</h2><ul class="nl">{"".join(rows)}</ul>' for d, rows in groups) or f"<p>{t['empty']}</p>"
        # Keep the feed, original links and dates; only the presentation changes.
        sources = sorted({item['source'] for item in items})
        filters = ''.join(f'<button type="button" data-source-filter="{escape(source, quote=True)}" aria-pressed="false">{escape(source)}</button>' for source in sources)
        filters = f'<button type="button" data-source-filter="ALL" aria-pressed="true">{B.DESIGN.text(B.T[lang], "all_sources")}</button>' + filters
        rows = []
        for item in items:
            at = datetime.fromisoformat(item['at']).astimezone(oslo)
            source, link, headline = [escape(item[k], quote=True) for k in ('source', 'link', 'title')]
            rows.append(f'<a class="news-row" data-news-source="{source}" href="{link}" target="_blank" rel="noopener nofollow"><span class="source-name"><time datetime="{at.isoformat()}">{at:%d.%m %H:%M}</time><br>{source}</span><div><h3>{headline}</h3><p>{B.DESIGN.text(B.T[lang], "open_original")} {source}</p></div><span class="blue" aria-hidden="true">↗</span></a>')
        listing = ''.join(rows) or f'<p>{t["empty"]}</p>'
        main = (f'<section class="space"><div class="wrap">' + B.DESIGN.title(B.T[lang], 'news', 'news_h', 'news_p')
                + f'<div class="news-layout"><aside class="news-sources">{filters}</aside><div class="news-list">{listing}<p class="news-note">{t["note"]}</p></div></div></div></section>')
        p = dict(B.T[lang], file=t["file"], other=t["other"])
        html = (B.head(p, f'{t["h1"]} - Kryptokompis', t["lead"]).replace("</head>", CSS + "</head>", 1)
                + B.nav(p) + f'<main id="main">{main}</main>' + B.footer(p))
        (SITE / t["file"]).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    news = collect()
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(news, ensure_ascii=False, indent=0), encoding="utf-8")
    render(news)
    print(f"wrote kryptonytt.html, crypto-news.html ({len(news)} headlines)")
