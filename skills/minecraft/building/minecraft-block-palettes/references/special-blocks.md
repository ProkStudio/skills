# Special block behaviour

Things that break builds or promises. Check before proposing.

## Creative / command-only

| Block | Note |
| --- | --- |
| Light block | Invisible light 0-15; the cleanest hidden lighting, but unobtainable in survival |
| Barrier, structure void, structure block, jigsaw block | Creative/command only |
| Command block, chain and repeating variants | Command only |
| Budding amethyst | Cannot be obtained even with Silk Touch |
| Monster spawner, end portal frame, bedrock, reinforced deepslate | Not obtainable in survival |
| Petrified oak slab | Not obtainable in survival |
| Debug stick | Creative only (item, not a block) |

In a survival answer, replace light blocks with lanterns under slabs, glowstone under carpets,
sea lanterns behind iron bars, or copper bulbs (1.21+).

## Gravity blocks

Sand, red sand, gravel, suspicious sand/gravel, concrete powder, anvils, dragon egg, pointed
dripstone (falls when unsupported). Never use them in unsupported shells; place them last or
support from below. Concrete powder turns to concrete on water contact - a feature for
large-scale placement.

## Piston behaviour (matters for hidden doors)

- **Immovable - the piston will not extend at all:** obsidian, crying obsidian, respawn
  anchors, bedrock, reinforced deepslate, barriers, light blocks, end portal frames, monster
  spawners, trial spawners (1.21+), vaults (1.21+), beacons, enchanting tables, ender chests,
  jukeboxes, lodestones, grindstones, command and structure blocks, creaking hearts (1.21.4+),
  sculk sensors, calibrated sculk sensors, sculk catalysts and sculk shriekers.
- **Cannot be pushed because they hold block entities** (Java only - Bedrock does move them):
  chests, trapped chests, copper chests (1.21.9+), barrels, furnaces, blast furnaces, smokers,
  hoppers, droppers, dispensers, crafters (1.21+), brewing stands, lecterns, chiseled
  bookshelves (1.20+), shelves (1.21.9+), conduits, beehives, bee nests and daylight detectors.
  When a design needs a container to move, redesign it.
- **Movable exceptions worth remembering:** anvils and shulker boxes can be pushed, and so can
  doors, trapdoors, fence gates, glass panes, walls and fences.
- **Break when pushed** (they drop as items): signs, hanging signs, banners, campfires and soul
  campfires. So does anything that needs a support block - torches, levers, buttons, pressure
  plates, rails, carpets, flowers and redstone dust pop off when the block they sit on moves.
- **Sticky blocks:** slime and honey blocks stick to their neighbours but **not to each other**.
  Honey does not slide entities standing on it; slime bounces them.
- Max 12 blocks moved per piston push.

## Waterlogging and water interaction

- **Waterloggable:** stairs, bottom slabs, fences, walls, iron bars, glass panes, trapdoors,
  ladders, signs and hanging signs, chests and trapped chests, scaffolding, chains (1.16+),
  lanterns and soul lanterns (1.16.2+), candles and amethyst clusters (1.17+), rails (1.17+),
  pointed dripstone, sculk sensors, and campfires (which go out but stay as a block). Use
  waterlogged stairs and walls in fountains and canals so the surface stays full instead of
  stepping down.
- **Water removes:** torches, redstone dust and other blocks that need dry support; it sets
  concrete powder into concrete and extinguishes fire and unwaterlogged campfires.
- Farmland is hydrated by water within 4 blocks. It reverts to dirt when mobs trample it or a
  falling block lands on it, not from being near water.
- Ice and packed ice melt in light unless they sit in a cold biome; blue ice never melts.
- Sea pickles only light when waterlogged (6 / 9 / 12 / 15 for 1-4 pickles).

## Light and spawning

- Since 1.18 hostile mobs need **block light 0**, so light level 1 on every walkable surface is
  enough to spawn-proof an area.
- Light passes through trapdoors, slabs (top-placed), carpets, glass, leaves - the basis of
  hidden lighting. See `../../minecraft-interiors/references/lighting.md` for the full table.
- Light-emitting blocks that surprise people: crying obsidian 10, enchanting table 7, redstone
  torch 7, sculk catalyst 6, amethyst cluster 5, magma 3, brewing stand 1, nether portal 11.
- Copper bulbs (1.21) dim as they oxidize: 15 / 12 / 8 / 4.

## Performance and entity cost

- Item frames, armor stands, mannequins (1.21.9), boats and paintings are **entities**, not
  blocks. Dozens per building tank server tick times in settlements - prefer block-based
  detail in public areas, and keep entity decoration for interiors the player actually enters.
- Shelves (1.21.9) display items without spawning an item-frame entity - prefer them when the
  version allows.
- Redstone that runs constantly (clocks, observers on flowing water) costs more than any
  decoration; keep decorative contraptions gated behind a lever.

## Blocks with orientation to double-check in commands

- Stairs: `facing`, `half` (top/bottom), `shape` (computed automatically).
- Slabs: `type` (top/bottom/double).
- Logs, stripped logs, wood, pillar quartz, basalt, purpur pillar, bone block, hay bales,
  muddy mangrove roots, deepslate (the plain rotatable one): `axis` x/y/z.
- Chiseled bookshelf (1.20+): `facing` plus one occupancy state per slot - place and fill it by
  hand rather than by command.
- Glazed terracotta: `facing` rotates the pattern - the whole point of the block.
- Trapdoors: `facing`, `half`, `open`.
- Observers, droppers, dispensers, jigsaws: `facing`, including up and down.
- **Never** write connection states (`north=`, `east=`, `up=`) for fences, walls, panes, bars
  or chains - the game computes them; see
  `../../minecraft-architecture/references/block-connection-rules.md`.

## Leaves, plants, decay

- Player-placed leaves are persistent and never decay; generated leaves decay when the log is
  removed.
- Plants need their support block: flowers/grass need dirt-family, cactus needs sand, nether
  plants need soul soil/netherrack, sea pickles need water, pale moss carpet (1.21.4) spreads
  on pale moss.
- Moss blocks + bone meal spread and convert nearby stone/dirt - useful for organic
  terraforming, dangerous near a finished build.
