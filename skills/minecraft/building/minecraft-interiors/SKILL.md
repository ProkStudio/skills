---
name: minecraft-interiors
description: Design and furnish Minecraft interiors for Java 1.21+. Use whenever the user wants to decorate, furnish or fix the inside of a build - living room, bedroom, kitchen, bathroom, library, tavern, inn, shop, throne room, temple, workshop, smithy, storage base, cellar, attic or ship cabin - or says a room feels empty, cramped, cluttered, flat, or like a hotel lobby. Covers room program and circulation, ceiling heights, ceiling structure, floor zoning, three-tier wall treatment, furniture assembled from stairs, trapdoors, barrels, signs, item frames, shelves and pots, focal points, clutter discipline, hidden lighting with real light levels, spawn-proofing, entity budget, and matching interior windows to exterior openings. Always asks 2-3 clarifying questions first.
version: 1.0.0
---

# Minecraft Interiors

An interior is architecture, not decoration sprinkled on a floor. Decide the program, the
section (heights), the surfaces and the light first - furniture is the last 20% of the work.

**Target:** Java Edition 1.21+, creative or survival. Late blocks (chiseled bookshelf 1.20,
decorated pots 1.20, copper grate/bulb and the tuff family 1.21, shelves and copper chests
from the Copper Age drop) are fair game; say so when a block is version-gated.

**Companion skill:** `../minecraft-architecture/SKILL.md` owns the shell - massing, roof,
facade, palette tiers. This skill owns everything inside the walls. When both are in play,
lock the exterior palette first and let the interior derive from it.

## Non-negotiables

1. **Ask 2-3 questions first** (Step 0). Never furnish on a one-line prompt.
2. **Never deliver a furniture list.** "Bed here, chest there" is a failure. Deliver rooms
   with a program, a section, surfaces, light and a focal point.
3. **Ceiling height is a design decision**, not leftover space. 3-block interiors read as a
   doll house for anything but a cellar or an attic. See `references/room-programs.md`.
4. **Three surface tiers per room** - floor, wall field + trim, ceiling - each with 2-3
   blocks of similar value and different texture. Never one block per surface.
5. **One focal point per room.** Everything else supports it. Two focal points = no focal point.
6. **Light must be motivated and mostly hidden.** No floating torch grid. Real light values
   and hiding techniques in `references/lighting.md`.
7. **Keep 50-60% of the floor walkable.** A room the player cannot cross is not furnished, it
   is blocked.
8. **Interior openings must line up with the exterior ones.** If the facade has a 2x3 window
   at y+6, the room behind it has that window at that height.
9. **Answer in the user's language**, with English block ids in brackets when the chat
   language is not English, so the user can find them in the creative inventory.

## Step 0 - Ask 2-3 questions

Pick the 2-3 whose answers most change the result. Offer a default for each so "just do it"
still produces a good interior.

Default trio:

1. **Which rooms and for whom** - solo survival base, family cottage, tavern for a server,
   showcase manor?
2. **Style and era** - offer 2-3 concrete options that match the shell (rustic, medieval,
   Japanese, modern, industrial).
3. **Shell facts** - interior footprint, floor count, ceiling clearance, where the windows and
   doors already are.

Swap in when relevant:

- **Survival or creative** - decides whether entity-heavy and rare-block decor is allowed.
- **Function vs looks** - does storage/farm/redstone have to actually work in this room?
- **Placement method** - hand-placed, commands, or WorldEdit.
- **Entity budget** - server or single player? Item frames, armor stands and boats are entities.

After the answers, restate the brief in 2-3 lines, then design.

## Step 1 - Program and circulation

List every room with its purpose, then lay them out before placing a block. Read
`references/room-programs.md` for sizes and adjacencies.

- Public to private gradient: entry -> hall/living -> kitchen/dining -> stairs -> bedrooms ->
  private storage. Never put a bedroom door directly on the entrance.
- Circulation is a shape, not leftovers: a corridor 2-3 wide, or a central hall that rooms
  open off. Never make a room a corridor to another room unless it is a tavern hall.
- Main door openings 2 wide; interior doors 1 wide only for closets, cellars and privies.
- Stairs need a landing: 2x3 minimum at top and bottom, and a headroom check (3 clear blocks
  above each step, or the player bonks).
- Every room needs a reason for its window position - a window behind a wardrobe is a bug.

## Step 2 - Section and ceiling

Set floor-to-ceiling clearance per room *before* furnishing:

| Room | Interior clearance |
| --- | --- |
| Cellar, attic, ship cabin, crawl storage | 3 |
| Bedroom, kitchen, bathroom, corridor | 4 |
| Living room, shop, library | 4-5 |
| Tavern hall, manor hall, workshop | 5-7 (plus a mezzanine or open truss) |
| Throne room, cathedral, atrium | 8-15, always with vertical accents |

Then give the ceiling a structure - exposed beams, coffers, a vault, a drop ceiling - from
`references/surfaces-and-structure.md`. A flat plank ceiling is the interior equivalent of a
box roof. Dark ceilings recede and make rooms feel taller; light ceilings feel cramped.

## Step 3 - Surfaces

Read `references/surfaces-and-structure.md`. Lock, per room:

- **Floor:** base block + 1-2 texture partners, plus a rug or a material change to zone the
  room (sitting area, walkway, work zone). Sink fixtures half a block by using a slab floor.
- **Walls:** base course or wainscot (1-2 blocks high), field material, trim/cornice at the
  ceiling line. Interior walls 2 blocks thick where possible so each room gets its own finish
  and you can hide lighting and shelving in the thickness.
- **Ceiling:** structure blocks (logs, beams, stripped wood, trapdoors, stairs) + infill.

Keep about two thirds of every surface calm so the detailed third reads.

## Step 4 - Furniture and focal point

Read `references/furniture-catalogue.md`. Order of placement:

1. **Focal point first** - fireplace, four-poster bed, bar, altar, forge, bay window, tree in
   an atrium. Put it on the wall the player sees when entering, or opposite the entry.
2. **Big anchors** - bed, table, counter run, bookcase wall, sofa group.
3. **Mid props** - chairs, shelves, barrels, chests, plants, lamps.
4. **Small clutter** - item frames, pots, candles, books, tools, food - only in groups of 3,
   with mixed heights, and never spread evenly.

Discipline: one prop cluster per 5x5 of floor, never two identical clusters in one build,
and at least one piece of furniture pulled away from the wall into the room.

## Step 5 - Light

Read `references/lighting.md`. Decide a warm/cool/magic light family and stick to it, place
the motivated sources (hearth, lantern, chandelier, window) and hide the rest in ceiling
coffers, under carpets, behind trapdoors, inside slabs and in beam recesses.

Spawn-proofing (Java 1.18+): hostile mobs need block light **0**, so light level 1 anywhere
is enough to stop spawns. That is why hidden low-level light beats torch spam.

## Step 6 - Function check

If the room has a job, verify it works: chest/barrel access not blocked by slabs, furnace
smoke path free, bed within 2 blocks of walkable floor, crafting station reachable, villager
workstation and bed pairing intact, hopper chains unbroken, minecart rails with clearance.
Decoration must never break the machine.

## Step 7 - QA before delivering

- [ ] Every room has a stated purpose, size and clearance; no leftover rooms.
- [ ] Circulation is continuous; 50-60% of each floor is walkable; stairs have landings.
- [ ] Ceiling has structure; ceiling material differs from wall material.
- [ ] 3 surface tiers per room; no surface is a single flat block.
- [ ] One clear focal point per room, placed on the sight line from the door.
- [ ] Light sources hidden or motivated; light family consistent; nothing below level 1.
- [ ] Interior window positions match the exterior facade.
- [ ] Furniture touches floor/wall logically - no floating slabs, no chairs facing a wall.
- [ ] Entity-based decor counted and justified (server builds: prefer block-based decor).
- [ ] Functional blocks still function.

## Delivery format

- **Hand-placed (default)** - per room: purpose, footprint and clearance, surface recipe
  (floor/wall/ceiling blocks), focal point, furniture list with build notes ("chair = oak
  stairs facing the table, spruce wall sign each side"), lighting plan. Then a build order:
  shell fixes -> floors -> wall tiers -> ceiling -> big anchors -> mid props -> lighting ->
  clutter.
- **Commands** - `/fill` for floors, walls and ceilings; `/setblock` for fixtures with the
  needed `facing=` and `half=` states spelled out. Never write connection states for panes,
  bars, fences or walls.
- **WorldEdit** - `//set`, `//replace`, `//stack` for repeating bays and floors; warn that
  bulk placement skips block updates, so reload chunks with F3+A afterwards.

End with 2-3 concrete levers the user can pull ("swap the hearth wall for a bay window",
"raise the hall to 6 and add a mezzanine").

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Feels empty" | Props only along walls, no focal point, no zoning | Step 4 - focal point first, then pull one anchor into the room, zone the floor |
| "Feels cramped/cluttered" | Every wall decorated, floor blocked | Step 4 discipline - 50-60% walkable, two thirds of surfaces calm |
| "Looks like a hotel" | Same surface recipe and prop cluster in every room | One palette accent + one unique prop cluster per room |
| "Ceiling is flat and low" | No section step | Step 2 - set clearance per room, add beams/coffers/vault |
| "Torch spam" | Lighting treated as spawn-proofing only | Step 5 - light level 1 blocks spawns; hide sources |
| "Furniture looks fake" | Single-block "chairs", no support logic | `references/furniture-catalogue.md` - build props from 3-5 blocks with visible support |
| "Windows in the wrong place" | Interior designed independently of the shell | Step 1 - take window positions from the facade first |
| "Lag in my base" | Hundreds of item frames/armor stands | Swap entity decor for blocks; keep entity decor for hero rooms |

## References

| File | Read it when |
| --- | --- |
| `references/room-programs.md` | Laying out rooms, sizes, adjacency, circulation |
| `references/surfaces-and-structure.md` | Floors, wall tiers, ceilings, beams, vaults |
| `references/furniture-catalogue.md` | Building any prop or fixture |
| `references/lighting.md` | Light levels, hidden lighting, spawn-proofing, mood |
| `references/build-type-interiors.md` | Tavern, shop, library, castle hall, workshop, base, ship, temple |
