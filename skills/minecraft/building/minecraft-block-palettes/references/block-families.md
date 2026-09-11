# Block families and the variant matrix

Everything here is Java Edition. Version gates are marked; unmarked blocks exist in 1.20+.

## Variant matrix - stone families

S = stairs, L = slab, W = wall, C = chiseled/decorative sibling.

| Family | S | L | W | Notes |
| --- | --- | --- | --- | --- |
| Stone | yes | yes | no | Stone wall does not exist |
| Cobblestone | yes | yes | yes | Mossy cobblestone has all three too |
| Smooth stone | **no** | yes | no | Slab only - the classic trap |
| Stone bricks | yes | yes | yes | + mossy, cracked, chiseled (chiseled has no variants) |
| Granite / diorite / andesite | yes | yes | yes | |
| Polished granite / diorite / andesite | yes | yes | **no** | No polished walls |
| Tuff (1.21) | yes | yes | yes | |
| Polished tuff (1.21) | yes | yes | yes | |
| Tuff bricks (1.21) | yes | yes | yes | + chiseled tuff, chiseled tuff bricks |
| Cobbled deepslate | yes | yes | yes | |
| Polished deepslate | yes | yes | yes | |
| Deepslate bricks | yes | yes | yes | + cracked |
| Deepslate tiles | yes | yes | yes | + cracked |
| Deepslate (raw block) | no | no | no | Chiseled deepslate is a single block |
| Blackstone | yes | yes | yes | Gilded blackstone has no variants |
| Polished blackstone | yes | yes | yes | + chiseled |
| Polished blackstone bricks | yes | yes | yes | + cracked |
| Basalt / polished basalt / smooth basalt | no | no | no | Pillar-textured, no variants |
| Bricks | yes | yes | yes | |
| Mud bricks (1.19) | yes | yes | yes | Packed mud has no variants |
| Resin bricks (1.21.4) | yes | yes | yes | + chiseled resin bricks |
| Sandstone | yes | yes | yes | + chiseled (no variants) |
| Smooth sandstone | yes | yes | no | |
| Cut sandstone | **no** | yes | no | Slab only |
| Red sandstone family | same as sandstone | | | Same traps apply |
| Nether bricks | yes | yes | yes | + chiseled, cracked |
| Red nether bricks | yes | yes | yes | |
| Quartz block | yes | yes | no | |
| Smooth quartz | yes | yes | no | |
| Quartz bricks / chiseled quartz / quartz pillar | no | no | no | Single blocks |
| Purpur block | yes | yes | no | Purpur pillar has no variants |
| End stone bricks | yes | yes | yes | End stone itself has none |
| Prismarine | yes | yes | yes | |
| Prismarine bricks | yes | yes | no | |
| Dark prismarine | yes | yes | no | |
| Cut copper (all oxidation stages) | yes | yes | no | Waxed versions of everything |
| Calcite / dripstone / amethyst / obsidian | no | no | no | Single blocks |

**No stairs, slabs or walls at all:** terracotta (plain and all 16 colours), glazed terracotta,
concrete, concrete powder, wool, all metal blocks (iron, gold, copper block, netherite),
lapis, bone block, calcite, magma, clay, packed mud, dripstone block, sculk blocks.

## Wood families

Every wood family has: log, wood, stripped log, stripped wood, planks, slab, stairs, fence,
fence gate, door, trapdoor, button, pressure plate, sign, hanging sign (1.20+), boat.

**There is no wooden wall** - use fences for open railings and trapdoors/panes for infill.

| Family | Colour read | Version |
| --- | --- | --- |
| Oak | mid warm brown | vanilla |
| Spruce | dark cool brown | vanilla |
| Birch | pale cream | vanilla |
| Jungle | red-brown | vanilla |
| Acacia | orange | vanilla |
| Dark oak | very dark brown | vanilla |
| Mangrove | deep red-brown | 1.19+ |
| Cherry | pale pink, purple log | 1.20+ |
| Pale oak | pale grey-cream | 1.21.4+ |
| Crimson (stem/hyphae) | maroon | nether |
| Warped (stem/hyphae) | teal | nether |

**Bamboo (1.20+)** is its own case: bamboo planks (full wood set), **bamboo mosaic** with
stairs and slab only (no fence/door/trapdoor), block of bamboo, stripped block of bamboo,
bamboo raft.

## Copper (the most useful gradient in the game)

- Oxidation stages: copper block -> exposed -> weathered -> oxidized. Applies to: block of
  copper, cut copper (+ stairs, slab), chiseled copper (1.21), copper grate (1.21), copper bulb
  (1.21), copper door (1.21), copper trapdoor (1.21), copper chest (1.21.9), copper chain
  (1.21.9), copper golem statue (1.21.9), copper lantern (1.21.9).
- Every one of those has a **waxed** version that pins the stage (honeycomb to wax, axe to
  scrape back one stage).
- Use copper as a ready-made vertical gradient: oxidized at the top of a roof, weathered and
  exposed lower, unoxidized at the eaves.

## Glass, bars and light

- Glass: glass, glass panes, 16 stained glass + panes, tinted glass (**no pane variant**).
- Iron bars, chains (+ copper chain 1.21.9), lanterns (+ soul, + copper lantern 1.21.9),
  torches (+ soul, + redstone), candles (16 colours, 1-4 per block), end rods, sea lanterns,
  glowstone, shroomlight, froglights (3 colours), glow lichen, glow berries, amethyst clusters,
  redstone lamps, copper bulbs (1.21), respawn anchors, campfires (+ soul).
- Light levels are listed in `../../minecraft-interiors/references/lighting.md`.

## Plants and ground cover

- Classic: grass, tall grass, ferns, large ferns, flowers, dead bush, vines, lily pads, moss
  block, moss carpet, azalea, flowering azalea, big dripleaf, small dripleaf, spore blossom,
  hanging roots, sculk vein.
- 1.20+: pink petals, torchflower, pitcher plant.
- 1.21.4+: pale moss block, pale moss carpet, pale hanging moss, open/closed eyeblossom, resin
  clump.
- 1.21.5+: leaf litter, wildflowers, bush, firefly bush, short dry grass, tall dry grass,
  cactus flower.
- Leaves: all wood families + azalea leaves, flowering azalea leaves, pale oak leaves (1.21.4).
  Player-placed leaves do not decay.

## Functional blocks used as decoration

Barrels, chests (+ copper chest 1.21.9), shelves (1.21.9), lecterns, chiseled bookshelves
(1.20+), bookshelves, cartography/fletching/smithing tables, looms, composters, cauldrons,
bells, grindstones, stonecutters, blast furnaces, smokers, anvils, decorated pots (1.20+),
brewing stands, flower pots, item frames, armor stands, mannequins (1.21.9), hoppers, scaffolding,
lightning rods, target blocks, honey/slime blocks, bee nests, beehives, sculk family.

## Naming discipline

When the user's language is not English, give the Russian (or local) name plus the English id:
"туфовые кирпичи (tuff bricks, 1.21+)". Commands and the creative search bar need the English
id, so never omit it.
