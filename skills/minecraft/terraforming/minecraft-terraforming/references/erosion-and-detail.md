# Strata, erosion and the detail pass

## Rock strata

Exposed rock is banded. Bands are horizontal-ish, 2-5 blocks thick, and they **bend with the
terrain** rather than staying perfectly level.

Good band sets:

| Depth / zone | Blocks |
| --- | --- |
| Above y0, temperate | stone, andesite, granite, diorite, cobblestone, tuff (1.21+) |
| Below y0 | deepslate, cobbled deepslate, tuff (1.21+), polished-free raw blocks only |
| Badlands / desert | terracotta colours, red sandstone, sandstone, smooth sandstone |
| Volcanic | basalt, smooth basalt, blackstone, magma, gravel |
| Coastal / chalk | calcite, diorite, smooth stone, bone block (thin seams) |
| Karst | calcite, smooth stone, diorite, dripstone block |

Rules:

1. One band per material, 2-5 blocks thick, with a 1-block mixed transition where two bands
   meet (alternate the two blocks in patches).
2. Thin seams (1 block) of a contrasting material every 8-15 blocks of height read as
   sedimentary layering and cost nothing.
3. Bands continue across a valley - both walls show the same sequence at the same heights.
4. Never use polished, brick or tile variants in natural rock. Those are man-made textures.
5. Gravel and coarse dirt belong in the weathered zones: the top 1-2 blocks under the surface,
   ledges, and the scree at the base.

## Surface layer by slope and aspect

| Condition | Surface |
| --- | --- |
| Flat to 1:4, sunny | grass block, tall grass, flowers, wildflowers (1.21.5+) |
| Flat to 1:4, shaded/wet | moss block, moss carpet, podzol, ferns, leaf litter (1.21.5+) |
| 1:3 to 1:1 | grass patches broken by coarse dirt, gravel, stone |
| Above 1:1 | stone/strata bare; only ledge pockets get dirt and plants |
| Ridge crest, wind-exposed | stone, gravel, short dry grass (1.21.5+), no trees |
| Above tree line (~y120 temperate) | stone, gravel, snow, powder snow pockets |
| Valley bottom, damp | rooted dirt, mud, moss, clay, coarse dirt |
| Desert | sand, red sand, sandstone outcrops, gravel in hollows |

Blend two surfaces with patches of 3-8 blocks and ragged edges; a 1-block checker is noise, a
straight seam is a wall.

## Erosion pass

### Scree / talus

Every cliff sheds rock. At the base, a fan of gravel + cobblestone + stone:

- Height ~20-25% of the cliff height, slope 1:2, widest under gullies and notches.
- Mix: 60% gravel, 25% cobblestone, 15% stone, with 3-6 loose boulders sitting on top.
- The fan overlaps the surface layer irregularly - grass creeping back over its lower edge.

### Gullies

Water cuts down the fall line. Every 15-25 blocks of slope width gets a channel:

- 2-4 blocks wide at the top, widening and deepening downhill.
- Cut 2-5 blocks into the slope, floor of gravel and stone.
- They join like tree branches (two merge into one), never cross.
- At the bottom each gully spills into an alluvial fan of gravel and coarse dirt.

### Crest rounding

Ridges are not knife edges unless freshly cut rock. Step each layer back 1-2 blocks at the top
so the crest reads rounded. Plateau rims get the same treatment, plus notches where gullies cut
back into them.

### Overhangs and undercuts

At least one per 30 blocks of cliff. Remove 2-4 blocks from the lower face and let the upper
rock project. Add hanging roots, vines, glow lichen, and dripstone underneath. Undercuts are
where a cliff stops looking like a wall.

### Boulders

3-8 blocks each, irregular, half-buried (a boulder sitting on the surface reads as placed).
Cluster them near their parent cliff and along gully mouths, with moss on the shaded side.

### Weathering by aspect

North-facing and shaded surfaces get moss, moss carpet, pale moss (1.21.4+), ferns, glow
lichen and snow that lingers. Sun-facing surfaces get dry grass, dead bushes, bare rock.
Applying weathering evenly all round removes the effect.

## Noise discipline

- **Never** single scattered blocks of a contrasting material on a slope.
- Patch size 3-8 blocks, edges feathered by 1 block of a mixed zone.
- Weight the mix per patch: about 70% primary, 20% secondary, 10% tertiary.
- Concentrate noise where a physical process would put it - ledges, bases, water lines, gully
  floors, tree roots.
- Leave 50%+ of any large surface calm, or the detail stops reading.

## Smoothing rules

- Hand smoothing: never leave a 1-block step repeated in a straight line. Alternate steps of 1
  and 2, and move the step line sideways every 3-5 blocks.
- Slabs and stairs smooth walkable surfaces (paths, terraces, beaches) but look wrong on cliffs
  - use them below eye level, sparingly.
- Tool smoothing (`//smooth`) flattens strata and deletes detail: smooth **before** strata and
  surface passes, never after.
- After any bulk operation, walk the seam between edited and untouched terrain and break it
  manually for 5-10 blocks.

## Underground detail

- Cave walls need the same strata treatment; add ore-like accents (coal, copper, iron ore) to
  suggest geology.
- Dripstone clusters at the ceiling and floor, water seeps and small pools, sculk near deep
  dark, amethyst geodes as focal points.
- Vary the cross-section constantly: 3-wide passage, 12-wide chamber, 2-wide squeeze. Uniform
  tunnels are the underground equivalent of uniform slope.
