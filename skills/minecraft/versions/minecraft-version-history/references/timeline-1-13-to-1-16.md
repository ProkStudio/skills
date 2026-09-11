# Timeline: 1.13 - 1.16

Builder-relevant changes only. Mobs, combat, enchanting and loot are omitted unless they
affect building or block behaviour.

## 1.13 - Update Aquatic (July 2018)

The most disruptive release in the game's history for anything technical.

**The Flattening.** Numeric block IDs and data values were removed. Every block became a
namespaced ID plus block states, so `minecraft:stone 1` became `minecraft:granite` and
`wool:14` became `red_wool`. Consequences:

- Every pre-1.13 command, command block, map, data pack and schematic needs conversion.
- Commands were rewritten: `/setblock` and `/fill` take block states, `/blockdata` became
  `/data`, and `/execute` gained its modern chained form.
- Data packs were introduced (`pack_format` 4).

**Waterlogging** was introduced as a block state: stairs, bottom slabs, fences, walls, iron
bars, glass panes, chests and (later in the cycle) trapdoors, ladders and signs can hold
water without breaking. This is the foundation of every underwater and fountain build.

**New building blocks**

- Stripped logs and stripped wood for all six overworld woods, plus the six-sided `wood`
  (full bark) blocks.
- Smooth stone, smooth sandstone, smooth red sandstone and smooth quartz became distinct
  blocks with their own stairs and slabs; cut sandstone and cut red sandstone appeared.
- Prismarine bricks and dark prismarine gained stairs and slabs; plain prismarine gained
  stairs, slab and wall.
- Blue ice, sea pickle, dried kelp block, conduit, turtle egg.
- All five coral blocks, coral fans and coral, plus their dead variants. Live coral dies
  out of water - use the dead variants for dry builds on purpose.

## 1.14 - Village & Pillage (April 2019)

The single most useful release for palette work, because it filled in the variant matrix.

**Variants added**

- Walls for most stone families: brick, sandstone, red sandstone, stone brick, mossy stone
  brick, mossy cobblestone, prismarine, nether brick, red nether brick, andesite, diorite,
  granite and end stone brick.
- Stairs and slabs for stone, smooth quartz, smooth sandstone, smooth red sandstone,
  polished granite, polished diorite, polished andesite, mossy variants, end stone bricks
  and cut sandstone slabs.
- Signs became per-wood blocks.

**New blocks**

- **Stonecutter** - turns one block into its stair, slab and wall variants at a 1:1 rate,
  which is why 1.14+ palettes can be variant-heavy without a resource problem.
- Barrel, blast furnace, smoker, lectern, composter, grindstone, loom, cartography table,
  fletching table, smithing table, bell.
- Campfire, lantern, scaffolding, bamboo, sweet berry bush.
- Jigsaw block (creative and structure work).

Campfires and scaffolding became waterloggable in this release; a waterlogged campfire
goes out.

## 1.15 - Buzzy Bees (December 2019)

- Honey block, honeycomb block, bee nest, beehive.
- Honey blocks stick to neighbours like slime but **do not stick to slime blocks**, which is
  what makes two-way flying machines and most modern piston doors possible. Entities on a
  honey block slide instead of bouncing.

## 1.16 - Nether Update (June 2020)

A second palette explosion, this time in dark and saturated tones.

**Wood sets**

- Crimson and warped: stems, stripped stems, hyphae, planks, stairs, slabs, fences, gates,
  doors, trapdoors, buttons, pressure plates, signs. They are fireproof and read as
  "not-wood", which makes them useful for alien, infernal and painted-timber looks.
- Nether wart block, warped wart block, shroomlight, nether sprouts, twisting and weeping
  vines, crimson and warped fungus and roots.

**Stone families**

- Blackstone, polished blackstone, polished blackstone bricks, cracked and chiseled
  variants, gilded blackstone, with stairs, slabs and walls where expected.
- Basalt, polished basalt, smooth basalt (smooth basalt arrived with 1.17 amethyst geodes in
  practice but the block itself is 1.16 in the nether update cycle - verify if it matters).
- Cracked nether bricks, chiseled nether bricks, quartz bricks.
- Soul soil, soul torch, soul lantern, soul campfire, soul fire - the cyan flame set.

**Utility and accent**

- Chain (waterloggable from 1.16), lodestone, respawn anchor, target block, crying obsidian,
  ancient debris, netherite block, nether gold ore.
- **1.16.2**: lanterns and soul lanterns became waterloggable.

## Mechanics state at the end of 1.16

- World height is `0` to `256`; the top placeable block is `y=255`.
- Hostile mobs spawn at block light level **7 or below**, so light level 8 is the
  spawn-proofing target. This changes in 1.18.
- Rails and candles cannot be waterlogged yet (1.17).
- `pack_format` for data packs: 4 (1.13-1.14.4), 5 (1.15-1.16.1), 6 (1.16.2-1.16.5).
