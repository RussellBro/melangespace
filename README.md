# melangespace.com

Static site. No build step. Three pages: `index.html`, `about.html`, `contact.html`. Styles in `css/style.css`. Assets in `assets/`.

## Status

Links and contact email are set. No X account is linked; add one to the nav and footer social blocks if you want it.

The Technical Advisor card in `about.html` is commented out. Do not enable it without written consent.

## Deploy

Any static host works. Fastest paths:

**Cloudflare Pages.** Create a project, upload this folder, set the custom domain to melangespace.com. Free, fast, no config.

**Netlify.** Drag the folder onto app.netlify.com, then add the custom domain.

**GitHub Pages.** Push to a repo, enable Pages on the root, point the domain's DNS at GitHub.

For any of them: DNS at your registrar gets an A or CNAME record pointing at the host, and the host issues the TLS certificate.

## Local preview

```
python -m http.server 8080
```

Then open http://localhost:8080.
