# Elevators, lifts, bridges and gates

## Vertical movement

| Design | Speed / cost | When to use |
| --- | --- | --- |
| Ladder shaft | Slow, free | Always the fallback; hide behind a trapdoor |
| Spiral stair | Slow, big footprint | When the stair itself is architecture |
| Bubble column (soul sand) | Fast up, no redstone | The default elevator in survival |
| Bubble column (magma block) | Fast down | Pair with the soul sand shaft |
| Water drop shaft | Fast down, free | Descent only; 1-block water column |
| Piston lift | Slow, expensive | Visible machinery in industrial/sci-fi builds |
| Minecart + powered rails | Medium | Long horizontal or diagonal runs |

### Bubble elevator (the practical choice)

- Shaft of **water source blocks** all the way up (fill with a bucket, or use kelp to convert a
  column to sources, then break the kelp).
- **Soul sand at the bottom** creates an upward bubble column; **a magma block** creates a
  downward whirlpool. The column appears about 1 second after placing the block.
- Cap the top so the player exits sideways into a landing; a door or trapdoor at the exit stops
  water from spilling into the room.
- Bubble columns refill air, so any shaft height is safe.
- Disguise the shaft as a well, a chimney, a lift car of iron bars and glass, or a stair core.
- One shaft up (soul sand) beside one shaft down (magma) reads as a working lift lobby.

### Piston lift (visible machinery)

Honest, slow, and expensive: a slime-block platform driven by a piston stack, or a
sticky-piston chain that steps the platform 2 blocks at a time. Only worth it when the build
*should* look mechanical (steampunk, dwarven, sci-fi). State plainly that a bubble column is
faster and cheaper, and offer it dressed as a lift car.

## Horizontal movement

- **Powered rails:** 1 powered rail every 8 blocks on flat ground (every 2-3 uphill), fed by a
  redstone torch or a block under each one. Hide the wiring in the ballast under the track.
- **Ice roads:** blue ice + boat is the fastest vanilla travel; frame it as a canal so it fits
  the build.
- **Soul speed paths** on soul sand/soul soil, or just a well-lit 3-wide road - often better for
  a settlement than any contraption.

## Bridges

| Design | Mechanism |
| --- | --- |
| Retracting deck | A row of sticky pistons under the deck pulling the walkway blocks down into the void, one per block; cheapest wide bridge |
| Slime sled drawbridge | A slime-block platform pushed out by a piston chain (respect the 12-block limit) |
| Trapdoor bridge | Trapdoors on the deck line, all powered from one line in the void; opens and closes instantly, ideal for a 1-2 block gap |
| Rising drawbridge | Pistons push a hinged panel (a column of blocks plus slime) upright against the gatehouse |
| Falling drawbridge | Gravity blocks are not reliable here; use the trapdoor or slime designs instead |

Design rules:

- Reserve 3 blocks under the deck for pistons and dust.
- Make the bridge deck a material with no block entities.
- Light the deck edges so mobs cannot spawn on a retracted bridge.
- Stage a long bridge in sections of up to 12 blocks, each with its own piston row, triggered
  along a repeater chain so it extends progressively - visually far better than all at once.

## Gates and portcullises

| Design | Mechanism |
| --- | --- |
| Piston portcullis | Iron bars or fence blocks pushed down from above into the gateway; sticky pistons above the opening, cavity 4+ blocks high |
| Trapdoor gate | A 3-5 wide row of trapdoors in the arch; opens flat against the ceiling |
| Double iron doors | Two iron doors side by side, one lever or two buttons; the least effort for a 2-wide gate |
| Slime-block gate leaves | Two leaves pushed sideways into the wall thickness, like a 2x2 flush door widened |
| Drop bar | A visible timber bar (logs) pulled aside by a piston - good for medieval builds |

For a castle gate, stack the layers the way a real one does: outer portcullis, then the gate
leaves, then a murder-hole corridor between them. Wire the two so the portcullis drops first.

## Other build-serving mechanisms

- **Hidden stairs:** a piston staircase that extends step by step from a wall; wire each piston
  through a repeater chain so the steps appear in sequence.
- **Rotating display:** a minecart on a circular rail under a glass floor, or an armor stand on
  a piston-shuffled platform.
- **Fountains:** dispensers with water buckets are unnecessary - use still water and slabs.
  Reserve redstone for a water-level change (dispenser toggling a source block).
- **Farm gates and animal pens:** fence gates on a shared line from one lever at the barn door.
- **Curtains and shutters:** trapdoors or panes on pistons, one line per facade; excellent for
  making a big facade feel alive.

## Timing and safety

- Test every mechanism with a player standing in it. Pistons push players; bridges retract under
  their feet.
- Any mechanism over a drop needs a fail-safe: a water landing, a ledge, or a lever position
  that leaves the bridge extended by default.
- After a chunk reload, mechanisms that store state in a moving block can desync. Prefer levers
  or copper bulbs (1.21+) for state, and test with F3+A.
