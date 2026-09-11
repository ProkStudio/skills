# Hidden doors and entrances

Ranked by build cost. Pick the cheapest design that satisfies the brief - a good disguise beats
a big mechanism.

## 1. No-redstone disguises (use these first)

| Design | How | Cost |
| --- | --- | --- |
| Painting door | A 1x2 or 2x2 painting over a 1x2 opening; walk through it | 1 painting |
| Trapdoor floor hatch | Trapdoor in a floor over a ladder shaft; hide under a carpet-edge pattern | 1 trapdoor |
| Rug-and-ladder | Carpet on a trapdoor, trapdoor over the shaft | 2 blocks |
| Bookshelf gap | A wall of bookshelves with one 1x2 recess behind a chiseled bookshelf | free |
| Barrel entrance | A barrel in a cellar floor is walkable-over storage; the shaft is beside it | free |
| Waterfall / vine curtain | A 1x2 opening behind falling water or vines; also hides light | free |

A painting door is invisible, silent, instant, and survives every update. Use redstone only
when the opening has to be **flush in a solid wall** or bigger than 2x2.

## 2. Piston doors - which one to choose

| Door | Opening | Cavity needed (approx.) | Notes |
| --- | --- | --- | --- |
| 1x2 piston door | 1 wide, 2 tall | 5x4x3 | Simplest flush door; one sticky piston per block |
| 2x2 flush piston door | 2x2 | 7x5x4 | The classic; 4 sticky pistons, fully flush both sides |
| 3x3 piston door | 3x3 | 11x7x5 | Needs slime/honey stacks or a staged design; big cavity |
| Hipster door | 2x2 | 6x5x3 | Compact, 4 pistons, opens with a visible shuffle |
| Trapdoor "barn" door | 2x2 to 4x4 | 3 deep | Pistons push trapdoor panels aside; cheapest wide door |
| Portcullis (falling) | 3-7 wide | 4 above the opening | Gravity + pistons; see `movement-and-elevators.md` |
| Drawbridge | 3-9 long | 3 under the deck | Horizontal piston chain or slime-block sled |

Always state the cavity. If the wall is 1 block thick and there is no room behind it, the answer
is a painting door or a thicker wall, not a piston door.

## 3. The 2x2 flush piston door - build discipline

The mechanism: four sticky pistons, two per side, retract the four door blocks sideways into the
wall. Two of them are pulled by pistons acting through a second pair, so timing must be staged
with repeaters or an observer.

What actually decides success:

1. **Door blocks must be pushable and not block entities.** Use plain stone/wood/terracotta -
   not chests, not barrels, not shelves.
2. **Pulse length.** Feed a button through a repeater set to 4 ticks, or use a lever; a bare
   button press often leaves one block behind.
3. **Symmetry.** Build one side, then mirror it exactly. Asymmetric timing is the usual cause of
   a door that closes 3 blocks out of 4.
4. **Both-side triggers.** Two levers into one line via a redstone torch OR gate, or two buttons
   into an OR of dust lines. State it explicitly - a secret door you cannot open from inside is
   a trap.
5. **Test after F3+A.** If the door's state depends on a powered block rather than the lever, it
   desyncs on reload.

Because these designs are timing-sensitive, name the design family and recommend the user follow
a current tutorial for the exact block-by-block layer plan rather than improvising.

## 4. Triggers and how to disguise them

| Trigger | Disguise |
| --- | --- |
| Lever | On the underside of a shelf, behind a painting, on the back of a bookshelf, on a fence post beside the door |
| Button | A stone button as a "keyhole" on a stone door frame, a wooden button in a timber post |
| Chiseled bookshelf (1.20+) | Insert a book into a specific slot; a comparator reads which slot, so only the right book opens the door |
| Lectern | Turn to a specific page; comparator value drives the circuit |
| Trapped chest | Opening a decorative chest unlocks the door |
| Cauldron | Fill level as a code |
| Item frame (comparator-readable) | Rotate the item a set number of clicks |
| Daylight sensor | Door only opens at night, or only in daylight |
| Sculk sensor (1.19+) | Step on a specific block; muffle the rest of the floor with wool |
| Target block | Shoot a hidden target with an arrow from across the room |

Combination locks: chain 2-3 of the above into an AND (dust lines in series through repeaters) so
both conditions must hold.

## 5. Integration rules

- **Hide the seam.** A flush piston door still shows a rectangle if the wall is one flat
  material. Run the palette's patch blending across the door line so the joint disappears.
- Break the wall's rhythm on purpose: put the door where a pilaster, a bookshelf bay, or a
  wainscot panel already divides the surface.
- Keep the interior side lit at level 1+ so mobs do not spawn in the secret room.
- Sound: pistons are audible. For a truly secret entrance in multiplayer, prefer a painting or
  trapdoor design.
- Leave the service void accessible - a hatch in the ceiling or floor of the hidden room.

## 6. Material notes for survival

| Part | Cost |
| --- | --- |
| Sticky piston | 1 piston + 1 slime ball each |
| Observer | 6 cobble + 2 redstone + 1 quartz |
| Repeater | 3 stone + 2 torches + 1 redstone |
| Slime block | 9 slime balls - the real bottleneck; plan a slime farm or swamp trips |
| Honey block | 4 honey bottles |

A 2x2 flush door is roughly 4 sticky pistons, 2-4 repeaters, 1-2 observers and 20-30 redstone -
an evening in survival. A 3x3 is several times that; say so before recommending it.
