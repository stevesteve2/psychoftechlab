# Psychology of Technology Lab — Website

Static site for the Psychology of Technology Lab at Carnegie Mellon University (Director: Steve Rathje).

## Editing
- Page content lives in `build_site.py` (one body string per page). Edit, then run `python3 build_site.py`.
- Shared nav/footer: `_nav.tmpl`, `_foot.tmpl`. Shared styles: `style.css`.
- Or edit the generated `.html` files directly if you prefer (just know a rebuild overwrites them).

## To-do before launch
- [ ] Add the TiCS cover image as `images/virality-cover.jpg` (the gradient placeholder shows until then)
- [ ] Replace the two YouTube embed URLs in `media.html` (search `REPLACE_ME`)
- [ ] Fill in the `<!-- EDIT -->` bio notes on `people.html`
- [ ] Add headshots (drop images in `images/`, swap the initials avatars for `<img>` tags)

## Hosting on GitHub Pages
Already set up: pushing to `main` deploys automatically (Settings → Pages → Deploy from branch → main /root).

## Connecting psychoftechlab.com (once you register it)
1. Register the domain (Cloudflare Registrar, Porkbun, or Namecheap — ~$10/yr).
2. At your registrar, add DNS records:
   - `A` records for `psychoftechlab.com` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - `CNAME` record for `www` → `stevesteve2.github.io`
3. In this repo: Settings → Pages → Custom domain → enter `psychoftechlab.com` → Save
   (this creates a `CNAME` file in the repo — commit it).
4. Wait for the DNS check, then tick **Enforce HTTPS**.
