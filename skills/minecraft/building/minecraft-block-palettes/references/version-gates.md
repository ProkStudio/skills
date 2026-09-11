# Version gates (Java Edition)

Annotate a gated block the first time it appears in an answer, and give a fallback. If the
user's version is unknown and the design depends on gated blocks, say so in one line.

This file is the short form. For the full per-version changelog from 1.13 onward, the
substitution tables, pack formats and migration tooling, use
`../../../versions/minecraft-version-history/SKILL.md`.

**Version numbering changed in 2026.** The `1.x` line ended at 1.21.11; releases are now
`year.drop.hotfix` (26.1, 26.2, 26.3), and Bedrock shares the year prefix with its own second
number. There is no 1.22.

## 1.20 "Trails & Tales"

| Added | Notes | Fallback before 1.20 |
| --- | --- | --- |
| Cherry wood set | Pale pink planks, purple-brown log | Birch + pink terracotta accents |
| Bamboo wood set + bamboo mosaic | Mosaic has stairs/slab only | Jungle or oak planks |
| Chiseled bookshelf | Storeable book display | Bookshelves |
| Hanging signs (all woods) | Shop signs, brackets | Regular signs on fences |
| Decorated pots | 4 sherd patterns | Flower pots, cauldrons |
| Pink petals | Ground cover | Flowers, moss carpet |
| Suspicious sand / gravel | Archaeology | Sand, gravel |
| Calibrated sculk sensor, piglin head, sniffer egg, torchflower, pitcher plant | | |

## 1.21 "Tricky Trials"

| Added | Notes | Fallback before 1.21 |
| --- | --- | --- |
| Tuff family | tuff stairs/slab/wall, polished tuff + stairs/slab/wall, tuff bricks + stairs/slab/wall, chiseled tuff, chiseled tuff bricks | Andesite, cobbled deepslate, stone bricks |
| Chiseled copper, copper grate, copper door, copper trapdoor | All oxidation stages + waxed | Cut copper, iron bars, iron door |
| Copper bulb | Light source, redstone-toggled, oxidation dims it | Redstone lamp, sea lantern |
| Crafter | Auto-crafting | Dispenser-based farms |
| Trial spawner, vault, heavy core, ominous items | Structure blocks | - |

## 1.21.4 "The Garden Awakens"

| Added | Notes | Fallback before 1.21.4 |
| --- | --- | --- |
| Pale oak wood set | Pale grey-cream planks, white-grey bark | Birch + white terracotta |
| Pale oak leaves, pale moss block, pale moss carpet, pale hanging moss | Cold dead-forest palette | Azalea leaves, moss, glow lichen |
| Block of resin, resin bricks + stairs/slab/wall, chiseled resin bricks | Warm orange masonry | Terracotta, bricks, honeycomb block |
| Creaking heart, resin clump | | |
| Open / closed eyeblossom | Pale garden flower | Any flower |

## 1.21.5 "Spring to Life"

| Added | Notes | Fallback before 1.21.5 |
| --- | --- | --- |
| Leaf litter | Flat ground cover, great under trees | Pink petals, moss carpet |
| Wildflowers | Multi-flower ground cover | Flowers, grass |
| Bush | Small shrub | Azalea, dead bush |
| Firefly bush | Emits particles, warm ambience | Glow lichen, glow berries |
| Short / tall dry grass | Dry biome cover | Dead bush, grass |
| Cactus flower | Grows on cactus | - |
| Fallen tree generation, falling leaf particles | Worldgen ambience | Hand-built fallen logs |

## 1.21.6 "Chase the Skies"

| Added | Notes |
| --- | --- |
| Dried ghast block | Placeable, hydrates in water; nether decoration |
| Happy ghast + harnesses | Rideable transport, changes how big builds are assembled |

## 1.21.9 "The Copper Age"

| Added | Notes | Fallback before 1.21.9 |
| --- | --- | --- |
| Copper chest | All oxidation stages + waxed; doubles like a normal chest | Barrels, chests |
| Shelf | Displays up to 3 items, wall-mounted | Item frames on trapdoors |
| Copper golem statue | Decorative, oxidizes | Armor stand with gear |
| Copper chain, copper lantern, copper equipment | Warm metal fixtures | Chain, lantern |
| Mannequins | NPC-like display figures | Armor stands |

## 1.21.10 - 1.21.11 (the end of the 1.x line)

| Added | Notes |
| --- | --- |
| 1.21.10 | Hotfix release only - no new blocks |
| 1.21.11 "Mounts of Mayhem" | No new building blocks, but a rendering pass: mipmaps on all blocks, graphics presets, texture and anisotropic filtering, a see-through-leaves toggle. Matters for screenshots, not for palettes |

## 26.1 "Tiny Takeover"

| Added | Notes | Fallback before 26.1 |
| --- | --- | --- |
| Note block trumpet | A note block on block of copper, cut copper or chiseled copper (any oxidation stage) plays a trumpet | Existing note block instruments |
| Golden dandelion | Flower, pottable; stops baby mobs ageing | Dandelion |
| Craftable name tags | - | Fishing and loot |

26.1 also requires the **Java 25 runtime**. A server that ran 1.21.x will not start 26.x
until the runtime is updated.

## 26.2 "Chaos Cubed"

| Added | Notes | Fallback before 26.2 |
| --- | --- | --- |
| Sulfur block set incl. sulfur bricks + stairs/slab/wall | Saturated yellow masonry - the game had no equivalent | Yellow terracotta and yellow concrete with glowstone |
| Cinnabar block set incl. brick variants | Deep red masonry | Red concrete, red nether bricks |
| Sulfur spike | Breakable by thrown tridents; 4 spikes craft 1 sulfur | Pointed dripstone |
| Potent sulfur | Geyser mechanic: magma below makes a geyser, a lava source makes it continuous; emits game events a sculk sensor can read | - |
| Sulfur caves biome, sulfur springs | Worldgen | - |

Also in 26.2: stalagmites no longer deal extra fall damage, and resource pack 88.0 renamed
`quartz_pillar.png` and `purpur_pillar.png` with a `_side` suffix.

## 26.3 "Wilderness Bound"

| Added | Notes | Fallback before 26.3 |
| --- | --- | --- |
| **Wool stairs and slabs, concrete stairs and slabs** | Every colour. Closes the oldest gap in the variant matrix - saturated flat colour can finally be used for roofs and trim | Stained terracotta mass with quartz or deepslate stairs in the nearest value |
| Poplar wood set | Full set incl. shelf, hanging sign and boat; three leaf colours | Birch or oak with orange leaves |
| Straw bed | 3 hay bales; skips night without moving the spawn point | Hay bale with a carpet on top |
| Cushion | Entity, crafted from 3 wool slabs of one colour; sittable | Carpet on a slab |
| Red shrub, shelf mushroom | Ground and trunk cover | Dead bush, brown mushroom |
| Abandoned camp, extra explorer maps, `/compute`, `/posteffect` | Worldgen and commands | - |

Terracotta and glazed terracotta were **not** included - they still have no stairs, slabs or
walls in any version.

## Older blocks worth flagging

| Block | Since | Why it matters |
| --- | --- | --- |
| Deepslate family, tuff (raw), calcite, amethyst, dripstone, moss, azalea, glow lichen, candles, lightning rod, copper (basic) | 1.17 | The backbone of most modern palettes |
| Mud, packed mud, mud bricks, mangrove, sculk family, froglights, reinforced deepslate | 1.19 | Earthy and organic palettes |
| Blackstone, basalt, soul lanterns, warped/crimson, target, chains | 1.16 | Nether-flavoured palettes |
| World height `-64` to `320`, spawn-proofing at light level 0 | 1.18 | Pre-1.18 builds are limited to `y=0`-`255` and need light 8 to be safe |
| The Flattening (namespaced ids, block states, data packs) | 1.13 | Nothing older is command- or schematic-compatible |

## Answer template

> Base: tuff bricks + polished tuff (**1.21+**; before that use deepslate bricks + polished
> deepslate), secondary: spruce, accent: oxidized cut copper stairs (1.17+).

One line, no lecture. If the user says which version they play, drop the annotations entirely
and simply build inside that version.
