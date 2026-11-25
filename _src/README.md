# Source of the manual

The pages are in `docs/` and the navigation in `mkdocs.yml`. `./build.sh` builds the site and copies it to the root of the
repository, which GitHub Pages serves. GitHub Pages does not serve this folder (its name starts with `_`).

- Every page has three files: `page.en.md` (default, at the root of the site), `page.es.md` (under `/es/`) and `page.zh.md`
  (Simplified Chinese, under `/zh/`). A change goes in the three; a missing page shows the English one.
- Links between pages end in plain `.md`. Anchors are the English ones in every language: `build.sh` runs `anchors.py`,
  which writes them in the other languages and fails if their headings differ from the English ones.
- An image is shared by every language unless there is one for a language beside it (`login.es.png`).
- A page removed from `docs/` has to be removed from the root by hand.
- The repository is public. Screenshots must show only invented organizations, users and devices, taken from a local
  stack with the released images, never from DEV or PROD.
