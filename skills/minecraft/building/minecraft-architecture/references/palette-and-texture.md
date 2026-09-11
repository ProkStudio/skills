# Palette and texture

A palette is a hierarchy, not a list. Same-style builds look identical when only the block
set changes, so palette work happens *after* massing - it is the skin, not the skeleton.

## Contents

- Tier system
- Value before hue
- Texture blending
- Gradients and weathering
- Glass and light
- Testing
- Anti-patterns

## Tier system

| Tier | Share | Role | Example (medieval) |
| --- | --- | --- | --- |
| Base | ~60% | dominant wall mass | stone bricks + cracked + mossy |
| Secondary | ~30% | structure, second material | spruce logs, stripped spruce |
| Accent | ~10% | roof, trim, highlights | deepslate tile stairs |
| Trim / neutral | thin lines | edges, sills, cornices | andesite, polished deepslate |
| Glass / light | points | openings, lanterns | glass panes, lanterns, candles |

One wood family and one stone family per build. Two wood families read as an accident unless
the difference is deliberate and structural (dark frame, light infill).

## Value before hue

Pick the light/mid/dark distribution first, then worry about colour.

- Aim for three clearly different values. If a build looks flat in a screenshot converted to
  grayscale, the values are too close.
- Roofs are usually the darkest element, base courses next, walls lightest. Inverting this
  (dark base, light roof) works but must be deliberate.
- Highly saturated blocks (red/lime/purple concrete, red nether brick, prismarine) are accent
  only - under 10%, ideally under 5%.
- Avoid pure `white_concrete` + `black_concrete` as a base pair outside modern styles; use
  calcite, diorite, bone block, smooth quartz for warm whites and deepslate, blackstone,
  polished basalt for softer blacks.

## Texture blending

Within each tier pick 2-3 blocks with similar value and different surface noise, then mix:

- Patches of 2-5 blocks, organic edges. **Not** a checkerboard, **not** uniform random noise.
- Weight the mix: ~70% primary, ~20% secondary, ~10% tertiary in that tier.
- Concentrate the rough/damaged variants where damage happens - ground level, corners,
  under the eaves, around openings, next to water.
- Good stone blend sets: stone bricks / cracked stone bricks / mossy stone bricks / andesite;
  deepslate bricks / deepslate tiles / cracked variants / polished deepslate; tuff bricks /
  polished tuff / chiseled tuff (1.21+); cobblestone / mossy cobblestone / gravel / stone.
- Good wood blend sets: spruce planks / stripped spruce log / spruce trapdoors (as panelling)
  / barrels; oak planks / stripped oak / bamboo mosaic.
- Smooth styles (modern, Japanese interiors) blend *less*: 1-2 blocks per tier, crisp joints.
  Blending is a rustic tool, not a universal one.

## Gradients and weathering

- Vertical gradient: darker, rougher, mossier at the bottom 1-3 blocks; cleaner and lighter
  higher up. Reverse (sun-bleached top) works for deserts and copper.
- Moss, vines, glow lichen, hanging roots and azalea only where water or shade would put
  them - north faces, undersides, bases, cracks. Never sprinkled evenly.
- Copper oxidation states (copper block -> exposed -> weathered -> oxidized) make a ready-made
  gradient; waxing pins the level.
- For ruins, remove blocks as well as changing them - missing corners and partial walls read
  better than cracked textures alone.

## Glass and light

- **Panes** for divided windows (framed by full blocks - see `block-connection-rules.md`).
- **Full glass blocks** for clean modern surfaces and large curtain walls; tinted glass blocks
  light while staying visually glassy.
- Coloured glass in accents only - brown/gray/light blue are the safest; light gray tinted
  panes read as a modern window well.
- Hide light sources: lanterns under slabs, sea lanterns behind trapdoors or iron bars,
  glowstone under carpets, candles on tables, copper bulbs (1.21+) as industrial fixtures,
  shroomlight in warm rustic ceilings, froglight for accents.
- Hostile mobs need light level 0 to spawn, so a single light source per 8-block radius is
  usually enough - prioritise how the light *looks*, then patch dark corners.
- Warm (lantern, campfire, shroomlight) vs cool (soul lantern, sea lantern, amethyst) light
  is a style decision - do not mix without reason.

## Testing

1. Look at the build from 40+ blocks away, and from directly below/above.
2. Check at night and in rain, and in shade (palettes that only work in direct sun are fragile).
3. Screenshot and desaturate mentally - is the value hierarchy still readable?
4. Count materials per element. More than 3-4 on one wall is almost always too many.

## Anti-patterns

- One material per surface ("stone brick box with oak roof").
- Checkerboard or pure-random block noise.
- Every wall the same mix, so the whole build averages into one grey tone.
- Accent colours used at 30%+ (the build becomes the accent).
- Mixing 3 wood types and 3 stone types "for texture".
- Full-brightness glowstone walls; visible torch spam.
- Copying a palette without adapting the value hierarchy to the biome light.
