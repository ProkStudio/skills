# Lighting control

Light *design* lives in `../../../building/minecraft-interiors/references/lighting.md`. This file
is only about making light switchable, automatic or animated - and keeping the wiring invisible.

## Switchable light sources

| Source | Light | Behaviour |
| --- | --- | --- |
| Redstone lamp | 15 | Lit while powered; turns off shortly after the signal stops |
| Copper bulb (1.21+) | 15 / 12 / 8 / 4 by oxidation | **Toggles** on a pulse and holds state; comparator can read whether it is lit |
| Redstone torch | 7 | Inverted state, warm and small |
| Dispenser + fire/lava | - | For fireplaces; risky, use decorative fire instead |
| Note blocks / jukebox | - | Sound to accompany a lighting scene |

The copper bulb (1.21+) is the best fixture for builders: one button press changes the state
permanently, so no circuit has to stay powered. Its oxidation stage also lets you dim a room
without any redstone at all.

## Hiding the fixture

- Recess the lamp 1 block into the wall or ceiling and cover with: iron bars, a trapdoor, a
  copper grate (1.21+), tinted glass, or a carpet if it is in the floor.
- Light passes through trapdoors, slabs, carpets, glass and leaves, so the source can sit behind
  or under any of them.
- In coffered ceilings, put the lamp in the coffer recess with a slab lip in front of it.
- Under-stair and under-bench lighting: lamp in the void, carpet or slab over it.
- Never place a redstone lamp flush in a finished surface; the off state is an obvious dark
  block and the on state is a glaring square.

## Automatic exterior lighting (street lamps)

The standard circuit:

1. Daylight detector on the roof or inside a lamp post housing.
2. **Right-click it to invert** so it outputs at night.
3. Feed the signal along the void under the street or through the lamp posts.
4. Repeater every 15 blocks; a lamp post every 8-10 blocks is enough for spawn-proofing.

Hiding the detector: inside a 2x2 post head, under a glass block, under a trapdoor with skylight
access, or on a roof behind a parapet. A detector needs sky access - if the post is under an
arcade, run the signal from a detector elsewhere on the same line.

Variants:

- **Whole-village lighting** from one inverted detector plus a repeater trunk in the road void.
  Add a lever in series so the owner can force the lights on.
- **Interior dusk lighting**: same circuit, wired to copper bulbs (1.21+) in ceiling coffers.
- **Dawn-only** effects: non-inverted detector for garden fountains, market awnings, or a bell.

## Switched interior scenes

- One lever at the door powering a lamp trunk in the floor void, with branches up into wall
  recesses. Put the trunk under the corridor so every room taps off it.
- Multi-room control: one lever per room on a shared trunk, each behind a styled panel.
- "All off" master switch: a redstone torch inverter in the trunk, driven by one lever at the
  entrance.
- Two-way switching (either of two levers toggles): an XOR is overkill for builds - use two
  levers into an OR and accept that both must be flipped, or use copper bulbs with buttons at
  both ends.

## Animated and ambient effects

| Effect | Circuit |
| --- | --- |
| Flickering fireplace | Two lamps, one behind a trapdoor, driven by an observer clock through a repeater chain; keep it slow (0.6-1 s) or it looks like a strobe |
| Pulsing reactor / crystal | Slow clock into a lamp bank; for sci-fi builds, cyan glass over the lamps |
| Beacon-style lighthouse | Lamp bank on a slow sequencer so the lit side rotates |
| Lit path on approach | Pressure plates or tripwire on the path into a lamp trunk; repeater chain gives a chasing effect |
| Sound scene | Note blocks beside the lamp trunk; tune with the block under them |

Rule: any repeating circuit costs server performance and makes noise. Put a lever in series so
the user can turn the animation off, and never run a clock in a settlement with dozens of
buildings.

## Spawn-proofing with light control

- Hostile mobs need block light **0** (1.18+), so light level 1 blocks spawning. A lamp under a
  carpet every 12-16 blocks is enough for interiors and streets.
- Automatic lighting on a daylight cycle leaves the area dark during the day - that is fine
  outdoors (skylight blocks spawns) but **not** indoors or under cover. Keep indoor lights on a
  lever, not a sensor.
- After building any lighting circuit, walk the space at night with F3 open and check the light
  level readout; patch dark corners with hidden sources rather than adding visible fixtures.

## Costs

| Part | Cost |
| --- | --- |
| Redstone lamp | 4 redstone + 1 glowstone |
| Copper bulb (1.21+) | 3 copper blocks + 1 blaze rod + 1 redstone |
| Daylight detector | 6 wooden slabs + 3 glass + 3 quartz |
| Repeater | 3 stone + 2 torches + 1 redstone |

A street of 12 lamps on one inverted detector is roughly 12 lamps, 4-6 repeaters and 60-80
redstone - cheap, and the single best-value redstone in any settlement.
