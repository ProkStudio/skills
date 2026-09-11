# Planting and biome blending

## Three-layer planting

Every planted area needs three heights or it reads as a lawn:

| Layer | Blocks |
| --- | --- |
| Canopy | trees (vanilla or custom), large mushrooms, azalea trees |
| Shrub | azalea, flowering azalea, bush (1.21.5+), sweet berry bush, dead bush, small dripleaf, bamboo, cactus |
| Ground | grass, tall grass, ferns, flowers, wildflowers (1.21.5+), leaf litter (1.21.5+), moss carpet, pink petals (1.20+), short/tall dry grass (1.21.5+), vines, glow lichen |

## Density and clustering

- Cluster 3-7 plants of 2-3 species, then leave a gap. Never an even spread, never a lone bush.
- Density gradient: dense in valleys, hollows and shaded slopes; sparse on ridges, crests and
  sun-baked faces; absent on rock above 1:1.
- Keep 30-50% of the ground plain so the planting reads as planting.
- Species count: 2-3 tree species per area maximum, one dominant (70%).
- Edges of woodland are denser and shrubbier than the interior - build the edge, then thin the
  middle.

## Custom trees (the highest-leverage upgrade)

Vanilla saplings look like filler next to good terrain. For any tree near a viewpoint:

- Trunk: 2x2 or 3x3 for large trees, leaning off vertical, with root flare - 3-6 logs spreading
  at the base into the ground, plus rooted dirt and hanging roots.
- Branches: 3-6, alternating sides and heights, each one rising then levelling; thickness drops
  with distance from the trunk (3 -> 2 -> 1).
- Canopy: irregular blobs at different heights, thinner at the edges (leaves on the outer ring
  only, with gaps so light comes through). Never a symmetrical ball.
- Details: stripped logs where a branch broke, vines, glow berries, moss, azalea leaves mixed
  into oak leaves, mushrooms and leaf litter (1.21.5+) at the base.
- Full step-by-step shapes are in
  `../../../building/minecraft-organic-shapes/references/natural-forms.md`.

## Biome transitions

A seam between two biomes must be a **zone**, 10-20 blocks wide:

1. Interleave the two surface blocks in patches of 3-8, shifting the ratio across the zone
   (80/20 -> 50/50 -> 20/80).
2. Mix the plant lists in the same ratio; both biomes' trees appear in the middle third.
3. Use a physical excuse for the change: a ridge, a river, a rock outcrop, a change of slope or
   aspect. Biomes change because the land changes.
4. Do not fight the grass tint - the game colours grass by biome, so a hand-blended zone still
   shows a colour step. Break it with non-grass surfaces (gravel, coarse dirt, stone, sand,
   leaf litter, moss) exactly where the tint changes.

| Transition | Best excuse |
| --- | --- |
| Forest -> plains | Woodland edge thinning over 15 blocks, scattered lone trees |
| Plains -> desert | Dry grass, dead bushes, sand patches growing, gravel blowouts |
| Temperate -> snowy | Rising elevation; snow first in shaded hollows and on north faces |
| Forest -> swamp | Ground drops 2-3 blocks, mud and water pockets appear, trees thin and lean |
| Grass -> badlands | Terracotta outcrops break through the grass, then take over |
| Land -> ocean | Beach, then shelving seabed with kelp and gravel |

## Biome-specific planting kits

| Biome | Kit |
| --- | --- |
| Temperate forest | oak/birch mix, azalea, ferns, leaf litter, moss patches, fallen logs |
| Taiga | spruce (2x2 trunks), podzol, ferns, sweet berry bushes, mossy boulders |
| Jungle | jungle trees with vines, bamboo clumps, cocoa, big dripleaf, moss, glow lichen |
| Savanna | acacia (flat wide canopies), dry grass, tall grass, sparse boulders |
| Desert | cactus clusters, dead bushes, dry grass, sandstone outcrops, one oasis with sugar cane |
| Snowy | spruce with snow-covered leaves, powder snow pockets, bare stone, blue ice patches |
| Swamp | mangrove/oak with vines, mud, lily pads, sugar cane, dead trees, frogs' spawn areas |
| Cherry grove (1.20+) | cherry trees, pink petals, calcite outcrops, moss |
| Pale garden (1.21.4+) | pale oak, pale moss carpet, pale hanging moss, eyeblossoms, grey palette |
| Nether | crimson/warped fungi, weeping and twisting vines, shroomlight, soul soil patches |

## Gardens and parks (designed planting)

- Formal: symmetry is allowed, but detail the symmetry - identical hedges with varied ground
  cover, paired trees with different canopies.
- Hedges: leaves (2-3 high) with a slab or fence core, trimmed flat, gaps for gates.
- Flowerbeds: 3-5 blocks of one colour, bordered by a slab or stair course; pink petals and
  wildflowers for soft edges.
- Lawn: plain grass, mown look, no tall grass; this is one of the few places where evenness is
  correct.
- Paths through planting: 1-2 wide, gravel or dirt path blocks, curving, with plants spilling
  over the edges by 1 block.
- Water features, topiary (leaf spheres from the organic-shapes tables), benches, lanterns on
  posts every 8-10 blocks.

## Anti-patterns

- Even grid of identical vanilla trees.
- One plant species carpeting a whole area.
- Tall grass everywhere including on ridges and rock.
- Flowers scattered as single blocks at uniform density.
- Straight-edged biome seams, especially along chunk borders.
- Forest with no edge zone and no clearings.
- Vines and moss applied to every face instead of shaded ones.
