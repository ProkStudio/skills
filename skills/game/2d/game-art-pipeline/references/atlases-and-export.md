# Atlases, export and file formats

## Why atlases

Packing many sprites into one texture reduces draw calls and state changes. The cost is bleeding,
because a sampler can read neighbouring pixels at the edges of a region.

## Padding and extrusion

| Technique | What it does | When |
| --- | --- | --- |
| Padding | Transparent gap (1-2 px) between packed regions | Always |
| Extrusion / edge bleed | Duplicates the outermost row of pixels outward | Tiles and anything scaled or filtered |
| Both | Padding plus extrusion | Tilemaps, the safest default |

Rules:

- 1 px of padding is enough at integer scale with point filtering; use 2 px if the texture is ever
  filtered, scaled or mipmapped.
- Extrusion is the fix for tile seams: the sampler reads a duplicate of the correct edge colour
  instead of the neighbour's pixel.
- Turn mipmaps off for 2D art; mipmaps average across region borders and both blur and bleed.
- If a seam appears only at certain camera positions or zoom levels, it is bleeding or filtering,
  never the art.

## Spritesheet export recipes

| Asset | Layout | Metadata needed |
| --- | --- | --- |
| Character animations | One row per animation, uniform cells | Cell size, pivot, tags, frame durations |
| Tileset | Grid in terrain order for the chosen autotiling scheme | Tile size, margin, spacing, collision notes |
| UI 9-slice | Single panel image | Slice insets (left/right/top/bottom) and inner padding |
| Effects | One row per effect, uniform cells | Frame count, duration, anchor point |
| Icons | Fixed grid, one icon per cell | Grid size, index-to-name mapping |

Keep the metadata in a file next to the image (JSON), not in someone's head or only in the engine.

## Aseprite CLI

Batch exporting from the command line keeps engine assets in sync with sources:

```
# spritesheet + JSON metadata with tags and durations
aseprite -b character.aseprite \
  --sheet character.png --data character.json \
  --format json-array --sheet-pack --inner-padding 1 \
  --filename-format "{tag}_{tagframe}"

# export each layer as a separate file (parallax layers, UI states)
aseprite -b scene.aseprite --split-layers --save-as scene_{layer}.png

# export a tag range only
aseprite -b character.aseprite --frame-tag walk --save-as walk_{frame1}.png
```

Verify flags against `aseprite --help` for your version; option names and defaults have changed
across releases. Wrap the calls in a script committed to the repo so every artist exports identically.

## Photoshop / Krita / other editors

- Export as PNG-24 with alpha; never JPEG for game art.
- Turn off any colour management and "convert to sRGB" steps; a converted PNG can shift palette
  colours by a few units and break palette-swap shaders.
- Disable resampling smoothing when resizing pixel art; use nearest neighbour only, at integer
  factors.
- Beware layer effects (glows, strokes) producing off-palette anti-aliased pixels; flatten and check.

## Palette-safe exports

For projects with a fixed palette:

1. Keep the palette as a file in the repo (`.gpl`, `.pal`, or a 1 px-per-colour PNG strip).
2. Export sprites as indexed PNG where the tooling allows, or validate that the exported RGB values
   are all in the palette.
3. A short validation script (read PNG, collect unique colours, diff against the palette) catches
   most accidental blending and anti-aliasing.
4. If the engine does palette swaps in a shader, the index order must be stable - never reorder the
   palette file after assets exist.

## Formats and compression

| Format | Use | Notes |
| --- | --- | --- |
| PNG | Everything 2D | Lossless, alpha, universally supported |
| Indexed PNG | Strict-palette pixel art | Smallest, guarantees on-palette colours |
| WebP / QOI | Size-constrained builds | Check engine support; ensure lossless mode |
| JPEG | Never for sprites or UI | Lossy artifacts destroy pixel edges and alpha |

In engine, disable lossy texture compression (DXT/ETC/ASTC) for pixel art and UI; the block
artifacts are visible exactly on the hard edges pixel art is made of. Keep textures uncompressed or
lossless, and rely on atlasing for memory savings.

## Build-time automation worth having

1. Export script that regenerates all sheets from sources.
2. Atlas packer run on build with fixed padding/extrusion settings.
3. Validation: off-palette pixels, wrong canvas sizes, missing metadata, non-power-of-two where
   required, sprites exceeding atlas size.
4. A report of total texture memory per scene, so growth is visible before it becomes a problem.
