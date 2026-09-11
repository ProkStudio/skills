# Palette library and palette swapping

## Named palettes worth knowing

| Palette | Colours | Character | Good for |
| --- | --- | --- | --- |
| PICO-8 | 16 fixed | Punchy, slightly toy-like, instantly recognisable | Jams, arcade, projects that want the fantasy-console look |
| DawnBringer 16 (DB16) | 16 | Balanced, built for low-res readability | Small projects, strong default |
| DawnBringer 32 (DB32) | 32 | The de facto pixel-art standard; ships as Aseprite's default | Most indie pixel games; safe starting point |
| Sweetie 16 | 16 | Bright, candy, high saturation | Cheerful platformers, casual and mobile |
| Endesga 32 / 64 | 32 / 64 | Modern, vivid, strong hue shifts built in | Action games, expressive characters |
| Nyx8 | 8 | Moody, desaturated, cool | Atmospheric, horror, jam constraint |
| AAP-64 / AAP-Splendor128 | 64 / 128 | Wide gamut with pre-built ramps | Detailed backgrounds, illustration-heavy work |
| Lost Century | 24 | Muted, earthy, cohesive | Medieval, cosy, narrative games |
| Resurrect 64 | 64 | Broad and well-ramped | Projects that outgrew 32 |

Using an existing palette is not cheating - it front-loads the hardest part (coherent ramps) and
lets you learn where its gaps are. Most teams eventually fork one: keep the ramps, add two accents,
drop the colours they never use.

## Hardware-style constraints as a style choice

| Constraint | What it forces |
| --- | --- |
| 4 shades of one hue (Game Boy) | Pure value composition; dithering as your only midtone |
| 3 colours + transparent per sprite (NES) | Extremely disciplined per-asset palettes, colour-coded enemy families |
| 16 colours per tile set (SNES-ish) | Grouping tiles into palette banks by biome |
| 1-bit (2 colours) | Pattern and silhouette do everything |

Declare the constraint in the repo and apply it uniformly, or it becomes an excuse rather than a style.

## Palette swapping

One sprite, many looks: remap palette indices instead of authoring new art. Standard uses:

| Use | How |
| --- | --- |
| Factions / teams | Swap the 2-3 accent colours only; keep values identical so silhouettes read the same |
| Enemy tiers | Shift hue and raise contrast for stronger variants (green slime to blue to black) |
| Day-night | Swap the whole world palette to a cooler, darker, lower-contrast variant; keep emissive colours untouched so lamps pop |
| Biomes | Reuse one tileset with three palettes instead of drawing three tilesets |
| Damage flash | Swap all colours to white for 2-3 frames - see `../../vfx-and-lighting-2d/SKILL.md` |
| Status effects | Tint toward one hue while keeping value structure (poison green, frozen cyan) |

Implementation notes:

- Keep an **index-based** source of truth: a palette strip plus sprites drawn strictly from it. Then
  a swap is a lookup-table shader, one texture, effectively free.
- Never author variants by hand-painting copies. The second variant will drift from the first.
- Emissive and UI colours should live in a reserved block that swaps never touch.
- Value-identical swaps preserve readability; if a variant changes values, re-run the contrast
  checks in `readability-and-contrast.md`.

## Choosing quickly

- No direction, needs to look good now: DB32.
- Wants vivid and modern: Endesga 32.
- Wants cosy and muted: Lost Century.
- Wants a hard constraint for focus: PICO-8 or Nyx8.
- Wants a custom identity: build 4-6 interlocking ramps from a written light story - see
  `palette-construction.md`.
