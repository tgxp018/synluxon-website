# Synluxon website

Canonical source for https://synluxon.com. English / Simplified Chinese static brand pages, independent of the product runtimes. No analytics, ad trackers, database, production Node server or JavaScript framework.

## Build and preview

Run `python3 scripts/build.py` from this repository. Generated HTML is checked in so production requires only static files. The browser language switch uses localStorage for its explicit preference and honors Chinese browser language on first visit; English works without JavaScript.

Serve `public/` with extensionless `.html` routes for local preview. Production routing is in `ops/synluxon.caddy`.

## Deploy

Deploy ONLY the contents of `public/` to an immutable `/var/www/synluxon/releases/<revision>/` directory, then atomically update `/var/www/synluxon/current`. Never publish `.git`, `ops`, `scripts` or this README. Make files readable by Caddy, but not writable by Caddy.

Preserve the existing Caddyfile and root behavior before cutover. Add only this root-domain site; preserve the Music host exactly. Validate with `caddy validate`, then gracefully reload Caddy. Confirm valid HTTPS before enabling the included root-only HSTS header. Do not restart product services. Do not add www until it has independently authorized DNS.

Verification covers six pages, robots/sitemap, EN/ZH, mobile/keyboard access, metadata, headers, TLS, the unchanged Music endpoint and unchanged Accounting subdomains.

## Rollback

Restore only the previous root-domain Caddy behavior using its preserved configuration and graceful reload. Point the static symlink back to its prior release if one existed. Do not roll back product binaries or restart product services for a website problem.

## Product destination provenance

Music: `https://t.me/SynluxonMusicApp`, the owner's sealed Music product.

Books: `https://t.me/SynluxonBooksApp`, a public username for the existing Accounting production bot. Mini App: `https://app.synluxon.com`, verified from its existing non-secret `MINIAPP_BASE_URL` configuration and public HTTPS response. These checks were read-only; no Accounting source/configuration was changed.

No unverified contact address or service-matrix destinations are published.

Clock: `https://t.me/SynluxonClockBot`, the live group attendance bot confirmed by OWNER for WEBSITE-CLOCK-01. Paid licenses are activated manually through the bot's existing private support entry.
