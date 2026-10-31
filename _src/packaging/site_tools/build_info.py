"""Builds the Info pages (site/info.html = Norwegian, site/info-en.html = English) with the same
head, navigation and footer as the landing pages (build_site.py).

Run:  python packaging/site_tools/build_info.py <site dir>"""
import sys
from pathlib import Path

import build_site as B
import markdown
import re
from html import escape

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
D, BUY = B.DISCORD, B.BUY

T = {
 "nb": dict(lang="nb", file="info.html", other="info-en.html", home="index.html", olabel="EN",
  title="Info - Kryptokompis", h1="Info", lead="Guider, eksempelrapporter, nyttige lenker og hvordan du får tak i oss.",
  nav=[("guider", "Guider"), ("eksempler", "Eksempelrapporter"), ("lenker", "Nyttige lenker"), ("om", "Om Kryptokompis"), ("kontakt", "Kontakt")],
  back="Til forsiden", buy="Kjøp - 99 kr",
  guides=f"""
<h2>Guider</h2>
<p class="sub">Fra installasjon til ferdige tall i skattemeldingen. Steg-for-steg-guider for hver børs finner du under <a href="guider.html">Guider og nyheter</a>.</p>
<details open><summary>Kom i gang</summary><ol class="st">
<li>Last ned og installer Kryptokompis (Windows eller Android). Godta vilkårene.</li>
<li><b>Data og oppsett → Deg:</b> navn på rapporten, og fra hvilket år full FIFO-beregning skal starte.</li>
<li><b>Børser og lommebøker → Legg til børs:</b> koble til med en API-nøkkel som bare kan lese, eller importer eksportfilen fra børsen.</li>
<li>Kryptokompis synker og regner ut. Se <b>Skatterapport → Kontroller</b>: alt grønt betyr at dataene henger sammen.</li>
<li>Med lisens får du tallene til skattemeldingen, PDF-rapporten og CSV-filene. Usikker? Prøv med <b>eksempeldata</b> først.</li></ol></details>
<details><summary>Lag en API-nøkkel som bare kan lese</summary>
<p>Kryptokompis trenger aldri å handle eller ta ut penger. Lag nøkkelen med bare lesetilgang:</p>
<table class="prose"><tr><th>Børs</th><th>Tilgang som trengs</th></tr>
<tr><td><b>Kraken</b></td><td>Query Funds, Query Open/Closed Orders &amp; Trades, Query Ledger Entries. <a href="https://support.kraken.com/articles/360000919966-how-to-create-an-api-key" target="_blank" rel="noopener">Krakens guide</a></td></tr>
<tr><td><b>Binance</b></td><td>Bare "Enable Reading". La handel og uttak være av. <a href="https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072" target="_blank" rel="noopener">Binances guide</a></td></tr>
<tr><td><b>Coinbase</b></td><td>Coinbase Developer Platform: "View only", signaturalgoritme ECDSA. <a href="https://help.coinbase.com/en/coinbase/getting-started/developer-platform/how-to-create-an-api-key" target="_blank" rel="noopener">Coinbases guide</a></td></tr>
<tr><td><b>KuCoin</b></td><td>API Management → bare "General" (ikke Trade, ikke Transfer). Passfrasen er den du valgte. KuCoins API gir bare de siste 12 månedene. <a href="https://www.kucoin.com/support/360015102174" target="_blank" rel="noopener">KuCoins guide</a></td></tr></table></details>
<details><summary>Eksportfiler (uten API-nøkkel)</summary><table class="prose"><tr><th>Børs</th><th>Slik henter du filen</th></tr>
<tr><td><b>Revolut X</b></td><td>Revolut-appen → Revolut X → Kontoutskrift → velg periode og Excel/CSV.</td></tr>
<tr><td><b>Firi</b></td><td>firi.com → Transaksjoner → Eksporter / Last ned CSV, alle år du har handlet.</td></tr>
<tr><td><b>Coinbase</b></td><td>coinbase.com → Profil → Statements / Reports → Transaction history → CSV. Én fil per år går fint.</td></tr>
<tr><td><b>KuCoin, eldre år</b></td><td>Orders → Spot Orders → Filled Orders → Export (huk av "Show Order-Splitting"). Eldre år får du fra KuCoins kundeservice.</td></tr>
<tr><td><b>Andre</b></td><td>Last ned Kryptokompis-malen i appen, fyll inn én rad per transaksjon og importer.</td></tr></table>
<p>Det er trygt å importere samme periode flere ganger - ingenting telles dobbelt.</p></details>
<details><summary>Slik fører du tallene i skattemeldingen</summary><ol class="st">
<li>I skattemeldingen: <b>Finans → Virtuelle eiendeler / kryptovaluta</b>. Du kan samle myntene på ett kort, men skal kunne vise summen mynt for mynt - det gjør PDF-en og CSV-filene.</li>
<li>Før inn beløpene fra Kryptokompis (kapittel 1 i PDF-en): Formuesverdi, Skattepliktig gevinst, Fradragsberettiget tap, Andre inntekter og Forvaltningskostnader.</li>
<li>Gevinst og tap føres i hvert sitt felt - de skal ikke trekkes fra hverandre.</li>
<li><b>Kontanter på børser</b> (dollar/kroner) er ikke en virtuell eiendel. Saldoen ved årsskiftet er formue, normalt et krav mot børsen. Hvor den føres, avhenger av saldoen, valutaen og hvor børsen holder til. <a href="guide-skattemeldingen.html">Mer i guiden</a>.</li>
<li>Ta vare på PDF-en og CSV-filene. Den sendes ikke inn, men er dokumentasjonen hvis Skatteetaten spør.</li></ol></details>
<details><summary>Flytt dataene til mobilen eller en annen PC</summary><ol class="st">
<li>På PC-en: <b>Data og oppsett → Flytt til en annen PC → Eksporter alt</b>. Velg et passord hvis API-nøklene skal være med.</li>
<li>Send filen til mobilen (e-post, sky, kabel).</li>
<li>På mobilen: samme sted → <b>Importer</b>, velg filen og skriv passordet.</li></ol></details>""",
  examples=f"""
<h2>Eksempelrapporter</h2>
<p class="sub">Laget av Kryptokompis fra et oppdiktet år (2025) med kjøp, salg med gevinst, bytte med tap, staking, overføring til egen lommebok og futures. Ingen ekte personer eller kurser.</p>
<div class="g2"><div class="card"><h3>PDF-rapporten</h3><p>Det du tar vare på som dokumentasjon: tallene til skattemeldingen, kontroller, hvert salg med FIFO-utregning, formue og vedlegg.</p>
<p class="dl" style="margin-top:12px"><a class="btn" href="eksempel/Kryptokompis-eksempelrapport-2025.pdf" target="_blank" rel="noopener">Eksempelrapport (norsk)</a><a class="btn g" href="eksempel/Kryptokompis-example-report-2025.pdf" target="_blank" rel="noopener">Example (English)</a></p></div>
<div class="card"><h3>CSV-filene</h3><p>Til Excel (semikolon og desimalkomma): per mynt, alle transaksjoner med FIFO, og alle futures-poster.</p>
<p class="dl" style="margin-top:12px"><a href="eksempel/tax_summary_2025_nb.csv">Per mynt</a> · <a href="eksempel/fifo_transactions_2025_nb.csv">Transaksjoner</a> · <a href="eksempel/futures_detail_2025_nb.csv">Futures</a></p></div></div>""",
  links=f"""
<h2>Nyttige lenker</h2>
<table class="prose"><tr><td><a href="https://www.skatteetaten.no/virtuellvaluta" target="_blank" rel="noopener">Skatteetaten - virtuelle eiendeler og kryptovaluta</a></td><td>Reglene og hvordan det føres</td></tr>
<tr><td><a href="https://www.skatteetaten.no/nn/person/til-fra-noreg/verdiar/inntekt-formue/inntekt-og-formue-i-utlandet/" target="_blank" rel="noopener">Skatteetaten - inntekt og formue i utlandet</a></td><td>Kontanter og fordringer i utlandet</td></tr>
<tr><td><a href="https://www.norges-bank.no/tema/Statistikk/Valutakurser/" target="_blank" rel="noopener">Norges Bank - valutakurser</a></td><td>USD/NOK-kursene Kryptokompis bruker</td></tr>
<tr><td><a href="{D}" target="_blank" rel="noopener">Kryptokompis på Discord</a></td><td>Spørsmål, hjelp og ønsker</td></tr></table>""",
  about="""
<h2>Om Kryptokompis</h2>
<p class="sub">Kryptokompis er laget i Norge av en utvikler som selv handler krypto og ville ha tall han kunne stole på. <a href="om.html">Les mer om hvem som lager det</a>.</p>
<ul class="ck"><li>Beregning: FIFO per mynt på tvers av børser (metoden Kryptokompis bruker, ikke et lovkrav), NOK-kurs fra Norges Bank på hver transaksjonsdato, gevinst og tap hver for seg.</li>
<li>Dataene dine blir på din egen enhet. API-nøkler kan bare lese.</li>
<li>Hver rapport viser hvilket regelsett som er brukt, og hva som er antatt.</li>
<li>Ikke skatterådgivning - du er selv ansvarlig for skattemeldingen. <a href="vilkar.html">Vilkår</a></li></ul>""",
  contact=f"""
<h2>Kontakt</h2>
<p class="sub">Raskest svar får du på Discord - spørsmål, feil, ønsker om nye børser og hjelp med kjøp og lisens.</p>
<p><a class="btn" href="{D}" target="_blank" rel="noopener">Bli med på Discord</a></p>
<p class="note">Du kan også sende en melding fra appen: Data og oppsett → Tilbakemelding og ønsker.</p>"""),
 "en": dict(lang="en", file="info-en.html", other="info.html", home="en.html", olabel="NO",
  title="Info - Kryptokompis", h1="Info", lead="Guides, example reports, useful links and how to reach us.",
  nav=[("guides", "Guides"), ("examples", "Example reports"), ("links", "Useful links"), ("about", "About Kryptokompis"), ("contact", "Contact")],
  back="Home", buy="Buy - 99 NOK",
  guides=f"""
<h2>Guides</h2>
<p class="sub">From installing to the figures in your tax return. Step-by-step guides for each exchange are under <a href="guides.html">Guides and news</a>.</p>
<details open><summary>Getting started</summary><ol class="st">
<li>Download and install Kryptokompis (Windows or Android). Accept the terms.</li>
<li><b>Data &amp; setup → You:</b> name on the report, and the year full FIFO starts from.</li>
<li><b>Exchanges &amp; wallets → Add exchange:</b> connect with a read-only API key, or import the exchange's export file.</li>
<li>Kryptokompis syncs and calculates. Check <b>Tax report → Checks</b>: all green means the data adds up.</li>
<li>A licence unlocks the figures for the tax return, the PDF report and the CSV files. Not sure? Try the <b>example data</b> first.</li></ol></details>
<details><summary>Create a read-only API key</summary>
<p>Kryptokompis never needs to trade or withdraw. Create the key with read access only:</p>
<table class="prose"><tr><th>Exchange</th><th>Permissions needed</th></tr>
<tr><td><b>Kraken</b></td><td>Query Funds, Query Open/Closed Orders &amp; Trades, Query Ledger Entries. <a href="https://support.kraken.com/articles/360000919966-how-to-create-an-api-key" target="_blank" rel="noopener">Kraken's guide</a></td></tr>
<tr><td><b>Binance</b></td><td>"Enable Reading" only. Leave trading and withdrawals off. <a href="https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072" target="_blank" rel="noopener">Binance's guide</a></td></tr>
<tr><td><b>Coinbase</b></td><td>Coinbase Developer Platform: "View only", signature algorithm ECDSA. <a href="https://help.coinbase.com/en/coinbase/getting-started/developer-platform/how-to-create-an-api-key" target="_blank" rel="noopener">Coinbase's guide</a></td></tr>
<tr><td><b>KuCoin</b></td><td>API Management → "General" only (no Trade, no Transfer). The passphrase is the one you chose. KuCoin's API only reaches the last 12 months. <a href="https://www.kucoin.com/support/360015102174" target="_blank" rel="noopener">KuCoin's guide</a></td></tr></table></details>
<details><summary>Export files (no API key)</summary><table class="prose"><tr><th>Exchange</th><th>How to get the file</th></tr>
<tr><td><b>Revolut X</b></td><td>Revolut app → Revolut X → Account statement → choose the period and Excel/CSV.</td></tr>
<tr><td><b>Firi</b></td><td>firi.com → Transaksjoner → Export / Download CSV, every year you traded.</td></tr>
<tr><td><b>Coinbase</b></td><td>coinbase.com → Profile → Statements / Reports → Transaction history → CSV. One file per year is fine.</td></tr>
<tr><td><b>KuCoin, older years</b></td><td>Orders → Spot Orders → Filled Orders → Export (tick "Show Order-Splitting"). Older years come from KuCoin support.</td></tr>
<tr><td><b>Others</b></td><td>Download the Kryptokompis template in the app, one row per transaction, and import it.</td></tr></table>
<p>Importing the same period again is safe - nothing is counted twice.</p></details>
<details><summary>Entering the figures in the tax return</summary><ol class="st">
<li>In skattemeldingen: <b>Finans → Virtuelle eiendeler / kryptovaluta</b>. You can put the coins on one card, but must be able to show the total coin by coin - the PDF and CSV files do that.</li>
<li>Enter the amounts from Kryptokompis (chapter 1 of the PDF): Formuesverdi, Skattepliktig gevinst, Fradragsberettiget tap, Andre inntekter and Forvaltningskostnader.</li>
<li>Gains and losses go in separate fields - they are not netted.</li>
<li><b>Cash on exchanges</b> (dollars/kroner) is not a virtual asset. The balance at the turn of the year is wealth, normally a claim against the exchange. Where to report it depends on the balance, the currency and where the exchange is based. <a href="guide-skattemeldingen-en.html">More in the guide</a>.</li>
<li>Keep the PDF and the CSV files. They are not submitted, but are your documentation if Skatteetaten asks.</li></ol></details>
<details><summary>Move your data to the phone or another PC</summary><ol class="st">
<li>On the PC: <b>Data &amp; setup → Move to another PC → Export everything</b>. Choose a password if the API keys should come along.</li>
<li>Send the file to the phone (email, cloud, cable).</li>
<li>On the phone: same place → <b>Import</b>, pick the file and enter the password.</li></ol></details>""",
  examples=f"""
<h2>Example reports</h2>
<p class="sub">Made by Kryptokompis from a made-up year (2025): purchases, a sale with a gain, a swap with a loss, staking, a transfer to an own wallet and futures. No real people or prices.</p>
<div class="g2"><div class="card"><h3>The PDF report</h3><p>What you keep as documentation: the figures for the tax return, checks, every sale with its FIFO working, wealth and appendices.</p>
<p class="dl" style="margin-top:12px"><a class="btn" href="eksempel/Kryptokompis-example-report-2025.pdf" target="_blank" rel="noopener">Example report (English)</a><a class="btn g" href="eksempel/Kryptokompis-eksempelrapport-2025.pdf" target="_blank" rel="noopener">Eksempel (norsk)</a></p></div>
<div class="card"><h3>The CSV files</h3><p>For Excel (semicolon, decimal comma): per coin, every transaction with FIFO, and every futures item.</p>
<p class="dl" style="margin-top:12px"><a href="eksempel/tax_summary_2025_en.csv">Per coin</a> · <a href="eksempel/fifo_transactions_2025_en.csv">Transactions</a> · <a href="eksempel/futures_detail_2025_en.csv">Futures</a></p></div></div>""",
  links=f"""
<h2>Useful links</h2>
<table class="prose"><tr><td><a href="https://www.skatteetaten.no/virtuellvaluta" target="_blank" rel="noopener">Skatteetaten - virtual assets and crypto</a></td><td>The rules and how to report</td></tr>
<tr><td><a href="https://www.skatteetaten.no/nn/person/til-fra-noreg/verdiar/inntekt-formue/inntekt-og-formue-i-utlandet/" target="_blank" rel="noopener">Skatteetaten - income and wealth abroad</a></td><td>Cash and claims abroad</td></tr>
<tr><td><a href="https://www.norges-bank.no/en/topics/Statistics/exchange_rates/" target="_blank" rel="noopener">Norges Bank - exchange rates</a></td><td>The USD/NOK rates Kryptokompis uses</td></tr>
<tr><td><a href="{D}" target="_blank" rel="noopener">Kryptokompis on Discord</a></td><td>Questions, help and requests</td></tr></table>""",
  about="""
<h2>About Kryptokompis</h2>
<p class="sub">Kryptokompis is made in Norway by a developer who trades crypto himself and wanted figures he could trust. <a href="about.html">More about who makes it</a>.</p>
<ul class="ck"><li>Calculation: FIFO per coin across exchanges (the method Kryptokompis uses, not a legal requirement), Norges Bank NOK rate on each transaction date, gains and losses kept apart.</li>
<li>Your data stays on your own device. API keys can only read.</li>
<li>Every report states which ruleset was used and what was assumed.</li>
<li>Not tax advice - you are responsible for your tax return. <a href="terms.html">Terms</a></li></ul>""",
  contact=f"""
<h2>Contact</h2>
<p class="sub">The fastest answer is on Discord - questions, bugs, requests for new exchanges and help with buying and licences.</p>
<p><a class="btn" href="{D}" target="_blank" rel="noopener">Join the Discord</a></p>
<p class="note">You can also send a message from the app: Data &amp; setup → Feedback and requests.</p>"""),
}


EXTRA = """<style>
.ihero{padding-top:64px;padding-bottom:24px}.ihero .lead{margin-top:16px}
.isec{padding:56px 0;border-top:1px solid var(--line)}.isec:nth-of-type(even){background:var(--sheet)}
.isec h2{margin-bottom:10px}.isec .sub{margin-bottom:22px}
.isec details{max-width:860px}.isec details p,.isec details td{color:var(--ink2)}
ol.st{list-style:none;padding:0;margin:0 0 20px;max-width:760px;counter-reset:n}ol.st li{margin:10px 0;padding-left:30px;position:relative;counter-increment:n}ol.st li:before{content:counter(n);position:absolute;left:0;top:1px;width:21px;height:21px;border-radius:50%;background:var(--mint);color:var(--spruce-d);font-size:13px;font-weight:700;display:grid;place-items:center}
.dl a{margin:6px 10px 0 0}.isec .ck{max-width:760px}
</style>"""

for L, t in T.items():
    site = B.T[L]
    page = dict(site, file=t["file"], other=t["other"])
    ids = [i for i, _ in t["nav"]]
    body = "".join(f'<section class="isec" id="{ids[k]}"><div class="w">{t[part]}</div></section>\n' for k, part in
                   enumerate(("guides", "examples", "links", "about", "contact")))
    html = (B.head(page, t["title"], t["lead"]).replace("</head>", EXTRA + "</head>", 1)
            + B.nav(page, home_page=False)
            + f'<main id="main" class="info-sections"><div class="w ihero"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p></div>{body}</main>'
            + B.footer(page))
    (SITE / t["file"]).write_text(html, encoding="utf-8")
    print("wrote", t["file"])


# Terms pages: the text lives in legal_<lang>.html next to this script (edit it there).
LEGAL = "<style>.legal{max-width:760px;padding-top:56px;padding-bottom:72px}.legal h1{font-size:clamp(34px,5vw,48px);margin-bottom:8px}" \
        ".legal h2{font-size:22px;margin:28px 0 6px}.legal ul{padding-left:22px}.legal li{margin:6px 0}.legal p{margin:14px 0}.legal .mu{color:var(--ink2)}.legal .card{margin-top:28px}</style>"
for L, f, srcname, other in (("nb", "vilkar.html", "legal_nb.html", "terms.html"), ("en", "terms.html", "legal_en.html", "vilkar.html"),
                              ("nb", "personvern.html", "legal_privacy_nb.html", "privacy.html"),
                              ("en", "privacy.html", "legal_privacy_en.html", "personvern.html")):
    src = (Path(__file__).with_name(srcname)).read_text(encoding="utf-8")
    title = src.split("title: ", 1)[1].split(" -->", 1)[0]
    page = dict(B.T[L], file=f, other=other)
    html = (B.head(page, title, title).replace("</head>", LEGAL + "</head>", 1) + B.nav(page, home_page=False)
            + '<main id="main">' + B.DESIGN.reading(page, src.split("-->", 1)[1]) + '</main>' + B.footer(page))
    (SITE / f).write_text(html, encoding="utf-8")
    print("wrote", f)


def methodology():
    """Render the reviewed examples from the source copied by sync_public.sh."""
    source = Path(__file__).with_name('pages') / 'slik-regner-vi.nb.md'
    content = re.sub(r'<!--.*?-->', '', source.read_text(encoding='utf-8'), flags=re.S)
    content = re.sub(r'^---\s*$', '', content, flags=re.M).strip()
    heading, intro = content.split('\n', 1)
    sections = re.split(r'^## (.+)$', intro, flags=re.M)
    body = [f'<header class="methodology-header"><p class="eyebrow">{B.DESIGN.text(B.T["nb"], "methodology")}</p>'
            f'<h1>{escape(heading.removeprefix("# "))}</h1>{markdown.markdown(sections[0])}</header>']
    for title, section in zip(sections[1::2], sections[2::2]):
        if title.startswith('Del '):
            part = title.split(':', 1)[0].split()[-1]
            examples = re.split(r'^### (.+)$', section, flags=re.M)
            cards = []
            for name, example in zip(examples[1::2], examples[2::2]):
                # Keep each labelled field in a separate paragraph; Markdown otherwise joins lines.
                example = re.sub(r'\n(?=\*\*|<small>)', '\n\n', example.strip())
                cards.append(f'<article class="calculation-card"><h3>{escape(name)}</h3>{markdown.markdown(example)}</article>')
            cards = '<div class="calculation-cards">' + ''.join(cards) + '</div>'
            if part == '1':
                body.append(f'<section class="calculation-part" id="del-{part}"><h2>{escape(title)}</h2>{cards}</section>')
            else:
                body.append(f'<details class="calculation-part" id="del-{part}"><summary><h2>{escape(title)}</h2></summary>{cards}</details>')
        else:
            body.append(f'<section class="methodology-notes"><h2>{escape(title)}</h2>{markdown.markdown(section)}</section>')
    page = dict(B.T['nb'], file='slik-regner-vi.html', other='guides.html', og_title='Slik regner vi - Kryptokompis')
    description = 'Se hvordan Kryptokompis regner, med eksempler på kjøp, salg, gebyrer og formue. Hvert eksempel er knyttet til en test.'
    # This page has no English counterpart yet; do not advertise the homepages as translations.
    head = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '',
                  B.head(page, page['og_title'], description))
    html = (head + B.nav(page, home_page=False)
            + '<main id="main" class="methodology"><div class="wrap methodology-wrap">' + ''.join(body)
            + '</div></main>' + B.footer(page))
    (SITE / page['file']).write_text(html, encoding='utf-8')
    print('wrote', page['file'])


methodology()
