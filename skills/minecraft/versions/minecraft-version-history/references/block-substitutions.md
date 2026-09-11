# Block substitutions by target version

When the target version lacks a family, substitute rather than cutting the design. Each row
keeps the *role* the missing block played: value tier, hue or texture grain.

## Greys and dark masonry

| Missing | Added in | Substitute |
| --- | --- | --- |
| Deepslate, polished deepslate, deepslate bricks and tiles | 1.17 | Stone bricks and cracked stone bricks for texture, gray concrete for flat mass, cobblestone and andesite for the rough tier |
| Tuff bricks, polished tuff, chiseled tuff | 1.21 | Polished andesite for the smooth tier, stone bricks for the brick tier, gravel and cobblestone for the rough tier |
| Tuff (plain) | 1.17 | Andesite, or gravel where it is a ground material |
| Calcite | 1.17 | Diorite for the pale tier, bone block or white terracotta for the warmest whites |
| Blackstone family | 1.16 | Polished andesite and stone bricks with black concrete or black terracotta for the deepest shadow |
| Smooth basalt, basalt | 1.16 | Polished andesite, or gray concrete with stone brick detail |

## Copper and metals

| Missing | Added in | Substitute |
| --- | --- | --- |
| Copper, cut copper, oxidation stages | 1.17 | Fresh copper: orange terracotta or acacia planks. Oxidized copper: warped planks, prismarine or cyan terracotta. Both lose the oxidation gradient, so pick one stage and commit |
| Chiseled copper, copper grate, copper door and trapdoor | 1.21 | Iron bars or iron trapdoors for the grate and door, cut copper (1.17+) or orange terracotta for the panel |
| Copper bulb | 1.21 | Redstone lamp; accept that it needs a held signal rather than a pulse toggle |
| Copper chest, shelf, copper lanterns and chains | 1.21.9 | Barrel or trapped chest, item frames on slabs for the shelf, lanterns and chains |

## Warm earth and brick

| Missing | Added in | Substitute |
| --- | --- | --- |
| Mud bricks, packed mud, mud | 1.19 | Bricks for the brick tier, brown and orange terracotta for mass, coarse dirt for raw mud |
| Resin bricks, block of resin | 1.21.4 | Orange terracotta, honey block for the translucent version, red sandstone for the masonry |
| Sulfur and cinnabar sets | 26.2 | Sulfur: yellow terracotta and yellow concrete with glowstone accents. Cinnabar: red concrete, red nether bricks, crimson planks |

## Woods

| Missing | Added in | Substitute |
| --- | --- | --- |
| Crimson and warped | 1.16 | Dark oak and spruce, with purple or cyan terracotta for the saturated notes; you lose fireproofing |
| Mangrove | 1.19 | Dark oak with acacia accents; use rooted dirt substitutes such as coarse dirt for roots |
| Cherry | 1.20 | Birch planks for the pale tier with pink wool or pink terracotta accents |
| Bamboo planks, bamboo mosaic | 1.20 | Jungle planks; for mosaic grain use alternating jungle and birch slabs |
| Pale oak | 1.21.4 | Birch, or stripped birch with white terracotta for the palest version |
| Poplar | 26.3 | Birch or oak with acacia and orange leaves for the autumn read |

## Nature and detail

| Missing | Added in | Substitute |
| --- | --- | --- |
| Moss block, moss carpet, azalea, dripleaf, glow lichen | 1.17 | Grass blocks and grass, oak leaves, vines, lily pads; green carpet for moss carpet |
| Leaf litter, wildflowers, bush, firefly bush, dry grass | 1.21.5 | Grass, ferns, flowers and dead bushes; accept a coarser ground layer |
| Sculk family | 1.19 | Black wool and blue terracotta with dark prismarine, warped wart for the organic mass |
| Froglights | 1.19 | Sea lantern and shroomlight |
| Amethyst, budding amethyst | 1.17 | Purpur block and magenta glass panes |
| Pink petals | 1.20 | Flower rows on grass, or pink carpet for a bed of colour |
| Decorated pots | 1.20 | Flower pots, cauldrons, and item frames for the painted face |

## Shapes and light

| Missing | Added in | Substitute |
| --- | --- | --- |
| Wool stairs and slabs, concrete stairs and slabs | 26.3 | Terracotta for flat mass with quartz, sandstone or deepslate stairs in the nearest value; or accept a blocky profile |
| Hanging signs | 1.20 | Sign on a fence post, or a sign under a chain |
| Chiseled bookshelf | 1.20 | Bookshelf with a trapdoor face, or barrels with item frames |
| Candles | 1.17 | Torches, end rods and redstone lamps behind carpets |
| Tinted glass | 1.17 | Gray stained glass; it will still pass light, so re-check spawn-proofing |
| Waterlogged rails | 1.17 | Route rails above water level or use a dry tunnel |
| Waterlogged lanterns | 1.16.2 | Sea lanterns or glowstone under glass |
| Straw bed, cushions | 26.3 | Hay bale with a white carpet on top; carpet on a slab for a seat |

## Mechanics that need a substitute, not a block

| Assumption | Valid from | Older-version workaround |
| --- | --- | --- |
| Building below `y=0`, top block `y=319` | 1.18 | Floor is `y=0`, ceiling `y=255`; re-datum the whole design |
| Spawn-proofing at light level 1 | 1.18 | Needs light 8 or above on every enclosed surface, which changes the lighting design |
| Sculk sensor wireless triggers | 1.17 | Pressure plates, tripwires and observers |
| Crafter automation | 1.21 | Manual crafting or a villager trade loop |
| Copper bulb state memory | 1.21 | A redstone latch driving a redstone lamp |
