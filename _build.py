"""Writes index.html, careers.html and contact.html from one shared shell.
Run:  python _build.py   (not needed on the server; the HTML files are committed)
Edit page text in PAGES below, then re-run."""
import pathlib

ROOT = pathlib.Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:site_name" content="Melange Space">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://melangespace.com/assets/og.jpg">
  <meta property="og:url" content="https://melangespace.com/{path}">
  <link rel="canonical" href="https://melangespace.com/{path}">
  <meta name="twitter:card" content="summary_large_image">
  <script>
    // Night mode: the visitor's own choice if they made one, else their system setting.
    (function () {{
      var m = null;
      try {{ m = localStorage.getItem('mode'); }} catch (e) {{}}
      if (m !== 'day' && m !== 'night') m = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'night' : 'day';
      document.documentElement.dataset.mode = m;
    }})();
  </script>
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="assets/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Spectral:wght@200;300&family=Archivo:wdth,wght@125,300;125,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="preload" as="image" href="assets/shackleton-terrain-2000.webp" imagesrcset="assets/shackleton-terrain-1100.webp 1100w, assets/shackleton-terrain-2000.webp 2000w" imagesizes="(max-width: 820px) 160vw, 100vw">
  <link rel="stylesheet" href="css/style.css">{extra_head}
</head>
<body>

<header class="nav" id="nav">
  <a class="brand" href="./" aria-label="Melange Space home"><span class="logo" role="img" aria-label="Melange"><span class="logo-mark"></span><span class="logo-word" aria-hidden="true">Melange</span></span></a>
  <a class="nav-link" href="careers.html"{cur_careers}>Careers</a>
  <button class="mode" type="button" aria-label="Switch between day and night mode">
    <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>
    <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.5 1.5M17.2 17.2l1.5 1.5M5.3 18.7l1.5-1.5M17.2 6.8l1.5-1.5"/></svg>
  </button>
  <a class="btn btn-nav" href="contact.html"{cur_contact}>Contact</a>
</header>

<main>
"""

HERO = """
  <section class="hero{short}" aria-label="{label}">
    <div class="hero-card">
      <div class="sky" aria-hidden="true">
        <div class="sky-glow"></div>
        <img class="terrain" alt="" decoding="async"
             src="assets/shackleton-terrain-2000.webp"
             srcset="assets/shackleton-terrain-1100.webp 1100w, assets/shackleton-terrain-2000.webp 2000w"
             sizes="(max-width: 820px) 160vw, 100vw">
        <div class="terrain-tint"></div>
        <div class="haze"></div>
        <div class="grain"></div>
      </div>
      <div class="hero-copy">
{copy}
      </div>
    </div>
  </section>
"""

FOOT = """
</main>

<footer class="footer{ruled}">
  <div class="footer-inner">
    <span class="logo" role="img" aria-label="Melange"><span class="logo-mark"></span><span class="logo-word" aria-hidden="true">Melange</span></span>
    <p class="copy">&copy; 2026 Melange Space Technologies Corp. El Segundo, California.</p>
    <span class="credit">Crater image: NASA Scientific Visualization Studio</span>
    <a class="foot-link" href="https://www.linkedin.com/company/melange-space/" target="_blank" rel="noopener">LinkedIn</a>
  </div>
</footer>

<script src="js/main.js" defer></script>
</body>
</html>
"""

ORG = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Melange Space Technologies Corp.",
    "alternateName": "Melange Space",
    "url": "https://melangespace.com/",
    "logo": "https://melangespace.com/assets/logo.png",
    "founder": { "@type": "Person", "name": "Russell Boyer" },
    "address": { "@type": "PostalAddress", "addressLocality": "El Segundo", "addressRegion": "CA", "addressCountry": "US" },
    "email": "russell@melangespace.com",
    "sameAs": ["https://www.linkedin.com/company/melange-space/"]
  }
  </script>"""

MAIL = "mailto:russell@melangespace.com"

LOC = "Los Angeles, CA (El Segundo for now). On site, full time"

# Roles match Dover (hiring fork, 24 Nov 2026). HOLD: nothing public until Russell previews in Dover and says go.
# Links are mailto placeholders until the Dover apply pages are active.
# Set PROPULSION = False to drop that row if Russell says no.
PROPULSION = True

def role(title, subject, extra=""):
    return f"""        <li><a href="{MAIL}?subject={subject}">
          <span class="role-main">
            <span class="role-title">{title}</span>
            <span class="role-meta">{LOC}{extra}.</span>
          </span>
          <span class="arrow" aria-hidden="true">&rarr;</span>
        </a></li>"""

ROLES = "\n".join(r for r in [
    role("Founding Engineer, Hardware Lead", "Founding%20Engineer%2C%20Hardware%20Lead"),
    role("Founding Engineer, Embedded Systems and Avionics", "Founding%20Engineer%2C%20Embedded%20Systems%20and%20Avionics"),
    role("Founding Engineer, Propulsion", "Founding%20Engineer%2C%20Propulsion") if PROPULSION else None,
    role("Chief Scientist", "Chief%20Scientist", ", with field days"),
] if r)

PAGES = {
    "index.html": dict(
        title="Melange Space", path="",
        desc="Water on the Moon is rocket fuel. Melange Space maps what lies beneath the lunar surface, the first step to building the first industry beyond Earth.",
        extra_head=ORG, short="", label="Melange Space", ruled="",
        copy="""        <h1 class="display rise" style="--d:.15s">Building the first industry beyond&nbsp;Earth</h1>""",
        body="""
  <section class="story" id="story">

    <div class="beat beat-solo reveal">
      <p class="tag"><span class="dot"></span>The rush</p>
      <h2 class="statement">Water on the Moon is rocket fuel. The first to find it will hold the keys to deep space. Water is the oil of space, and the rush for it is&nbsp;coming.</h2>
    </div>

    <div class="beat reveal">
      <div class="beat-text">
        <p class="tag"><span class="dot"></span>Where we start</p>
        <h2 class="statement">But first, we must map. Thousands of penetrator probes chart water, resources and ground strength across a whole site, so whoever builds there knows what they're standing&nbsp;on.</h2>
      </div>
      <figure class="shot shot-wide"><img src="assets/field-drone.jpg" alt="A drone carrying the Melange test probe over a lake and desert hills" loading="lazy" width="1600" height="1000"></figure>
    </div>

    <div class="proof reveal">
      <figure class="shot shot-tall"><img src="assets/field-probe.jpg" alt="The Melange test probe standing in the ground after a drop" loading="lazy" width="1000" height="1250"></figure>
      <div class="proof-text">
        <p class="tag"><span class="dot"></span>26 October 2026</p>
        <h2 class="statement">We dropped our probe 20 times from the maximum commercial drone height, and the airframe and the electronics inside survived every&nbsp;time.</h2>
      </div>
    </div>

    <div class="closer reveal">
      <p class="tag"><span class="dot"></span>Our bet</p>
      <h2 class="statement">We must look before we&nbsp;leap.<br>And only then will the spice&nbsp;flow.</h2>
      <div class="actions">
        <a class="btn" href="careers.html">Join us</a>
        <a class="btn btn-ghost" href="contact.html">Get in touch</a>
      </div>
    </div>

  </section>
""",
    ),
    "careers.html": dict(
        title="Careers | Melange Space", path="careers.html",
        desc="Open roles at Melange Space in Los Angeles.",
        extra_head="", short=" hero-short", label="Careers", ruled=" ruled",
        copy="""        <h1 class="display rise" style="--d:.15s">Careers</h1>""",
        body=f"""
  <section class="page">
    <div class="page-head reveal">
      <h2 class="statement">We're hiring the first team. Come build the probes that map what's under the&nbsp;Moon.</h2>
    </div>
    <div class="reveal">
      <ul class="roles">
{ROLES}
      </ul>
      <p class="fine">All roles are on site in Los Angeles (El Segundo for now) and require being a U.S. person as defined by ITAR. Don't see your role? <a href="{MAIL}">russell@melangespace.com</a></p>
    </div>
  </section>
""",
    ),
    "contact.html": dict(
        title="Contact | Melange Space", path="contact.html",
        desc="Get in touch with Melange Space.",
        extra_head="", short=" hero-short", label="Contact", ruled=" ruled",
        copy="""        <h1 class="display rise" style="--d:.15s">Contact</h1>""",
        body=f"""
  <section class="page">
    <div class="page-head reveal">
      <h2 class="statement">If what's under the lunar surface matters to what you're building, we'd like to hear from&nbsp;you.</h2>
      <a class="btn" href="{MAIL}">Get in touch</a>
    </div>
    <dl class="details reveal">
      <div><dt>Email</dt><dd><a href="{MAIL}">russell@melangespace.com</a></dd></div>
      <div><dt>Location</dt><dd>El Segundo, California</dd></div>
      <div><dt>Company</dt><dd>Melange Space Technologies Corp.</dd></div>
    </dl>
  </section>
""",
    ),
}

for name, p in PAGES.items():
    html = HEAD.format(
        title=p["title"], desc=p["desc"], path=p["path"], extra_head=p["extra_head"],
        cur_careers=' aria-current="page"' if name == "careers.html" else "",
        cur_contact=' aria-current="page"' if name == "contact.html" else "",
    ) + HERO.format(short=p["short"], label=p["label"], copy=p["copy"]) + p["body"] + FOOT.format(ruled=p["ruled"])
    (ROOT / name).write_text(html, encoding="utf8", newline="\n")
    print("wrote", name, len(html))
