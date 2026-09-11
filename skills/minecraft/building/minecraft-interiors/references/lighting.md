# Interior lighting

## Mechanics you must respect (Java)

- Hostile mobs need block light level **0** to spawn (1.18+). Light level **1** anywhere in a
  room is enough to prevent spawns. You never need to flood a room with torches.
- Light passes through non-opaque blocks: glass, panes, trapdoors, slabs, stairs, carpets,
  leaves, fences, bars. This is what makes hidden lighting possible.
- Light spreads 1 level per block, so a level-15 source lights usefully for ~7-8 blocks before
  it feels dim.
- `light` blocks (`/setblock ~ ~ ~ light[level=15]`) are invisible and creative/command only -
  perfect for showcase builds, unavailable in vanilla survival.

## Light levels of common sources

| Level | Sources |
| --- | --- |
| 15 | Glowstone, sea lantern, shroomlight, froglights (ochre/verdant/pearlescent), jack o'lantern, lit redstone lamp, campfire, lava, beacon, conduit, unoxidized copper bulb (1.21), 4 waterlogged sea pickles |
| 14 | Torch, end rod, cave vines with glow berries |
| 12 | 4 candles, exposed copper bulb, 3 waterlogged sea pickles |
| 10 | Soul torch, soul lantern, soul campfire, crying obsidian |
| 8-9 | Weathered copper bulb (8), 3 candles (9), 2 waterlogged sea pickles (9) |
| 7 | Redstone torch, enchanting table, ender chest, glow lichen |
| 6 | Sculk catalyst, 2 candles, 1 waterlogged sea pickle |
| 3-5 | Amethyst cluster (5), oxidized copper bulb (4), magma block (3), 1 candle (3) |
| 1-2 | Brewing stand, amethyst buds, dragon egg |

Practical consequence: candles, amethyst, copper bulbs and sculk are *mood* lights - they need
a level-15 partner nearby (hidden) to light a room properly.

## Hidden lighting techniques

1. **Ceiling coffer:** recess a 2x2 panel, put glowstone/froglight in it, cover with trapdoors
   or a slab one block lower. Light leaks, source invisible.
2. **Under carpet:** glowstone or sea lantern in the floor with a carpet on top - full light,
   zero visible source. Best for corridors and shops.
3. **Behind trapdoors:** a wall niche 1 deep with a light block inside and a trapdoor over it;
   open trapdoors read as shutters.
4. **In the beam:** replace one block of a ceiling beam with a light source and frame it with
   stairs/slabs so only a glow line shows.
5. **Behind the sconce:** put the real source inside the wall behind a lantern or an end rod,
   so the visible fixture reads warm without a bright hotspot.
6. **Cove lighting (modern):** drop ceiling with a 1-block gap at the perimeter, light sources
   in the gap, slabs hiding them.
7. **Under stair treads and furniture:** a light block under an open staircase or a counter run
   lights the floor with no visible source.
8. **Water and wall accents:** sea pickles in an aquarium, glow lichen on stone, amethyst in a
   cellar - motivated, low-level, atmospheric.

## Motivated visible fixtures

- **Rustic/medieval:** lanterns on chains, hanging lanterns from a trapdoor bracket, campfire
  hearth, candles on tables and mantels, torch in an iron-bar sconce.
- **Manor/classical:** chandelier (fence post + chains + lanterns + candles on a ring of
  trapdoors), wall sconces at 4-5 block spacing, candelabra with 3-4 candles.
- **Modern:** end rods recessed in the ceiling, redstone lamps behind glass, cove strips,
  hanging copper bulbs on chains (1.21).
- **Japanese:** paper-lamp look with white glass or white concrete + lantern inside, shoji
  panels of glass framed with stripped wood, floor lanterns.
- **Industrial/steampunk:** copper bulbs on chains, redstone lamps in iron-bar cages,
  lightning rods, lanterns behind copper grates (1.21).
- **Magic/arcane:** end rods, amethyst clusters, sculk, soul lanterns for a cold cast,
  glow berries dripping from the ceiling.

## Lighting a room properly

1. Pick one colour family and stay in it: warm (torch, lantern, campfire, ochre froglight,
   copper bulb), cool (sea lantern, soul lantern, verdant froglight, glow lichen), or arcane
   (end rod, amethyst, sculk, soul fire).
2. Place the motivated hero fixture first - hearth, chandelier, bar lanterns.
3. Add hidden fill so no walkable block is below level 1 and the whole room reads evenly.
4. Add accents last: candles, amethyst, glow item frames on the focal wall.
5. Contrast check: leave one corner darker than the rest. Even light is dead light.

## Switchable and dynamic light

- Redstone lamp + lever/button for rooms the player wants dark.
- Daylight detector (inverted) + redstone lamps for street or window lighting that turns on
  at dusk.
- Observer/piston-hidden light for cinematic reveals; copper bulbs hold state and toggle with
  a single pulse (1.21) - the cleanest vanilla latch for lighting.

## Mistakes

| Mistake | Fix |
| --- | --- |
| Torch grid on every wall | Hidden fill + 1-2 motivated fixtures |
| Mixing warm and cool randomly | One family per space; cool only for windows/magic accents |
| Glowstone ceiling patch left visible | Recess it and cover with trapdoors/slabs |
| Candles as the only light | Pair with a hidden level-15 source |
| Dark unreachable corners in survival | Spawn-check: every walkable block at level 1+ |
| Chandelier floating with no chain | Hang it: chain to the beam, or fence post + trapdoors |
