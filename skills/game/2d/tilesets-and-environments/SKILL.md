---
name: tilesets-and-environments
description: Design 2D tilesets, textures and level art that tile seamlessly and read clearly. Use whenever the user is drawing tiles, terrain, walls, floors, platforms, backgrounds or repeating textures for a 2D game, asks how many tiles a terrain needs, asks about autotiling, bitmasks, Wang or blob tilesets, asks why their level looks like graph paper, repetitive, flat, noisy or unreadable, or wants parallax and depth in a 2D scene. Covers tile size and grid choice, the 16-tile, 47-tile blob, dual-grid and mini-tile autotiling schemes with their exact tile counts, seamless edge construction, breaking visible repetition with variants and decals, silhouette and value zoning so gameplay stays readable, foreground and background separation, parallax layer budgets and scroll ratios, prop and decal libraries, biome recolours, and composition rules for levels. Always asks for tile size, engine autotiling support and whether art must sit behind gameplay before drawing tiles.
version: 1.0.0
---

# Tilesets and environments

A tileset is a *system*, not a pile of images. The job is to draw the smallest set of tiles that
can build any shape the level designer needs, never shows a visible seam, and never competes with
characters for attention.

## When to use

- Drawing terrain, walls, floors, platforms, cliffs, water or repeating textures.
- Deciding how many tiles a terrain type needs, or setting up autotiling in an engine.
- The level looks like graph paper, or like the same 3 tiles repeated forever.
- Characters get lost in the background; the level is pretty but unreadable.
- Adding depth: parallax layers, foreground occlusion, atmospheric perspective.

Drawing craft is in `../pixel-art-fundamentals/SKILL.md`; colour zoning is in
`../color-and-palettes/references/readability-and-contrast.md`.

## Ask first

1. **Tile size and grid** - 8, 16, 32 or 48 px? Square grid, isometric, or hex?
2. **Engine and autotiling support** - Godot terrain sets, Unity Rule Tiles, Tiled terrain/Wang
   sets, custom bitmask code, or hand placement? This decides whether you draw 6 tiles or 47.
3. **Does art sit behind gameplay?** Platformer collision surfaces and top-down walkable areas have
   hard readability constraints; pure background art does not.
4. **Camera** - fixed screens, scrolling, zoomable? Zoom kills pixel grids.
5. **Scope** - one biome or eight? Palette swaps may be cheaper than new art.

## Core rules

1. **Design the system before the pixels.** Decide which autotiling scheme you are drawing for; the
   tile count and the art both follow from it.
2. **Seams are a geometry problem, not a texture problem.** Edge pixels of adjacent tiles must form
   a continuous pattern, which means designing the edge motif first.
3. **Repetition is broken by variants and decals, not by busier tiles.** A detailed tile repeated
   twenty times looks worse than a plain one, because the eye locks onto its pattern.
4. **Zone the values.** Level geometry lives in a value band; characters, pickups and hazards live
   in another. Decorate inside your band.
5. **Overhang beats grid alignment.** Grass blades, roof edges, vines and rubble that break the tile
   boundary are what stop a tile map from looking like a spreadsheet.
6. **Collision stays on the grid even when art does not.** Draw overhang as decoration only.

## Workflow

**Step 0 - pick the scheme.** 16-tile, 47-tile blob, dual-grid or mini-tile, based on what the
   engine supports and how much art you can afford. See `references/grids-and-autotiling.md`.

**Step 1 - draw the core surface tile.** One flat tile that tiles with itself invisibly. Test it in
   a 4x4 block before anything else.

**Step 2 - build the edge family.** Top, sides, bottom, outer corners, inner corners - the exact
   list depends on the scheme.

**Step 3 - add variants.** 2-4 alternates of the most-used tiles, differing in *detail*, not in
   value or silhouette, so they can be swapped randomly.

**Step 4 - decals and props.** Separate layer: rocks, cracks, plants, puddles, debris. These carry
   most of the visual variety at a fraction of the cost. See `references/props-and-composition.md`.

**Step 5 - layer the scene.** Background, midground, gameplay layer, foreground. Assign value and
   saturation ranges and parallax ratios. See `references/depth-and-parallax.md`.

**Step 6 - playtest the readability.** Screenshot, desaturate, and check that every platform edge,
   hazard and interactable is still obvious.

## References

| File | Read it for |
| --- | --- |
| `references/grids-and-autotiling.md` | Tile sizes, square vs isometric vs hex, the 16 / 47 / dual-grid / mini-tile schemes with exact counts and trade-offs, what each engine supports, slopes and one-way platforms |
| `references/seamless-and-variation.md` | Building a tile that tiles with itself, edge motif design, the 3 causes of visible seams, variant strategy, breaking repetition, dither and texture crawl in tiles |
| `references/depth-and-parallax.md` | Layer budgets, scroll ratios, atmospheric perspective, foreground occlusion, value compression by distance, parallax mistakes |
| `references/props-and-composition.md` | Decal libraries, density rules, leading the eye, landmarks and navigation, biome recolours, level composition checklist |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../pixel-art-fundamentals/SKILL.md` | Drawing craft for individual tiles, texture recipes, edge cleanup |
| `../color-and-palettes/SKILL.md` | Value zoning, biome palettes, keeping backgrounds behind characters |
| `../vfx-and-lighting-2d/SKILL.md` | Light shafts, animated water, emissive tiles, weather |
| `../sprite-animation/SKILL.md` | Animated tiles: water, torches, machinery, foliage sway |
| `../game-art-pipeline/SKILL.md` | Atlas bleed between tiles, seams from filtering, import settings, tilemap performance |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Visible grid lines between tiles | Atlas bleeding or bilinear filtering, not the art | Point filtering, 1-2 px extrude/padding, mipmaps off |
| "Looks like graph paper" | Every shape aligned to the grid, no overhang | Add overhang decoration, break silhouettes, vary edge tiles |
| Obvious repeating pattern | One high-contrast detail inside a tile | Move the detail to a decal, flatten the tile, add plain variants |
| Level reads as noise | Tiles and characters share values and saturation | Mute the level, reserve a value band for gameplay |
| Players miss platforms | No consistent edge language | One distinctive top-edge treatment used only on standable surfaces |
| Autotiling has holes | Art drawn for the wrong scheme (16 vs 47) | Identify the scheme, fill in the missing corner cases |
| Water/foliage shimmer | Dither or texture phase changes per frame | Lock patterns to world position, not to frame |
| Eight biomes eat the schedule | Redrawing instead of recolouring | One tileset, several palettes - see `../color-and-palettes/references/palette-library.md` |

## Answering style

- Give tile counts and a concrete tile list: "6 source tiles, expanded to the 47-tile blob set".
- Name the scheme you are designing for before discussing art.
- Separate engine problems (seams, filtering) from art problems (repetition, readability). Seams are
  almost always the engine.
- Prefer the cheapest system that covers the level shapes the game actually needs.
