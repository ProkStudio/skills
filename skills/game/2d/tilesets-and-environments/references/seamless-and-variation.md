# Seamless tiles and killing repetition

## Building a tile that tiles with itself

1. Draw the flat surface texture on a single tile.
2. Duplicate it into a 4x4 block and look at it at 100% zoom. Every defect appears here and nowhere
   else.
3. Fix wrapping first: a pattern crossing the right edge must continue exactly at the left edge (and
   top to bottom). Offset the canvas by half a tile and redraw the join if your editor supports it.
4. Then fix *clustering*: even with a perfect wrap, a bright detail near one corner creates a
   diagonal pattern across the block. Push detail toward the tile's interior and keep edges quiet.
5. Aim for a tile that is boring alone. Tiles are wallpaper; interest comes from decals and props.

## The three causes of visible seams

| Cause | How to recognise | Fix |
| --- | --- | --- |
| Atlas bleeding / filtering | Thin lines *between* tiles that change with camera position or zoom | Point filtering, 1-2 px extrude in the atlas, mipmaps off, snap camera to pixels - see `../../game-art-pipeline/references/pixel-perfect-rendering.md` |
| Bad wrap | The same line always appears at the same place inside the pattern | Redraw the edge motif with a half-tile offset |
| Value mismatch | A checkerboard of slightly lighter and darker tiles | Keep average brightness identical across variants |

If the seam moves when the camera moves, it is the engine. If it stays put, it is the art.

## Variants

Draw 2-4 variants of the highest-traffic tiles (plain ground, wall fill, floor). Rules:

- Variants differ in **detail**, never in average value or in silhouette - otherwise random
  placement produces visible blotches.
- Weight them: about 70-80% plain, 20-30% detailed. A uniform random spread over 4 equally busy
  variants reads as noise.
- Keep 1-2 "rare" variants (a cracked slab, a mossy stone) at under 5% frequency. These read as
  care rather than as pattern.

## Decals beat tiles

A separate decoration layer placed freely - not on the grid - buys more variety per hour than any
number of tile variants:

- Small: cracks, pebbles, tufts, stains, bolts, scratches.
- Medium: bushes, rubble piles, puddles, signage, roots, hanging vines.
- Large: dead trees, broken columns, banners, machinery.

Decals may overhang tile boundaries and break the grid silhouette, which is exactly what you want.
Keep them on their own layer so level designers can move them without touching terrain.

## Animated tiles

- Water, lava, torches, machinery, foliage sway: 3-6 frames, 8-12 fps.
- Animate *phase by world position*, not per tile instance, or neighbouring tiles will visibly
  animate out of sync (or, worse, all in perfect sync, which reads as a strobe).
- Lock dither and texture patterns to world position too. Patterns that shift per frame crawl -
  `../../pixel-art-fundamentals/references/dither-and-texture.md`.
- Animated tiles are expensive attention magnets. Use them where you want the player to look.

## Detail budget for surfaces

- Flat surfaces the player walks on: minimum detail, mid values, low saturation.
- Vertical faces (walls, cliffs): more detail, because the player stares at them.
- Anything behind gameplay: reduce contrast, not just brightness.
- Reserve the highest contrast in the scene for gameplay-relevant edges: the top of a platform, the
  lip of a pit, the mouth of a doorway.

## Checklist before shipping a tileset

1. 4x4 block test at 100% - no wrap seams, no diagonal clustering.
2. All autotiling cases filled for the chosen scheme (16 / 47 / dual-grid / mini-tile).
3. Variants match in average value.
4. Standable surfaces have a unique top-edge treatment.
5. Desaturated screenshot: gameplay geometry still readable.
6. Tested in engine at the real camera zoom with point filtering.
