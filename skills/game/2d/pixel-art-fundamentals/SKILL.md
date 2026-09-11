---
name: pixel-art-fundamentals
description: Draw readable, non-muddy pixel art and other low-resolution 2D game textures. Use whenever the user is making sprites, tiles, items, icons, portraits or textures for a 2D game, asks what canvas size or how many colours to use, asks how to start a piece, or shows work that looks blurry, noisy, flat, muddy, jagged or "like a beginner". Covers canvas and sprite sizing, integer-friendly base resolutions, keeping one pixel density across a project, silhouette-first construction, line art and outline styles, jaggies and doubles, deliberate anti-aliasing, value structure and light logic, dithering, texture recipes per material, and a named catalogue of the classic defects - pillow shading, banding, noise, orphan pixels, AA halos, mixed pixel sizes - each with a concrete fix. Includes a critique checklist for reviewing existing sprites. Always asks for target resolution, colour budget and where the art will be seen before drawing.
version: 1.0.0
---

# Pixel art fundamentals

Pixel art is not "art with big pixels". It is art where every pixel is placed on purpose, at a
resolution low enough that a single wrong pixel is visible. This skill covers the craft layer:
how to size a sprite, build it silhouette-first, control edges, shade with a light logic, and
diagnose why a finished piece looks amateurish.

## When to use

- The user is drawing a sprite, tile, item, icon, portrait or texture for a 2D game.
- The user asks "what size should my character be", "how many colours", "why does my sprite look bad".
- The user pastes a sprite and wants critique or a fix.
- The user's art looks fine zoomed in but falls apart in the game.
- The user wants a non-pixel 2D texture but the same rules about silhouette, value and edges apply.

For colour choices go to `../color-and-palettes/SKILL.md`, for motion to
`../sprite-animation/SKILL.md`, for tiling rules to `../tilesets-and-environments/SKILL.md`.

## Ask first

Ask two or three of these before drawing anything. The answers change every later decision.

1. **Resolution and grid** - how tall is the character in pixels, what is the tile size, what is
   the game's base resolution? "32 px tall on a 16 px tile grid at 384x216" is an answer you can work with.
2. **Colour budget** - free, or a fixed palette (PICO-8, DB32, 4-shade Game Boy, custom 12)?
3. **Where it will be seen** - zoomed pixel-perfect view, scaled with the camera, a phone screen,
   an icon in UI at 1:1? A sprite that reads at 4x scale can be mush at 1x.
4. **Reference and mood** - one existing game whose look they want to land near.

## Workflow

**Step 0 - lock the grid.** Choose sprite height, tile size and base resolution together, not
separately. Write them down; every asset in the project obeys them. See
`references/canvas-and-density.md`.

**Step 1 - silhouette only.** Draw the shape in one solid colour. If it is not identifiable as a
black shape, no amount of shading will save it. Fix proportion and pose here, where it costs
nothing. Aim for a distinctive outer contour: one big shape, one or two secondary shapes.

**Step 2 - values before colour.** Block in 3 values (base, shadow, light) in greys. Decide the
light direction now and write it down (for example "upper left, 45 degrees") so the whole set matches.
See `references/shading-and-form.md`.

**Step 3 - colour.** Map the greys onto a ramp, then hue-shift. Details in
`../color-and-palettes/SKILL.md`.

**Step 4 - edges.** Clean jaggies, choose an outline style, add anti-aliasing only where a curve
needs it and only in the direction of the slope. See `references/lines-and-edges.md`.

**Step 5 - texture and detail, last.** Add material indication and dithering only after the form
reads. Spend detail where the eye goes: face, weapon, silhouette edge. See
`references/dither-and-texture.md`.

**Step 6 - test at true size.** Run the checklist in `references/critique-checklist.md`: silhouette
test, value test, squint test, 1:1 test, and - if it is a game asset - a look at it in the engine on
the real background. Most defects are invisible at 800% zoom.

## References

| File | Read it for |
| --- | --- |
| `references/canvas-and-density.md` | Sprite and tile sizes, base resolutions that scale to 1080p and 4K by integers, historic hardware limits, keeping one pixel density, proportions at small sizes, when pixel art is the wrong choice |
| `references/lines-and-edges.md` | Jaggies and doubles, line thickness, five outline styles, anti-aliasing rules, banding and band compression, curve drawing without a line tool |
| `references/shading-and-form.md` | Light direction, 3-5 value structure, form vs cast vs contact shadow, bounce light, pillow shading and its fix, specular rules, material cheat sheet, what to cut at 16 px |
| `references/dither-and-texture.md` | Dither patterns and when dithering is wrong, dither crawl in animation, per-material texture recipes, noise vs texture, the 60/30/10 detail budget |
| `references/critique-checklist.md` | The review procedure in order, a symptom-to-fix table of named defects, how to give feedback on someone else's sprite |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../color-and-palettes/SKILL.md` | Choosing or fixing colours, building a palette, contrast and readability |
| `../sprite-animation/SKILL.md` | The sprite has to move, or detail is fighting the frame budget |
| `../tilesets-and-environments/SKILL.md` | The asset is a tile, must repeat seamlessly, or is part of a level |
| `../vfx-and-lighting-2d/SKILL.md` | Glows, emissive materials, impact effects |
| `../game-ui-and-hud/SKILL.md` | The asset is an icon, panel, bar or font |
| `../game-art-pipeline/SKILL.md` | It looks right in the editor and wrong in the engine: filtering, scaling, atlas bleed |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "It looks blurry" | Non-integer scaling or bilinear filtering, not the art | Point/nearest filtering, integer scale - see `../game-art-pipeline/SKILL.md` |
| "It looks flat" | Shading follows the outline inward (pillow shading), no light direction | Pick a direction, shade by plane, add a contact shadow |
| "It looks noisy" | Single stray pixels that belong to no cluster | Merge pixels into clusters of 2+, cut detail, squint test |
| "It looks jagged" | Inconsistent step lengths in a curve | Rebuild the curve with a regular step pattern, then AA |
| "It looks muddy" | Too many mid-tones, too little value separation | Cut to 3 values, push the extremes apart |
| "My sprites don't fit together" | Mixed pixel densities or mixed outline conventions | One grid, one outline rule per project |
| "Great zoomed in, mush in game" | Detail below the display resolution, dither that greys out | Test at 1:1, move detail into bigger shapes |

## Answering style

- Give pixel counts and value counts, not adjectives: "32 px tall, 3 values plus a 1 px specular".
- Name the defect. "That is pillow shading" teaches more than "the shading is off".
- One priority at a time. Silhouette before shading, shading before texture, texture before polish.
- When the user shows work, say what already reads before listing problems, then give the single
  highest-impact fix first.
- Never claim a fixed rule is a law of the medium; say which style or constraint it comes from.
