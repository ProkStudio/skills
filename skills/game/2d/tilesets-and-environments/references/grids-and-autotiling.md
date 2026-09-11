# Grids and autotiling schemes

## Tile size

| Size | Pros | Cons |
| --- | --- | --- |
| 8 px | Fine level detail, tiny memory, very cheap tiles | Hard to detail; needs many tiles per structure |
| 16 px | The default: good detail-to-cost ratio | Some structures need multi-tile assemblies |
| 32 px | Rich single-tile detail, fewer tiles per structure | 4x the authoring cost of 16 px; coarser level geometry |
| 48-64 px | Near-illustration quality per tile | Level shapes become blocky; usually hand-placed art instead |

Pick one tile size for the project. Mixing a 16 px terrain grid with 24 px props is the same defect
as mixing pixel densities (`../../pixel-art-fundamentals/references/canvas-and-density.md`).

## Grid types

- **Square** - simplest, works with every autotiling scheme, best for platformers and top-down.
- **Isometric** - 2:1 diamond tiles (for example 32x16); needs depth sorting, harder autotiling,
  and every prop must be drawn in the projection.
- **Hex** - good for strategy; 6 neighbours means autotiling rules differ from square schemes.

## Autotiling: the four schemes

Autotiling picks a tile based on which neighbours share the same terrain. Encode the neighbours as
bits (a bitmask), then look up the tile.

| Scheme | Tiles needed | Handles corners? | Art cost | Best for |
| --- | --- | --- | --- | --- |
| 4-bit bitmask (sides only) | 16 | No | Low | Prototypes, blocky styles, platforms |
| 8-bit "blob" (sides + corners) | 47 | Yes | Medium | Polished 2D terrain, organic shapes |
| Dual grid (offset half-tile) | 16 | Yes | Low | Smooth terrain transitions with cheap art |
| Mini-tile / 2x2 quadrant (RPG Maker style) | 5 shapes per quadrant | Yes | Low | Compact sets, many terrain types |

Notes on each:

- **4-bit**: one bit per side (N, E, S, W) gives 2^4 = 16 combinations. Inner corners cannot be
  expressed, so concave junctions look wrong for organic terrain - fine for hard-edged platforms.
- **47-tile blob**: 8 neighbours would be 256 combinations, but corner bits only matter when both
  adjacent sides are filled, which collapses to 47 distinct tiles. This is the classic "complete"
  terrain set and what most polished 2D games use.
- **Dual grid**: keep a data grid of terrain values and a display grid offset by half a tile, so
  each drawn tile looks at the 4 data cells around its corners - 2^4 = 16 tiles, with correct
  corners. Cheapest way to get blob-quality transitions; the trade-off is that the visual grid no
  longer aligns with the data grid, which can complicate hand-authored decoration.
- **Mini-tile**: each tile is assembled from 4 quadrants, each quadrant chosen from a handful of
  shapes. Very compact source art, which is why RPG Maker sets look small yet transition smoothly.

## Engine support

- **Godot**: TileSet terrain sets support both the simple sides-only matching and full corner-and-side
  matching, i.e. the 16-tile and 47-tile styles.
- **Unity**: Rule Tiles (2D Tilemap Extras) let you define neighbour rules per tile; equivalent to
  hand-rolling any of these schemes.
- **Tiled**: terrain and Wang sets, with user-defined edge/corner colours; exports for most engines.
- **Custom**: a bitmask plus a lookup table is about 40 lines of code. Cache results and recompute
  only on edit.

Confirm the scheme with the programmer before drawing. Delivering 16 tiles for a 47-tile system
leaves holes at every inner corner; delivering 47 for a 16-tile system wastes a third of the work.

## Transitions between terrain types

- Two terrains meeting need their own transition tiles, or one terrain must always sit "on top" and
  overlap the other with a decorative edge.
- Cheapest approach: pick a layering order (rock under dirt under grass under snow) and draw only
  the top-edge overlap for each, drawn as a decal strip rather than full tiles.
- Avoid all-pairs transitions: n terrains would need n x (n-1) sets. Layering keeps it linear.

## Platform specifics

- **Slopes**: pick fixed angles (1:1 and 1:2), draw the matching tiles, and make collision match the
  art exactly. Arbitrary slope angles multiply tiles and bugs.
- **One-way platforms**: need a distinct silhouette (thin, with a visible underside) so players can
  tell them from solid ground without trial and error.
- **Ledges and edges**: the top edge of standable geometry deserves its own treatment, used nowhere
  else. This one convention removes most "can I stand on that?" confusion.
- **Ceilings** are not flipped floors - light comes from above, so ceiling tiles need their own
  shading (`../../pixel-art-fundamentals/references/shading-and-form.md`).
