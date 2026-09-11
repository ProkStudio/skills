# Timeline: the 2026 drops

Snapshot taken September 2026. 26.1 and 26.2 are released; 26.3 was in pre-release at the
time of writing, so treat its list as near-final but verify at release.

## The numbering change (announced December 2025)

- Versions are numbered by **year**: everything released in 2026 starts with `26`.
- Java uses `year.drop.hotfix`: `26.1`, `26.1.1`, `26.1.2`, `26.2`, `26.3`.
- Bedrock shares the `26` prefix but keeps its own second number, so the same drop has two
  numbers. Snapshots are `26w05a`-style or `26.3-snapshot-9`.
- **The `1.x` line ended at 1.21.11.** There is no 1.22.

| Drop | Java | Bedrock | Released |
| --- | --- | --- | --- |
| Tiny Takeover | 26.1 (hotfixes 26.1.1, 26.1.2) | 26.10 | 24 March 2026 |
| Chaos Cubed | 26.2 | 26.30 (experiment in 26.20) | 16 June 2026 |
| Wilderness Bound | 26.3 | 26.50 (experiment in 26.40) | September 2026 |

## 26.1 - Tiny Takeover (24 March 2026)

A small drop for builders, but two hard technical changes.

- **Requires the Java 25 runtime.** A server or launcher profile that ran 1.21.x will refuse
  to start 26.x until the runtime is updated. This is the most common 2026 upgrade failure.
- First release shipped fully unobfuscated, and the first to use the new version format.
- **Note block trumpet**: a note block placed on a block of copper, cut copper or chiseled
  copper plays a trumpet, with separate sounds for the exposed, weathered and oxidized
  stages. Useful for note-block builds that were previously limited to the classic set.
- Golden dandelion - a new flower, crafted from a dandelion and gold nuggets, that stops
  baby mobs from ageing. Usable as decoration like any flower, and pottable.
- Every baby mob that lacked a unique model got one, plus new baby and adult animal sound
  variants. Purely visual, but it changes how farm and petting-zoo builds read.
- Name tags became craftable.
- The drop also carried stonecutter and tripwire tweaks; check the changelog before relying
  on either in a contraption.

## 26.2 - Chaos Cubed (16 June 2026)

The first genuinely new building palette of 2026, in yellow and red.

**Blocks**

- **Sulfur** block set and **cinnabar** block set, including brick variants with stairs,
  slabs and walls. Sulfur is a strong saturated yellow, cinnabar a deep red - the game had
  no comparable masonry in either hue before this.
- **Sulfur spike** - a spike block, breakable by thrown tridents; four spikes craft into one
  sulfur.
- **Potent sulfur** - the mechanic block of the drop. With a magma block beneath it, it forms
  a geyser; with a **source** lava block beneath, the geyser erupts continuously. Eruptions
  emit game events at start and end, so a sculk sensor can read them, and the plume boosts
  entities and pushes noxious gas through non-collidable blocks. Naturally generated sulfur
  springs erupt roughly every 45 seconds.

**World generation**

- **Sulfur caves** biome: sulfur pools, cinnabar, sulfur spikes, glow lichen and shallow
  water. **Sulfur springs** generate on the surface as a visual marker for the cave below,
  in sizes from small to extra large, surrounded by cinnabar, granite and tuff.

**Mob with building consequences**

- **Sulfur cube** - a physics-driven mob that absorbs a block and takes on its behaviour:
  honeycomb makes it sticky, wood bouncy, TNT explosive, magma hot, ice slippery. With a
  block inside it is immune to explosions. Treat it as a hazard around finished builds,
  especially the TNT archetype, which can be primed by redstone, fire or nearby explosions.

**Other**

- Music disc "Bounce" (comparator output 8) and five new ambient tracks.
- **Stalagmites no longer deal extra fall damage**, which changes cave and trap design.
- Experimental Vulkan renderer plus a "Graphics API" video option; friends list; a
  `flat_all_dimensions` world preset.
- Resource pack 88.0 renamed `block/quartz_pillar.png` and `block/purpur_pillar.png` with a
  `_side` suffix - a small but breaking change for texture packs. Data pack format 106.1.

## 26.3 - Wilderness Bound (September 2026)

The most builder-focused drop in years. Two additions close gaps the game has had since
release.

**Wool and concrete finally get shapes**

- **Wool stairs and wool slabs**, and **concrete stairs and concrete slabs**, in every
  colour. Any guidance that says "wool and concrete have no stairs or slabs" is correct only
  up to 1.21.11 and wrong from 26.3. Terracotta and glazed terracotta were **not** included.
- Roofs, mouldings and trim can now be done in saturated flat colour, which previously
  forced a compromise on wool and concrete builds.

**Poplar**

- Dappled forest biome with poplar trees in three leaf colours (autumnal range).
- Full poplar wood set: log, stripped log, wood, stripped wood, planks, stairs, slab, sign,
  hanging sign, button, pressure plate, door, fence, fence gate, trapdoor, **shelf**, plus
  poplar boat and chest boat.

**Camp dressing**

- **Straw bed** - crafted from three hay bales, lets a player skip the night without
  resetting the spawn point. A furniture block with a real use.
- **Cushion** - an entity rather than a block, crafted from three wool slabs of one colour
  and found in abandoned camps. Sittable, so it is the first proper vanilla seat.
- Red shrub, shelf mushroom.
- Abandoned camp structure, plus explorer maps for ancient city, abandoned camp, desert
  pyramid, mineshaft and warm ocean ruins.
- New commands `/compute` and `/posteffect`.

## What this means for a project in 2026

| If the project floor is | Then |
| --- | --- |
| 1.21.x | Wool and concrete are flat blocks only; no sulfur or cinnabar masonry; no poplar |
| 26.1 | Runtime must be Java 25; note block trumpet available |
| 26.2 | Sulfur and cinnabar masonry available; do not rely on stalagmite fall damage |
| 26.3 | Wool and concrete stairs and slabs, poplar, cushions and straw beds available |

For anything released after September 2026, check `minecraft.wiki` rather than this file.
