# NUAST Computer Science — GitHub Pages Homepage

A simple, editable homepage for the NUAST Computer Science GitHub organisation, built with plain HTML, CSS, and a small JavaScript file. No frameworks, no build step.

---

## Quick start

1. **Edit text and links** — open `index.html` in any text editor. Look for the `<!-- EDIT: … -->` comments throughout the file; they mark every place you need to update.
2. **Change colours / fonts** — open `style.css` and edit the values under *Section 1 – CSS Custom Properties* near the top of the file.
3. **Add a repository card** — copy one `<article class="repo-card">` block in `index.html` and update the link, title, description, and tag.
4. **Replace placeholder images** — drop your own files into `assets/images/` and update the `src` attributes in `index.html`.
5. **Deploy** — push to your GitHub Pages branch (usually `main` or `gh-pages`).

---

## File structure

```
nuast/
├── index.html          ← Main homepage (edit content here)
├── style.css           ← All styles (edit colours / fonts here)
├── script.js           ← Minimal JS: mobile nav toggle only
├── README.md           ← This file
└── assets/
    └── images/
        ├── logo.svg    ← School logo placeholder (replace with your own)
        └── hero.svg    ← Hero illustration placeholder (replace with your own)
```

---

## Editing guide

### Changing text

Every editable piece of content is marked with a comment like:

```html
<!-- EDIT: Replace with your repository name and link -->
```

Search for `EDIT:` in `index.html` to jump to every place that needs updating.

### Changing the colour scheme

Open `style.css` and find **Section 1 – CSS Custom Properties** (near the top). Edit the hex values next to the comments:

```css
--colour-primary:       #1e6bb8;   /* EDIT: main brand colour */
--colour-accent:        #f5a623;   /* EDIT: highlight / tag colour */
```

All other colours in the file are derived from these variables, so changing them here updates the whole site.

### Adding a new repository card

1. Open `index.html`.
2. Find the `<!-- EDIT: Card 4 — placeholder -->` comment in the *Featured Resources* section.
3. Copy the entire `<article class="repo-card">…</article>` block.
4. Paste it immediately after the closing `</article>` of the last card.
5. Update the `href`, heading text, description, and `data-tag` / `<span class="tag">` values.

### Replacing placeholder images

| File | Purpose | Recommended size |
|------|---------|-----------------|
| `assets/images/logo.svg` | Site logo in the header | 96 × 96 px, SVG or PNG |
| `assets/images/hero.svg` | Hero section illustration | 960 × 640 px, SVG or PNG |

After adding a new image, update the `src` attribute in `index.html`:

```html
<img src="assets/images/your-image.png" alt="Descriptive alt text" />
```

Always provide a meaningful `alt` attribute for accessibility.

### Adding a live GitHub Pages project

1. Find the *Live Student Sites* section in `index.html`.
2. Copy the placeholder `<article class="repo-card repo-card--placeholder">` block.
3. Update the link (the live `*.github.io` URL), title, and description.
4. Remove the `repo-card--placeholder` class once it is a real entry.

---

## Deployment (GitHub Pages)

1. Push all files to the `main` branch (or whichever branch you use).
2. Go to **Settings → Pages** in your GitHub repository.
3. Under *Source*, select your branch and the root folder (`/`).
4. Click **Save**. GitHub will build and publish the site — usually within a minute or two.
5. The URL will be `https://<organisation>.github.io/<repository>/`.

### Using a custom domain

1. Add a `CNAME` file to the root of the repository containing your domain name (e.g. `cs.nuast.example.com`).
2. Configure your DNS provider to point that subdomain to `<organisation>.github.io`.
3. Enable *Enforce HTTPS* in the GitHub Pages settings once DNS has propagated.

---

## Linking to the `nuast-dev` organisation

All inter-organisation links follow this pattern:

```
https://github.com/nuast-dev/<repository-name>
```

For a GitHub Pages site published by `nuast-dev`:

```
https://nuast-dev.github.io/<repository-name>/
```

---

## Accessibility notes

- All images have `alt` attributes. Set `alt=""` only for purely decorative images.
- Navigation includes `aria-label` and keyboard-accessible focus styles.
- The mobile menu toggle uses `aria-expanded` to communicate state to screen readers.
- Colour contrast meets WCAG AA (4.5 : 1 for normal text, 3 : 1 for large text).

---

## Frequently asked questions

**Do I need Node.js / npm to edit this site?**
No. Open the HTML and CSS files in any text editor (e.g. VS Code, Notepad++) and edit them directly.

**Can I add more pages?**
Yes. Copy `index.html`, rename it (e.g. `resources.html`), and update the `<nav>` link in both files.

**Can I add a Google Font?**
Yes. Add a `<link>` tag inside `<head>` in `index.html` (copy the snippet from Google Fonts) and then update `--font-body` and/or `--font-heading` in `style.css`.

**The placeholder images look odd. Can I remove them?**
Yes. Delete the `<div class="hero-image">` block from `index.html` and remove `.hero-image { … }` from `style.css`, or simply replace the files in `assets/images/`.
