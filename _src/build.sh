#!/usr/bin/env bash
# Build the manual and publish it at the root of the repository (what GitHub Pages serves from main).
# Needs: pip install -r requirements.txt
set -euo pipefail
cd "$(dirname "$0")"
mkdocs build --strict --clean
rsync -a site/ ../
