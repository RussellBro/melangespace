# melangespace.com

Static site, no build step on the server. GitHub Pages serves `main` at melangespace.com (see `CNAME`).

- `index.html`: the hero only.
- `careers.html`, `contact.html`: inner pages with a shorter hero.
- `_build.py`: writes those three pages from one shared shell (head, nav, hero, footer). Edit the text in `PAGES`, run `python _build.py`, commit the HTML.
- `css/style.css`: all styles. Day mode tokens are in `:root`, night mode in `[data-mode="night"]`.
- `js/main.js`: day and night toggle, scroll reveals, nav.
- `assets/`: logo (white PNG, coloured by CSS mask), favicon, `shackleton-terrain-*.webp` (hero), `og.jpg` (share image).
- `about.html`: redirect stub so the old link still lands.

## Night mode

Follows the visitor's system setting. The moon or sun button in the nav overrides it and the choice is remembered in the browser.

## Hero image

Shackleton crater, lunar South Pole. NASA Scientific Visualization Studio, "Visualizing Shackleton Crater" (SVS 4716), natural colour with a transparent sky. Credit line is in the footer.

## Careers

Roles are rows in `_build.py` (the `role(...)` lines). Each row is a mailto link. No pay on the site.

## Local preview

```
python -m http.server 8093
```

Then open http://localhost:8093.
