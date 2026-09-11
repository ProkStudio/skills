# Water, rivers and coasts

## Water mechanics that constrain design

- A water source spreads **7 blocks horizontally** on a flat surface before it dries up.
- Overworld lava flows **3 blocks** horizontally; Nether lava flows 7.
- Water flows downhill indefinitely; it will find every unsealed gap, so seal channel floors
  before filling.
- Two source blocks diagonally adjacent create infinite water - fine for lakes, a hazard when
  you want a shallow puddle.
- Waterloggable blocks (stairs, slabs, walls, fences, panes, bars, chains, scaffolding) let you
  shape a full water surface over a sloped floor - the key to natural-looking shallows.
- Ice and packed ice melt near light in warm biomes; blue ice never melts.
- Sponge, or `//replacenear water air`, is the fastest way to fix a flooding mistake.

## Rivers

### Plan

- **Meander, always.** Amplitude 8-20 blocks, wavelength 25-60. No straight run over ~7 blocks.
- Width: stream 2-4, small river 5-9, large river 10-20, with local variation of +/-30%.
- Depth: 1-2 for streams, 3-5 for rivers, deeper on the outside of bends.
- Rivers get wider and shallower downstream, and they never split and rejoin except in deltas.

### Cross-section

Outer bend (fast water) is **undercut and deep**: steep bank, exposed roots, stone and gravel,
occasional small cliff. Inner bend (slow water) is a **deposit**: shallow shelf of sand, gravel
and clay, plants growing into the water, 3-6 blocks wide.

### Bed and banks

- Bed: gravel core with sand patches, clay in slow sections, a few stone and cobble boulders.
- Banks: rooted dirt, coarse dirt, mud, clay, with grass overhanging the edge by 1 block.
- Add 1-2 block wide shallows on the inside of every bend so the water shows a light-dark
  gradient.
- Fallen logs across narrow sections, lily pads and reeds (sugar cane) in slow water.

### Gradient

Drop 1 block per 15-40 blocks of length for a lowland river; steeper for mountain streams, with
rapids (water over exposed cobble), small drops of 1-2 blocks, and plunge pools below each drop.

## Lakes and ponds

- Outline: lobed and irregular, no symmetry, one long axis. Inlet and outlet both visible.
- Depth profile: 1-2 block shelf around most of the shore, dropping to the deepest point
  off-centre, usually near the steepest bank.
- Shore materials rotate around the lake: sand beach on the shallow side, gravel and cobble on
  the wind-exposed side, mud and clay in the reed corner, rock where a slope meets the water.
- Include one peninsula and one island or submerged shoal for interest.
- Plant in zones: lily pads and sugar cane in the shallows, tall grass and ferns at the edge,
  trees set back 2-4 blocks so the bank stays readable.

## Waterfalls

1. The lip: a hard rock layer, 1-3 blocks of overhang, water splitting around 1-2 boulders.
2. The fall: 5-40 blocks. Break tall falls with one ledge that spreads the flow wider.
3. The plunge pool: 3-6 blocks deep, wider than the fall, with a gravel ring and foam
   suggestion (white-ish blocks like calcite or diorite in the pool floor).
4. The spray zone: moss, ferns, azalea, glow lichen, hanging roots, dripstone, 3-8 blocks
   around the base; wet-looking dark blocks on the wall behind the fall.
5. Hide a cave or a passage behind the curtain - the single best payoff of building one.

## Coasts

| Coast type | Build |
| --- | --- |
| Sand beach | 4-10 blocks wide, sand -> gravel -> clay going underwater, dune ridge behind |
| Shingle / rocky | gravel and cobble, boulders in the surf, tide pools (1-block water) |
| Cliff coast | 15-40 vertical, strata visible, sea stacks and arches offshore, scree at the waterline |
| Mangrove / wetland | mud, rooted dirt, mangrove roots, 1-block water islands, braided channels |
| Harbour | natural bay, headland on the windward side, shelving bottom for docks |

Rules:

- The underwater slope continues the land slope. A vertical drop at the shoreline is only
  correct where the cliff also continues below the surface.
- Vary the shoreline every 10-20 blocks: a spit, a notch, a boulder, a stream mouth.
- Kelp, seagrass, coral (warm ocean only), sea pickles and gravel patches keep the seabed from
  reading as a flat sand desert.
- Sea level is a single y-value - check it before you start, and keep every water body that
  connects to the sea at exactly that height.

## Wetlands, springs and irrigation

- Marsh: 1-block water pockets separated by mud and rooted dirt, reeds, dead bushes, patchy
  trees. Height variation of 2 blocks maximum.
- Spring: a single source in a rock hollow, moss ring, small channel leading away, often the
  narrative excuse for a settlement's well.
- Canals and mill races (man-made): straight is correct here, lined with stone or wood, sluice
  gates from trapdoors and iron bars, a 1-block drop where a wheel would sit.
- Farm irrigation: water every 4 blocks covers farmland within 4 blocks in each direction -
  a 9x9 field with a centre source is the classic module.

## Anti-patterns

- Straight rivers, constant width, symmetrical banks.
- Lakes with flat bottoms at uniform depth and a hard grass edge.
- Waterfalls with no plunge pool and no wet zone.
- Water surface at two different heights in the same connected body.
- Sand rings of even width around every water body.
- Floating source blocks on a wall with no catchment above them.
- Filling a valley with water instead of carving a channel for it.
