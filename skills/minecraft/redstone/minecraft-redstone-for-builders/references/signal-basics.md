# Signal rules, timing and debugging

Enough theory to wire a build correctly and to diagnose the usual failures. Java Edition.

## Transmission

- Redstone dust starts at strength **15** at the source and loses 1 per block, so it dies after
  15 blocks. A repeater restores it to 15.
- Dust powers: the block **under** it, and any mechanism (lamp, piston, door, dispenser) directly
  adjacent to it or adjacent to a block it powers.
- A **powered block** (a solid block receiving power) activates mechanisms touching it. This is
  the main tool for hiding wiring: power the wall, and the lamp on the other side lights.
- Dust climbs blocks only on the side of a full block; it cannot climb a slab, stair or glass.
- Dust connects to adjacent dust, repeaters and comparators automatically; cut connections with
  a block between, or by routing around.

## Timing

| Component | Behaviour |
| --- | --- |
| Repeater | Delay 2, 4, 6 or 8 game ticks (0.1 / 0.2 / 0.3 / 0.4 s). Also acts as a diode and as a pulse extender at 4+ |
| Comparator | 2 game tick delay; subtract or compare mode; reads containers |
| Redstone torch | Inverter with a 2 game tick delay; burns out if pulsed faster than ~1 per tick continuously |
| Observer | Emits a short pulse (2 game ticks) when the watched block changes state |
| Stone button | 20 game tick pulse (1 s) |
| Wooden button | 30 game tick pulse (1.5 s) |
| Pressure plate | Powered while stood on, plus a short trailing pulse |
| Lever / daylight sensor | Continuous state, not a pulse |

20 game ticks = 1 second. A "redstone tick" is 2 game ticks.

**Pulse length matters for doors.** A button press is often too short for multi-stage piston
doors; feed the signal through a repeater set to 4 (0.4 s) or use a lever for stateful designs.

## Quasi-connectivity (Java only)

Pistons, dispensers and droppers also check the block **one above** them for power. Consequences:

- You can power a piston from a block above it - useful for hiding wiring in a ceiling.
- A circuit routed above a piston can fire it accidentally. If a mechanism activates for no
  visible reason, look one block up.
- Quasi-connected mechanisms sometimes need a block update to react - the basis of block update
  detectors, and the reason an observer is the reliable modern alternative.

Bedrock has no quasi-connectivity. A Java design that relies on it will simply not work there.

## Reading containers with comparators

A comparator behind a container outputs a signal based on **average slot fullness**, where each
slot counts `items / max stack size`. Unstackable items therefore count as a full slot.

Comparator-readable blocks include: chests, trapped chests, large chests, barrels, copper chests
(1.21.9+), hoppers, droppers, dispensers, furnaces, blast furnaces, smokers, brewing stands,
shulker boxes, chiseled bookshelves (1.20+), shelves (1.21.9+), lecterns, jukeboxes, composters,
cauldrons, cakes, decorated pots (1.20+), item frames, respawn anchors, end portal frames,
bee nests and hives, copper golem statues (1.21.9+).

Useful build applications:

- Chiseled bookshelf: a comparator reads **which slot** was filled last - a 3-state book switch
  for a hidden door.
- Lectern: comparator outputs a value by page number - a dial.
- Cauldron: fill level as a 3-step switch.
- Composter and cake: cheap one-shot triggers for puzzles.

## Detection components

| Component | Detects | Build use |
| --- | --- | --- |
| Lever | Manual state | The default for anything that must stay on |
| Button | Manual pulse | Doors, hidden switches, keyholes |
| Pressure plate | Entities standing on it | Public doors, shop entries; avoid in secret rooms |
| Tripwire hook + string | Entities crossing a line | Traps, gates, invisible thresholds across 2-40 blocks |
| Daylight detector | Sky light 0-15; right-click to invert | Street lamps, automatic interior lighting |
| Observer | Block state change in front of it | Reliable triggers, replaces old BUD tricks |
| Target block | Projectile hit, strength by accuracy | Archery-triggered gates, puzzles |
| Sculk sensor (1.19+) | Vibrations within ~8 blocks | Ambience, alarms; wool muffles vibrations |
| Calibrated sculk sensor (1.20+) | One vibration frequency only | Filtered triggers |
| Lightning rod | Lightning strike | Storm-triggered effects |
| Trapped chest | Being opened | Traps, shop tells |

## Piston rules that constrain design

- A piston pushes at most **12 blocks**.
- Block entities cannot be pushed: chests, trapped chests, barrels, furnaces, hoppers, droppers,
  dispensers, shulker boxes, beacons, jukeboxes, lecterns, bells, brewing stands, campfires,
  decorated pots, bee nests, copper chests and shelves (1.21.9+).
- Obsidian, bedrock, reinforced deepslate, barriers and end portal frames are immovable.
- Slime and honey blocks drag adjacent blocks, but **do not stick to each other**. Use that
  boundary deliberately in flying machines and doors.
- Sticky pistons pull one block back; a normal piston leaves it.
- Blocks that pop off when their support moves: torches, levers, buttons, pressure plates,
  carpets, flowers, redstone dust, rails, signs on the face being moved.

## Debugging checklist

1. Follow the dust and count blocks - over 15 without a repeater is the most common fault.
2. Look one block above every piston, dispenser and dropper for stray power.
3. Check pulse length: replace the button with a lever to see whether timing is the issue.
4. Check for a block entity or immovable block in a piston's path.
5. Reload chunks (F3+A) and relog - state-dependent designs fail here.
6. Check for accidental dust connections where two lines pass within 1 block.
7. In multiplayer, check that no one stands in the door's path; entities block piston movement
   only for some designs but will break doors that close on them.
8. Torch burnout: a torch pulsed continuously locks off until the signal stops.
