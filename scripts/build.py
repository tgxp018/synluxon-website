#!/usr/bin/env python3
"""Build the public static pages. No runtime dependencies or network requests."""
from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
BASE = 'https://synluxon.com'
MUSIC = 'https://t.me/yinyueshebot'
BOOKS = 'https://t.me/SynluxonBooksbot'
MINIAPP = 'https://app.synluxon.com'
UPDATED = '2026-10-07'

def text(en, zh, tag='span', cls='', extra=''):
    return f'<{tag} class="{cls}" data-en="{esc(en, quote=True)}" data-zh="{esc(zh, quote=True)}" {extra}>{esc(en)}</{tag}>'

def link(url, en, zh, cls='', external=False):
    return f'<a class="{cls}" href="{url}"'+(' rel="noopener noreferrer"' if external else '')+'>'+text(en, zh)+'</a>'

def header():
    return f'''<a class="skip" href="#main">{text('Skip to content','跳到正文')}</a>
<header class="site-header"><div class="shell header-inner">
<a class="wordmark" href="/" aria-label="Synluxon home"><span class="mark" aria-hidden="true">S</span>Synluxon</a>
<nav aria-label="Main navigation" data-en-aria="Main navigation" data-zh-aria="主导航">
{link('/#products','Products','产品')}{link('/#about','About','关于')}{link('/privacy','Privacy','隐私')}{link('/terms','Terms','条款')}
</nav><div class="language" role="group" aria-label="Language" data-en-aria="Language" data-zh-aria="语言">
<button type="button" data-language="en" aria-pressed="true" lang="en">EN</button><button type="button" data-language="zh" aria-pressed="false" lang="zh-CN">简体中文</button>
</div></div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="shell footer-inner"><div><a class="wordmark" href="/">Synluxon</a><p>{text('Useful tools, built for Telegram.','为 Telegram 打造简单、实用的工具。')}</p></div><nav aria-label="Footer navigation" data-en-aria="Footer navigation" data-zh-aria="页脚导航">{link('/#products','Products','产品')}{link('/privacy','Privacy','隐私')}{link('/terms','Terms','条款')}</nav><small>© 2026 Synluxon</small></div></footer>'''

def page(slug, title_en, title_zh, desc_en, desc_zh, body):
    path = '/' + slug if slug else '/'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title data-en="{esc(title_en)}" data-zh="{esc(title_zh)}">{esc(title_en)}</title>
<meta name="description" content="{esc(desc_en)}" data-en-content="{esc(desc_en)}" data-zh-content="{esc(desc_zh)}">
<link rel="canonical" href="{BASE}{path}"><meta name="theme-color" content="#111315"><meta name="color-scheme" content="dark">
<meta property="og:type" content="website"><meta property="og:site_name" content="Synluxon"><meta property="og:url" content="{BASE}{path}">
<meta property="og:title" content="{esc(title_en)}" data-en-content="{esc(title_en)}" data-zh-content="{esc(title_zh)}"><meta property="og:description" content="{esc(desc_en)}" data-en-content="{esc(desc_en)}" data-zh-content="{esc(desc_zh)}">
<meta property="og:image" content="{BASE}/assets/og.jpg"><meta property="og:image:width" content="1730"><meta property="og:image:height" content="909"><meta property="og:image:alt" content="Synluxon — Useful tools, built for Telegram.">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title_en)}" data-en-content="{esc(title_en)}" data-zh-content="{esc(title_zh)}"><meta name="twitter:description" content="{esc(desc_en)}" data-en-content="{esc(desc_en)}" data-zh-content="{esc(desc_zh)}"><meta name="twitter:image" content="{BASE}/assets/og.jpg">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/site.css"><script src="/assets/site.js" defer></script></head><body>{header()}<main id="main">{body}</main>{footer()}</body></html>'''

home = f'''<section class="hero shell"><div class="hero-top"><p class="eyebrow">SYNLUXON</p><p class="hero-note">{text('Two focused tools. Inside Telegram.','两个实用工具，都在 Telegram 里。')}</p></div>
<h1>{text('Useful tools,','简单、实用的工具，',cls='hero-line')}{text('built for Telegram.','为 Telegram 打造。',cls='hero-line accent-line')}</h1>
<p class="hero-translation" lang="zh-CN">为 Telegram 打造简单、实用的工具。</p>
<div class="hero-bottom"><p class="hero-copy">{text('Music to discover. Records to keep. Focused tools that fit naturally into your conversations.','发现喜欢的音乐，记下每一笔收支。让实用工具，自然融入你的聊天。')}</p>{link('#products','Explore Products','探索产品','button primary')}</div></section>
<section id="products" class="products shell"><div class="section-heading"><p class="eyebrow">{text('OUR PRODUCTS','我们的产品')}</p><h2>{text('A little less friction.','让日常，轻松一点。')}</h2></div>
<div class="product-grid"><article class="product-card music-card"><div class="card-top"><span class="product-number">01</span><span class="product-kind">{text('MUSIC','音乐')}</span></div><div class="product-symbol" aria-hidden="true">♫</div><h3>Synluxon Music</h3><p class="product-summary">{text('Search, discover and enjoy music directly in Telegram.','在 Telegram 里搜索、发现和获取喜欢的音乐。')}</p><ul class="compact-list"><li>{text('Find songs by title or artist','按歌名或歌手查找')}</li><li>{text('Discover music and keep favorites','发现音乐，收藏喜欢的歌曲')}</li><li>{text('Listen without leaving the conversation','在聊天中获取和收听音乐')}</li></ul><div class="card-actions">{link(MUSIC,'Open in Telegram','在 Telegram 中打开','button secondary',True)}{link('/music','Product details','了解产品','text-link')}</div><p class="bot-handle">@yinyueshebot</p></article>
<article class="product-card books-card"><div class="card-top"><span class="product-number">02</span><span class="product-kind">{text('BOOKKEEPING','记账')}</span></div><div class="product-symbol ledger-symbol" aria-hidden="true">≡</div><h3>Synluxon Books</h3><p class="product-summary">{text('A smart ledger built for Telegram.','长在 Telegram 里的智能账本。')}</p><p class="card-description">{text('Record income and expenses in chat. Manage ledgers and view statistics in the Mini App, on your own or with a team.','聊天里直接记账，Mini App 看账和统计，个人和团队都能用。')}</p><div class="card-actions">{link(BOOKS,'Open in Telegram','在 Telegram 中打开','button secondary',True)}{link('/books','Product details','了解产品','text-link')}</div><p class="bot-handle">@SynluxonBooksbot</p></article></div></section>
<section id="about" class="about shell"><div class="about-heading"><p class="eyebrow">{text('WHY SYNLUXON','为什么选择 Synluxon')}</p><h2>{text('Useful by design.','让工具回归实用。')}</h2><p>{text('Synluxon is a software brand building focused tools for the place your conversations already happen.','Synluxon 是一个软件产品品牌，在你熟悉的聊天环境里，打造专注、实用的工具。')}</p></div><div class="principles"><article><span class="principle-index">01</span><h3>{text('Built for Telegram','为 Telegram 而生')}</h3><p>{text('Work with bots and Mini Apps in a familiar space.','用机器人和 Mini App，在熟悉的环境中完成日常事项。')}</p></article><article><span class="principle-index">02</span><h3>{text('Simple by design','简单，是设计的起点')}</h3><p>{text('Clear actions, focused features, less to get in your way.','清晰的操作，专注的功能，减少不必要的步骤。')}</p></article><article><span class="principle-index">03</span><h3>{text('A tool for the task','专注每一件事')}</h3><p>{text('Music for listening. Books for keeping your records in order.','Music 帮你发现音乐，Books 帮你理清收支。')}</p></article></div></section>'''

music = f'''<section class="product-hero shell"><p class="eyebrow">SYNLUXON MUSIC</p><h1>{text('Your next song.','下一首喜欢的歌。')}<br>{text('Already in the chat.','就在聊天里。',cls='accent-line')}</h1><p class="lead">{text('Search, discover and enjoy music directly in Telegram.','在 Telegram 里搜索、发现和获取喜欢的音乐。')}</p><div class="actions">{link(MUSIC,'Open Synluxon Music','打开 Synluxon Music','button primary',True)}<span class="bot-handle">@yinyueshebot</span></div></section>
<section class="features shell"><div class="section-heading"><p class="eyebrow">{text('LISTEN YOUR WAY','按你的方式听歌')}</p><h2>{text('From a name to a favorite.','从一个歌名，到一首收藏。')}</h2></div><div class="feature-grid"><article><h3>{text('Search','搜索')}</h3><p>{text('Find music by song title or artist, right in the bot.','在机器人里，按歌名或歌手查找音乐。')}</p></article><article><h3>{text('Discover','发现')}</h3><p>{text('Browse results and choose the track you want to hear.','浏览搜索结果，选择你想听的歌曲。')}</p></article><article><h3>{text('Keep favorites','收藏')}</h3><p>{text('Save favorites and revisit them from your personal list.','把喜欢的歌曲加入收藏，随时回到个人列表查看。')}</p></article></div></section><section class="closing shell"><h2>{text('Start with a song you love.','从一首喜欢的歌开始。')}</h2><p>{text('Open the bot in Telegram and enter a song or artist name.','在 Telegram 打开机器人，输入歌名或歌手名。')}</p>{link(MUSIC,'Open in Telegram','在 Telegram 中打开','button secondary',True)}</section>'''
books = f'''<section class="product-hero shell"><p class="eyebrow">SYNLUXON BOOKS</p><h1>{text('A smart ledger,','长在 Telegram 里的',cls='hero-line')}{text('built for Telegram.','智能账本。',cls='hero-line accent-line')}</h1><p class="lead">{text('Record income and expenses in chat. Manage your books and see statistics in the Mini App — for yourself or your team.','聊天里直接记账，Mini App 看账和统计，个人和团队都能用。')}</p><div class="actions">{link(BOOKS,'Open Synluxon Books','打开 Synluxon Books','button primary',True)}{link(MINIAPP,'Open Mini App','打开 Mini App','button secondary',True)}</div><p class="bot-handle">@SynluxonBooksbot</p></section>
<section class="features shell"><div class="section-heading"><p class="eyebrow">{text('YOUR RECORDS, IN ORDER','收支有记录，账目更清楚')}</p><h2>{text('Keep the conversation moving.','记账，不打断聊天。')}</h2></div><div class="feature-grid books-features"><article><h3>{text('Income & expenses','记录收入支出')}</h3><p>{text('Add everyday transactions directly in Telegram.','在 Telegram 里直接记录日常收支。')}</p></article><article><h3>{text('Multiple ledgers','多个账本')}</h3><p>{text('Keep different sets of records in separate ledgers.','把不同用途的记录，放进各自的账本。')}</p></article><article><h3>{text('Personal & team use','个人与团队')}</h3><p>{text('Use your own ledger or work with a team.','管理自己的账本，也可以与团队一起使用。')}</p></article><article><h3>{text('Statistics','统计')}</h3><p>{text('Review income, expenses and your recorded activity.','查看收入、支出与已记录的账目。')}</p></article><article><h3>{text('Mini App management','Mini App 管理')}</h3><p>{text('View and manage your books from the Telegram Mini App.','在 Telegram Mini App 中查看和管理账本。')}</p></article></div></section><section class="closing shell"><h2>{text('Make room for clearer records.','给每一笔收支，一个清楚的去处。')}</h2><p>{text('Start with the bot. Open the Mini App when you want a closer look.','从机器人开始记账，需要查看详情时，再打开 Mini App。')}</p>{link(BOOKS,'Open in Telegram','在 Telegram 中打开','button secondary',True)}</section>'''

legal = {
'privacy': ('Privacy','隐私说明', [
 ('This website','本网站','You can browse this website without an account. It has no analytics, advertising trackers or marketing cookies. Your selected language is saved locally in your browser.','浏览本网站无需账户。本网站不使用网站分析、广告追踪器或营销 Cookie。你选择的语言保存在浏览器本地。'),
 ('Website requests','网站请求','Like other websites, serving a page involves processing connection information such as an IP address and request headers. Connection and operational information may be retained to run and maintain the website.','和其他网站一样，提供网页需要处理 IP 地址、请求头等连接信息。为运行与维护本网站，连接和运行信息可能会被保留。'),
 ('Synluxon Music','Synluxon Music','Music requests, settings and favorites are handled within the Music product. Information needed to operate the service may be retained. Consult the current privacy notice in the bot for product-specific details.','音乐请求、设置和收藏由 Music 产品处理。为运行服务所需的信息可能会被保留。产品的具体说明，请查看机器人内的现行隐私说明。'),
 ('Synluxon Books','Synluxon Books','Books processes the records, ledger settings and access information needed for its accounting features. Product-specific privacy information and controls are provided within Books.','Books 会处理记账功能所需的记录、账本设置和访问信息。具体隐私说明和相关控制，请查看 Books 产品内的内容。'),
 ('External destinations','外部链接','Telegram links open Telegram services, where Telegram’s own policies apply. Product links open the relevant Synluxon product, whose notices may differ from this website summary.','Telegram 链接会打开 Telegram 服务，适用 Telegram 自身的政策。产品链接会打开对应的 Synluxon 产品，产品说明可能与本网站概要不同。')]),
'terms': ('Terms','使用条款', [
 ('Website information','网站信息','This website introduces Synluxon products. Features, availability and product rules may change; consult the current information shown in each product.','本网站介绍 Synluxon 产品。功能、可用性和产品规则可能调整，请以各产品内展示的现行信息为准。'),
 ('Responsible use','合理使用','Use the website and products lawfully, respect other people’s rights and privacy, and do not misuse or disrupt the services.','请依法使用本网站与产品，尊重他人的权利与隐私，不要滥用或干扰服务。'),
 ('Synluxon Music','Synluxon Music','Only request or use music that you are permitted to access. Product-specific usage rules and limits are shown in Music; this website does not grant rights to third-party content.','请仅请求或使用你有权访问的音乐。Music 产品内提供具体使用规则和限制；本网站不授予第三方内容的权利。'),
 ('Synluxon Books','Synluxon Books','Review the accuracy of the records you enter and manage access to your ledgers carefully. Product-specific plans, permissions and rules are shown within Books.','请核对你录入记录的准确性，并谨慎管理账本访问权限。Books 产品内提供具体套餐、权限与使用规则。'),
 ('Product-specific notices','产品具体说明','Music and Books are separate products. Their in-product notices govern the relevant product details; this page is a brief brand-level introduction, not a replacement for those notices.','Music 与 Books 是不同的产品。各产品的具体事项请参阅其产品内说明；本页是品牌层面的简要介绍，不代替产品的具体说明。')])}

def legal_body(kind):
    en,zh,sections=legal[kind]
    body=f'<section class="legal shell"><p class="eyebrow">SYNLUXON</p><h1>{text(en,zh)}</h1><p class="updated">{text("Last updated:","最近更新：")} <time datetime="{UPDATED}">{UPDATED}</time></p><div class="legal-content">'
    for a,b,c,d in sections:body+=f'<section><h2>{text(a,b)}</h2><p>{text(c,d)}</p></section>'
    return body+f'</div><div class="legal-products">{link(MUSIC,"Open Music","打开 Music","text-link",True)}{link(BOOKS,"Open Books","打开 Books","text-link",True)}</div></section>'

pages = {
 '': ('Synluxon — Useful tools, built for Telegram.','Synluxon — 为 Telegram 打造简单、实用的工具。','Discover Synluxon Music and Synluxon Books: focused tools for music and bookkeeping in Telegram.','发现 Synluxon Music 和 Synluxon Books：在 Telegram 里搜索音乐、记录收支。',home),
 'music': ('Synluxon Music — Music in Telegram','Synluxon Music — 在 Telegram 里发现音乐','Search, discover and enjoy music directly in Telegram with Synluxon Music.','用 Synluxon Music 在 Telegram 里搜索、发现和获取喜欢的音乐。',music),
 'books': ('Synluxon Books — A smart ledger for Telegram','Synluxon Books — 长在 Telegram 里的智能账本','Record income and expenses in chat. Manage multiple ledgers and statistics in the Synluxon Books Mini App.','聊天里记录收入支出，用 Synluxon Books Mini App 管理多个账本与统计。',books),
 'privacy': ('Privacy — Synluxon','隐私说明 — Synluxon','Website privacy information and product-specific navigation for Synluxon Music and Synluxon Books.','Synluxon 网站隐私信息，以及 Music 与 Books 产品具体说明入口。',legal_body('privacy')),
 'terms': ('Terms — Synluxon','使用条款 — Synluxon','A concise introduction to Synluxon website use and product-specific notices for Music and Books.','Synluxon 网站使用简介，以及 Music 与 Books 产品具体说明。',legal_body('terms')),
}
for slug,content in pages.items():
    (PUBLIC / ((slug or 'index')+'.html')).write_text(page(slug,*content),encoding='utf-8')
(PUBLIC/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://synluxon.com/sitemap.xml\n')
(PUBLIC/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}/{slug}</loc><lastmod>{UPDATED}</lastmod></url>' for slug in pages)+'</urlset>\n')
print('Built five static bilingual pages.')
