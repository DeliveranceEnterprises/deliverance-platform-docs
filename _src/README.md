# Source of the manual

The pages are in `docs/` (Spanish) and the navigation in `mkdocs.yml`. `./build.sh` builds the site and copies it to the
root of the repository, which GitHub Pages serves. GitHub Pages does not serve this folder (its name starts with `_`).

- A page removed from `docs/` has to be removed from the root by hand.
- The repository is public. Screenshots must show only invented organizations, users and devices, taken from a local
  stack with the released images, never from DEV or PROD.
