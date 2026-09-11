# Timeline: 1.17 - 1.19

## 1.17 - Caves & Cliffs Part I (June 2021)

The release that modern building palettes are built on. If a tutorial uses greys, copper or
candles, it needs 1.17 or newer.

**Copper**

- Block of copper, cut copper, cut copper stairs, cut copper slab.
- Four oxidation stages (copper, exposed, weathered, oxidized) and a waxed twin for every
  one of them - wax with honeycomb to freeze the stage.
- Lightning rod.

**Deepslate and greys**

- Deepslate, cobbled deepslate, polished deepslate, deepslate bricks, deepslate tiles,
  chiseled deepslate, cracked variants, with stairs, slabs and walls for the main families.
- Tuff (plain block only in 1.17 - the brick and polished families are 1.21).
- Calcite, smooth basalt, amethyst block, budding amethyst, amethyst cluster and buds.
- Raw iron, raw copper and raw gold blocks.

**Nature and cave dressing**

- Moss block, moss carpet, azalea, flowering azalea, azalea leaves, big and small dripleaf,
  hanging roots, rooted dirt, spore blossom, cave vines with glow berries, glow lichen.
- Dripstone block and pointed dripstone.
- Powder snow.

**Light and glass**

- Candles in all 16 colours plus plain, 1-4 per block, waterloggable, light 3/6/9/12.
- Tinted glass - blocks light but is transparent. There is no tinted glass pane.
- Light block (creative and commands only, `light[level=0..15]`).
- Sculk sensor, the first wireless redstone component.

**Waterlogging additions**

- Rails, candles, pointed dripstone, amethyst clusters and sculk sensors became
  waterloggable in 1.17. Before this, rails and water do not mix.

## 1.18 - Caves & Cliffs Part II (November 2021)

Almost no new blocks, but the two changes that break old advice most often.

- **World height is now `-64` to `320`.** The top placeable block is `y=319` and the bottom
  is `y=-64`. Existing worlds were extended automatically: rows 257-320 filled with air,
  and the new space below `y=0` depends on how the world was migrated.
- **New light engine.** Hostile mobs now require block light level **0** to spawn, so a
  single light source at level 1 spawn-proofs an area. Every pre-1.18 tutorial that says
  "keep it above light 7" is over-lighting the build.
- Terrain generation was rewritten: biomes are decoupled from surface shape, aquifers and
  noise caves appear, mountains are taller and flatter-topped. Terraforming advice from
  earlier versions still works, but reference screenshots will not match.

## 1.19 - The Wild Update (June 2022)

**Mangrove and mud**

- Mangrove log, wood, stripped variants, planks and the full plank set, plus mangrove roots
  and muddy mangrove roots, mangrove propagule, mangrove leaves.
- Mud, packed mud, mud bricks with stairs, slab and wall - the cheapest warm earthy
  masonry in the game and a good terracotta substitute at range.

**The deep dark**

- Sculk, sculk vein, sculk catalyst, sculk shrieker, reinforced deepslate (unobtainable in
  survival, immovable by pistons).
- Ochre, verdant and pearlescent froglight - light level 15 in three muted colours.
- Ancient city structure, deep dark biome.
- Frogspawn.

**Minor releases**

- 1.19.3 and 1.19.4 are mostly technical; 1.19.4 shipped the 1.20 feature set behind
  experimental flags, so screenshots from that period can show blocks that are not in the
  release.

## Mechanics state at the end of 1.19

- Height `-64` to `320`, spawn-proofing target light 1, rails and lanterns waterloggable.
- `pack_format` for data packs: 7 (1.17), 8 (1.18-1.18.1), 9 (1.18.2), 10 (1.19-1.19.3),
  12 (1.19.4).
- Tuff exists but has no variants. Copper has no doors, grates or bulbs yet.
