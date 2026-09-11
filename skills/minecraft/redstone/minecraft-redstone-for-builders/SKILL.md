---
name: minecraft-redstone-for-builders
description: Hide and integrate redstone in Minecraft Java 1.21+ builds - secret piston doors, hidden entrances, bookshelf and painting switches, switched and automatic lighting, daylight-sensor street lamps, elevators, drawbridges, gates, portcullises, item sorters and hidden storage rooms. Use whenever the user wants a mechanism inside a build rather than a technical farm: a door that looks like a wall, a lever that lights a whole hall, a bridge that retracts, a lamp that turns on at dusk, a sorting room behind a shop counter, or when redstone wiring is visible, breaking the facade, or failing after a chunk reload. Covers signal distance and repeater and comparator timing, quasi-connectivity, piston push limits and immovable blocks, container reading, wiring concealment inside walls and floors, survival material costs and a QA pass before delivery.
version: 1.0.0
---

# Minecraft Redstone for Builders

Redstone in a build is a **detailing problem**, not an engineering problem. The circuit only has
to be reliable; the job is making it invisible and making the visible part look intentional.

**Target:** Java Edition 1.21+. Bedrock differs on quasi-connectivity and some piston timings -
say so if the user is on Bedrock instead of silently giving a Java circuit.

**Scope:** mechanisms that serve architecture. Mob farms, rates, chunk loading and large
technical contraptions are out of scope; say so and keep the answer to the build.

**Companions:**

| Skill | Takes over when |
| --- | --- |
| `../../building/minecraft-architecture/SKILL.md` | The shell the mechanism hides inside |
| `../../building/minecraft-interiors/references/lighting.md` | Light levels, fixtures and hidden light placement |
| `../../building/minecraft-block-palettes/references/special-blocks.md` | Which blocks pistons cannot move, what a comparator can read |
| `../../building/minecraft-settlements/SKILL.md` | Street lighting and gates at settlement scale |

## Non-negotiables

1. **Ask 2-3 questions first**: survival or creative, Java or Bedrock, and what the mechanism
   must look like when idle (invisible, or visibly mechanical).
2. **Reserve the space before wiring.** Decide the service void - a 2-3 block cavity under the
   floor, inside a thick wall, or in a basement - at massing time. Retrofitting wiring into a
   finished build is why redstone "ruins" builds.
3. **Nothing visible unless it is styled.** Dust, repeaters and observers live behind the wall.
   Levers, buttons, trapdoors, lamps, iron bars and copper grates (1.21+) are the only parts the
   player should see, and they must fit the palette.
4. **Never promise a mechanism without stating its footprint.** A 2x2 flush piston door needs a
   cavity of roughly 7x5x4 around the opening; if the build cannot spare it, choose another door.
5. **Test the reload.** Announce the F3+A check: observers, pistons and some doors misbehave
   after a chunk reload if they depend on a powered state rather than a stored state.
6. **Prefer the simplest circuit that works.** A lever and a redstone lamp beat a clever
   contraption in a build that must survive a year of play.
7. **Answer in the user's language**, with English block ids in brackets.

## Step 0 - Ask 2-3 questions

1. **Survival or creative?** Survival means slime/honey and piston counts cost real time, and
   observers and pistons need iron and redstone budgets.
2. **Java or Bedrock?** Quasi-connectivity, piston timings and some door designs differ.
3. **Idle appearance** - fully hidden (wall, bookshelf, floor), or visible machinery (industrial
   and sci-fi styles often want the mechanism on show)?

Swap in: who triggers it (owner only, any player, automatic), whether it must be silent, whether
it must work with a single button press, and how much space exists behind the wall.

## Step 1 - Choose the mechanism

| Need | Go to |
| --- | --- |
| A wall, floor or bookshelf that opens | `references/hidden-doors.md` |
| Lighting on a switch, sensor or schedule | `references/lighting-control.md` |
| Elevators, lifts, bridges, gates, portcullises | `references/movement-and-elevators.md` |
| Sorting, hidden storage, shop mechanics | `references/storage-and-sorters.md` |
| Why a circuit does not fire | `references/signal-basics.md` |

## Step 2 - Place the service void

- **Floor void:** 2 blocks under the finished floor is the most useful cavity in any build; it
  carries dust, repeaters and hopper lines anywhere.
- **Thick walls:** make feature walls 3 blocks thick (outer face, void, inner face) wherever a
  mechanism is planned; the void also reads as masonry depth from outside.
- **Basement / crawlspace:** best for sorters and anything noisy; connect with a ladder shaft
  behind a trapdoor.
- **Ceiling void:** 1-2 blocks above a coffered ceiling hides lamp wiring and observers.
- Keep a maintenance access: a trapdoor, a removable slab, or a hatch behind a painting. A
  sealed circuit you cannot reach is a rebuild waiting to happen.

## Step 3 - Wire it

Read `references/signal-basics.md` for the rules. The three that break builds most often:

- Dust carries **15 blocks**, then needs a repeater. Long facades need a repeater chain in the
  void, and each repeater adds 0.1-0.4 s.
- Dust powers the block it sits on plus adjacent blocks; a powered block passes power **into**
  mechanisms touching it. This is how a lamp inside a wall lights from wiring behind it.
- Pistons, dispensers and droppers in Java are **quasi-connected**: power in the block above
  activates them. Free trick above the mechanism, mystery bug when you did not intend it.

## Step 4 - Style the interface

- Levers on a wall look best on a 1-block contrasting panel, at 1-2 blocks height, beside a
  door frame - or hidden on the back of a bookshelf wall.
- Buttons fit stone builds as "keyholes"; use a stone button on stone, wooden on timber.
- Pressure plates in doorways are for public buildings and shops; never for a secret room.
- Lamps: redstone lamps read as fixtures only when framed - recess them 1 block behind iron
  bars, a trapdoor, or a copper grate (1.21+). Copper bulbs (1.21+) are the best-looking
  switched light and hold their state after the pulse.
- Levers, note blocks and target blocks can all be dressed as part of the furniture.

## Step 5 - QA before delivering

- [ ] Footprint of the mechanism stated, with the cavity dimensions.
- [ ] Nothing of the circuit visible from any player-accessible angle, including from below and
      through windows.
- [ ] Works twice in a row from every trigger, and from both sides if it is a door.
- [ ] Survives a chunk reload (F3+A) and a relog.
- [ ] No block entity in a piston's path (chests, barrels, furnaces, hoppers, shelves and copper
      chests cannot be pushed).
- [ ] Piston push limit of 12 blocks respected.
- [ ] Slime/honey stacks checked: slime and honey do **not** stick to each other; that is either
      the trick or the failure.
- [ ] Light level after the mechanism runs still spawn-proofs the room (level 1+ everywhere).
- [ ] Material list given for survival, including redstone, iron and slime counts.
- [ ] Maintenance access exists.

## Delivery format

1. One-line description of what the player sees and what happens.
2. Footprint: the cavity needed, in x/y/z.
3. Build order as numbered layers (bottom layer first), with block names and orientation. Layer
   diagrams beat prose for redstone - describe row by row.
4. Trigger and timing notes (pulse length, repeater settings).
5. Material list.
6. Failure checklist: the 2-3 things that most commonly go wrong with that specific design.

For complex contraptions, prefer a **known design family** (2x2 flush piston door, 3x3 piston
door, hipster door) and describe it precisely, rather than inventing a circuit that has not been
tested. Say plainly when a design should be checked against a video tutorial.

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Redstone ruins my build" | No service void reserved | Step 2 - plan the cavity at massing time |
| Circuit dies partway | Dust exceeded 15 blocks | Repeater every 15 blocks |
| Door opens once, then jams | Pulse too short, or sticky piston pulled the wrong block | Lengthen the pulse with a repeater at 4; check slime/honey adjacency |
| Piston refuses to move a block | Block entity or immovable block in the path | `../../building/minecraft-block-palettes/references/special-blocks.md` |
| Mechanism fires when nothing touched it | Quasi-connectivity from a block above | Move the wiring, or isolate with a solid unpowered block |
| Works, then breaks after relog | State stored in a powered block or observer chain | Use a lever/copper bulb for stateful designs; test F3+A |
| Lamp visible as a bright square | Lamp placed flush in the surface | Recess 1 block behind bars, trapdoor, or grate |
| Torches/levers everywhere | Interface not styled | Step 4 - panel, frame, keyhole |
| Villagers or mobs trigger plates | Pressure plates on public floors | Use buttons or levers, or raise the plate on a slab step |
| Sorter overflows and jams | No overflow protection | `references/storage-and-sorters.md` |

## References

| File | Read it when |
| --- | --- |
| `references/signal-basics.md` | Any wiring question, timing, debugging |
| `references/hidden-doors.md` | Secret doors, piston doors, hidden entrances |
| `references/lighting-control.md` | Switched, automatic, or scheduled lighting |
| `references/movement-and-elevators.md` | Elevators, lifts, bridges, gates, portcullises |
| `references/storage-and-sorters.md` | Sorting, hidden storage, shop and display mechanics |
