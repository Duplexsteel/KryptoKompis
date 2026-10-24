"""Approved October 2026 site layouts. Content and routing stay with the generators.

This module has no app/database imports. Shared copy is bilingual; integrations use
build_site.T's supported-exchange list and guides remain subject to draft/date checks.
"""
import json
import re
from html import escape
from pathlib import Path

CSS = Path(__file__).with_suffix('.css').read_text(encoding='utf-8')

# Customer-facing text belongs in translation tables, including layout captions.
COPY = {
    'try': ('Prøv appen', 'Try the app'),
    'product': ('Produktet', 'Product'),
    'resources': ('Nytt og nyttig', 'News and resources'),
    'portfolio': ('Portefølje', 'Portfolio'),
    'tax': ('Skatt og rapporter', 'Tax and reports'),
    'imports': ('Børser og import', 'Exchanges and import'),
    'insights': ('Kontroller og personvern', 'Checks and privacy'),
    'pricing': ('Priser og nedlasting', 'Pricing and download'),
    'guides': ('Guider og blogg', 'Guides and blog'),
    'news': ('Kryptonytt', 'Crypto news'),
    'faq': ('Spørsmål og svar', 'Questions and answers'),
    'about': ('Om og kontakt', 'About and contact'),
    'info': ('Info og ressurser', 'Info and resources'),
    'terms': ('Bruksvilkår', 'Terms'),
    'privacy': ('Personvern', 'Privacy'),
    'foot_note': ('Laget i Norge. Ikke skatterådgivning.<br>Du er selv ansvarlig for skattemeldingen.', 'Made in Norway. Not tax advice.<br>You are responsible for your tax return.'),
    'slogan': ('Kryptoen din.<br>Samlet oversikt.<br>Enklere skatt.', 'Your crypto.<br>One clear overview.<br>Simpler taxes.'),
    'ribbon_h': ('Se kryptoen din i en større sammenheng.', 'See your crypto in context.'),
    'ribbon_p': ('Prøv porteføljen før du velger en lisens.', 'Try the portfolio before choosing a licence.'),
    'start': ('Prøv Kryptokompis', 'Try Kryptokompis'),
    'free': ('Gratis å prøve', 'Free to try'),
    'free_h': ('Porteføljen først. Velg lisens når du trenger den.', 'Your portfolio first. Choose a licence when you need it.'),
    'pricing_h': ('Start med oversikten.<br><span>Velg lisens når du trenger den.</span>', 'Start with an overview.<br><span>Choose a licence when you need it.</span>'),
    'free_portfolio': ('Porteføljen er gratis.', 'The portfolio is free.'),
    'free_p': ('Se om Kryptokompis passer for deg før du velger.', 'See whether Kryptokompis works for you before choosing.'),
    'download': ('Gå til nedlasting', 'Go to downloads'),
    'ready': ('Klar for å prøve?', 'Ready to try?'),
    'win_p': ('For Windows 10 og 11.', 'For Windows 10 and 11.'),
    'windows_help': ('Windows kan vise «Windows beskyttet PC-en»: trykk <b>Mer info → Kjør likevel</b>.', 'Windows may show “Windows protected your PC”: click <b>More info → Run anyway</b>.'),
    'windows_help_link': ('Les hele forklaringen', 'Read the full explanation'),
    'android_p': ('Installer APK-filen på Android.', 'Install the APK on Android.'),
    'versions': ('Alle versjoner', 'All versions'),
    'latest_h': ('Nytt og nyttig, også mellom skattemeldingene.', 'Useful all year, between tax returns too.'),
    'latest_all': ('Alle guider og innlegg', 'All guides and posts'),
    'guide_kicker': ('Guider', 'Guides'),
    'guide_h': ('Fra første import til samlet oversikt.', 'From your first import to a clear overview.'),
    'guide_p': ('Finn forklaringer om API, historikk og dokumentasjon - i ditt eget tempo.', 'Explore API connections, history and documentation at your own pace.'),
    'guide_cta': ('Finn en guide', 'Find a guide'),
    'import_h': ('Finn børsen din.<br><span>Samle historikken.</span>', 'Find your exchange.<br><span>Bring your history together.</span>'),
    'search_exchange': ('Søk etter børs', 'Search exchanges'),
    'all': ('Alle', 'All'),
    'file': ('CSV / fil', 'CSV / file'),
    'exchange_count': ('oppførte børser', 'listed exchanges'),
    'no_exchanges': ('Ingen treff. Prøv et annet søk eller en annen importmetode.', 'No matches. Try a different search or import method.'),
    'coverage': ('Hva støttes?', 'What is supported?'),
    'check_import': ('Kontroller hvilken importmetode og historikk du trenger før du kobler til.', 'Check which import method and history you need before connecting.'),
    'kraken_futures': ('Futures på Kraken krever en egen Kraken Futures-nøkkel.', 'Kraken futures require a separate Kraken Futures key.'),
    'guide_link': ('Åpne veiledningen', 'Open the guide'),
    'another_exchange': ('En annen børs eller lommebok?', 'Another exchange or wallet?'),
    'template_p': ('Andre kilder kan legges inn via importmalen i appen. Det er et eget format, ikke en automatisk integrasjon.', 'Other sources can be entered using the import template in the app. This is a separate format, not an automatic integration.'),
    'contact': ('Ta kontakt på Discord', 'Get in touch on Discord'),
    'integration_note': ('Nye integrasjoner føres opp når de er klare.', 'New integrations are listed when they are ready.'),
    'portfolio_h': ('Kryptoen din,<br><span>i sammenheng.</span>', 'Your crypto,<br><span>in context.</span>'),
    'portfolio_p': ('Se beholdningen samlet, forstå fordelingen og følg verdien i kroner.', 'See your holdings together, understand the allocation and follow the value in NOK.'),
    'portfolio_panel': ('Porteføljeoversikt', 'Portfolio overview'),
    'example': ('Eksempeldata', 'Example data'),
    'allocation': ('Fordeling', 'Allocation'),
    'total_value': ('Samlet verdi', 'Total value'),
    'asset': ('Eiendel', 'Asset'),
    'value': ('Verdi', 'Value'),
    'day': ('24 timer', '24 hours'),
    'share': ('Andel', 'Share'),
    'chart_note': ('Illustrasjon med oppdiktede tall. Verdiutvikling er ikke det samme som avkastning.', 'Illustration with fictional figures. Changes in value are not the same as investment returns.'),
    'holdings_h': ('Samlet beholdning', 'Holdings together'),
    'holdings_p': ('Se verdien og fordelingen på tvers av kildene du har lagt til.', 'See the value and allocation across the sources you have added.'),
    'history_h': ('Se historikken', 'See the history'),
    'history_p': ('Gå fra beholdningen til transaksjonene som ligger bak.', 'Go from your holdings to the transactions behind them.'),
    'basis_h': ('Forstå grunnlaget', 'Understand the basis'),
    'basis_p': ('Beholdning basert på filer og beholdning hentet fra API kan ha ulikt grunnlag.', 'Holdings calculated from files and balances fetched through APIs can have different bases.'),
    'tax_h': ('Fra transaksjoner<br><span>til dokumentasjon.</span>', 'From transactions<br><span>to documentation.</span>'),
    'tax_p': ('Samle grunnlaget og se tallene i en rapport du kan gå gjennom.', 'Gather your records and see the figures in a report you can review.'),
    'report_link': ('Se eksempelrapport', 'View example report'),
    'annual_report': ('Årsoversikt', 'Annual summary'),
    'report_year': ('Eksempelrapport · 2025', 'Example report · 2025'),
    'report_formats': ('Eksempeldata · PDF og CSV', 'Example data · PDF and CSV'),
    'report_h': ('En rapport du kan følge tilbake til historikken.', 'A report you can trace back to the history.'),
    'basis_step': ('Se grunnlaget', 'Review the records'),
    'basis_step_p': ('Gå gjennom historikken og eventuelle varsler før du lager rapporten.', 'Review the history and any warnings before creating the report.'),
    'docs_step': ('Samle dokumentasjonen', 'Gather the documentation'),
    'docs_step_p': ('Få oversikt over beregningene og opplysningene rapporten bygger på.', 'See the calculations and records behind the report.'),
    'export_step': ('Åpne PDF og CSV', 'Open PDF and CSV'),
    'export_step_p': ('Bruk rapporten og detaljfilene til å kontrollere og dokumentere tallene.', 'Use the report and detailed files to review and document the figures.'),
    'report_note': ('Eksempelrapporten viser format og oppbygging. Resultatet for deg avhenger av dataene du legger inn.', 'The example report shows the format and structure. Your results depend on the data you enter.'),
    'controls_h': ('Se hva som mangler.<br><span>Behold kontrollen.</span>', 'See what is missing.<br><span>Stay in control.</span>'),
    'controls_p': ('En oversikt blir mer nyttig når du også ser grunnlaget og eventuelle avvik.', 'An overview is more useful when you can also see the records and any discrepancies.'),
    'checks': ('Kontroller før rapport', 'Checks before reporting'),
    'checks_example': ('Eksempel på presentasjon av kontroller.', 'Illustrative presentation of checks.'),
    'imported': ('Historikk er importert', 'History imported'),
    'imported_p': ('Se hvilke kilder og perioder som er med.', 'See which sources and periods are included.'),
    'review': ('Et grunnlag trenger gjennomgang', 'A record needs review'),
    'review_p': ('Varsler samles med forklaring og neste steg.', 'Warnings include an explanation and next steps.'),
    'export_check': ('Se detaljer før du eksporterer', 'Review details before exporting'),
    'flow_kicker': ('Slik henger dataene sammen', 'How the data fits together'),
    'flow_h': ('Fra kildene dine til en lokal oversikt.', 'From your sources to a local overview.'),
    'api_csv': ('API og CSV', 'API and CSV'),
    'history_added': ('Historikken du legger til', 'The history you add'),
    'local': ('Lokal lagring', 'Local storage'),
    'devices': ('På PC eller Android', 'On PC or Android'),
    'reports': ('Oversikt og rapporter', 'Overview and reports'),
    'documentation': ('Kontroll og dokumentasjon', 'Review and documentation'),
    'device_h': ('Data på enheten', 'Data on your device'),
    'device_p': ('Transaksjoner, innstillinger og rapporter lagres lokalt.', 'Transactions, settings and reports are stored locally.'),
    'keys_h': ('Nøkler med lesetilgang', 'Read-only keys'),
    'keys_p': ('Bruk børsens tillatelser slik den verifiserte veiledningen beskriver.', 'Use exchange permissions as described in the verified instructions.'),
    'network_h': ('Åpen om nettverk', 'Transparent about network use'),
    'network_p': ('Import, priser, lisensfornyelse og oppdateringer kan bruke nettverk.', 'Imports, prices, licence renewal and updates can use the network.'),
    'network_note': ('Lokal lagring betyr ikke at appen aldri bruker internett. Personvernerklæringen beskriver hvem appen og nettsiden kontakter.', 'Local storage does not mean the app never uses the internet. The privacy policy describes who the app and website contact.'),
    'faq_h': ('Hva lurer du på?', 'What would you like to know?'),
    'faq_p': ('Finn hjelp om oppstart, import, lisens og bruk av Kryptokompis.', 'Find help with getting started, importing, licences and using Kryptokompis.'),
    'faq_search': ('Søk i spørsmål og svar', 'Search questions and answers'),
    'faq_empty': ('Ingen spørsmål passer til søket.', 'No questions match your search.'),
    'on_page': ('På denne siden', 'On this page'),
    'guide_page_h': ('Finn forklaringen<br><span>du trenger.</span>', 'Find the explanation<br><span>you need.</span>'),
    'blog_h': ('Fra Kryptokompis', 'From Kryptokompis'),
    'news_h': ('Følg med,<br><span>uten å miste oversikten.</span>', 'Keep up,<br><span>without losing the overview.</span>'),
    'news_p': ('Overskrifter og lenker fra nyhetskildene. Les hele saken hos utgiveren.', 'Headlines and links from news sources. Read the full story at the publisher.'),
    'all_sources': ('Alle kilder', 'All sources'),
    'open_original': ('Les hos', 'Read at'),
    'about_h': ('Laget av en som<br><span>savnet oversikten selv.</span>', 'Made by someone<br><span>who wanted a clearer overview.</span>'),
    'about_p': ('Jeg heter Christian Thesen, og jeg lager Kryptokompis.', 'My name is Christian Thesen, and I make Kryptokompis.'),
    'contact_h': ('Spørsmål, ønsker eller tilbakemelding?', 'Questions, ideas or feedback?'),
    'contact_p': ('Ta kontakt på Discord. Du finner meg også på LinkedIn.', 'Get in touch on Discord. You can also find me on LinkedIn.'),
}


def text(t, key):
    return COPY[key][t['lang'] != 'nb']


def a(href, label, cls=''):
    return f'<a href="{escape(href, quote=True)}" class="{cls}">{label}</a>'


def windows_help(lang):
    t = {'lang': lang}
    faq = 'sporsmal.html' if lang == 'nb' else 'faq.html'
    return f'<span class="download-help">{text(t,"windows_help")} {a(faq+"#windows-smartscreen",text(t,"windows_help_link"))}</span>'


def title(t, key, heading, intro=''):
    return f'<p class="eyebrow">{text(t,key)}</p><h1 class="page-title">{text(t,heading)}</h1>' + (f'<p class="intro">{text(t,intro)}</p>' if intro else '')


def nav(B, t):
    home = B.T[t['lang']]['file']
    links = ''.join(a(B.url(t,k),text(t,k)) for k in ('portfolio','tax','imports','guides','news'))
    extra = ''.join(a(B.url(t,k),text(t,k)) for k in ('insights','pricing','faq'))
    about = 'om.html' if t['lang']=='nb' else 'about.html'
    other = a(t['other'], 'EN' if t['lang']=='nb' else 'NO', 'language-link')
    return f'''<a class="skip-link" href="#main">{'Til innhold' if t['lang']=='nb' else 'Skip to content'}</a>
<header class="site-design-header"><nav class="site-design-nav" aria-label="{t['menu']}">{a(home,B.MARK+'Kryptokompis','wordmark')}<div class="navlinks">{links}</div>{other}{a(B.url(t,'pricing'),text(t,'try'),'btn small')}<button type="button" class="menu-toggle" aria-expanded="false" aria-controls="site-menu">{t['menu']}</button></nav><div class="mobile-menu" id="site-menu">{links}{extra}{a(about,text(t,'about'))}{a(t['info'],text(t,'info'))}{other}</div></header>'''


def footer(B,t):
    nb=t['lang']=='nb'
    product=''.join(a(B.url(t,k),text(t,k)) for k in ('portfolio','tax','imports','insights','pricing'))
    resources=''.join(a(B.url(t,k),text(t,k)) for k in ('guides','blog','news','faq') if k!='blog')
    resources+=a('blogg.html' if nb else 'blog.html',text(t,'blog_h'))
    resources+=a('om.html' if nb else 'about.html',text(t,'about'))+a(t['info'],text(t,'info'))
    return f'''<footer class="site-design-footer"><div class="wrap"><div class="footergrid"><div>{a(B.T[t['lang']]['file'],B.MARK+'Kryptokompis','wordmark')}<p class="footer-slogan">{text(t,'slogan')}</p></div><div class="footlinks"><h3>{text(t,'product')}</h3>{product}</div><div class="footlinks"><h3>{text(t,'resources')}</h3>{resources}</div></div><div class="footerbase"><div>{text(t,'foot_note')}</div><div>{a('vilkar.html' if nb else 'terms.html',text(t,'terms'))}{a('personvern.html' if nb else 'privacy.html',text(t,'privacy'))}{a(B.DISCORD,'Discord')}{a(t['other'],'English' if nb else 'Norsk')}</div></div></div></footer>{SCRIPT}</body></html>'''


def ribbon(B,t):
    return f'<div class="cta-ribbon"><div class="wrap"><div><h2>{text(t,"ribbon_h")}</h2><p>{text(t,"ribbon_p")}</p></div>{a(B.url(t,"pricing"),text(t,"start")+" →","btn")}</div></div>'


def plans(B,t,compact=False):
    rows=[]
    for i,(name,amount,cadence,description,key,button) in enumerate(B.X[t['lang']]['tiers']):
        href=B.url(t,'pricing') if compact else B.BUY if key=='beta' else B.PLAN_LINKS[key]
        cta=a(href,button,'btn small') if compact or key=='beta' or B.PLANS_LIVE else f'<span>{B.X[t["lang"]]["soon"]}</span>'
        tag=f'<span class="method">{B.X[t["lang"]]["now_tag"]}</span>' if i==0 else ''
        rows.append(f'<div class="plan-line {"featured" if i==0 else ""}"><div class="plan-name">{name} {tag}</div><div class="plan-price">{amount}<small>{cadence}</small></div><div class="plan-description">{description}</div>{cta}</div>')
    return '<div class="pricing-open">'+''.join(rows)+'</div>'


def home_end(B,t):
    download_heading, download = t['go_steps'][0]
    return f'''<section class="space white"><div class="wrap"><div class="rowtitle"><div><p class="eyebrow">{text(t,'free')}</p><h2 class="sectiontitle">{text(t,'free_h')}</h2></div>{a(B.url(t,'pricing'),text(t,'pricing')+' →','arrowlink')}</div><p class="intro">{B.X[t['lang']]['tiers_sub']}</p>{plans(B,t,True)}<div class="home-download"><h3>{download_heading}</h3><p>{download}</p></div></div></section><!--LATEST-->{ribbon(B,t)}'''


def latest(B,t,rows):
    return f'''<section class="space"><div class="wrap"><div class="rowtitle"><h2 class="sectiontitle">{text(t,'latest_h')}</h2>{a(B.url(t,'guides'),text(t,'latest_all')+' →','arrowlink')}</div><div class="editorial"><div class="feature-article"><p class="eyebrow">{text(t,'guide_kicker')}</p><h2>{text(t,'guide_h')}</h2><p>{text(t,'guide_p')}</p><div class="cta">{a(B.url(t,'guides'),text(t,'guide_cta')+' →','btn g')}</div></div><div class="article-list">{rows}</div></div></div></section>'''


def lines(t,keys):
    return '<div class="explain-lines">'+''.join(f'<div><span class="number">{i:02}</span><b>{text(t,k+"_h")}</b><p>{text(t,k+"_p")}</p></div>' for i,k in enumerate(keys,1))+'</div>'


def exchanges(B,t):
    rows=[]
    for i,(name,method,coverage) in enumerate(t['ex'][:-1]):
        methods='API CSV' if 'API' in method and method != 'API' else 'API' if method == 'API' else 'CSV'
        badges=''.join(f'<span class="method">{m}</span>' for m in methods.split())
        guide='guide-kraken'+('.html' if t['lang']=='nb' else '-en.html')
        detail=f'<h3>{text(t,"coverage")}</h3><p>{coverage}.</p>'
        detail+=f'<p>{text(t,"kraken_futures")}</p>{a(guide,text(t,"guide_link")+" →")}' if name=='Kraken' else f'<p>{text(t,"check_import")}</p>'
        rows.append(f'<details class="exchange-row" data-name="{name.lower()}" data-method="{methods}" {"open" if i==0 else ""}><summary><span class="exchange-initial">{name[:2]}</span><span class="exchange-name">{name}</span><span>{badges}</span><span class="coverage">{coverage}</span></summary><div class="exchange-detail">{detail}</div></details>')
    filters=''.join(f'<button type="button" class="filter {"active" if value=="ALL" else ""}" data-filter="{value}" aria-pressed="{str(value=="ALL").lower()}">{label}</button>' for value,label in [('ALL',text(t,'all')),('API','API'),('CSV',text(t,'file'))])
    count=text(t,'exchange_count')
    return f'''<section class="space" id="{t['ids'][2]}"><div class="wrap"><div class="hero-split"><div>{title(t,'imports','import_h')}<p class="intro">{t['hero_import']}</p></div><img class="fox-small" src="assets/hero-fox.webp" alt="" width="260" height="260"></div><div class="exchange-search-area"><label for="exchange-search" class="tiny">{text(t,'search_exchange')}</label><input type="search" class="field" id="exchange-search" placeholder="{text(t,'search_exchange')} …"><div class="filters" aria-label="{text(t,'imports')}">{filters}</div></div><p class="tiny" id="exchange-count" role="status" aria-live="polite" data-label="{count}">{len(rows)} {count}</p><div class="exchange-list">{''.join(rows)}</div><p id="exchange-empty" hidden>{text(t,'no_exchanges')}</p><div class="template-row"><div><h2>{text(t,'another_exchange')}</h2><p class="muted">{text(t,'template_p')}</p></div>{a(B.DISCORD,text(t,'contact')+' →','btn g')}</div><p class="tiny">{text(t,'integration_note')}</p></div></section>'''


def portfolio(B,t):
    legend=''.join(f'<li><span class="dot" style="--coin:{color}"></span><b>{asset}</b><span class="share">{share} %</span></li>' for asset,share,color in B.HERO_ALLOCATION)
    amounts=['44 684','32 768','21 846'] if t['lang']=='nb' else ['44,684','32,768','21,846']
    currency='kr' if t['lang']=='nb' else 'NOK'
    total='99 298 kr' if t['lang']=='nb' else '99,298 NOK'
    rows=''.join(f'<tr><td><b>{asset}</b></td><td>{amount} {currency}</td><td>{change}</td><td>{share} %</td></tr>' for (asset,share,_),amount,change in zip(B.HERO_ALLOCATION,amounts,['+1.2 %','−0.8 %','+3.1 %']))
    columns=''.join(f'<th scope="col">{text(t,k)}</th>' for k in ('asset','value','day','share'))
    return f'''<section class="space" id="{t['ids'][0]}"><div class="wrap">{title(t,'portfolio','portfolio_h','portfolio_p')}<div class="product-panel"><div class="product-bar"><b>{text(t,'portfolio_panel')}</b><span class="examplelabel">{text(t,'example')}</span></div><div class="portfolio-dash"><div class="allocation"><div class="demo-donut"><span>{text(t,'allocation')}</span></div><ul class="demo-legend">{legend}</ul></div><div class="history"><span class="tiny">{text(t,'total_value')}</span><div class="product-total">{total}</div>{B.hero_history(t)}</div></div><table class="asset-table"><thead><tr>{columns}</tr></thead><tbody>{rows}</tbody></table><p class="tiny">{text(t,'chart_note')}</p></div>{lines(t,['holdings','history','basis'])}</div></section>{ribbon(B,t)}'''


def tax(B,t):
    items=''.join(f'<div><dt>{a}</dt><dd>{v}</dd></div>' for a,v in t['story_report_items'])
    paper=f'<div class="document-display"><div class="story-paper"><p class="report-brand">Kryptokompis</p><h2>{text(t,"annual_report")}</h2><p class="report-year">{text(t,"report_year")}</p><dl>{items}</dl><p class="report-formats">{text(t,"report_formats")}</p></div></div>'
    chapters=''.join(f'<div><span class="number">{i:02}</span><strong>{text(t,k)}</strong><p>{text(t,k+"_p")}</p></div>' for i,k in enumerate(['basis_step','docs_step','export_step'],1))
    return f'''<section class="space" id="{t['ids'][1]}"><div class="wrap hero-split"><div>{title(t,'tax','tax_h','tax_p')}<div class="cta">{a(t['report_pdf'],text(t,'report_link')+' →','btn')}</div><p class="tiny">{t['warn']}</p></div>{paper}</div></section><section class="space white"><div class="wrap"><h2 class="sectiontitle">{text(t,'report_h')}</h2><div class="chapter-list">{chapters}</div><div class="open-note">{text(t,'report_note')}</div><div class="cta">{''.join(a(h,label,'btn g') for h,label in t['files'])}</div></div></section>{ribbon(B,t)}'''


def pricing(B,t):
    x=B.X[t['lang']]
    # Reuse the existing, functioning resend form/script without issuing any request during build.
    old=B.sec_start(t,False)
    lost=old[old.index('<div class="tip" id="lost">'):old.rindex('</div></section>')]
    lost=lost.replace('class="tip"','class="licence-help"').replace('class="lost"','class="inline-form"')
    download=''.join(f'<div class="download-option"><span class="device-sign" aria-hidden="true">{symbol}</span><div><h3>{name}</h3><p>{text(t,key)} v{B.VERSION}</p>{a(href,name+" ↓","btn")}{windows_help(t["lang"]) if key=="win_p" else ""}</div></div>' for symbol,name,key,href in [('▦','Windows','win_p',B.DL_WIN),('▣','Android (APK)','android_p',B.DL_APK)])
    return f'''<section class="space white"><div class="wrap">{title(t,'pricing','pricing_h')}<p class="intro">{t['go_sub']}</p><div class="free-line"><div><strong>{text(t,'free_portfolio')}</strong><p class="muted">{text(t,'free_p')}</p></div>{a('#'+t['ids'][4],text(t,'download')+' ↓','arrowlink')}</div>{plans(B,t)}<p class="tiny">{t['pay_note']}</p></div></section><section class="space" id="{t['ids'][4]}"><div class="wrap"><h2 class="sectiontitle">{text(t,'ready')}</h2><div class="downloads">{download}</div><p>{a(B.RELEASES,text(t,'versions')+' →','arrowlink')}</p><div class="support-area"><div><p class="eyebrow">{x['portal_h']}</p><h3>{x['portal_btn']}</h3><p>{x['portal_p']}</p>{a(B.PORTAL,x['portal_btn']+' →','arrowlink')}</div>{lost}</div></div></section>'''


def controls(B,t):
    checks=''.join(f'<div class="checkline"><span class="statusdot {"ok" if i==0 else ""}"></span><div><b>{text(t,h)}</b><p>{text(t,p)}</p></div></div>' for i,(h,p) in enumerate([('imported','imported_p'),('review','review_p'),('export_check','checks_example')]))
    flow='<span aria-hidden="true">→</span>'.join(f'<div><b>{text(t,h)}</b><small>{text(t,p)}</small></div>' for h,p in [('api_csv','history_added'),('local','devices'),('reports','documentation')])
    return f'''<section class="space navy-feature" id="{t['ids'][3]}"><div class="wrap hero-split equal"><div>{title(t,'insights','controls_h','controls_p')}</div><div class="check-example"><div class="rowtitle"><b>{text(t,'checks')}</b><span class="examplelabel">{text(t,'example')}</span></div>{checks}</div></div></section><section class="space white" id="{t['ids'][5]}"><div class="wrap"><p class="eyebrow">{text(t,'flow_kicker')}</p><h2 class="sectiontitle">{text(t,'flow_h')}</h2><div class="flow">{flow}</div>{lines(t,['device','keys','network'])}<div class="open-note">{text(t,'network_note')}</div>{a('personvern.html' if t['lang']=='nb' else 'privacy.html',text(t,'privacy')+' →','arrowlink')}</div></section>'''


def faq(B,t):
    items=[]
    for i,(q,answer) in enumerate(t['faq']):
        anchor = 'id="windows-smartscreen"' if q.startswith('Windows ') else ''
        question = escape(re.sub('<[^>]+>', '', q+' '+answer).lower(), quote=True)
        opened = 'open' if i == 0 else ''
        items.append(f'<details class="faq-item" {anchor} data-question="{question}" {opened}><summary>{q}</summary><p>{answer}</p></details>')
    items=''.join(items)
    groups=''.join(a(B.url(t,k),text(t,k)) for k in ('imports','pricing','insights'))
    return f'''<section class="space" id="{t['ids'][6]}"><div class="wrap">{title(t,'faq','faq_h','faq_p')}<label class="sr-only" for="faq-search">{text(t,'faq_search')}</label><input type="search" id="faq-search" class="field faq-search" placeholder="{text(t,'faq_search')} …"><div class="faq-layout"><aside class="faq-groups">{groups}</aside><div id="faq-items">{items}<p id="faq-empty" role="status" hidden>{text(t,'faq_empty')}</p><div class="open-note">{a(B.DISCORD,text(t,'contact')+' →')}</div><p class="tiny">{t['warn']}</p></div></div></div></section>''' + '''<script>
function openFaqTarget(){const item=document.getElementById(location.hash.slice(1));if(item&&item.matches('.faq-item')){item.hidden=false;item.open=true;item.scrollIntoView()}}
openFaqTarget();window.addEventListener('hashchange',openFaqTarget);
</script>'''


def reading(t,content):
    """Add navigation without rewriting legal/article text. Preserve existing heading IDs."""
    headings=[]
    def heading(m):
        attrs,label=m.groups()
        ident=re.search(r'\bid="([^"]+)"',attrs)
        anchor=ident.group(1) if ident else f'chapter-{len(headings)+1}'
        headings.append((anchor,re.sub('<[^>]+>','',label)))
        return f'<h2{attrs}{"" if ident else chr(32)+"id="+chr(34)+anchor+chr(34)}>{label}</h2>'
    content=re.sub(r'<h2([^>]*)>(.*?)</h2>',heading,content,flags=re.S)
    toc=''.join(a('#'+ident,escape(label)) for ident,label in headings)
    return f'<section class="space white"><div class="wrap reading"><aside class="toc"><p>{text(t,"on_page")}</p>{toc}</aside><article class="prose-reader">{content}</article></div></section>'


def about(B,t,content,photo):
    about_title=title(t,'about','about_h','about_p')
    resources=''.join(a(B.url(t,k),text(t,k)+' →') for k in ('guides','pricing','insights'))+a(t['info'],text(t,'info')+' →')
    return f'''<section class="space white"><div class="wrap hero-split"><div>{about_title}</div>{photo.replace('class="who"','class="owner-photo"').replace('width="120" height="120"','width="310" height="360"')}</div></section><section class="space"><div class="wrap editorial"><div class="prose-reader">{content}</div><aside class="resource-lines"><p class="eyebrow">{text(t,'info')}</p>{resources}</aside></div><div class="wrap"><div class="contact-band"><div><p class="eyebrow">{text(t,'about')}</p><h2>{text(t,'contact_h')}</h2><p class="muted">{text(t,'contact_p')}</p></div><div>{a(B.DISCORD,'Discord ↗','btn')}{a('https://www.linkedin.com/in/christian-thesen','LinkedIn ↗','arrowlink')}</div></div></div></section>'''


SCRIPT = r'''<script>
const toggle=document.querySelector('.menu-toggle');const menu=document.getElementById('site-menu');
if(toggle&&menu){const close=()=>{toggle.setAttribute('aria-expanded','false');menu.classList.remove('open')};toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));menu.classList.toggle('open',open)});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true'){close();toggle.focus()}});menu.addEventListener('click',e=>{if(e.target.closest('a'))close()});}
const search=document.getElementById('exchange-search');let method='ALL';
function filterEx(){let count=0;document.querySelectorAll('.exchange-row').forEach(r=>{const show=r.dataset.name.includes(search.value.trim().toLowerCase())&&(method==='ALL'||r.dataset.method.split(' ').includes(method));r.hidden=!show;if(show)count++});const status=document.getElementById('exchange-count');status.textContent=count+' '+status.dataset.label;document.getElementById('exchange-empty').hidden=count>0}
if(search){search.addEventListener('input',filterEx);document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{method=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>{x.classList.toggle('active',x===b);x.setAttribute('aria-pressed',String(x===b))});filterEx()}))}
const faqSearch=document.getElementById('faq-search');if(faqSearch)faqSearch.addEventListener('input',()=>{let count=0;document.querySelectorAll('[data-question]').forEach(x=>{x.hidden=!x.dataset.question.includes(faqSearch.value.trim().toLowerCase());if(!x.hidden)count++});document.getElementById('faq-empty').hidden=count>0});
document.querySelectorAll('[data-source-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-news-source]').forEach(row=>row.hidden=button.dataset.sourceFilter!=='ALL'&&row.dataset.newsSource!==button.dataset.sourceFilter);document.querySelectorAll('[data-source-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===button)))}));
</script>'''
