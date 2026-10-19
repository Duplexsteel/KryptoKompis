"""Guides, news, the About page, RSS feeds and the sitemap for kryptokompis.no.

Content lives as Markdown next to this script - edit there, never in site/:
  guides/<slug>.nb.md and guides/<slug>.en.md   one guide or news post per language
  pages/om.nb.md, pages/about.en.md             the About page
Front matter (between --- lines): title, date (YYYY-MM-DD), summary, draft (yes = hidden), kind (guide | news | blog - news/blog go on the blog page),
optional order (reading order of guides on the list page), optional video (a YouTube id, embedded privacy-friendly via youtube-nocookie.com).

New post every other week: add the two .md files, run this script, push the site.
Output (flat, so the shared head/nav/footer links keep working):
  guide-<slug>.html / guide-<slug>-en.html, guider.html / guides.html, blogg.html / blog.html, om.html / about.html,
  the three newest posts on the front page (<!--LATEST-->),
  rss.xml / rss-en.xml, sitemap.xml, robots.txt

Run:  python packaging/site_tools/build_guides.py <site dir>   (needs: pip install markdown)"""
import json
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from html import escape
from pathlib import Path

import markdown

import build_site as B

HERE = Path(__file__).parent
SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")

L = {
    "nb": dict(list="guider.html", about="om.html", about_src="om.nb.md", other_list="guides.html", other_about="about.html",
               rss="rss.xml", h1="Guider",
               lead="Steg-for-steg for hver børs, og hvordan du fører krypto i skattemeldingen. Ny artikkel annenhver uke.",
               blog="blogg.html", other_blog="blog.html", blog_h1="Blogg", blog_lead="Nytt fra Kryptokompis, nye versjoner og tanker om krypto og skatt i Norge.",
               guides="Guider", news="Nyheter", rss_label="Følg med via RSS", back="Alle guider",
               cta="Last ned Kryptokompis", cta_href="priser.html#kom-i-gang", updated="Publisert", watch="Se videoen",
               feed_title="Kryptokompis - guider og nyheter", keys_h="Slik lager du API-nøkler",
               keys_p="Steg-for-steg for hver børs, skrevet og på video. Nøklene kan bare lese - Kryptokompis kan aldri handle eller ta ut penger.",
               key_api="API-nøkkel som bare kan lese", api_intro="▶ Start her: Hva er en API? (video)", key_file="Eksportfil (ingen API-nøkkel)", video="▶ Video", months=["januar", "februar", "mars", "april", "mai", "juni", "juli",
               "august", "september", "oktober", "november", "desember"]),
    "en": dict(list="guides.html", about="about.html", about_src="about.en.md", other_list="guider.html", other_about="om.html",
               rss="rss-en.xml", h1="Guides",
               lead="Step by step for each exchange, and how to report crypto in the Norwegian tax return. A new article every other week.",
               blog="blog.html", other_blog="blogg.html", blog_h1="Blog", blog_lead="News from Kryptokompis, new versions and thoughts on crypto and tax in Norway.",
               guides="Guides", news="News", rss_label="Follow via RSS", back="All guides",
               cta="Download Kryptokompis", cta_href="pricing.html#get-started", updated="Published", watch="Watch the video",
               feed_title="Kryptokompis - guides and news", keys_h="How to create API keys",
               keys_p="Step by step for each exchange, written and on video. The keys can only read - Kryptokompis can never trade or withdraw.",
               key_api="Read-only API key", api_intro="▶ Start here: What is an API? (video, Norwegian)", key_file="Statement file (no API key)", video="▶ Video (Norwegian)", months=["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]),
}

CSS = """<style>
.art{max-width:760px;padding-top:56px;padding-bottom:72px}.art h1{font-size:clamp(32px,5vw,46px);margin:6px 0 12px}
.art .meta{color:var(--ink2);font-size:15px}.art h2{font-size:22px;margin:30px 0 8px}.art p,.art li{color:var(--ink2)}
.art p{margin:12px 0}.art ul{padding-left:22px}.art li{margin:7px 0}.art li ul{margin:6px 0}
.art ol{list-style:none;padding:0;counter-reset:n}.art ol>li{counter-increment:n;padding-left:32px;position:relative}
.art ol>li:before{content:counter(n);position:absolute;left:0;top:2px;width:22px;height:22px;border-radius:50%;background:var(--mint);color:var(--spruce-d);font-size:13px;font-weight:700;display:grid;place-items:center}.art b,.art strong{color:var(--ink)}
.art code{background:var(--sheet);border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-size:.9em;word-break:break-all}
.art table{border-collapse:collapse;width:100%;margin:16px 0}.art td,.art th{padding:10px 10px 10px 0;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
.art th{font-size:14px;color:var(--ink2)}.art .vid{position:relative;padding-top:56.25%;margin:22px 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--line)}
.art .vid iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.art .end{margin-top:40px;display:flex;gap:12px;flex-wrap:wrap}
.glist{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:12px;max-width:860px}
.glist a{display:block;padding:18px 20px;border:1px solid var(--line);border-radius:var(--r);background:var(--sheet);color:var(--ink);text-decoration:none}
.glist a:hover{border-color:var(--spruce)}.glist b{font-size:18px}.glist span{display:block;color:var(--ink2);margin-top:4px}
.glist small{color:var(--ink2)}.whohead{display:flex;gap:28px;align-items:center;margin-bottom:8px}
.who{width:120px;height:120px;border-radius:50%;object-fit:cover;flex:none;border:3px solid var(--mint)}
@media(max-width:560px){.whohead{flex-direction:column;align-items:flex-start;gap:16px}.who{width:96px;height:96px}}.krow{display:flex;gap:10px}.krow>a:first-child{flex:1}
.glist a.yt{flex:none;display:grid;place-items:center;padding:0 22px;font-weight:700;color:#fff;background:var(--spruce);border-color:var(--spruce)}
.glist a.yt:hover{background:var(--spruce-d)}.gsec{margin-top:40px}.rss{font-size:15px}
</style>"""


def read(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    _, fm, body = text.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    meta["html"] = markdown.markdown(body.strip(), extensions=["tables", "sane_lists"])
    return meta


def nice_date(d: str, t: dict) -> str:
    dt = datetime.strptime(d, "%Y-%m-%d")
    return f"{dt.day}. {t['months'][dt.month - 1]} {dt.year}" if t is L["nb"] else f"{dt.day} {t['months'][dt.month - 1]} {dt.year}"


def page(lang: str, file: str, other: str, title: str, desc: str, main: str) -> str:
    p = dict(B.T[lang], file=file, other=other)
    return (B.head(p, title, desc).replace("</head>", CSS + "</head>", 1) + B.nav(p, home_page=False)
            + f"<main>{main}</main>" + B.footer(p))


def video(vid: str, t: dict) -> str:
    return (f'<div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/{escape(vid)}" title="{t["watch"]}" '
            'loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>')


def today() -> str:
    """Oslo date; SITE_TODAY=YYYY-MM-DD overrides it (to preview what goes live on a later day)."""
    import os
    from zoneinfo import ZoneInfo
    return os.getenv("SITE_TODAY") or datetime.now(ZoneInfo("Europe/Oslo")).strftime("%Y-%m-%d")


def live_videos() -> dict:
    """videos.json: {slug: {"youtube": id, "publish": "YYYY-MM-DD"}} - a video shows from its publish day."""
    f = HERE / "videos.json"
    data = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    return {k: v["youtube"] for k, v in data.items() if v.get("youtube") and v.get("publish", "") <= today()}


# The exchanges in the "How to create API keys" block, in order: (guide slug, name, needs an API key)
KEY_GUIDES = [("kraken", "Kraken", True), ("binance", "Binance", True), ("coinbase", "Coinbase", True),
              ("kucoin", "KuCoin", True), ("firi", "Firi", False), ("revolut-x", "Revolut X", False)]


def build() -> list:
    urls = []
    posts = {}
    vids = live_videos()
    for lang in L:
        posts[lang] = []
        for f in sorted((HERE / "guides").glob(f"*.{lang}.md")):
            slug = f.name[: -len(f".{lang}.md")]
            m = read(f)
            if str(m.get("draft", "")).lower() in ("yes", "true", "1"):   # draft: not on the site until verified
                print(f"draft: {f.name}")
                continue
            if m["date"] > today():                  # scheduled: goes live on its date (daily site build)
                print(f"scheduled {m['date']}: {f.name}")
                continue
            m["slug"] = slug
            m.setdefault("video", vids.get(slug, ""))
            m["file"] = f"guide-{slug}.html" if lang == "nb" else f"guide-{slug}-en.html"
            m["other"] = f"guide-{slug}-en.html" if lang == "nb" else f"guide-{slug}.html"
            posts.setdefault(lang, []).append(m)
        posts[lang].sort(key=lambda m: (m["date"], m["title"]), reverse=True)        # newest first (RSS, news)

    for lang, t in L.items():
        for m in posts[lang]:
            back = (t["blog"], t["blog_h1"]) if m.get("kind", "guide") != "guide" else (t["list"], t["back"])
            main = (f'<article class="w art"><p class="meta"><a href="{back[0]}">{back[1]}</a> · {t["updated"]} {nice_date(m["date"], t)}</p>'
                    f'<h1>{escape(m["title"])}</h1><p class="lead">{escape(m["summary"])}</p>'
                    + (video(m["video"], t) if m.get("video") else "") + m["html"]
                    + f'<p class="end"><a class="btn" href="{t["cta_href"]}">{t["cta"]}</a>'
                      f'<a class="btn g" href="{B.DISCORD}" target="_blank" rel="noopener">Discord</a></p></article>')
            (SITE / m["file"]).write_text(page(lang, m["file"], m["other"], f'{m["title"]} - Kryptokompis', m["summary"], main), encoding="utf-8")
            urls.append((m["file"], m["date"]))

        def items(kind):
            chosen = [m for m in posts[lang] if m.get("kind", "guide") == kind]
            if kind == "guide":                     # guides in a fixed reading order (front matter "order")
                chosen.sort(key=lambda m: int(m.get("order", 99)))
            return "".join(f'<li><a href="{m["file"]}"><b>{escape(m["title"])}</b><span>{escape(m["summary"])}</span>'
                           f'<small>{nice_date(m["date"], t)}</small></a></li>' for m in chosen)
        live = {m["slug"] for m in posts[lang]}
        rows = "".join(
            f'<li class="krow"><a href="{"guide-" + g + (".html" if lang == "nb" else "-en.html")}"><b>{n}</b>'
            f'<span>{t["key_api"] if api else t["key_file"]}</span></a>'
            + (f'<a class="yt" href="https://youtu.be/{vids[g]}" target="_blank" rel="noopener">{t["video"]}</a>' if g in vids else "")
            + '</li>' for g, n, api in KEY_GUIDES if g in live)
        intro = next((m for m in posts[lang] if m["slug"] == "hva-er-api"), None)      # the explainer video, first
        start = (f'<p><a class="btn s" href="{intro["file"]}">{t["api_intro"]}</a></p>' if intro else "")
        keys = f'<div class="gsec"><h2>{t["keys_h"]}</h2><p>{t["keys_p"]}</p>{start}<ul class="glist">{rows}</ul></div>' if rows else ""
        main = (f'<div class="w art" style="max-width:900px"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>'
                f'<p class="rss"><a href="{t["rss"]}">{t["rss_label"]}</a></p>'
                + keys + f'<div class="gsec"><h2>{t["guides"]}</h2><ul class="glist">{items("guide")}</ul></div></div>')
        (SITE / t["list"]).write_text(page(lang, t["list"], t["other_list"], f'{t["h1"]} - Kryptokompis', t["lead"], main), encoding="utf-8")
        urls.append((t["list"], posts[lang][0]["date"] if posts[lang] else None))

        # Blog: news and blog posts (kind news | blog), newest first
        blog = "".join(f'<li><a href="{m["file"]}"><b>{escape(m["title"])}</b><span>{escape(m["summary"])}</span>'
                       f'<small>{nice_date(m["date"], t)}</small></a></li>' for m in posts[lang] if m.get("kind", "guide") != "guide")
        main = (f'<div class="w art" style="max-width:900px"><h1>{t["blog_h1"]}</h1><p class="lead">{t["blog_lead"]}</p>'
                f'<p class="rss"><a href="{t["rss"]}">{t["rss_label"]}</a></p><ul class="glist">{blog}</ul></div>')
        (SITE / t["blog"]).write_text(page(lang, t["blog"], t["other_blog"], f'{t["blog_h1"]} - Kryptokompis', t["blog_lead"], main), encoding="utf-8")
        urls.append((t["blog"], None))

        # Front page: the three newest posts in place of <!--LATEST--> (written by build_site.py)
        home = SITE / B.T[lang]["file"]
        if home.exists():
            x = B.X[lang]
            cards = "".join(f'<a href="{m["file"]}"><small>{nice_date(m["date"], t)}</small><b>{escape(m["title"])}</b>'
                            f'<span>{escape(m["summary"])}</span></a>' for m in posts[lang][:3])
            block = (f'<section><div class="w"><div class="headrow"><h2>{x["latest_h"]}</h2>'
                     f'<a href="{t["list"]}">{x["latest_all"]} →</a></div><div class="latest">{cards}</div></div></section>')
            html = home.read_text(encoding="utf-8")
            if "<!--LATEST-->" in html:
                home.write_text(html.replace("<!--LATEST-->", block), encoding="utf-8")

        a = read(HERE / "pages" / t["about_src"])
        photo = (f'<img class="who" src="{escape(a["photo"])}" alt="{escape(a.get("photo_alt", ""))}" width="120" height="120">'
                 if a.get("photo") else "")
        main = (f'<article class="w art"><div class="whohead">{photo}<div><h1>{escape(a["title"])}</h1>'
                f'<p class="lead">{escape(a["summary"])}</p></div></div>{a["html"]}</article>')
        (SITE / t["about"]).write_text(page(lang, t["about"], t["other_about"], f'{a["title"]} - Kryptokompis', a["summary"], main), encoding="utf-8")
        urls.append((t["about"], None))

        # RSS 2.0: newest first, full summary + link
        newest = posts[lang][0]["date"] if posts[lang] else today()      # stable: no daily diff when nothing new
        now = format_datetime(datetime.strptime(newest, "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc))
        rss_items = "".join(
            f"<item><title>{escape(m['title'])}</title><link>{B.SITE_URL}/{m['file']}</link><guid>{B.SITE_URL}/{m['file']}</guid>"
            f"<pubDate>{format_datetime(datetime.strptime(m['date'], '%Y-%m-%d').replace(hour=8, tzinfo=timezone.utc))}</pubDate>"
            f"<description>{escape(m['summary'])}</description></item>" for m in posts[lang])
        feed = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
                f"<title>{t['feed_title']}</title><link>{B.SITE_URL}/{t['list']}</link><description>{escape(t['lead'])}</description>"
                f"<language>{'nb-NO' if lang == 'nb' else 'en'}</language><lastBuildDate>{now}</lastBuildDate>"
                f'<atom:link href="{B.SITE_URL}/{t["rss"]}" rel="self" type="application/rss+xml"/>{rss_items}</channel></rss>\n')
        (SITE / t["rss"]).write_text(feed, encoding="utf-8")
    return urls


def sitemap(urls: list) -> None:
    fixed = ["index.html", "en.html", "info.html", "info-en.html", "vilkar.html", "terms.html", "personvern.html", "privacy.html"]
    fixed += [f for lang in B.PAGES for k, f in B.PAGES[lang].items() if k not in ("guides", "blog")]
    rows = [f"<url><loc>{B.SITE_URL}/{u}</loc></url>" for u in fixed]
    rows += [f"<url><loc>{B.SITE_URL}/{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>" for u, d in urls]
    (SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + "".join(rows) + "</urlset>\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {B.SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    u = build()
    sitemap(u)
    print(f"wrote {len(u)} pages, rss.xml, rss-en.xml, sitemap.xml, robots.txt")
