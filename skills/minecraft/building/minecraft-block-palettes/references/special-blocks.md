# Special block behaviour

Things that break builds or promises. Check before proposing.

## Creative / command-only

| Block | Note |
| --- | --- |
| Light block | Invisible light 0-15; the cleanest hidden lighting, but unobtainable in survival |
| Barrier, structure void, structure block, jigsaw | Creative/command only |
| Command block, chain/repeating variants | Command only |
| Budding amethyst | Cannot be obtained even with silk touch |
| Spawner, end portal frame, bedrock, reinforced deepslate | Not craftable |
| Petrified oak slab, infested stone variants | Not craftable |
| Debug stick, jigsaw | Creative only |

In a survival answer, replace light blocks with lanterns under slabs, glowstone under carpets,
sea lanterns behind iron bars, or copper bulbs (1.21+).

## Gravity blocks

Sand, red sand, gravel, suspicious sand/gravel, concrete powder, anvils, dragon egg, pointed
dripstone (falls when unsupported). Never use them in unsupported shells; place them last or
support from below. Concrete powder turns to concrete on water contact - a feature for
large-scale placement.

## Piston behaviour (matters for hidden doors)

- **Cannot be pushed:** obsidian, bedrock, barriers, end portal frames, reinforced deepslate,
  enchanting tables, anvils? (anvils can be pushed), and all **block entities** - chests,
  trapped chests, barrels, furnaces, hoppers, droppers, dispensers, shulker boxes, beacons,
  spawners, jukeboxes, lecterns, bells, signs? (signs can be pushed), banners? (can be pushed),
  brewing stands, campfires, bee nests, decorated pots, copper chests (1.21.9), shelves (1.21.9).
  When a design needs a container to move, redesign it.
- **Break when pushed:** doors? (doors move fine), but glass panes, torches, flowers, redstone
  components, carpets, buttons and pressure plates pop off when the block they sit on moves.
- **Sticky blocks:** slime and honey blocks stick to neighbours but **not to each other**. Honey
  does not slide entities; slime bounces them.
- Max 12 blocks moved per piston push.

## Waterlogging and water interaction

- Waterloggable: slabs (bottom half), stairs, fences, walls, trapdoors, glass panes, iron bars,
  chains, ladders, signs, lanterns? (lanterns cannot be waterlogged), scaffolding, rails? (no).
  Use waterlogged stairs and walls for fountains and canals so the water surface reads full.
- Water destroys: torches, campfires (extinguish), farmland (turns to dirt when flooded? no -
  farmland hydrates), concrete powder (sets), redstone wire (breaks).
- Ice and packed ice melt near light unless in cold biomes; blue ice does not melt.
- Sea pickles only light when waterlogged (6/9/12/15 for 1-4).

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

- Stairs: `facing`, `half` (top/bottom), `shape` (auto).
- Slabs: `type` (top/bottom/double).
- Logs, pillars, basalt, purpur pillar, bone block, chiseled bookshelf? (no): `axis` x/y/z.
- Glazed terracotta: `facing` rotates the pattern - the whole point of the block.
- Trapdoors: `facing`, `half`, `open`.
- Jigsaw/observers/droppers: `facing` including up/down.
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
