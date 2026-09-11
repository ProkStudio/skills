# Depth, layers and parallax

## A layer budget that works

| Layer | Scroll ratio | Value / saturation | Content |
| --- | --- | --- | --- |
| Sky / far background | 0 to 0.1 | Lightest or darkest, very low contrast | Gradient, clouds, distant mountains, stars |
| Mid background | 0.3-0.5 | Compressed value range, muted | Hills, buildings, tree lines, city skyline |
| Near background | 0.7-0.85 | Slightly muted, more contrast | Structures behind the play space, big props |
| Gameplay layer | 1.0 | Full contrast band reserved for play | Terrain, platforms, hazards, characters |
| Foreground | 1.1-1.4 | Darkest, often silhouettes | Leaves, pillars, railings, fog |

Four to five layers is plenty. More layers mostly cost memory and confusion; the depth illusion
comes from value compression, not from layer count.

## Atmospheric perspective in 2D

Distance is communicated by, in order of strength:

1. **Value compression** - distant layers use a narrow value range close to the sky's value.
2. **Saturation loss** - distant colours drift toward the atmosphere hue.
3. **Detail loss** - distant shapes become silhouettes; no texture, no small props.
4. **Scroll speed** - the parallax itself.

If layers are distinguished by scroll speed alone, the scene looks like sliding stickers. Compress
the values and the same art reads as distance.

## Foreground layers

Foreground elements sell depth faster than any background, because they pass quickly and occlude
the player.

- Keep them dark, low-detail, and mostly around the screen edges.
- Never occlude gameplay-critical space. A branch over a pit that hides a spike is a bug.
- Semi-transparent or soft foregrounds break the pixel-art contract; if the project is pixel-strict,
  use dithered transparency or solid silhouettes instead.

## Parallax mistakes

| Mistake | Result | Fix |
| --- | --- | --- |
| Too many layers at similar speeds | Visual mush, no readable depth | 4-5 layers with clearly separated ratios |
| Background as detailed as gameplay layer | Characters get lost | Compress background contrast |
| Vertical parallax ignored | Layers slide wrongly when jumping or in vertical levels | Apply a smaller vertical ratio, often half the horizontal one |
| Non-integer scroll positions | Background pixels shimmer | Snap each layer's offset to whole pixels |
| Repeating background with an obvious landmark | Player sees the same tower every 3 seconds | Wider tiles, several variants, or move the landmark to a non-looping layer |
| Parallax on the gameplay layer's decorations | Props detach from the ground they sit on | Anything that touches the ground scrolls at 1.0 |

## Vertical levels and cameras

- In tall levels, the sky layer should change value with altitude - it is free storytelling.
- Zooming cameras and pixel art do not mix: any zoom other than integer steps breaks the grid.
  Either lock the zoom, or accept non-pixel-perfect rendering as a project decision
  (`../../game-art-pipeline/references/pixel-perfect-rendering.md`).
- Camera shake must shake all layers by the same world offset, or the depth illusion snaps.

## Fast depth checklist

1. Is there a foreground layer at all?
2. Do background layers use a narrower value range than the gameplay layer?
3. Is the highest contrast in the frame on gameplay geometry?
4. Do all layers snap to whole pixels?
5. Does anything decorative overlap where the player needs to see?
