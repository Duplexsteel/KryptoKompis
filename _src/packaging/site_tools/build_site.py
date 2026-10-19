"""Builds the public site's landing pages (site/index.html = Norwegian, site/en.html = English)
from one template, plus the shared head/nav/footer that the Info pages (build_info.py) reuse.

Run:  python packaging/site_tools/build_site.py <site dir>
Facts on the page must match the app (prices in app/core/version.py, exchanges in accounts.py)."""
import json
import shutil
import sys
from pathlib import Path

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
BUY = "https://buy.stripe.com/4gM28r4nj6pf3oG257eUU00"
DISCORD = "https://discord.gg/hnAGgsAQ5V"
RELEASES = "https://github.com/Duplexsteel/KryptoKompis/releases"
import re as _re
VERSION = _re.search(r'APP_VERSION = "([^"]+)"', (Path(__file__).resolve().parents[2] / "app" / "core" / "version.py").read_text()).group(1)
DL_WIN = f"{RELEASES}/download/v{VERSION}/Kryptokompis-Setup-{VERSION}.exe"
DL_APK = f"{RELEASES}/download/v{VERSION}/Kryptokompis-{VERSION}.apk"
FONTS = "https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap"
ASSETS = Path(__file__).with_name("assets")

MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><g fill="currentColor">'
        '<rect x="5" y="5" width="5" height="22" rx="1.4"/><rect x="20" y="5" width="8" height="3.6" rx="1.4"/>'
        '<rect x="16" y="9.6" width="8" height="3.6" rx="1.4"/><rect x="12" y="14.2" width="8" height="3.6" rx="1.4"/>'
        '<rect x="16" y="18.8" width="8" height="3.6" rx="1.4"/><rect x="20" y="23.4" width="8" height="3.6" rx="1.4"/></g></svg>')

FLAG = ('<svg class="flag" viewBox="0 0 22 16" role="img" aria-label="{label}"><rect width="22" height="16" rx="2" fill="#BA0C2F"/>'
        '<path d="M6 0h4v16H6zM0 6h22v4H0z" fill="#fff"/><path d="M7 0h2v16H7zM0 7h22v2H0z" fill="#00205B"/></svg>')

CSS = """
:root{--paper:#F4F7F5;--sheet:#FFFFFF;--ink:#15302A;--ink2:#3F5650;--line:#D3DFD8;--spruce:#2E7D64;--spruce-d:#246652;
--mint:#E1F0E8;--mint2:#9AD8BD;--loss:#A3473A;--dark:#15302A;--r:10px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 "Schibsted Grotesk",system-ui,sans-serif;
 -webkit-font-smoothing:antialiased}

a{color:var(--spruce-d);text-underline-offset:3px}a:hover{color:var(--ink)}
:focus-visible{outline:3px solid var(--spruce);outline-offset:3px;border-radius:4px}
img,svg{display:block}
.w{max-width:1120px;margin:0 auto;padding:0 24px}
h1,h2,h3{margin:0;color:var(--ink);font-weight:700;letter-spacing:-.015em}
h1{font-size:clamp(40px,6.2vw,66px);line-height:1.02;font-weight:800;letter-spacing:-.03em}
h2{font-size:clamp(28px,3.4vw,38px);line-height:1.12}
h3{font-size:19px;line-height:1.3}
p{margin:0}
.lead{font-size:20px;line-height:1.55;color:var(--ink2);max-width:36em}
.sub{color:var(--ink2);max-width:38em;margin-top:12px}
.note{color:var(--ink2);font-size:15px;margin-top:10px}

/* nav */
header{position:sticky;top:0;z-index:40;background:rgba(244,247,245,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
nav{display:flex;align-items:center;gap:26px;height:66px}
.brand{display:flex;align-items:center;gap:9px;color:var(--ink);text-decoration:none;font-weight:700;font-size:21px;letter-spacing:-.02em}
.brand .mark{width:28px;height:28px;color:var(--spruce)}
nav .sp{flex:1}
nav .l{color:var(--ink2);text-decoration:none;font-size:16px;font-weight:500}nav .l:hover{color:var(--ink)}
.lang{color:var(--ink2);text-decoration:none;font-size:14px;font-weight:600;border:1px solid var(--line);border-radius:6px;padding:4px 9px}
.dd{position:relative}
.dd>button,.menu-btn{font:inherit;font-size:16px;font-weight:500;color:var(--ink2);background:none;border:0;cursor:pointer;padding:8px 0;display:flex;align-items:center;gap:6px}
.dd>button:after{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:translateY(-2px) rotate(45deg)}
.dd>button[aria-expanded=true]:after{transform:translateY(2px) rotate(225deg)}
.dd .m{display:none;position:absolute;left:-14px;top:44px;min-width:230px;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:8px;box-shadow:0 14px 36px rgba(21,48,42,.14)}
.dd>button[aria-expanded=true]+.m{display:block}
.dd .m a{display:block;padding:10px 12px;border-radius:6px;color:var(--ink);text-decoration:none;font-weight:500}
.dd .m a:hover{background:var(--mint)}
.menu-btn{display:none}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 22px;border-radius:999px;
 background:var(--spruce);color:#fff;font-weight:600;font-size:16px;text-decoration:none;border:2px solid var(--spruce);transition:background .15s}
.btn:hover{background:var(--spruce-d);border-color:var(--spruce-d);color:#fff}
.btn.g{background:transparent;color:var(--ink);border-color:var(--ink)}
.btn.g:hover{background:var(--ink);color:#fff}
.btn.s{min-height:40px;padding:0 16px;font-size:15px}
.dark .btn{background:var(--mint2);border-color:var(--mint2);color:var(--ink)}.dark .btn:hover{background:#fff;border-color:#fff}

/* hero */
.hero{display:grid;grid-template-columns:1.02fr .98fr;gap:56px;align-items:center;padding:72px 0 88px}
.hero h1{margin-bottom:22px}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.hero .note{max-width:32em}
.sheet{background:var(--sheet);border:1px solid var(--line);border-radius:14px;padding:22px 22px 18px;
 box-shadow:0 1px 0 rgba(21,48,42,.04),0 22px 50px -18px rgba(21,48,42,.22)}
.sheet h3{font-size:15px;color:var(--ink2);font-weight:600;margin-bottom:10px}
.rows{list-style:none;margin:0;padding:0;font-size:14.5px}
.rows li{display:grid;grid-template-columns:92px 1fr auto;gap:12px;padding:7px 10px;border-radius:6px;background:var(--paper);margin-bottom:5px}
.rows .d{color:var(--ink2)}.rows .v{text-align:right;font-weight:600}
.into{display:flex;align-items:center;gap:10px;margin:14px 0 10px;color:var(--ink2);font-size:14px}
.into:before,.into:after{content:"";flex:1;height:1px;background:var(--line)}
.fields{width:100%;border-collapse:collapse;font-size:16px}
.fields td{padding:9px 2px;border-bottom:1px solid var(--line)}.fields tr:last-child td{border-bottom:0}
.fields td:last-child{text-align:right;font-weight:700;font-size:18px}
.fields .gain{color:var(--spruce-d)}.fields .loss{color:var(--loss)}
.fields small{display:block;color:var(--ink2);font-size:13px;font-weight:400}
.cap{font-size:13.5px;color:var(--ink2);margin-top:12px}
.ptotal{font-size:40px;font-weight:800;letter-spacing:-.03em;line-height:1.1}
.pchange{font-weight:700;font-size:15px;margin:2px 0 10px}.up{color:var(--spruce-d)}.down{color:var(--loss)}
.coins{list-style:none;margin:0;padding:0}
.coins li{display:grid;grid-template-columns:70px 1fr auto;gap:14px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.coins li:last-child{border-bottom:0}.coins small{display:block;font-size:13px;color:var(--ink2);font-weight:500}
.cv{text-align:right}.cv small.up{color:var(--spruce-d)}.cv small.down{color:var(--loss)}
.cb{height:8px;background:var(--mint);border-radius:999px;overflow:hidden}.cb i{display:block;height:100%;background:var(--spruce);border-radius:999px}
.htax{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.htax div{background:var(--paper);border-radius:8px;padding:10px 12px}
.htax small{display:block;font-size:12.5px;color:var(--ink2)}.htax b{font-size:17px}.htax .gain{color:var(--spruce-d)}.htax .loss{color:var(--loss)}
.flag{display:inline-block;width:20px;height:auto;vertical-align:-2px;border-radius:2px}
.rules-tag{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:600;color:var(--ink2);background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:3px 10px 3px 6px;margin-left:8px;white-space:nowrap;flex:none}
.made{display:inline-flex;align-items:flex-start;gap:8px}.made .flag{margin-top:5px;flex:none}
@media (prefers-reduced-motion:no-preference){
 .rows li,.coins li{animation:settle .7s cubic-bezier(.2,.8,.2,1) both}
 .coins li:nth-child(1){--x:48px;animation-delay:.15s}.coins li:nth-child(2){--x:28px;animation-delay:.27s}.coins li:nth-child(3){--x:48px;animation-delay:.39s}
 .rows li:nth-child(1){--x:64px;animation-delay:.15s}.rows li:nth-child(2){--x:38px;animation-delay:.25s}
 .rows li:nth-child(3){--x:14px;animation-delay:.35s}.rows li:nth-child(4){--x:38px;animation-delay:.45s}
 .rows li:nth-child(5){--x:64px;animation-delay:.55s}.rows li:nth-child(6){--x:84px;animation-delay:.65s}
 .htax b,.ptotal{animation:show .5s ease both .9s}
 @keyframes settle{from{opacity:0;transform:translateX(var(--x))}to{opacity:1;transform:none}}
 @keyframes show{from{opacity:0}to{opacity:1}}}

/* sections */
section{padding:88px 0}
.band{background:var(--sheet);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.dark{background:var(--dark);color:#E7F0EB}.dark h2,.dark h3{color:#fff}.dark .sub,.dark .note{color:#B9CCC3}.dark a{color:var(--mint2)}
.head{margin-bottom:44px}

/* steps: a real sequence */
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:28px;counter-reset:s;position:relative}
.steps:before{content:"";position:absolute;top:21px;left:22px;right:calc(25% - 15px);height:2px;background:var(--line)}
.steps li{position:relative;counter-increment:s}
.steps li:before{content:counter(s);display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--paper);
 border:2px solid var(--spruce);color:var(--spruce-d);font-weight:700;font-size:18px;margin-bottom:18px;position:relative}
.steps h3{margin-bottom:8px}.steps p{color:var(--ink2);font-size:16px}
.effort{margin-top:40px;padding:16px 20px;border-left:4px solid var(--spruce);background:var(--mint);border-radius:0 var(--r) var(--r) 0;max-width:46em}

/* output */
.out{display:grid;grid-template-columns:1fr 1fr;gap:64px}
.ck{list-style:none;margin:20px 0 0;padding:0}
.ck li{position:relative;padding-left:30px;margin:12px 0}
.ck li:before{content:"";position:absolute;left:2px;top:7px;width:14px;height:8px;border-left:2.5px solid var(--spruce);border-bottom:2.5px solid var(--spruce);transform:rotate(-45deg)}
.rules{margin:20px 0 0;padding:0}
.rules div{display:grid;grid-template-columns:minmax(150px,.8fr) 1.2fr;gap:16px;padding:13px 0;border-bottom:1px solid var(--line)}
.rules dt{font-weight:600}.rules dd{margin:0;color:var(--ink2);font-size:16px}
.files{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}
.callout{margin-top:36px;padding:22px 24px;border-radius:var(--r);background:var(--paper);border:1px solid var(--line)}
.callout h3{margin-bottom:6px}

/* exchanges */
.ex{width:100%;border-collapse:collapse}
.ex th{text-align:left;font-size:14px;color:var(--ink2);font-weight:600;padding:0 12px 10px 0;border-bottom:2px solid var(--ink)}
.ex td{padding:16px 12px 16px 0;border-bottom:1px solid var(--line);vertical-align:top}
.ex td:first-child{font-weight:700;font-size:18px;white-space:nowrap}
.how{display:inline-block;font-size:14px;font-weight:600;padding:3px 10px;border-radius:999px;background:var(--mint);color:var(--spruce-d);white-space:nowrap}
.how.f{background:#ECEFF3;color:#3E4C5E}

/* pricing */
.price{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:start}
.amount{display:flex;align-items:baseline;gap:14px;margin:18px 0 6px}
.amount b{font-size:72px;line-height:1;font-weight:800;letter-spacing:-.03em;color:#fff}
.amount span{font-size:18px;color:#B9CCC3}
.dark .ck li:before{border-color:var(--mint2)}
.pf{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.free-tag{display:inline-block;font-size:14px;font-weight:700;color:var(--spruce-d);background:var(--mint);border-radius:999px;padding:3px 11px;margin-bottom:14px}
.hold{width:100%;border-collapse:collapse;font-size:16px}.hold th{text-align:left;font-size:13.5px;color:var(--ink2);font-weight:600;padding:0 0 8px;border-bottom:1px solid var(--line)}
.hold td{padding:11px 0;border-bottom:1px solid var(--line)}.hold td:first-child{font-weight:700;width:64px}.hold td.e{color:var(--ink2);font-size:14.5px}
.hold td:last-child,.hold th:last-child{text-align:right;font-weight:700}.hold tr.t td{border-bottom:0;font-size:18px}
.later{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 4px}.later div{flex:1 1 90px;border:1px solid #2F4D45;border-radius:8px;padding:10px 12px}
.later b{display:block;color:#fff;font-size:20px}.later span{font-size:14px;color:#B9CCC3}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-bottom:44px}
.grid4 div{border-top:2px solid var(--ink);padding-top:16px}.grid4 h3{margin-bottom:8px}.grid4 p{color:var(--ink2);font-size:16px}
.ins div{border-top-color:var(--spruce)}
.go{margin-bottom:56px}.steps.go{grid-template-columns:repeat(3,1fr)}.steps.go:before{right:calc(33.3% - 6px)}.dark .steps:before{background:#2F4D45}.dark .steps li:before{background:var(--dark);border-color:var(--mint2);color:var(--mint2)}
.dark .steps p{color:#B9CCC3}.dark a.dl{display:inline-block;margin:6px 8px 6px 0;padding:8px 14px;border-radius:999px;background:var(--mint2);color:var(--ink);font-weight:700;text-decoration:none}.dark a.dl:hover{background:#fff}.dark .steps small{font-size:14px}.dark .price h3{font-size:24px}
.free{border:1px solid #2F4D45;border-radius:var(--r);padding:24px}
.free h3{margin-bottom:12px}
.free dl{margin:0}.free dt{font-weight:600;color:#fff;margin-top:14px}.free dd{margin:4px 0 0;color:#B9CCC3;font-size:16px}

/* trust */
.trust{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
.trust div{border-top:2px solid var(--ink);padding-top:16px}.trust h3{margin-bottom:8px}.trust p{color:var(--ink2);font-size:16px}

/* faq */
.faq{max-width:780px}
details{border-bottom:1px solid var(--line)}
summary{list-style:none;cursor:pointer;padding:20px 40px 20px 0;font-weight:600;font-size:18px;position:relative}
summary::-webkit-details-marker{display:none}
summary:after{content:"";position:absolute;right:8px;top:27px;width:9px;height:9px;border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:rotate(45deg)}
details[open] summary:after{transform:rotate(225deg);top:31px}
details>div,details>p,details>table,details>ol,details>ul{margin:0 0 20px}
details p{color:var(--ink2)}
.warn{margin-top:36px;max-width:780px;padding:18px 20px;border-radius:var(--r);background:#FBF3E4;border:1px solid #EBD7B0;color:#4A3B1C;font-size:16px}

/* generic pieces used by the Info pages */
.card{background:var(--sheet);border:1px solid var(--line);border-radius:var(--r);padding:24px}
.card h3{margin-bottom:8px}.card p{color:var(--ink2);font-size:16px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
table{border-collapse:collapse;width:100%}
.prose td,.prose th{padding:11px 10px 11px 0;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:16px}
.prose th{font-size:14px;color:var(--ink2)}

footer{border-top:1px solid var(--line);padding:36px 0 48px;color:var(--ink2);font-size:15px}
.foot{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;align-items:flex-start}
.foot .brand{font-size:18px}.foot .brand .mark{width:22px;height:22px}
.foot ul{list-style:none;margin:0;padding:0;display:flex;gap:20px;flex-wrap:wrap}
.foot p{margin-top:8px;max-width:30em}

@media (max-width:900px){
 .hero,.out,.price,.pf{grid-template-columns:1fr;gap:44px}.hero{padding:44px 0 64px}
 .steps,.steps.go{grid-template-columns:1fr 1fr}.steps:before{display:none}
 .trust{grid-template-columns:1fr;gap:28px}.g2{grid-template-columns:1fr}.grid4{grid-template-columns:1fr 1fr}
 nav .l,nav .dd{display:none}.menu-btn{display:flex}
 nav{gap:14px}
 .mobile{display:none;border-top:1px solid var(--line);padding:8px 0 16px}
 .mobile.open{display:block}
 .mobile a{display:block;padding:12px 0;color:var(--ink);text-decoration:none;font-weight:500;font-size:17px}
 .mobile .grp{color:var(--ink2);font-size:14px;margin-top:10px}
 .mobile .in{padding-left:14px}
}
@media (min-width:901px){.mobile{display:none!important}}
@media (max-width:600px){
 .w{padding-left:16px;padding-right:16px}section{padding:60px 0}
 body{font-size:16px}.lead{font-size:18px}
 .steps,.steps.go{grid-template-columns:1fr}.grid4{grid-template-columns:1fr}
 nav .lang{display:none}
 .brand{font-size:19px}
 header .btn.s{padding:0 12px}
 .rows li{grid-template-columns:78px 1fr auto;gap:8px;font-size:13px;padding:6px 8px}
 .htax{grid-template-columns:1fr}.htax div{display:flex;justify-content:space-between;align-items:baseline}.coins li{grid-template-columns:60px 1fr auto;gap:10px}.ptotal{font-size:34px}
 .ex thead{display:none}.ex tr{display:block;padding:14px 0;border-bottom:1px solid var(--line)}
 .ex td{display:block;border:0;padding:2px 0}.ex td:first-child,.ex td:nth-child(2){display:inline-block;font-size:18px;margin-right:10px}
 .rules div{grid-template-columns:1fr;gap:2px}
 .amount b{font-size:60px}
 .cta .btn{flex:1 1 100%}
}
"""

SITE_URL = "https://kryptokompis.no"
T = {
"nb": dict(
 lang="nb", locale="nb_NO", file="index.html", other="en.html", other_label="English", info="info.html",
 title="Kryptokompis - kryptoportefølje og kryptoskatt for Norge",
 desc="Kryptokompis samler kryptoporteføljen din fra alle børsene, med verdi i kroner og endring siste 24 timer - automatisk. Og skatterapport for krypto etter norske regler: kostpris, gevinst, tap og formue. Gratis å prøve.",
 og_title="Kryptokompis - din kryptokompis for oversikt og skatt",
 nav=[("#portefolje", "Portefølje"), ("#skatt", "Skatt"), ("#import", "Import"), ("#innsikt", "Innsikt"), ("#sporsmal", "Spørsmål")],
 ids=["portefolje", "skatt", "import", "innsikt", "kom-i-gang", "data", "sporsmal"],
 info_items=[("guider.html", "Guider og nyheter"), ("eksempler", "Eksempelrapporter"), ("lenker", "Nyttige lenker"), ("om.html", "Om Kryptokompis"), ("kontakt", "Kontakt")],
 menu="Meny", cta="Kom i gang", home="Til forsiden",
 h1="Din kryptokompis for oversikt og skatt.",
 lead="Se alle myntene dine fra alle børsene på ett sted, med verdien i kroner oppdatert av seg selv. Og når skattemeldingen kommer, er tallene allerede regnet ut etter norske regler.",
 cta2="Se en eksempelrapport", report_pdf="eksempel/Kryptokompis-eksempelrapport-2025.pdf",
 hero_note="Gratis å prøve. For Windows og Android.",
 hero_kicker="DIN KRYPTOKOMPIS",
 hero_lines=("Kryptoen din.", "Samlet oversikt.", "Enklere skatt."),
 hero_intro="Følg porteføljen gjennom året, og få oversikt når du trenger tallene til skattemeldingen.",
 hero_import="Koble til støttede kryptobørser via API, eller last opp CSV-filer med transaksjonene dine.",
 hero_try="Prøv Kryptokompis", hero_find="Finn børsen din",
 hero_demo="Eksempeldata", hero_allocation="Fordeling", hero_history="Verdi over tid",
 hero_demo_note="Illustrasjon med oppdiktede tall.", hero_exports="PDF og CSV",
 hero_history_desc="Eksempel på porteføljeverdi i norske kroner fra mai til oktober. Verdien svinger fra 35 000 kr ved starten til 99 298 kr ved slutten. Innskudd og uttak kan påvirke verdien; kurven viser ikke avkastning.",
 hero_months=("Mai", "Jun", "Jul", "Aug", "Sep", "Okt"),
 story_lines=("Oversikt i hverdagen.", "Rapporter når du trenger dem."),
 story_intro="Følg porteføljen, hold deg oppdatert og samle grunnlaget til skattemeldingen.",
 story_daily="01 / GJENNOM ÅRET", story_daily_h="Se hva du eier. Forstå historikken.",
 story_report="02 / NÅR DU TRENGER DET", story_report_h="Fra oversikt til rapport.",
 story_example="Forenklet eksempel", story_transactions="Transaksjonshistorikk",
 story_transaction_note="Kjøp, salg og belønninger", story_columns=("Dato", "Hendelse", "Eiendel", "Verdi (NOK)"),
 story_rows=(("19.01.2025", "Kjøp", "ETH", "67 200 kr", "buy"),
             ("06.02.2025", "Kjøp", "XRP", "8 663 kr", "buy"),
             ("14.03.2025", "Belønning", "ETH", "139 kr", "reward"),
             ("19.04.2025", "Salg", "BTC", "19 950 kr", "sell")),
 story_caption="Forenklet visning med oppdiktede transaksjoner.", story_portfolio="Se mer om porteføljen",
 story_report_title="Årsoversikt", story_report_example="Eksempelrapport · 2025",
 story_report_items=(("Gevinst", "7 527 kr"), ("Tap", "6 616 kr"), ("Inntekt", "428 kr"), ("Formue", "99 298 kr")),
 story_report_link="Se eksempelrapport", story_report_formats="PDF og CSV til dokumentasjonen din",
 story_news_kicker="NYTT OG NYTTIG", story_news_h="Kryptonytt og guider",
 story_news_intro="Følg markedet og finn forklaringer underveis.", story_news_link="Utforsk kryptonytt", story_guides_link="Finn en guide",
 story_local="Lokalt på Windows og Android.", story_privacy="Les om personvern",
 sheet_title="Fra transaksjoner ...",
 rows=[("19.01.2025", "Kjøp 2 ETH", "67 200 kr"), ("06.02.2025", "Kjøp 1 500 XRP", "8 663 kr"),
       ("14.03.2025", "Staking-belønning ETH", "139 kr"), ("19.04.2025", "Salg 0,02 BTC", "19 950 kr"),
       ("13.06.2025", "Bytte XRP til ETH", "2 625 kr"), ("30.09.2025", "Salg 1 ETH", "27 300 kr")],
 into="... til tallene i skattemeldingen",
 fields=[("Formuesverdi", "", "99 298 kr", ""), ("Skattepliktig gevinst", "", "7 527 kr", "gain"),
         ("Fradragsberettiget tap", "", "6 616 kr", "loss"), ("Andre inntekter", "staking og belønninger", "428 kr", "")],
 cap='Eksempel: inntektsår 2025 med oppdiktede tall, utdrag fra <a href="eksempel/Kryptokompis-eksempelrapport-2025.pdf">eksempelrapporten</a>.',
 flag_label="Norsk flagg", flag_tag="Norske regler",
 # portfolio
 pf_free="Gratis", pf_h="Kryptoporteføljen din, automatisk",
 pf_sub="Som en kurs-app, bare uten å føre noe for hånd: Kryptokompis henter beholdningen fra børsene dine og viser hva alt er verdt nå, i kroner.",
 pf_list=["Alle børsene lagt sammen: én beholdning per mynt, også fra Earn og futures",
          "Verdi i kroner, endring siste 24 timer og andel av porteføljen",
          "Oppdateres av seg selv mens appen er åpen",
          "Snittkost og urealisert gevinst eller tap per mynt",
          "Bare eksportfiler? Da regnes beholdningen ut fra transaksjonene"],
 pf_cols=("Mynt", "Verdi", "24 t", "Andel"),
 pf_rows=[("BTC", "0,04", "39 480 kr", "+1,2 %", "39,8 %", 40), ("ETH", "1,09", "37 769 kr", "−0,8 %", "38,0 %", 38), ("XRP", "1 000", "22 050 kr", "+3,1 %", "22,2 %", 22)],
 pf_total="Totalt", pf_total_v="99 298 kr", pf_change="+827 kr (+0,8 %) siste 24 timer", pf_change_pct="+0,8 %", pf_cap="Eksempel med oppdiktede tall, samlet fra Kraken, Binance og Coinbase.",
 hero_pf_title="Porteføljen din", hero_tax_title="... og tallene til skattemeldingen",
 hero_tax=[("Skattepliktig gevinst", "7 527 kr", "gain"), ("Fradragsberettiget tap", "6 616 kr", "loss"), ("Formuesverdi", "99 298 kr", "")],
 hero_cap='Eksempel med oppdiktede tall, fra <a href="eksempel/Kryptokompis-eksempelrapport-2025.pdf">eksempelrapporten</a>.',
 # tax
 tax_h="Kryptoskatt for Norge", tax_sub="Skatterapport for krypto som følger de norske reglene, med tallene klare for kortet Virtuelle eiendeler i skattemeldingen.",
 out_list=["Tallene til skattemeldingen, i samme rekkefølge som feltene der",
           "Hvert salg og bytte med FIFO-utregning: hvilke kjøp som ble brukt, og til hvilken pris",
           "Formue per 31.12 med kursene som er brukt",
           "Futures oppsummert per kategori, med alle poster i en egen CSV",
           "PDF du kan vise Skatteetaten eller regnskapsføreren, og CSV-filer til Excel"],
 files=[("eksempel/Kryptokompis-eksempelrapport-2025.pdf", "Eksempelrapport (PDF)"), ("eksempel/fifo_transactions_2025_nb.csv", "Eksempel-CSV")],
 rules_h="Slik regnes det",
 rules=[("FIFO per mynt", "Første kjøp ut først, på tvers av alle børsene dine."),
        ("Bytte mellom mynter", "Er et salg, også til og fra stablecoins."),
        ("Overføring mellom egne kontoer", "Er ikke et salg."),
        ("Gebyr betalt i mynt", "Regnes som et lite salg av mynten."),
        ("Staking og belønninger", "Inntekt til markedsverdi, som også blir kostprisen."),
        ("Gevinst og tap", "Føres hver for seg, aldri trukket fra hverandre."),
        ("Formue", "Markedsverdi 31.12. Kontanter på børser vises for seg.")],
 rules_note="Regelsettet heter NO-krypto-2026.1 og står i hver rapport.",
 # imports + cost basis
 imp_h="Transaksjoner og kostpris", imp_sub="Kryptokompis henter historikken din og gir hvert kjøp riktig kostpris i kroner. Det meste av jobben din er å koble til børsene første gang.",
 imp=[("API-nøkkel som bare kan lese", "Børsene synkes automatisk i bakgrunnen. Kryptokompis kan aldri handle eller ta ut penger."),
      ("Eller børsens egen eksportfil", "Last opp filen, så kjenner Kryptokompis igjen børsen. Det er trygt å importere samme periode igjen - ingenting telles dobbelt."),
      ("Kostpris krypto, i kroner", "Hvert kjøp får kostpris på sin egen dato, med Norges Banks dagskurs. Den følger mynten videre gjennom bytter og overføringer."),
      ("Gamle tap kan telle igjen", "Mynter fra forrige oppgang som ligger med tap? Importer den gamle historikken, så regnes det reelle tapet når du selger - aldri mer enn du faktisk tapte.")],
 ex_cols=("Børs", "Hvordan", "Hva som dekkes"),
 ex=[("Kraken", "API", "Spot, futures, staking og Earn-belønninger, innskudd og uttak"),
     ("Binance", "API", "Spothandler, innskudd og uttak"),
     ("Coinbase", "API eller fil", "Kjøp, salg, konverteringer, sendinger, mottak og belønninger"),
     ("KuCoin", "API og fil", "Siste 12 måneder via API, eldre år fra KuCoins eksportfil"),
     ("Firi", "Fil", "Handler, staking-belønninger, innskudd, uttak og gebyrer"),
     ("Revolut X", "Fil", "Kjøp, salg, sendinger og gebyrer"),
     ("Andre", "Mal", "Andre børser og lommebøker via importmalen i Kryptokompis")],
 file_word=("Fil", "Mal"),
 ex_more=f'Mangler børsen din? Si fra på <a href="{{DISCORD}}">Discord</a>, så legges den til.',
 # insights
 ins_h="Innsikt og varsler", ins_sub="Kryptokompis sier fra når noe ikke stemmer, i stedet for å gjette.",
 ins=[("Kontroller før du leverer", "Beholdningen avstemmes mot det børsene viser at du eier, og rapporten merkes foreløpig eller endelig."),
      ("Hull i dataene", "Salg uten kjøpshistorikk, beløp uten kronekurs, mynter uten pris og handler som er lagret to ganger blir varslet."),
      ("Resultater per mynt og periode", "Realisert gevinst og tap, gebyrer og vinnerandel per mynt - per uke, måned eller år. Krever lisens."),
      ("Varsler i appen", "Når en ny versjon er ute, og når en kostnad over 10 000 kr ikke er betalt via bank og kanskje ikke gir fradrag.")],
 # get started + price
 go_h="Kom i gang", go_sub="Prøv gratis først. Betal når du trenger tallene til skattemeldingen.",
 go_steps=[("Last ned", f'<a class="dl" href="{DL_WIN}" data-goatcounter-click="download-windows" data-goatcounter-title="Download Windows {VERSION}">Windows 10 og 11</a> <a class="dl" href="{DL_APK}" data-goatcounter-click="download-android" data-goatcounter-title="Download Android {VERSION}">Android (APK)</a><br><small>Versjon {VERSION}. <a href="{{RELEASES}}">Alle versjoner</a>. Viser Windows en blå advarsel: Mer info, Kjør likevel.</small>'),
           ("Koble til børsene", "Porteføljen og kontrollene er gratis. Total formue vises."),
           ("Kjøp lisens", "Lisensen låser opp tallene til skattemeldingen, PDF-rapporten og CSV-filene.")],
 price_h="Betalisens", amount="99 kr", once="én gang",
 price_sub="Kryptokompis er i beta, og betalisensen selges til de første 50. Den gjelder for alltid.",
 price_list=["Hele programmet: alle børser, kontroller, PDF og CSV", "Oppdateringer og nye børser inkludert",
             "Ingen abonnement", "Én lisens gjelder både PC og mobil", "Direkte kontakt med utvikleren på Discord"],
 buy="Kjøp betalisens - 99 kr",
 pay_note="Betaling med kort via Stripe. Lisensnøkkelen kommer på e-post med en gang. Du legger den inn én gang - abonnement fornyes av seg selv i appen.",
 later_h="Etter betaen", later=[("49 kr", "per måned"), ("399 kr", "per år"), ("999 kr", "livstid")],
 # trust
 trust_h="Dataene dine",
 trust=[("Blir på din enhet", "Ingen konto og ingen sky. Transaksjoner, rapporter og innstillinger lagres hos deg."),
        ("Nøkler som bare kan lese", "Kryptokompis kan aldri handle eller ta ut penger. På PC lagres API-nøklene i Windows sitt eget nøkkellager."),
        ("Snakker bare med det som trengs", "Børsene dine, offentlige kilder for priser og valutakurser, og Kryptokompis-nettsiden for å se etter oppdateringer. Tilbakemeldinger sendes bare når du trykker Send, uten transaksjonsdata.")],
 faq_h="Spørsmål og svar",
 faq=[("Hvordan skattlegges krypto i Norge?", "Gevinst ved salg eller bytte er skattepliktig, og tap gir fradrag, begge med 22 % skatt. Staking og andre belønninger er inntekt. Kryptoen teller også med i formuen, med verdien per 31.12. Kryptokompis regner ut alt dette i kroner - sjekk alltid tallene før du leverer."),
      ("Er dette skatterådgivning?", "Nei. Kryptokompis er et beregningsverktøy som bruker de norske reglene slik det tolker dem, og oppgir hvilket regelsett som er brukt i hver rapport. Du er selv ansvarlig for skattemeldingen - spør Skatteetaten eller en regnskapsfører hvis du er usikker."),
      ("Hva med tidligere år?", "Du velger hvor full FIFO-beregning starter. År som allerede er levert på annen måte, forblir lukket. For mynter der du har hele historikken, kan de reelle gamle kjøpsprisene brukes - så et reelt tap kan føres opp når du selger."),
      ("Hva med kontanter på børsene?", "Dollar og kroner som ligger på en børs, er formue - normalt et krav mot børsen - men ikke en virtuell eiendel. Kryptokompis viser saldoen ved årsskiftet for seg. Hvor den skal føres, avhenger av saldoen, valutaen og hvor børsen holder til."),
      ("Hvilke enheter?", "Windows-PC og Android-mobil. Én lisens gjelder begge. iPhone kan komme senere."),
      ("Windows sier «Windows beskyttet PC-en». Er det trygt?", "Meldingen kommer fordi Kryptokompis er nytt og ennå ikke har bygget opp et rykte hos Microsoft, ikke fordi noe er galt. Trykk <b>Mer info</b> og så <b>Kjør likevel</b>. Installasjonen trenger ikke administrator, og alt havner i din egen brukermappe. Filens SHA-256-sjekksum står ved hver versjon på nedlastingssiden."),
      ("Hvordan installerer jeg på Android?", "Last ned APK-filen på mobilen og åpne den. Første gang ber Android deg tillate installasjon fra nettleseren - slå det på for denne ene gangen. Play Store-versjonen kommer senere, og da får du oppdateringer automatisk."),
      ("Kan jeg trekke fra Kryptokompis på skatten?", "Kostnader til å forvalte kryptoen din, som et verktøy for oversikt og skatt, kan normalt føres som forvaltningskostnader i skattemeldingen. Fradraget er verdt 22 % av beløpet (18,5 % i Nord-Troms og Finnmark). Ta vare på kvitteringen. Sjekk hva som gjelder for deg hos Skatteetaten - dette er ikke skatterådgivning."),
      ("Hvordan får jeg hjelp?", f'Spør på <a href="{{DISCORD}}">Discord</a>, eller send en melding fra appen: Data og oppsett, Tilbakemelding og ønsker.')],
 warn="<b>Viktig:</b> Resultatet blir bare så komplett som dataene du gir Kryptokompis. Transaksjoner appen aldri ser - andre børser, lommebøker, historikk en børs ikke lenger gir ut - må importeres, ellers blir resultatet feil. Kontrollene hjelper deg å finne hull.",
 foot_p="Laget i Norge. Ikke skatterådgivning - du er selv ansvarlig for skattemeldingen.",
 foot_links=[("vilkar.html", "Vilkår"), ("personvern.html", "Personvern"), ("info.html", "Info"), ("{DISCORD}", "Discord"), ("{RELEASES}", "Nedlastinger"), ("en.html", "English")],
),
"en": dict(
 lang="en", locale="en_US", file="en.html", other="index.html", other_label="Norsk", info="info-en.html",
 title="Kryptokompis - crypto portfolio and Norwegian crypto tax",
 desc="Kryptokompis brings your crypto portfolio from every exchange together, valued in NOK with the 24-hour change - automatically. Plus your Norwegian crypto tax report: cost basis, gains, losses and wealth. Free to try.",
 og_title="Kryptokompis - your crypto companion for overview and tax",
 nav=[("#portfolio", "Portfolio"), ("#tax", "Tax"), ("#imports", "Imports"), ("#insights", "Insights"), ("#faq", "Questions")],
 ids=["portfolio", "tax", "imports", "insights", "get-started", "data", "faq"],
 info_items=[("guides.html", "Guides and news"), ("examples", "Example reports"), ("links", "Useful links"), ("about.html", "About Kryptokompis"), ("contact", "Contact")],
 menu="Menu", cta="Get started", home="Home",
 h1="Your crypto companion for overview and tax.",
 lead="See all your coins from every exchange in one place, valued in NOK and updated by themselves. And when the tax return comes, the figures are already worked out under Norwegian rules.",
 cta2="See an example report", report_pdf="eksempel/Kryptokompis-example-report-2025.pdf",
 hero_note="Free to try. For Windows and Android.",
 hero_kicker="YOUR CRYPTO COMPANION",
 hero_lines=("Your crypto.", "One clear overview.", "Simpler tax."),
 hero_intro="Follow your portfolio throughout the year, and get an overview when you need the figures for your tax return.",
 hero_import="Connect supported crypto exchanges via API, or upload CSV files with your transactions.",
 hero_try="Try Kryptokompis", hero_find="Find your exchange",
 hero_demo="Example data", hero_allocation="Allocation", hero_history="Value over time",
 hero_demo_note="Illustration with made-up figures.", hero_exports="PDF and CSV",
 hero_history_desc="Example portfolio value in Norwegian kroner from May to October. The value fluctuates from NOK 35,000 at the start to NOK 99,298 at the end. Deposits and withdrawals can affect value; this is not an investment-return chart.",
 hero_months=("May", "Jun", "Jul", "Aug", "Sep", "Oct"),
 story_lines=("Clarity every day.", "Reports when you need them."),
 story_intro="Follow your portfolio, stay informed and bring together the figures for your tax return.",
 story_daily="01 / THROUGHOUT THE YEAR", story_daily_h="See what you own. Understand its history.",
 story_report="02 / WHEN YOU NEED IT", story_report_h="From overview to report.",
 story_example="Simplified example", story_transactions="Transaction history",
 story_transaction_note="Buys, sells and rewards", story_columns=("Date", "Event", "Asset", "Value (NOK)"),
 story_rows=(("19 Jan 2025", "Buy", "ETH", "67,200", "buy"),
             ("6 Feb 2025", "Buy", "XRP", "8,663", "buy"),
             ("14 Mar 2025", "Reward", "ETH", "139", "reward"),
             ("19 Apr 2025", "Sell", "BTC", "19,950", "sell")),
 story_caption="Simplified view with made-up transactions.", story_portfolio="Explore the portfolio",
 story_report_title="Annual overview", story_report_example="Example report · 2025",
 story_report_items=(("Gains", "NOK 7,527"), ("Losses", "NOK 6,616"), ("Income", "NOK 428"), ("Wealth", "NOK 99,298")),
 story_report_link="View example report", story_report_formats="PDF and CSV for your records",
 story_news_kicker="NEWS AND KNOW-HOW", story_news_h="Crypto news and guides",
 story_news_intro="Follow the market and find explanations along the way.", story_news_link="Explore crypto news", story_guides_link="Find a guide",
 story_local="Local on Windows and Android.", story_privacy="Read about privacy",
 sheet_title="From transactions ...",
 rows=[("19 Jan 2025", "Buy 2 ETH", "NOK 67,200"), ("6 Feb 2025", "Buy 1,500 XRP", "NOK 8,663"),
       ("14 Mar 2025", "Staking reward ETH", "NOK 139"), ("19 Apr 2025", "Sell 0.02 BTC", "NOK 19,950"),
       ("13 Jun 2025", "Swap XRP to ETH", "NOK 2,625"), ("30 Sep 2025", "Sell 1 ETH", "NOK 27,300")],
 into="... to the figures in your tax return",
 fields=[("Wealth", "Formuesverdi", "NOK 99,298", ""), ("Taxable gain", "Skattepliktig gevinst", "NOK 7,527", "gain"),
         ("Deductible loss", "Fradragsberettiget tap", "NOK 6,616", "loss"), ("Other income", "Andre inntekter: staking, rewards", "NOK 428", "")],
 cap='Example: tax year 2025 with made-up figures, taken from the <a href="eksempel/Kryptokompis-example-report-2025.pdf">example report</a>.',
 flag_label="Norwegian flag", flag_tag="Norwegian rules",
 pf_free="Free", pf_h="Your crypto portfolio, automatic",
 pf_sub="Like a price tracker, without typing anything in: Kryptokompis fetches your holdings from your exchanges and shows what it is all worth now, in NOK.",
 pf_list=["Every exchange added up: one holding per coin, Earn and futures included",
          "Value in NOK, change over the last 24 hours and share of the portfolio",
          "Updates by itself while the app is open",
          "Average cost and unrealised gain or loss per coin",
          "Only export files? Then holdings are worked out from the transactions"],
 pf_cols=("Coin", "Value", "24 h", "Share"),
 pf_rows=[("BTC", "0.04", "NOK 39,480", "+1.2 %", "39.8 %", 40), ("ETH", "1.09", "NOK 37,769", "−0.8 %", "38.0 %", 38), ("XRP", "1,000", "NOK 22,050", "+3.1 %", "22.2 %", 22)],
 pf_total="Total", pf_total_v="NOK 99,298", pf_change="+NOK 827 (+0.8 %) last 24 hours", pf_change_pct="+0.8 %", pf_cap="Example with made-up figures, added up from Kraken, Binance and Coinbase.",
 hero_pf_title="Your portfolio", hero_tax_title="... and the figures for your tax return",
 hero_tax=[("Taxable gain", "NOK 7,527", "gain"), ("Deductible loss", "NOK 6,616", "loss"), ("Wealth", "NOK 99,298", "")],
 hero_cap='Example with made-up figures, from the <a href="eksempel/Kryptokompis-example-report-2025.pdf">example report</a>.',
 tax_h="Crypto tax for Norway", tax_sub="A crypto tax report that follows the Norwegian rules, with the figures ready for the Virtuelle eiendeler card in your tax return.",
 out_list=["The figures for the tax return, in the same order as its fields",
           "Every sale and swap with its FIFO working: which purchases were used, at what price",
           "Wealth at 31.12 with the prices used",
           "Futures summarised per category, with every item in its own CSV",
           "A PDF to show Skatteetaten or your accountant, and CSV files for Excel"],
 files=[("eksempel/Kryptokompis-example-report-2025.pdf", "Example report (PDF)"), ("eksempel/fifo_transactions_2025_en.csv", "Example CSV")],
 rules_h="How it is calculated",
 rules=[("FIFO per coin", "First purchase out first, across all your exchanges."),
        ("Swapping coins", "Is a sale, also to and from stablecoins."),
        ("Transfers between your own accounts", "Are not a sale."),
        ("Fees paid in coin", "Count as a small sale of that coin."),
        ("Staking and rewards", "Income at market value, which also becomes the cost."),
        ("Gains and losses", "Reported separately, never netted."),
        ("Wealth", "Market value at 31.12. Cash on exchanges is shown separately.")],
 rules_note="The ruleset is called NO-krypto-2026.1 and is stated in every report.",
 imp_h="Transactions and cost basis", imp_sub="Kryptokompis collects your history and gives every purchase the right cost in NOK. Most of your work is connecting the exchanges the first time.",
 imp=[("Read-only API keys", "Exchanges sync automatically in the background. Kryptokompis can never trade or withdraw."),
      ("Or the exchange's own export file", "Upload the file and Kryptokompis recognises the exchange. Importing the same period again is safe - nothing is counted twice."),
      ("Crypto cost basis, in NOK", "Every purchase gets its cost on its own date, at Norges Bank's daily rate. It follows the coin through swaps and transfers."),
      ("Old losses can count again", "Holding coins from the last bull run at a loss? Import the old history and the real loss is calculated when you sell - never more than you actually lost.")],
 ex_cols=("Exchange", "How", "What is covered"),
 ex=[("Kraken", "API", "Spot, futures, staking and Earn rewards, deposits and withdrawals"),
     ("Binance", "API", "Spot trades, deposits and withdrawals"),
     ("Coinbase", "API or file", "Buys, sells, converts, sends, receives and rewards"),
     ("KuCoin", "API and file", "Last 12 months via API, older years from KuCoin's export file"),
     ("Firi", "File", "Trades, staking rewards, deposits, withdrawals and fees"),
     ("Revolut X", "File", "Buys, sells, sends and fees"),
     ("Others", "Template", "Other exchanges and wallets via the Kryptokompis import template")],
 file_word=("File", "Template"),
 ex_more=f'Exchange missing? Tell us on <a href="{{DISCORD}}">Discord</a> and it gets added.',
 ins_h="Insights and alerts", ins_sub="Kryptokompis tells you when something doesn't add up, instead of guessing.",
 ins=[("Checks before you file", "Holdings are reconciled with what the exchanges say you own, and the report is marked provisional or final."),
      ("Gaps in your data", "Sales without purchase history, amounts without a NOK rate, coins without a price and trades stored twice are flagged."),
      ("Results per coin and period", "Realised gains and losses, fees and win rate per coin - per week, month or year. Needs a licence."),
      ("Alerts in the app", "When a new version is out, and when a cost over NOK 10,000 wasn't paid via a bank and may not be deductible.")],
 go_h="Get started", go_sub="Try it free first. Pay when you need the figures for your tax return.",
 go_steps=[("Download", f'<a class="dl" href="{DL_WIN}" data-goatcounter-click="download-windows" data-goatcounter-title="Download Windows {VERSION}">Windows 10 and 11</a> <a class="dl" href="{DL_APK}" data-goatcounter-click="download-android" data-goatcounter-title="Download Android {VERSION}">Android (APK)</a><br><small>Version {VERSION}. <a href="{{RELEASES}}">All versions</a>. If Windows shows a blue warning: More info, Run anyway.</small>'),
           ("Connect your exchanges", "The portfolio and the checks are free. Total wealth is shown."),
           ("Buy a licence", "The licence unlocks the figures for the tax return, the PDF report and the CSV files.")],
 price_h="Beta licence", amount="99 NOK", once="once",
 price_sub="Kryptokompis is in beta, and the beta licence is sold to the first 50 buyers. It is yours for good.",
 price_list=["The whole program: all exchanges, checks, PDF and CSV", "Updates and new exchanges included",
             "No subscription", "One licence covers both PC and phone", "Direct contact with the developer on Discord"],
 buy="Buy the beta licence - 99 NOK",
 pay_note="Card payment via Stripe. Your licence key is emailed to you straight away. You enter it once - subscriptions renew by themselves in the app.",
 later_h="After the beta", later=[("49 NOK", "per month"), ("399 NOK", "per year"), ("999 NOK", "lifetime")],
 trust_h="Your data",
 trust=[("Stays on your device", "No account and no cloud. Transactions, reports and settings are stored with you."),
        ("Read-only keys", "Kryptokompis can never trade or withdraw. On a PC the API keys are kept in Windows' own credential store."),
        ("Talks only to what it needs", "Your exchanges, public sources for prices and exchange rates, and the Kryptokompis website to check for updates. Feedback is sent only when you press Send, without transaction data.")],
 faq_h="Questions and answers",
 faq=[("How is crypto taxed in Norway?", "Gains on a sale or swap are taxable and losses are deductible, both at 22 %. Staking and other rewards are income. Your crypto also counts towards wealth, at its value on 31.12. Kryptokompis works all of this out in NOK - always check the figures before you file."),
      ("Is this tax advice?", "No. Kryptokompis is a calculation tool that applies the Norwegian rules as it interprets them, and states the ruleset used in every report. You are responsible for your tax return - ask Skatteetaten or an accountant if unsure."),
      ("What about earlier years?", "You choose where full FIFO starts. Years already filed another way stay closed. For coins where you have the full history, the real old purchase prices can be used - so a real loss can be claimed when you sell."),
      ("What about cash on exchanges?", "Dollars and kroner held on an exchange are wealth - normally a claim against the exchange - but not a virtual asset. Kryptokompis shows the balance at the turn of the year separately. Where to report it depends on the balance, the currency and where the exchange is based."),
      ("Which devices?", "Windows PC and Android phone. One licence covers both. iPhone may come later."),
      ("Windows says \u201cWindows protected your PC\u201d. Is it safe?", "The message appears because Kryptokompis is new and has not yet built a reputation with Microsoft, not because anything is wrong. Click <b>More info</b>, then <b>Run anyway</b>. The installer needs no administrator rights and everything goes into your own user folder. Each version's SHA-256 checksum is listed on the downloads page."),
      ("How do I install on Android?", "Download the APK on your phone and open it. The first time, Android asks you to allow installs from your browser - allow it this once. A Play Store version comes later, with automatic updates."),
      ("Can I deduct Kryptokompis on my tax?", "Costs of managing your crypto, such as a tool for overview and tax, can normally be claimed as management costs (forvaltningskostnader) in the Norwegian tax return. The deduction is worth 22 % of the amount (18.5 % in Nord-Troms and Finnmark). Keep the receipt. Check what applies to you with Skatteetaten - this is not tax advice."),
      ("How do I get help?", f'Ask on <a href="{{DISCORD}}">Discord</a>, or send a message from the app: Data &amp; setup, Feedback and requests.')],
 warn="<b>Important:</b> the result is only as complete as the data you give Kryptokompis. Transactions it never sees - other exchanges, wallets, history an exchange no longer provides - must be imported, or the result will be wrong. The checks help you find gaps.",
 foot_p="Made in Norway. Not tax advice - you are responsible for your tax return.",
 foot_links=[("terms.html", "Terms"), ("privacy.html", "Privacy"), ("info-en.html", "Info"), ("{DISCORD}", "Discord"), ("{RELEASES}", "Downloads"), ("index.html", "Norsk")],
),
}
# fill in the shared links
for _t in T.values():
    for _k, _v in list(_t.items()):
        if isinstance(_v, str):
            _t[_k] = _v.replace("{DISCORD}", DISCORD).replace("{RELEASES}", RELEASES)
        elif isinstance(_v, list):
            _t[_k] = [tuple(x.replace("{DISCORD}", DISCORD).replace("{RELEASES}", RELEASES) if isinstance(x, str) else x for x in i)
                      if isinstance(i, tuple) else i for i in _v]


def head(t, title, desc, path=None, body_class=""):
    url = f"{SITE_URL}/{path or t['file']}"
    return f"""<!doctype html>
<html lang="{t['lang']}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{'#F5FAFF' if body_class == 'home-blue' else '#F4F7F5'}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Kryptokompis">
<meta property="og:title" content="{t.get('og_title', title)}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:locale" content="{t['locale']}">
<meta property="og:image" content="{SITE_URL}/assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="nb" href="{SITE_URL}/index.html"><link rel="alternate" hreflang="en" href="{SITE_URL}/en.html">
<link rel="alternate" type="application/rss+xml" title="{'Kryptokompis - guider og nyheter' if t['lang'] == 'nb' else 'Kryptokompis - guides and news'}" href="{SITE_URL}/{'rss.xml' if t['lang'] == 'nb' else 'rss-en.xml'}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="icon.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>{CSS}</style>
<script data-goatcounter="https://duplexsteel.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script></head><body{f' class="{body_class}"' if body_class else ''}>
"""


# ---------------------------------------------------------------------------------------------
# Page structure (2026-10-18): a short front page that sums up the app and sends people on to one
# page per topic. PAGES maps a topic to its file per language; the old one-page anchors
# (index.html#skatt etc.) are forwarded by OLD_ANCHORS so links already shared keep working.
PORTAL = "https://billing.stripe.com/p/login/4gM28r4nj6pf3oG257eUU00"     # Stripe customer portal: cancel / change card
LICENCE_API = "https://kryptokompis-licence.kryptokompis.workers.dev"     # licence-service/: /resend for a lost key
PLAN_LINKS = {"month": "https://buy.stripe.com/28EeVd1b700RcZg113eUU01?prefilled_promo_code=START99",
              "year": "https://buy.stripe.com/cNi9ATg61bJzaR8dNPeUU02",
              "life": "https://buy.stripe.com/bJe5kD5rnaFv0cueRTeUU03"}
PLANS_LIVE = True       # licences are delivered and renewed by the licence service (licence-service/)

PAGES = {
    "nb": dict(portfolio="portefolje.html", tax="skatt.html", imports="borser.html", insights="innsikt.html",
               pricing="priser.html", faq="sporsmal.html", guides="guider.html", blog="blogg.html", news="kryptonytt.html"),
    "en": dict(portfolio="portfolio.html", tax="tax.html", imports="exchanges.html", insights="insights.html",
               pricing="pricing.html", faq="faq.html", guides="guides.html", blog="blog.html", news="crypto-news.html"),
}
OLD_ANCHORS = {
    "nb": {"portefolje": "portefolje.html", "skatt": "skatt.html", "import": "borser.html", "innsikt": "innsikt.html",
           "kom-i-gang": "priser.html#kom-i-gang", "data": "innsikt.html#data", "sporsmal": "sporsmal.html"},
    "en": {"portfolio": "portfolio.html", "tax": "tax.html", "imports": "exchanges.html", "insights": "insights.html",
           "get-started": "pricing.html#get-started", "data": "insights.html#data", "faq": "faq.html"},
}

ICON = {   # simple line icons for the feature cards (24x24, stroke = currentColor)
    "pie": '<path d="M12 3a9 9 0 1 0 9 9h-9z"/><path d="M15 3.5A9 9 0 0 1 20.5 9H15z"/>',
    "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "plug": '<path d="M9 3v5M15 3v5M7 8h10v3a5 5 0 0 1-10 0zM12 16v5"/>',
    "check": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "lock": '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "dev": '<rect x="2" y="4" width="14" height="10" rx="1.5"/><path d="M6 18h6"/><rect x="17" y="8" width="5" height="12" rx="1.2"/>',
}

X = {
    "nb": dict(
        feat_h="Alt på ett sted", feat_sub="Kryptokompis gjør to jobber: holder oversikt over kryptoen din hver dag, og regner ut skatten når skattemeldingen kommer.",
        more="Les mer",
        feats=[("pie", "Portefølje", "Alle myntene fra alle børsene lagt sammen, med verdi i kroner og endring siste 24 timer. Oppdateres av seg selv.", "portfolio", "Gratis"),
               ("doc", "Kryptoskatt", "Gevinst, tap, inntekt og formue etter norske regler, klart for kortet Virtuelle eiendeler. Med PDF og CSV som dokumentasjon.", "tax", ""),
               ("plug", "Børser og import", "Kraken, Binance, Coinbase og KuCoin med API-nøkkel som bare kan lese. Firi, Revolut X og resten med fil.", "imports", ""),
               ("check", "Kontroller", "Beholdningen avstemmes mot børsene, og du får beskjed om hull i stedet for at appen gjetter.", "insights", ""),
               ("lock", "Dataene blir hos deg", "Ingen konto og ingen sky. Alt lagres på din PC eller mobil, og nøklene kan aldri handle eller ta ut penger.", "insights#data", ""),
               ("dev", "PC og mobil", "Windows 10 og 11, og Android. Én lisens gjelder begge, og nye versjoner installeres med ett klikk.", "pricing#kom-i-gang", "")],
        ex_h="Fungerer med", ex_chips=["Kraken", "Binance", "Coinbase", "KuCoin", "Firi", "Revolut X", "Alle andre via mal"],
        tiers_h="Priser", tiers_sub="Porteføljen er gratis. Du betaler når du trenger tallene til skattemeldingen.",
        tiers=[("Beta", "99 kr", "én gang", "Livstidslisens til de første 50. Oppdateringer og nye børser inkludert.", "beta", "Kjøp betalisens"),
               ("Måned", "49 kr", "per måned", "De tre første månedene for 99 kr til sammen. Si opp når du vil.", "month", "Velg måned"),
               ("År", "399 kr", "per år", "Det samme som 33 kr i måneden. Si opp når du vil.", "year", "Velg år"),
               ("Livstid", "999 kr", "én gang", "Betal én gang og bruk Kryptokompis for alltid.", "life", "Kjøp livstid")],
        soon="Etter betaen", now_tag="Nå", all_prices="Se alle detaljer om priser",
        deduct_h="Tips: Kryptokompis kan gi fradrag",
        deduct='Kostnader du har for å forvalte kryptoen din, som et verktøy for oversikt og skatt, kan normalt føres som <b>forvaltningskostnader</b> i skattemeldingen. Fradraget er verdt 22 % av beløpet (18,5 % i Nord-Troms og Finnmark). 399 kr i året kan altså gi omtrent 88 kr lavere skatt. Ta vare på kvitteringen. Dette er ikke skatterådgivning - sjekk hva som gjelder for deg hos <a href="https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/aksjer-og-verdipapirer/om/virtuelle-eiendeler/">Skatteetaten</a>.',
        portal_h="Abonnement", portal_p="Du administrerer abonnementet selv hos Stripe: si opp, bytt kort eller last ned kvitteringer. Skriv inn e-posten du betalte med, så får du en kode.",
        portal_btn="Administrer eller si opp abonnement",
        lost_h="Mistet lisensnøkkelen?", lost_p="Skriv e-posten du betalte med, så sender vi nøklene dine på nytt.",
        lost_btn="Send nøkkelen på nytt", lost_ok="Hvis vi finner et kjøp på denne adressen, kommer e-posten om et minutt. Sjekk også søppelpost.",
        lost_err="Noe gikk galt. Prøv igjen litt senere, eller spør på Discord.",
        latest_h="Siste guider og nytt", latest_all="Alle guider",
        final_h="Prøv Kryptokompis gratis", final_p="Last ned, koble til børsene og se porteføljen din på få minutter.",
        kicker="Funksjoner",
        pages=dict(
            portfolio=("Kryptoporteføljen din, automatisk", "Se alle myntene dine fra alle børsene på ett sted, med verdien i kroner og endring siste 24 timer."),
            tax=("Kryptoskatt for Norge", "Gevinst, tap, inntekt og formue etter norske regler - klart for skattemeldingen."),
            imports=("Børser og import", "Slik henter Kryptokompis transaksjonene dine, og hvilke børser som støttes."),
            insights=("Kontroller og personvern", "Kryptokompis sier fra når noe ikke stemmer, og dataene dine blir hos deg."),
            pricing=("Priser og nedlasting", "Prøv gratis først. Betal når du trenger tallene til skattemeldingen."),
            faq=("Spørsmål og svar", "Det folk lurer mest på om kryptoskatt og Kryptokompis.")),
        nav_feat="Funksjoner", nav_price="Priser", nav_read="Ressurser", nav_info="Info",
        read_items=[("guides", "Guider"), ("blog", "Blogg"), ("news", "Kryptonytt")],
        info_extra=[("faq", "Spørsmål og svar")],
        foot_extra=[("pricing", "Priser"), (PORTAL, "Administrer abonnement")],
    ),
    "en": dict(
        feat_h="Everything in one place", feat_sub="Kryptokompis does two jobs: keeps track of your crypto every day, and works out the tax when the tax return comes.",
        more="Read more",
        feats=[("pie", "Portfolio", "All your coins from every exchange added up, valued in NOK with the 24-hour change. Updates by itself.", "portfolio", "Free"),
               ("doc", "Crypto tax", "Gains, losses, income and wealth under Norwegian rules, ready for the Virtuelle eiendeler card. With PDF and CSV as documentation.", "tax", ""),
               ("plug", "Exchanges and imports", "Kraken, Binance, Coinbase and KuCoin with a read-only API key. Firi, Revolut X and the rest with a file.", "imports", ""),
               ("check", "Checks", "Holdings are reconciled with the exchanges, and you are told about gaps instead of the app guessing.", "insights", ""),
               ("lock", "Your data stays with you", "No account and no cloud. Everything is stored on your PC or phone, and the keys can never trade or withdraw.", "insights#data", ""),
               ("dev", "PC and phone", "Windows 10 and 11, and Android. One licence covers both, and new versions install with one click.", "pricing#get-started", "")],
        ex_h="Works with", ex_chips=["Kraken", "Binance", "Coinbase", "KuCoin", "Firi", "Revolut X", "Everything else via template"],
        tiers_h="Pricing", tiers_sub="The portfolio is free. You pay when you need the figures for your tax return.",
        tiers=[("Beta", "99 NOK", "once", "Lifetime licence for the first 50. Updates and new exchanges included.", "beta", "Buy the beta licence"),
               ("Monthly", "49 NOK", "per month", "The first three months for 99 NOK in total. Cancel any time.", "month", "Choose monthly"),
               ("Yearly", "399 NOK", "per year", "The same as 33 NOK a month. Cancel any time.", "year", "Choose yearly"),
               ("Lifetime", "999 NOK", "once", "Pay once and use Kryptokompis for good.", "life", "Buy lifetime")],
        soon="After the beta", now_tag="Now", all_prices="See all pricing details",
        deduct_h="Tip: Kryptokompis can be tax deductible",
        deduct='Costs of managing your crypto, such as a tool for overview and tax, can normally be claimed as <b>management costs (forvaltningskostnader)</b> in the Norwegian tax return. The deduction is worth 22 % of the amount (18.5 % in Nord-Troms and Finnmark), so 399 NOK a year can mean about 88 NOK less tax. Keep the receipt. This is not tax advice - check what applies to you with <a href="https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/shares-and-securities/about-shares-and-securities/virtual-currency/">Skatteetaten</a>.',
        portal_h="Subscription", portal_p="You manage your subscription yourself at Stripe: cancel, change card or download receipts. Enter the email you paid with and you get a code.",
        portal_btn="Manage or cancel subscription",
        lost_h="Lost your licence key?", lost_p="Enter the email you paid with and we send your keys again.",
        lost_btn="Send the key again", lost_ok="If we find a purchase for this address, the email arrives within a minute. Check your spam folder too.",
        lost_err="Something went wrong. Try again a bit later, or ask on Discord.",
        latest_h="Latest guides and news", latest_all="All guides",
        final_h="Try Kryptokompis for free", final_p="Download, connect your exchanges and see your portfolio in minutes.",
        kicker="Features",
        pages=dict(
            portfolio=("Your crypto portfolio, automatic", "See all your coins from every exchange in one place, valued in NOK with the 24-hour change."),
            tax=("Crypto tax for Norway", "Gains, losses, income and wealth under Norwegian rules - ready for the tax return."),
            imports=("Exchanges and imports", "How Kryptokompis collects your transactions, and which exchanges are supported."),
            insights=("Checks and privacy", "Kryptokompis tells you when something doesn't add up, and your data stays with you."),
            pricing=("Pricing and download", "Try it free first. Pay when you need the figures for your tax return."),
            faq=("Questions and answers", "What people ask most about crypto tax and Kryptokompis.")),
        nav_feat="Features", nav_price="Pricing", nav_read="Resources", nav_info="Info",
        read_items=[("guides", "Guides"), ("blog", "Blog"), ("news", "Crypto news")],
        info_extra=[("faq", "Questions and answers")],
        foot_extra=[("pricing", "Pricing"), (PORTAL, "Manage subscription")],
    ),
}


def url(t, key):
    """A topic key ('tax', 'pricing#kom-i-gang') -> file name; anything else is returned as is."""
    k, _, frag = key.partition("#")
    f = PAGES[t["lang"]].get(k)
    return (f + (f"#{frag}" if frag else "")) if f else key


def nav(t, home_page=True):           # home_page kept for the callers in build_info / build_guides
    x = X[t["lang"]]
    home = "index.html" if t["lang"] == "nb" else "en.html"
    info = [(i if i.endswith(".html") else t["info"] + "#" + i, lab) for i, lab in t["info_items"] if not i.startswith("guide")]
    info += [(url(t, k), lab) for k, lab in x["info_extra"]]
    groups = [(x["nav_feat"], [(url(t, k), x["pages"][k][0].split(",")[0]) for k in ("portfolio", "tax", "imports", "insights")], "feat-m"),
              (x["nav_read"], [(url(t, k), lab) for k, lab in x["read_items"]], "read-m"),
              (x["nav_info"], info, "info-m")]
    short = {"portfolio": x["feats"][0][1], "tax": x["feats"][1][1], "imports": x["feats"][2][1], "insights": x["pages"]["insights"][0]}
    groups[0] = (x["nav_feat"], [(url(t, k), short[k]) for k in ("portfolio", "tax", "imports", "insights")], "feat-m")
    dd = lambda g: (f'<div class="dd"><button type="button" aria-expanded="false" aria-controls="{g[2]}">{g[0]}</button>'
                    f'<div class="m" id="{g[2]}">' + "".join(f'<a href="{h}">{lab}</a>' for h, lab in g[1]) + "</div></div>")
    desk = dd(groups[0]) + f'<a class="l" href="{url(t, "pricing")}">{x["nav_price"]}</a>' + dd(groups[1]) + dd(groups[2])
    mob = "".join(f'<div class="grp">{g[0]}</div><div class="in">' + "".join(f'<a href="{h}">{lab}</a>' for h, lab in g[1]) + "</div>"
                  for g in groups[:1]) + f'<a href="{url(t, "pricing")}">{x["nav_price"]}</a>' + "".join(
                  f'<div class="grp">{g[0]}</div><div class="in">' + "".join(f'<a href="{h}">{lab}</a>' for h, lab in g[1]) + "</div>" for g in groups[1:])
    start = url(t, "pricing") + "#" + t["ids"][4]
    return f"""<header><div class="w"><nav aria-label="{'Hovedmeny' if t['lang']=='nb' else 'Main'}">
<a class="brand" href="{home}">{MARK}Kryptokompis</a>
{desk}
<span class="sp"></span><a class="lang" href="{t['other']}" lang="{'en' if t['lang']=='nb' else 'nb'}">{'EN' if t['lang']=='nb' else 'NO'}</a>
<a class="btn s" href="{start}">{t['cta']}</a>
<button type="button" class="menu-btn" aria-expanded="false" aria-controls="mob">{t['menu']}</button></nav>
<div class="mobile" id="mob">{mob}<a href="{t['other']}">{t['other_label']}</a></div></div></header>
"""


SCRIPT = """<script>
document.querySelectorAll('.dd>button,.menu-btn').forEach(function(b){
  var panel=document.getElementById(b.getAttribute('aria-controls'));
  b.addEventListener('click',function(e){e.stopPropagation();var o=b.getAttribute('aria-expanded')!=='true';
    document.querySelectorAll('.dd>button').forEach(function(x){if(x!==b)x.setAttribute('aria-expanded','false')});
    b.setAttribute('aria-expanded',o);if(b.classList.contains('menu-btn'))panel.classList.toggle('open',o);});
  panel.addEventListener('click',function(e){if(e.target.tagName==='A'){b.setAttribute('aria-expanded','false');panel.classList.remove('open');}});
});
document.addEventListener('click',function(){document.querySelectorAll('.dd>button').forEach(function(b){b.setAttribute('aria-expanded','false')})});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('[aria-expanded=true]').forEach(function(b){b.click()})});
</script>"""

CSS += """
/* 2026-10-18: front page summary + one page per topic */
.feat{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.feat a{display:flex;flex-direction:column;gap:10px;padding:26px 24px 22px;background:var(--sheet);border:1px solid var(--line);border-radius:14px;
 color:var(--ink);text-decoration:none;transition:border-color .15s,transform .15s,box-shadow .15s}
.feat a:hover{border-color:var(--spruce);transform:translateY(-2px);box-shadow:0 18px 40px -22px rgba(21,48,42,.35);color:var(--ink)}
.feat .ic{width:44px;height:44px;border-radius:12px;background:var(--mint);color:var(--spruce-d);display:grid;place-items:center}
.feat .ic svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.feat h3{display:flex;align-items:center;gap:10px}.feat p{color:var(--ink2);font-size:16px;flex:1}
.feat .go2{font-weight:600;color:var(--spruce-d);font-size:15px}.feat .go2:after{content:" →"}
.feat .tag{font-size:12.5px;font-weight:700;color:var(--spruce-d);background:var(--mint);border-radius:999px;padding:2px 9px}
.chips{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:36px}
.chips b{font-size:15px;color:var(--ink2);font-weight:600;margin-right:6px}
.chips span{padding:7px 14px;border:1px solid var(--line);border-radius:999px;background:var(--sheet);font-weight:600;font-size:15px}
.tiers{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:8px}
.tier{border:1px solid #2F4D45;border-radius:14px;padding:22px 20px;display:flex;flex-direction:column;gap:8px}
.tier.on{border:2px solid var(--mint2);background:rgba(154,216,189,.07)}
.tier h3{display:flex;justify-content:space-between;align-items:center;font-size:18px}
.tier .pill{font-size:12px;font-weight:700;border-radius:999px;padding:2px 9px;background:var(--mint2);color:var(--ink)}
.tier .pill.soon{background:transparent;border:1px solid #4A6A61;color:#B9CCC3}
.tier .p{font-size:36px;font-weight:800;color:#fff;letter-spacing:-.02em;line-height:1.1}.tier .p small{font-size:15px;font-weight:500;color:#B9CCC3;margin-left:6px}
.tier p{color:#B9CCC3;font-size:15px;flex:1}.tier .btn{margin-top:6px;width:100%}
.tier .btn.off{background:transparent;border-color:#4A6A61;color:#B9CCC3;pointer-events:none}
.tip{margin-top:28px;padding:20px 22px;border-radius:var(--r);background:rgba(154,216,189,.1);border:1px solid #2F4D45}
.lost{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.lost input{flex:1 1 220px;min-height:40px;border-radius:999px;border:1px solid #4A6A61;
 background:rgba(255,255,255,.06);color:#fff;padding:0 16px;font:inherit;font-size:15px}.lost-msg{margin-top:10px;color:var(--mint2)!important}
.tip h3{font-size:17px;margin-bottom:6px}.tip p{color:#CFE0D8;font-size:15.5px}
.latest{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.latest a{display:block;padding:22px;border:1px solid var(--line);border-radius:14px;background:var(--sheet);color:var(--ink);text-decoration:none}
.latest a:hover{border-color:var(--spruce)}.latest small{color:var(--ink2)}.latest b{display:block;font-size:18px;margin:6px 0}
.latest span{color:var(--ink2);font-size:15.5px}
.headrow{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-bottom:28px}
.phead{padding:64px 0 8px}.phead .kick{font-weight:700;color:var(--spruce-d);font-size:15px;margin-bottom:10px}
.phead h1{font-size:clamp(34px,5vw,54px);margin-bottom:16px}
.final{text-align:center}.final .cta{justify-content:center}.final .sub{margin:12px auto 0}
.final .dl{margin:0 6px}
@media (max-width:900px){.feat,.latest{grid-template-columns:1fr 1fr}.tiers{grid-template-columns:1fr 1fr}}
@media (max-width:600px){.feat,.latest,.tiers{grid-template-columns:1fr}.phead{padding-top:40px}}
"""


def footer(t):
    x = X[t["lang"]]
    links = [(url(t, h), lab) for h, lab in x["foot_extra"]] + list(t["foot_links"])
    links = "".join(f'<li><a href="{h}">{lab}</a></li>' for h, lab in links)
    home = "index.html" if t["lang"] == "nb" else "en.html"
    return f"""<footer><div class="w foot"><div><a class="brand" href="{home}">{MARK}Kryptokompis</a><p><span class="made">{FLAG.format(label=t['flag_label'])}{t['foot_p']}</span></p></div>
<ul>{links}</ul></div></footer>
{SCRIPT}
</body></html>
"""


# --- sections (each used on its own page; head=False when the page header already says it) ---
def _li(xs):
    return "".join(f"<li>{x}</li>" for x in xs)


def _head(h, sub, show):
    return f'<div class="head"><h2>{h}</h2><p class="sub">{sub}</p></div>' if show else ""


def sec_portfolio(t, head=True):
    pfr = "".join(f'<tr><td>{a}</td><td>{v}</td><td class="{"up" if ch.startswith("+") else "down"}">{ch}</td><td>{sh}</td></tr>'
                  for a, q, v, ch, sh, w in t["pf_rows"])
    return f"""<section id="{t['ids'][0]}" class="band"><div class="w pf">
 <div><span class="free-tag">{t['pf_free']}</span>{f"<h2>{t['pf_h']}</h2><p class='sub'>{t['pf_sub']}</p>" if head else ""}<ul class="ck">{_li(t['pf_list'])}</ul></div>
 <figure class="sheet" style="margin:0"><table class="hold"><thead><tr>{"".join(f"<th>{c}</th>" for c in t['pf_cols'])}</tr></thead>
  <tbody>{pfr}<tr class="t"><td>{t['pf_total']}</td><td>{t['pf_total_v']}</td><td class="up">{t['pf_change_pct']}</td><td>100 %</td></tr></tbody></table>
  <figcaption class="cap">{t['pf_cap']}</figcaption></figure>
</div></section>"""


def sec_tax(t, head=True):
    rows = "".join(f'<li><span class="d">{d}</span><span>{w}</span><span class="v">{v}</span></li>' for d, w, v in t["rows"])
    fields = "".join(f'<tr><td>{a}{f"<small>{b}</small>" if b else ""}</td><td class="{c}">{v}</td></tr>' for a, b, v, c in t["fields"])
    files = "".join(f'<a class="btn g s" href="{h}">{lab}</a>' for h, lab in t["files"])
    rules = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in t["rules"])
    return f"""<section id="{t['ids'][1]}"><div class="w">
 {_head(t['tax_h'], t['tax_sub'], head)}
 <div class="out">
  <div><ul class="ck">{_li(t['out_list'])}</ul><div class="files">{files}</div>
   <h3 style="margin-top:40px">{t['rules_h']}</h3><dl class="rules">{rules}</dl><p class="note">{t['rules_note']}</p></div>
  <figure class="sheet" style="margin:0;align-self:start"><h3>{t['sheet_title']}</h3><ul class="rows">{rows}</ul>
   <div class="into">{t['into']}</div><table class="fields">{fields}</table>
   <figcaption class="cap">{t['cap']}</figcaption></figure>
 </div>
</div></section>"""


def sec_imports(t, head=True):
    imp = "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in t["imp"])
    ex = "".join(f'<tr><td>{n}</td><td><span class="how{" f" if h in t["file_word"] else ""}">{h}</span></td><td>{c}</td></tr>' for n, h, c in t["ex"])
    return f"""<section id="{t['ids'][2]}" class="band"><div class="w">
 {_head(t['imp_h'], t['imp_sub'], head)}
 <div class="grid4">{imp}</div>
 <table class="ex"><thead><tr><th>{t['ex_cols'][0]}</th><th>{t['ex_cols'][1]}</th><th>{t['ex_cols'][2]}</th></tr></thead><tbody>{ex}</tbody></table>
 <p class="note">{t['ex_more']}</p>
</div></section>"""


def sec_insights(t, head=True):
    ins = "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in t["ins"])
    return f"""<section id="{t['ids'][3]}"><div class="w">
 {_head(t['ins_h'], t['ins_sub'], head)}
 <div class="grid4 ins">{ins}</div>
</div></section>"""


def sec_trust(t):
    trust = "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in t["trust"])
    return f"""<section id="{t['ids'][5]}" class="band"><div class="w">
 <div class="head"><h2>{t['trust_h']}</h2></div><div class="trust">{trust}</div>
</div></section>"""


def tiers(t, buy_links=True):
    x = X[t["lang"]]
    out = []
    for name, amount, per, txt, key, btn in x["tiers"]:
        live = key == "beta" or PLANS_LIVE
        href = BUY if key == "beta" else PLAN_LINKS[key]
        pill = f'<span class="pill">{x["now_tag"]}</span>' if key == "beta" else ""
        b = (f'<a class="btn s" href="{href}" target="_blank" rel="noopener" data-goatcounter-click="buy-{key}">{btn}</a>' if live
             else f'<span class="btn s off">{x["soon"]}</span>') if buy_links else ""
        out.append(f'<div class="tier{" on" if key == "beta" else ""}"><h3>{name}{pill}</h3><div class="p">{amount}<small>{per}</small></div><p>{txt}</p>{b}</div>')
    return '<div class="tiers">' + "".join(out) + "</div>"


def sec_start(t, head=True):
    x = X[t["lang"]]
    go = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in t["go_steps"])
    return f"""<section id="{t['ids'][4]}" class="dark"><div class="w">
 {_head(t['go_h'], t['go_sub'], head)}
 <ol class="steps go">{go}</ol>
 <div class="head" style="margin-bottom:20px"><h2>{x['tiers_h']}</h2><p class="sub">{x['tiers_sub']}</p></div>
 {tiers(t)}
 <p class="note">{t['pay_note']}</p>
 <div class="tip"><h3>{x['deduct_h']}</h3><p>{x['deduct']}</p></div>
 <div class="tip"><h3>{x['portal_h']}</h3><p>{x['portal_p']}</p><div class="cta" style="margin-top:14px"><a class="btn s" href="{PORTAL}" target="_blank" rel="noopener">{x['portal_btn']}</a></div></div>
 <div class="tip" id="lost"><h3>{x['lost_h']}</h3><p>{x['lost_p']}</p>
  <form class="lost" onsubmit="return lostKey(this)"><input type="email" name="email" required autocomplete="email" placeholder="navn@epost.no" aria-label="E-post">
  <button class="btn s" type="submit">{x['lost_btn']}</button></form><p class="lost-msg" role="status" aria-live="polite"></p></div>
<script>function lostKey(f){{var m=f.parentNode.querySelector('.lost-msg');f.querySelector('button').disabled=true;
fetch('{LICENCE_API}/resend',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify({{email:f.email.value}})}})
.then(function(r){{m.textContent=r.ok?{json.dumps(x['lost_ok'])}:{json.dumps(x['lost_err'])}}})
.catch(function(){{m.textContent={json.dumps(x['lost_err'])}}}).finally(function(){{f.querySelector('button').disabled=false}});return false}}</script>
</div></section>"""


def sec_faq(t):
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    return f"""<section id="{t['ids'][6]}"><div class="w">
 <div class="faq">{faq}</div>
 <p class="warn">{t['warn']}</p>
</div></section>"""


def final_cta(t):
    x = X[t["lang"]]
    return f"""<section class="dark final"><div class="w">
 <h2>{x['final_h']}</h2><p class="sub">{x['final_p']}</p>
 <div class="cta"><a class="btn" href="{DL_WIN}" data-goatcounter-click="download-windows" data-goatcounter-title="Download Windows {VERSION}">Windows</a>
 <a class="btn" href="{DL_APK}" data-goatcounter-click="download-android" data-goatcounter-title="Download Android {VERSION}">Android (APK)</a>
 <a class="btn g" style="color:#fff;border-color:#fff" href="{url(t, 'pricing')}">{x['nav_price']}</a></div>
</div></section>"""


HOME_HERO_CSS = """
/* Approved homepage hero. Keep this scoped so topic pages retain their layout. */
.home-blue{--paper:#F5FAFF;--ink:#10254A;--ink2:#425675;--line:#D7E4F4;
 --spruce:#1260E8;--spruce-d:#0B4DC2;--mint:#E6F2FF;--mint2:#B8D9FF;--dark:#10254A}
.home-blue header{background:rgba(255,255,255,.96);border-bottom-color:#E4EDFA}
.home-blue header .w{max-width:1440px;padding-inline:32px}
.home-blue .brand .mark{color:#1260E8}
.home-blue .tier{border-color:#365078}.home-blue .tier.on{background:rgba(184,217,255,.07)}
.home-blue .tier p,.home-blue .tier .p small{color:#CBD9EF}
.brand-hero{position:relative;isolation:isolate;background:#F0F7FF;overflow:hidden}
.brand-hero:before{content:"";position:absolute;inset:0;z-index:-1;
 background:linear-gradient(90deg,rgba(248,252,255,.98) 0%,rgba(248,252,255,.88) 35%,rgba(240,247,255,.1) 75%),
 url('assets/hero-mountains.webp') right bottom/cover no-repeat}
.brand-hero:after{content:"";position:absolute;inset:auto 0 0;height:64px;z-index:-1;
 background:linear-gradient(transparent,var(--paper))}
.hero-shell{max-width:1440px;margin:0 auto;padding:64px 32px 78px;display:grid;
 grid-template-columns:1.04fr 1fr;gap:30px;align-items:center}
.hero-copy{position:relative;z-index:2;min-width:0}
.hero-kicker{font-size:14px;font-weight:700;letter-spacing:.055em;color:#0B4DC2;margin-bottom:18px}
.hero-copy h1{font-size:clamp(40px,5.1vw,72px);line-height:1.07;letter-spacing:-.045em;margin-bottom:25px}
.hero-copy h1 span{display:block}.hero-copy h1 .accent{color:#1260E8}
.hero-copy .hero-intro,.hero-copy .hero-import{font-size:clamp(17px,1.4vw,20px);line-height:1.55;max-width:31em}
.hero-copy .hero-import{margin-top:16px;color:var(--ink2)}
.hero-copy .cta{gap:12px;margin-top:28px}.hero-copy .btn{min-height:54px;padding:0 22px}
.hero-copy .hero-secondary{background:#fff;border-color:#fff;color:#0B4DC2;box-shadow:0 5px 20px #163C6D08}
.hero-copy .hero-secondary:hover{background:#E6F2FF;border-color:#D7E4F4;color:#10254A}
.hero-copy .btn svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.hero-copy .note{font-size:14px;margin-top:20px}
.hero-scene{position:relative;min-width:0;min-height:590px;display:flex;align-items:flex-start;padding-top:12px}
.hero-portfolio{width:73%;max-width:400px;position:relative;z-index:1;margin:0;padding:24px;
 background:rgba(255,255,255,.97);border:1px solid #E2ECF8;border-radius:22px;box-shadow:0 18px 55px #17457C13}
.demo-heading{display:flex;align-items:center;justify-content:space-between;gap:8px}
.demo-heading h2{font-size:17px;line-height:1.3;letter-spacing:-.02em}
.demo-badge{font-size:11px;color:#425675;background:#EDF4FF;border-radius:999px;padding:5px 9px;white-space:nowrap}
.demo-total{font-size:39px;line-height:1.2;font-weight:800;letter-spacing:-.045em;margin:10px 0 18px}
.demo-distribution{border-top:1px solid #E4ECF8;border-bottom:1px solid #E4ECF8;padding:19px 0;
 display:flex;align-items:center;gap:20px}
.demo-donut{width:132px;aspect-ratio:1;flex:none;border-radius:50%;display:grid;place-items:center;
 background:conic-gradient(#1260E8 0% 45%,#21A9B0 45% 78%,#A989EF 78% 100%)}
.demo-donut span{display:grid;place-items:center;width:68%;height:68%;background:#fff;border-radius:50%;
 font-size:12px;font-weight:700;color:#10254A}
.demo-legend{list-style:none;margin:0;padding:0;flex:1;font-size:13px}
.demo-legend li{display:flex;align-items:center;gap:8px;padding:7px 0}
.demo-legend .dot{width:10px;height:10px;border-radius:50%;background:var(--coin);flex:none}
.demo-legend b{font-weight:700}.demo-legend .share{margin-left:auto;color:#425675;white-space:nowrap}
.demo-history{margin:18px 0 0}.demo-history h3{font-size:15px;margin-bottom:12px}
.demo-chart{width:100%;height:auto;overflow:visible;font-family:inherit}
.demo-chart text{fill:#536989;font-size:10px}.demo-chart .grid{stroke:#E1EAF7;stroke-dasharray:3 4;stroke-width:1}
.demo-chart .value-line{stroke:#1260E8;stroke-width:2.7;stroke-linecap:round;stroke-linejoin:round;fill:none}
.demo-chart .endpoint{fill:#fff;stroke:#1260E8;stroke-width:2.7}
.demo-chart .end-label{fill:#10254A;font-size:10px;font-weight:600}
.demo-export{display:flex;gap:10px;align-items:center;margin-top:16px;padding-top:16px;border-top:1px solid #E4ECF8;
 font-size:14px;color:#10254A;text-decoration:none}
.demo-export svg{width:19px;height:19px;fill:none;stroke:#1260E8;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.demo-export .export-arrow{margin-left:auto}.demo-export:hover{color:#0B4DC2}
.hero-portfolio figcaption{font-size:10.5px;color:#536989;margin-top:11px}
.hero-fox{position:absolute;z-index:2;right:-45px;bottom:0;width:50%;height:auto;pointer-events:none;
 filter:drop-shadow(0 14px 14px #163B7010)}
@media(min-width:1500px){.hero-copy h1{font-size:76px}}
@media(max-width:1100px) and (min-width:901px){
 .hero-shell{gap:24px;padding:52px 28px 70px;grid-template-columns:1fr 1fr}
 .hero-copy h1{font-size:52px}.hero-copy .cta{flex-direction:column;align-items:flex-start}
 .hero-scene{min-height:570px;padding-bottom:92px}.hero-portfolio{width:82%;padding:20px}.demo-distribution{gap:12px}
 .demo-donut{width:112px}.demo-legend{font-size:12px}.hero-fox{width:190px;right:-14px;bottom:-58px}
}
@media(max-width:900px){
 .hero-shell{grid-template-columns:1fr;gap:30px;padding:44px 28px 56px;max-width:760px}
 .hero-copy h1{font-size:clamp(40px,7.6vw,65px)}.hero-copy .hero-intro,.hero-copy .hero-import{max-width:34em}
 .hero-scene{min-height:560px;width:100%;max-width:660px;margin:0 auto;padding-top:0}
 .hero-portfolio{width:70%;max-width:440px}.hero-fox{right:-10px;bottom:-4px;width:38%;max-width:260px}
 .brand-hero:before{background-position:center bottom;background-size:auto 100%}
 .home-blue header .w{padding-inline:24px}
}
@media(max-width:600px){
 .home-blue header .w{padding-inline:16px}.home-blue nav{gap:10px}.home-blue header .brand{font-size:17px;gap:6px}
 .home-blue header .brand .mark{width:24px;height:24px}.home-blue header .btn.s{font-size:13px;min-height:36px;padding:0 10px}
 .hero-shell{padding:35px 20px 40px;gap:30px}.hero-kicker{font-size:12px;margin-bottom:14px}
 .hero-copy h1{font-size:clamp(35px,9.25vw,53px);letter-spacing:-.045em;margin-bottom:20px}
 .hero-copy .hero-intro,.hero-copy .hero-import{font-size:17px;line-height:1.55}
 .hero-copy .cta{gap:10px;margin-top:23px}.hero-copy .btn{min-height:50px;font-size:15px}
 .hero-copy .note{font-size:12px;margin-top:15px}
 .hero-scene{min-height:0;display:block;padding-bottom:104px}
 .hero-portfolio{width:100%;max-width:none;padding:20px;border-radius:18px}
 .demo-heading h2{font-size:16px}.demo-total{font-size:36px}.demo-distribution{gap:24px}
 .demo-donut{width:122px}.demo-legend{font-size:13px}.demo-badge{font-size:10px}
 .hero-fox{width:145px;right:-13px;bottom:-3px;max-width:none}
 .hero-portfolio figcaption{max-width:175px}.demo-export{padding-right:75px}
}
@media(max-width:359px){
 .hero-shell{padding-inline:16px}.hero-copy h1{font-size:33px}.home-blue header .btn.s{display:none}
 .demo-distribution{gap:14px}.demo-donut{width:108px}.hero-portfolio{padding:16px}
}
"""
CSS += HOME_HERO_CSS


# Fictional marketing data: NOK values, not investment returns or live quotes.
HERO_VALUES = (35000, 40500, 38000, 47000, 52000, 59000, 56000, 46000, 42000,
               49000, 53500, 60000, 65000, 61000, 74500, 79000, 85000, 92000,
               81000, 76000, 69000, 73500, 78000, 86000, 82000, 91000, 95000, 99298)
HERO_ALLOCATION = (("BTC", 45, "#1260E8"), ("ETH", 33, "#21A9B0"), ("XRP", 22, "#A989EF"))


def hero_history(t):
    """An accessible, static example chart; axes and endpoint use the same NOK data."""
    left, right, top, bottom, maximum = 42, 346, 16, 132, 120000
    points = [(left + i * (right - left) / (len(HERO_VALUES) - 1),
               bottom - v * (bottom - top) / maximum) for i, v in enumerate(HERO_VALUES)]
    line = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in points)
    area = line + f" L{right},{bottom} L{left},{bottom} Z"
    grid = "".join(
        f'<line class="grid" x1="{left}" x2="{right}" y1="{bottom - value * (bottom - top) / maximum:.2f}" y2="{bottom - value * (bottom - top) / maximum:.2f}"/>'
        f'<text x="34" y="{bottom - value * (bottom - top) / maximum + 3:.2f}" text-anchor="end">{value // 1000}k</text>'
        for value in (0, 40000, 80000, 120000))
    months = "".join(f'<text x="{left + i * (right - left) / 5:.2f}" y="153" text-anchor="middle">{month}</text>'
                     for i, month in enumerate(t["hero_months"]))
    x, y = points[-1]
    return f'''<svg class="demo-chart" viewBox="0 0 364 162" role="img" aria-labelledby="history-title history-desc">
<title id="history-title">{t['hero_history']}</title><desc id="history-desc">{t['hero_history_desc']}</desc>
<defs><linearGradient id="history-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1260E8" stop-opacity=".17"/><stop offset="100%" stop-color="#1260E8" stop-opacity=".02"/></linearGradient></defs>
{grid}<path d="{area}" fill="url(#history-fill)"/><path class="value-line" d="{line}"/>
<circle class="endpoint" cx="{x:.2f}" cy="{y:.2f}" r="4"/>
<text class="end-label" x="{x}" y="{y - 12:.2f}" text-anchor="end">{t['pf_total_v']}</text>{months}</svg>'''


def homepage_hero(t):
    headline = "".join(f'<span class="accent">{line}</span>' if i == 1 else f'<span>{line}</span>'
                       for i, line in enumerate(t["hero_lines"]))
    legend = "".join(f'<li><span class="dot" style="--coin:{color}" aria-hidden="true"></span><b>{asset}</b><span class="share">{share} %</span></li>'
                     for asset, share, color in HERO_ALLOCATION)
    arrow = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
    search = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 4.5 4.5"/></svg>'
    document = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h8l4 4v14H6zM14 3v5h4M9 12h6M9 16h6"/></svg>'
    return f'''<div class="brand-hero"><div class="hero-shell">
 <div class="hero-copy"><p class="hero-kicker">{t['hero_kicker']}</p>
  <h1>{headline}</h1><p class="hero-intro">{t['hero_intro']}</p><p class="hero-import">{t['hero_import']}</p>
  <div class="cta"><a class="btn" href="{url(t, 'pricing')}#{t['ids'][4]}">{t['hero_try']}{arrow}</a>
   <a class="btn hero-secondary" href="{url(t, 'imports')}">{search}{t['hero_find']}</a></div>
  <p class="note">{t['hero_note']}</p></div>
 <div class="hero-scene">
  <figure class="hero-portfolio" aria-labelledby="demo-title demo-caption">
   <div class="demo-heading"><h2 id="demo-title">{t['hero_pf_title']}</h2><span class="demo-badge">{t['hero_demo']}</span></div>
   <p class="demo-total">{t['pf_total_v']}</p>
   <div class="demo-distribution" role="group" aria-label="{t['hero_allocation']}">
    <div class="demo-donut" aria-hidden="true"><span>{t['hero_allocation']}</span></div><ul class="demo-legend">{legend}</ul></div>
   <div class="demo-history"><h3>{t['hero_history']}</h3>{hero_history(t)}</div>
   <a class="demo-export" href="{url(t, 'tax')}">{document}<span>{t['hero_exports']}</span><span class="export-arrow">→</span></a>
   <figcaption id="demo-caption">{t['hero_demo_note']}</figcaption>
  </figure>
  <img class="hero-fox" src="assets/hero-fox.webp" alt="" width="800" height="800" fetchpriority="high" decoding="async">
 </div>
</div></div>'''


CSS += """
/* Approved overview spread: one product story, not a repeated feature-card grid. */
.overview-story{position:relative;isolation:isolate;overflow:hidden;padding:86px 0 70px;background:#fff}
.overview-story:before{content:"";position:absolute;z-index:-1;inset:170px -14% 100px;
 background:linear-gradient(120deg,#F5FAFF,#E8F4FF 65%,#F8FCFF);border-radius:50%;transform:rotate(-9deg)}
.story-shell{max-width:1440px;margin:0 auto;padding:0 40px}
.story-heading{display:grid;grid-template-columns:2.35fr 1fr;gap:48px;align-items:center;margin-bottom:48px}
.story-heading h2{font-size:clamp(32px,3.55vw,51px);line-height:1.12;letter-spacing:-.04em}
.story-heading h2 span{display:block}.story-heading h2 .accent{color:#1260E8}
.story-heading>p{font-size:17px;line-height:1.65;color:#425675}
.story-spread{display:grid;grid-template-columns:minmax(0,2.55fr) minmax(260px,1fr);gap:42px;align-items:start}
.story-chapter{padding-left:17px;border-left:4px solid #1260E8;min-height:61px;margin-bottom:25px}
.story-kicker{font-size:11px;font-weight:700;letter-spacing:.08em;color:#0B4DC2;margin-bottom:8px}
.story-chapter h3{font-size:clamp(19px,1.75vw,25px);letter-spacing:-.035em;line-height:1.2}
.story-window{margin:0;min-width:0;overflow:hidden;border:1px solid #DFEAF6;border-radius:14px;background:#fff;box-shadow:0 18px 50px #214B7D0D}
.story-window-top{display:flex;align-items:center;justify-content:space-between;gap:12px;background:#10254A;color:#fff;padding:16px 22px}
.story-app-name{display:flex;align-items:center;gap:8px;font-size:21px;font-weight:700;letter-spacing:-.025em}
.story-app-name .mark{width:25px;height:25px;color:#B8D9FF}
.story-example{font-size:10px;white-space:nowrap;border:1px solid #597091;border-radius:5px;padding:3px 7px;color:#E6F2FF}
.story-window-body{padding:25px 24px 8px}.story-window-body h4{font-size:23px;line-height:1.3;letter-spacing:-.03em;margin:0 0 6px;color:#10254A}
.story-window-body>p{font-size:13px;color:#536989;margin-bottom:22px}
.story-table{width:100%;border-collapse:collapse;table-layout:fixed;color:#10254A}
.story-table col:nth-child(1){width:25%}.story-table col:nth-child(2){width:25%}
.story-table col:nth-child(3){width:18%}.story-table col:nth-child(4){width:32%}
.story-table th{font-size:12px;text-align:left;font-weight:600;color:#536989;background:#F3F7FD;padding:11px 12px}
.story-table td{font-size:14px;padding:18px 12px;border-bottom:1px solid #E8EFF8;vertical-align:middle}
.story-table th:last-child,.story-table td:last-child{text-align:right}
.story-table td:first-child{font-size:12px;color:#536989;white-space:nowrap}.story-table td:last-child{white-space:nowrap}
.story-event{display:flex;align-items:center;gap:9px}
.story-event i{font-size:15px;font-style:normal;width:25px;height:25px;border-radius:50%;display:grid;place-items:center;flex:none;
 background:#E6F2FF;color:#0B4DC2}.story-event.reward i{background:#F2EDFF;color:#7352AA}
.story-asset{font-size:12px;font-weight:700;letter-spacing:.02em}
.story-window figcaption{font-family:inherit;font-size:11px;color:#536989;padding:16px 24px 21px}
.story-portfolio-link{font-size:14px;display:inline-block;margin-top:18px;text-decoration:none;font-weight:600}
.story-report{min-width:0}.story-report-stack{position:relative;margin:0 8px 24px 0;isolation:isolate}
.story-report-stack:before{content:"";position:absolute;inset:16px -9px -9px 11px;background:#EDF4FD;transform:rotate(5deg);z-index:-1;
 border:1px solid #E1EBF7;box-shadow:0 14px 32px #173E7410}
.story-paper{background:#fff;border:1px solid #E6EEF7;box-shadow:0 12px 30px #173E7410;transform:rotate(3deg);padding:27px 25px 23px;color:#10254A;min-height:414px}
.story-paper .report-brand{font-size:13px;font-weight:800;letter-spacing:-.025em;margin-bottom:22px}
.story-paper h4{font-size:28px;line-height:1.15;letter-spacing:-.035em;margin:0 0 7px}
.story-paper .report-year{font-size:11px;color:#536989;padding-bottom:18px;border-bottom:2px solid #E6F2FF}
.story-paper dl{margin:5px 0 0}.story-paper dl>div{padding:13px 0;border-bottom:1px solid #E6EEF7}
.story-paper dt{font-size:12px;font-weight:600}.story-paper dd{font-size:17px;font-weight:700;margin:3px 0 0;color:#0B4DC2}
.story-paper .report-formats{font-size:10px;color:#536989;margin-top:17px;line-height:1.5}
.story-report-link{font-size:14px;font-weight:600;display:inline-block;margin:8px 0 0 8px}
.story-news{display:flex;align-items:end;justify-content:space-between;gap:30px;border-top:1px solid #B8D9FF;margin-top:50px;padding-top:25px}
.story-news h3{font-size:27px;letter-spacing:-.03em;margin:0 0 5px}.story-news p{font-size:15px;color:#425675}
.story-news .story-kicker{font-size:11px;color:#0B4DC2;margin-bottom:7px}
.story-news-links{display:flex;gap:22px;flex-wrap:wrap;margin-top:13px}.story-news-links a{font-size:14px;font-weight:600;text-decoration:none}
.story-local{text-align:right;flex:none}.story-local p{font-size:12px}.story-local a{font-size:12px}
@media(max-width:1100px){
 .story-shell{padding-inline:28px}.story-heading{gap:30px;grid-template-columns:2fr 1fr}.story-heading h2{font-size:39px}
 .story-spread{gap:28px;grid-template-columns:minmax(0,2fr) minmax(245px,1fr)}
 .story-window-body{padding:22px 16px 5px}.story-table td,.story-table th{padding-inline:6px}.story-paper{padding:24px 20px}
}
@media(max-width:800px){
 .overview-story{padding:58px 0}.story-heading{grid-template-columns:1fr;gap:18px;margin-bottom:35px}
 .story-heading h2{font-size:clamp(32px,5vw,41px)}.story-heading>p{max-width:34em;font-size:16px}
 .story-spread{grid-template-columns:1fr;gap:38px}.story-report{max-width:430px;width:100%;margin:0 auto}
 .story-chapter{min-height:0}.story-chapter h3{font-size:23px}.story-news{margin-top:42px}
}
@media(max-width:480px){
 .story-shell{padding-inline:20px}.overview-story{padding:44px 0 40px}.story-heading h2{font-size:32px}
 .story-chapter{padding-left:12px;margin-bottom:20px}.story-chapter h3{font-size:21px}
 .story-window-top{padding:13px 12px;gap:6px}.story-app-name{font-size:15px;gap:5px}.story-app-name .mark{width:19px;height:19px}
 .story-example{font-size:8px;padding:3px 5px}.story-window-body{padding:18px 12px 0}.story-window-body h4{font-size:21px}
 .story-window-body>p{font-size:11px;margin-bottom:17px}.story-table th{font-size:9px;padding:9px 3px}
 .story-table td{font-size:11px;padding:15px 3px}.story-table td:first-child{font-size:9px}
 .story-event{gap:5px}.story-event i{display:none}.story-asset{font-size:10px}.story-window figcaption{font-size:10px;padding:14px 15px 18px}
 .story-paper{min-height:0}.story-news{display:block}.story-news h3{font-size:25px}.story-local{text-align:left;margin-top:25px}
 .story-news-links{gap:18px}.story-news p{font-size:14px}
}
"""


def homepage_overview(t):
    """A simplified, labelled view of existing transaction/report functionality."""
    headings = "".join(f'<span class="accent">{line}</span>' if i else f'<span>{line}</span>'
                       for i, line in enumerate(t["story_lines"]))
    columns = "".join(f'<th scope="col">{label}</th>' for label in t["story_columns"])
    symbols = {"buy": "+", "reward": "◇", "sell": "−"}
    rows = "".join(f'<tr><td>{date}</td><td><span class="story-event {kind}"><i aria-hidden="true">{symbols[kind]}</i>{event}</span></td>'
                   f'<td><span class="story-asset">{asset}</span></td><td>{value}</td></tr>'
                   for date, event, asset, value, kind in t["story_rows"])
    report = "".join(f'<div><dt>{label}</dt><dd>{value}</dd></div>' for label, value in t["story_report_items"])
    return f'''<section class="overview-story" aria-labelledby="overview-title"><div class="story-shell">
 <div class="story-heading"><h2 id="overview-title">{headings}</h2><p>{t['story_intro']}</p></div>
 <div class="story-spread">
  <div class="story-daily"><div class="story-chapter"><p class="story-kicker">{t['story_daily']}</p><h3>{t['story_daily_h']}</h3></div>
   <figure class="story-window" aria-labelledby="story-transactions-title story-transactions-caption">
    <div class="story-window-top"><span class="story-app-name">{MARK}Kryptokompis</span><span class="story-example">{t['story_example']}</span></div>
    <div class="story-window-body"><h4 id="story-transactions-title">{t['story_transactions']}</h4><p>{t['story_transaction_note']}</p>
     <table class="story-table"><colgroup><col><col><col><col></colgroup><thead><tr>{columns}</tr></thead><tbody>{rows}</tbody></table>
    </div><figcaption id="story-transactions-caption">{t['story_caption']}</figcaption>
   </figure><a class="story-portfolio-link" href="{url(t, 'portfolio')}">{t['story_portfolio']} →</a>
  </div>
  <div class="story-report"><div class="story-chapter"><p class="story-kicker">{t['story_report']}</p><h3>{t['story_report_h']}</h3></div>
   <figure class="story-report-stack" aria-labelledby="story-report-title story-report-caption"><div class="story-paper">
    <p class="report-brand">Kryptokompis</p><h4 id="story-report-title">{t['story_report_title']}</h4>
    <p class="report-year" id="story-report-caption">{t['story_report_example']}</p><dl>{report}</dl><p class="report-formats">{t['story_report_formats']}</p>
   </div></figure><a class="story-report-link" href="{t['report_pdf']}">{t['story_report_link']} →</a>
  </div>
 </div>
 <div class="story-news"><div><p class="story-kicker">{t['story_news_kicker']}</p><h3>{t['story_news_h']}</h3><p>{t['story_news_intro']}</p>
  <div class="story-news-links"><a href="{url(t, 'news')}">{t['story_news_link']} →</a><a href="{url(t, 'guides')}">{t['story_guides_link']} →</a></div></div>
  <div class="story-local"><p>{t['story_local']}</p><a href="{url(t, 'insights')}#{t['ids'][5]}">{t['story_privacy']} →</a></div>
 </div>
</div></section>'''


def page(t):
    """The front page: hero, product overview, prices and latest posts."""
    x = X[t["lang"]]
    redirect = ("<script>(function(){var m=" + __import__("json").dumps(OLD_ANCHORS[t["lang"]]) +
                ";var h=location.hash.slice(1);if(m[h])location.replace(m[h]);})();</script>")
    return (head(t, t["title"], t["desc"], body_class="home-blue") + redirect + nav(t) + f"""<main>
{homepage_hero(t)}

{homepage_overview(t)}

<section class="dark"><div class="w">
 <div class="headrow"><div><h2>{x['tiers_h']}</h2><p class="sub">{x['tiers_sub']}</p></div><a href="{url(t, 'pricing')}">{x['all_prices']} →</a></div>
 {tiers(t)}
 <p class="note">{t['pay_note']}</p>
</div></section>

<!--LATEST-->
</main>
""" + footer(t))


def subpage(t, key, body):
    x = X[t["lang"]]
    h1, lead = x["pages"][key]
    p = dict(t, file=PAGES[t["lang"]][key], other=PAGES["en" if t["lang"] == "nb" else "nb"][key])
    kick = f'<p class="kick">{x["kicker"]}</p>' if key in ("portfolio", "tax", "imports", "insights") else ""
    return (head(p, f"{h1} - Kryptokompis", lead, p["file"]) + nav(p) + f"""<main>
<div class="w phead">{kick}<h1>{h1}</h1><p class="lead">{lead}</p></div>
{body}
{final_cta(t) if key != "pricing" else ""}
</main>
""" + footer(p))


def subpages(t):
    return {
        "portfolio": subpage(t, "portfolio", sec_portfolio(t, head=False)),
        "tax": subpage(t, "tax", sec_tax(t, head=False)),
        "imports": subpage(t, "imports", sec_imports(t, head=False)),
        "insights": subpage(t, "insights", sec_insights(t, head=False) + sec_trust(t)),
        "pricing": subpage(t, "pricing", sec_start(t, head=False)),
        "faq": subpage(t, "faq", sec_faq(t)),
    }


if __name__ == "__main__":
    (SITE / "assets").mkdir(parents=True, exist_ok=True)
    for asset in ("hero-fox.webp", "hero-mountains.webp"):
        shutil.copy2(ASSETS / asset, SITE / "assets" / asset)
    for t in T.values():
        (SITE / t["file"]).write_text(page(t), encoding="utf-8")
        print("wrote", t["file"])
        for key, html in subpages(t).items():
            (SITE / PAGES[t["lang"]][key]).write_text(html, encoding="utf-8")
            print("wrote", PAGES[t["lang"]][key])
