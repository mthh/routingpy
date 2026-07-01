# routingpy documentation

The documentation site is built with [zensical](https://zensical.org/), and the API reference is generated from the
source docstrings via [mkdocstrings](https://mkdocstrings.github.io/). It is published to GitHub Pages at
<https://mthh.github.io/routingpy/> by the [`Documentation` workflow](../.github/workflows/docs.yml) on every push to
`master`.

> This file is intentionally kept out of the built site (it lives next to, not inside, `docs_dir`). It only serves as a
> readme when browsing the `docs/` folder on GitHub.

## Layout

| Path | Purpose |
|---|---|
| `zensical.toml` | Site configuration (`docs_dir = "content"`, theme, markdown extensions, mkdocstrings handler). |
| `content/index.md` | Home page — a symlink to the repository's top-level `README.md`. |
| `content/api.md` | API reference, assembled from `::: routingpy.…` mkdocstrings autodoc blocks. |
| `site/` | Build output (git-ignored). |

## Working on the docs

Docstrings stay in Sphinx/reStructuredText style (`:param:`, `:type:`, `:returns:`, `:rtype:`, `:raises:`); Griffe parses
them natively, so no rewriting is needed when documenting new code.

```bash
# Live preview with auto-reload
uv run zensical serve -f docs/zensical.toml

# One-off build into docs/site/
uv run zensical build -f docs/zensical.toml
```
