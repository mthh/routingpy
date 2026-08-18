# routingpy brand assets

Web-friendly logo collection generated from the source `routingpy-logo.svg`.
The original artwork carried a ~20 KB embedded C2PA/AI-provenance metadata blob;
it has been stripped here.

Logo dimensions: **522 × 656** (portrait). Palette: `#1D6AB6` (blue),
`#FE805A` (orange), `#FA9476` / `#F3B89B` (peach), `#F1F0EB` (cream).

## Contents

| File | Use |
|------|-----|
| `routingpy-logo.svg` | Clean, human-readable vector — primary source of truth |
| `routingpy-logo.min.svg` | Minified vector for embedding on the web |
| `png/routingpy-logo-{64,128,256,512,1024}.png` | Raster, aspect-preserving (transparent bg) |
| `favicon/favicon-{16,32,48}.png` | Square favicons (transparent bg) |
| `favicon/favicon.ico` | Multi-resolution ICO (16/32/48) |
| `favicon/apple-touch-icon.png` | 180×180, white bg (iOS renders transparency as black) |
| `favicon/icon-512.png` | 512×512 square, e.g. PWA / web app manifest |

## HTML snippet

```html
<link rel="icon" type="image/svg+xml" href="assets/routingpy-logo.min.svg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32.png">
<link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png">
```

## Regenerating

Requires `scour`, `rsvg-convert`, and ImageMagick (`magick`). See git history / the
session that created these for the exact commands; in short:

1. Strip `<metadata>` + `c2pa`/`xlink` namespaces from the source SVG → `routingpy-logo.svg`
2. `scour` → `routingpy-logo.min.svg`
3. `rsvg-convert -h <size>` for aspect PNGs; render + `magick -extent NxN` for square icons
4. `magick 16 32 48 → favicon.ico`
