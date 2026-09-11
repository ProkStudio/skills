---
name: game-art-pipeline
description: Set up the technical side of 2D game art so it looks in-engine exactly as it looked in the editor. Use whenever the user asks why their pixel art is blurry, shimmering, wobbling, showing seams or thin lines between tiles, asks what base resolution to pick, how to scale to 1080p or 4K, how to configure sprite import settings, how to pack atlases, how to avoid texture bleeding, how to export spritesheets or 9-slice UI, or how to organise and name game art files and keep them versioned. Covers resolution and integer-scaling maths with concrete base resolutions, point filtering, mipmaps and compression settings, camera and sprite pixel snapping, sub-pixel and rotation problems, atlas packing with padding and extrusion, export automation from Aseprite and Photoshop, Godot and Unity import and stretch settings, folder and naming conventions, source-versus-export separation, and asset review checklists. Always asks for engine, target resolutions and whether the project is pixel-strict before recommending settings.
version: 1.0.0
---

# Game art pipeline

Most "my pixel art looks bad in engine" problems are not art problems. They are resolution,
filtering, snapping and atlas problems, and each of them has a specific, boring fix.

## When to use

- Art looks blurry, soft, shimmering, wobbling or inconsistently sized in engine.
- Thin lines or seams appear between tiles or at sprite edges.
- Choosing a base resolution, or supporting 1080p through 4K and odd aspect ratios.
- Configuring import settings, atlases, spritesheets, 9-slice assets or fonts.
- Setting up folder structure, naming conventions and source-file hygiene for a team.
- Automating exports so the engine always has current art.

Drawing craft belongs to `../pixel-art-fundamentals/SKILL.md`; this skill is about everything
between the editor and the running game.

## Ask first

1. **Engine and version** - Godot, Unity, GameMaker, Love2D, custom? Settings differ and names
   change between versions.
2. **Pixel-strict or stylised?** A strict project accepts no sub-pixel motion, no rotation, no
   non-integer scaling. A stylised one can trade purity for smoothness.
3. **Base resolution and targets** - what native resolution is the art authored for, and which
   output resolutions must be supported?
4. **Camera behaviour** - fixed, scrolling, zooming, rotating? Zoom and rotation are the two biggest
   threats to a pixel grid.
5. **Team size and tools** - solo with Aseprite, or several artists needing conventions and
   automation?

## Core rules

1. **Pick one base resolution and one pixel size for the whole project.** Everything else follows
   from this.
2. **Integer scaling only** for pixel art. Non-integer scale factors resample pixels unevenly, which
   is what "blurry" and "wobbly" actually mean.
3. **Point (nearest-neighbour) filtering, mipmaps off, no lossy compression** for pixel textures.
4. **Snap the camera and sprite positions to whole pixels** every frame, at the render step.
5. **Pad or extrude every atlas entry.** Texture bleeding is the cause of nearly all tile seams.
6. **Never transform pixel art at runtime**: no rotation, no arbitrary scaling, no flipping that
   moves a light source. Draw discrete angles instead.
7. **Source files and exports are different things.** Commit both, but never edit an export.

## Workflow

**Step 0 - decide the base resolution** and the scaling strategy for each target output. See
   `references/pixel-perfect-rendering.md`.

**Step 1 - configure the engine once**: viewport/stretch mode, integer scaling, default filtering,
   camera snapping. Document it in the repo. See `references/engine-import.md`.

**Step 2 - set up folders and naming** before the second artist joins. See
   `references/naming-and-versioning.md`.

**Step 3 - define export recipes** per asset class: sprites, sheets, tilesets, UI 9-slices, fonts.
   See `references/atlases-and-export.md`.

**Step 4 - automate** what you can: Aseprite CLI batch exports, atlas packing on build, a validation
   script that flags off-palette pixels and wrong sizes.

**Step 5 - verify in engine** at every supported resolution, with a test scene containing a 1 px
   checkerboard, a fine-detail sprite, a tiled surface, and UI text.

**Step 6 - review before merge** using the checklist at the end of
   `references/naming-and-versioning.md`.

## References

| File | Read it for |
| --- | --- |
| `references/pixel-perfect-rendering.md` | Base resolution table with integer multiples to 1080p and 4K, integer vs fractional scaling, letterboxing vs viewport expansion, camera and sprite snapping, sub-pixel motion, rotation and zoom, shimmer and wobble diagnosis |
| `references/atlases-and-export.md` | Atlas packing, padding and extrusion against bleeding, spritesheet export recipes, Aseprite CLI, 9-slice export, palette-safe export settings, file formats and compression |
| `references/engine-import.md` | Godot stretch modes and texture filters, Unity sprite import and pixel-perfect setup, GameMaker and generic engine notes, font rendering, shader-based palette swaps |
| `references/naming-and-versioning.md` | Folder structure, naming conventions, source vs export separation, git and LFS for binary art, review checklist, validation automation |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../pixel-art-fundamentals/SKILL.md` | Canvas size, pixel density consistency, drawing craft |
| `../color-and-palettes/SKILL.md` | Palette files, palette-swap shaders, keeping exports on-palette |
| `../sprite-animation/SKILL.md` | Sheet layout, pivots, tags, per-frame durations |
| `../tilesets-and-environments/SKILL.md` | Tile seams, autotiling data, tilemap performance |
| `../game-ui-and-hud/SKILL.md` | UI scaling, 9-slice assets, font sizes across resolutions |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Sprites look blurry | Bilinear filtering, or non-integer scale | Point filter; integer scale; mipmaps off |
| Pixels different sizes across the screen | Fractional scaling resampling unevenly | Integer scale with letterboxing, or a fixed render target upscaled |
| Sprite edges shimmer while moving | Sub-pixel positions | Snap render positions to whole pixels |
| Thin lines between tiles | Atlas bleeding | 1-2 px padding plus edge extrusion; disable mipmaps |
| Sprite "wobbles" when rotating | Runtime rotation of a pixel grid | Pre-draw discrete angles; never rotate |
| Colours shifted after export | Colour profile or lossy compression | Export as PNG, sRGB, no colour management, no compression |
| Art sizes inconsistent between artists | No documented base resolution and pixel size | Publish the standard; add a validation script |
| Text crisp on one machine, soft on another | Font scaling not integer, or DPI scaling | Bitmap font at integer scale, or lock UI scale steps |
| Build has stale art | Manual exports | Automate exports; never commit hand-edited exports |

## Answering style

- Always name the engine setting exactly, and note that names shift between engine versions.
- Give the maths: base resolution, scale factor, resulting output resolution.
- Distinguish art defects from rendering defects before proposing a fix; "blurry" is almost always
  rendering.
- Prefer one project-wide standard over per-asset workarounds.
