# Terrain integration

A good build on a flattened square still looks generated. The joint between build and ground
is where most of the realism lives.

## Contents

- The rules
- Foundations on slopes
- Ground transition
- Paths
- Planting
- Water, cliffs, caves
- Orientation
- Anti-patterns

## The rules

1. Never flatten more than the building's own footprint, and preferably not even that.
2. No floating corners and no half-buried walls - every corner meets the ground deliberately.
3. The build must exchange materials with the site: a terrain block appears in the base
   course, and a building block appears in the paths and retaining walls.
4. Terrain edits are part of the build, not a preparation step - terrace, carve and mound as
   design moves.

## Foundations on slopes

Pick a strategy (or mix them across masses):

| Strategy | How | Best for |
| --- | --- | --- |
| Stepped plinth | base course follows the slope in 1-block steps | gentle slopes, villages |
| Terracing | cut 2-4 block platforms with retaining walls | towns, farms, hillside districts |
| Cut and cover | dig one wall into the hill, expose the other | nordic, hobbit, dwarven |
| Stilts / piers | posts, arches or a podium carry an overhanging mass | modern, docks, jungle |
| Podium | deliberately formal raised base with stairs | temples, palaces, monuments |

Fill under the whole footprint with the base material (or stone/cobble) so there is no void
or grass visible beneath the floor, and let the foundation material continue 1-3 blocks into
the ground line.

## Ground transition

Between wall and terrain, place a 1-2 block transition zone:

- Coarse dirt, rooted dirt, gravel or podzol against the wall, feathering into grass.
- Tall grass, ferns and moss carpet in the corners.
- A few loose blocks of the wall material lying in the grass (cobble, bricks, gravel).
- Mossy variants and glow lichen on the bottom 1-2 courses, heavier on shaded faces.
- Dirt paths that erode the grass edge irregularly - never a straight border.

## Paths

- Width hierarchy: main 3-5, secondary 2-3, garden 1-2.
- Irregular edges: alternate the path block with gravel or coarse dirt along the border, and
  vary the width by 1 every few blocks.
- Mixes that read well: dirt path + gravel + coarse dirt; cobblestone + andesite + gravel;
  stone + cobbled deepslate + tuff (1.21+); sand + suspicious sand? no - sand + smooth
  sandstone + gravel for deserts.
- Slopes use stairs or 1-block steps with a slab landing; long staircases need landings every
  6-8 steps.
- Paths connect to the door, and to *something else* (another build, a road, a dock, a gate).
  A path that stops in a field is a tell.

## Planting

- Cluster 3-5 plants of 2-3 species; never a single lone bush, never an even grid.
- Layer heights: tree, shrub (azalea, sweet berry, dead bush), ground cover (grass, ferns,
  pink petals, moss carpet), so the eye reads depth.
- Custom trees near the build: 2x2 trunks and irregular canopies for large builds; vanilla
  saplings look like filler next to good architecture.
- Vines, glow berries and hanging roots only where shade or water justifies them.
- Leave negative space - a clear yard or approach makes the build readable. Do not carpet
  everything in foliage.

## Water, cliffs, caves

- Waterfront: docks, retaining walls, stilts, mooring posts, a shoreline of gravel and clay
  rather than a clean grass edge.
- Cliffs: overhangs and rock strata (layer 2-3 stone variants horizontally) make a wall of
  stone read as a cliff; the build should either cap it or be carved into it.
- Cave/underground entrances: frame with a structure at the surface, and light the throat of
  the passage gradually from bright outside to dim inside.

## Orientation

Align the long axis with the dominant terrain line (ridge, shore, road), not with the
compass. Rotate the build a few degrees off-grid only if the whole build supports it -
diagonal builds need slab/full-block roofs (see `roofs.md`).

## Anti-patterns

- Superflat platform under a natural-style build.
- Building 1 block above the ground "to be safe" - the gap reads as floating.
- A rectangle of dirt path exactly matching the footprint.
- Symmetrical landscaping (two identical trees flanking the door) outside formal styles.
- Terraforming after the build is finished - it always looks bolted on.
