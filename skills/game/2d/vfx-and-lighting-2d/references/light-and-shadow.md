# Lighting and shadow in 2D

## Decide these three things first

1. **Light direction** - one global direction for the whole game, usually top or top-left. Every
   sprite and tile must obey it. Mirroring a sprite flips the highlight to the wrong side; redraw
   or accept the inconsistency deliberately.
2. **Ambient colour** - the colour of everything not directly lit. This single choice defines the
   mood of an area more than any asset.
3. **Lighting model** - baked into the art, or computed by the engine? Mixing both is the most
   common source of "muddy" 2D lighting.

## Baked (hand-painted) vs engine lighting

| Approach | Pros | Cons |
| --- | --- | --- |
| Baked into sprites and tiles | Full artistic control, cheap, always on-palette, classic pixel-art look | Static; no dynamic lights; a torch cannot really light the room |
| Engine 2D lights (light nodes / URP 2D lights) | Dynamic, reactive, cheap mood changes | Fights baked shading, easily muddies pixel art, needs sprite lighting authored flat |
| Normal maps on sprites | Proper dynamic shading in 2D | Expensive to author per sprite; looks "plastic" if the normals are rough |
| Hybrid: baked mid-tone art + additive light overlays | Practical and common | Requires discipline about what the baked art assumes |

Practical rule: if you want dynamic lights, author the art at a neutral mid-light level with soft
baked form shading only, and let the engine add coloured light and darkness on top.

## Shadows

- **Contact shadow** - a small dark ellipse or a few dark pixels under every character and prop.
  This is the single highest-value shading addition in 2D: without it, everything floats.
- **Form shadow** - the shaded side of an object, baked into the sprite.
- **Cast shadow** - the object's shape projected onto the ground. Expensive to author; usually
  simplified to a skewed silhouette or omitted.
- Shadows are not black. Shift them toward the ambient hue (cool blue for daylight, warm brown for
  firelight) and keep a little saturation
  (`../../color-and-palettes/references/ramps-and-hue-shifting.md`).
- Shadow size follows height: a jumping character's contact shadow should shrink and stay on the
  ground. This tiny detail reads as physics.

## Emissive objects

- Anything that emits light - torches, lamps, crystals, screens, lava, eyes - uses the reserved
  bright palette slots and nothing else does.
- Add a soft halo: 2-3 rings of decreasing brightness, dithered if pixel-strict.
- Animate the emission subtly: 2-4 frames of flicker at slightly irregular timing. Perfectly regular
  flicker reads as a strobe.
- Emissive light should visibly affect its surroundings, even if only as a hand-painted pool of
  warmer colour on the floor.

## Glow and bloom without ruining pixel art

| Technique | Pixel-strict? | Notes |
| --- | --- | --- |
| Hand-drawn halo rings | Yes | Cheapest and most controllable |
| Dithered gradient halo | Yes | Checkerboard falloff reads as glow on-palette |
| Additive sprite with low alpha | No | Introduces off-palette colours |
| Post-process bloom | No | Must be applied *before* upscaling, or the pixels smear |

If you use post-process effects, apply them at native resolution and upscale afterwards with integer
scaling and point filtering (`../../game-art-pipeline/references/pixel-perfect-rendering.md`).

## Area mood and day-night

- Change the ambient colour and the light colour, not the art. A palette swap of the light layer
  turns day into dusk into night for free.
- Night is not darker daylight: it is lower contrast, cooler ambient, with a few high-contrast
  emissive pockets.
- Keep gameplay-critical contrast intact at every time of day. If the player cannot see platform
  edges at night, the night pass is broken.
- Interiors: pick one dominant light source and let everything else fall into ambient.

## Fog, shafts and weather

- **Fog**: a low-contrast overlay that compresses values with distance. Works best as a parallax
  layer (`../../tilesets-and-environments/references/depth-and-parallax.md`).
- **Light shafts**: straight-edged polygons from a window or above, 15-25% brightness, slow drift.
  Add dust motes for scale.
- **Rain**: 2-3 px streaks at a consistent angle, 2-4 layers at different speeds, plus splash
  effects at contact. Never pure white.
- **Snow**: slow, drifting, sine-wave horizontal motion, 2-3 sizes at different speeds.
- **Wind**: the cheapest weather - sway the foliage tiles and move a few leaf particles.

Weather must not compete with gameplay contrast. Keep it in a narrow value band near the ambient.

## Lighting checklist

1. Is there one consistent light direction across all assets?
2. Does every character and prop have a contact shadow?
3. Are shadows hue-shifted rather than black?
4. Are the brightest palette slots reserved for light only?
5. Does each area have a distinct ambient colour?
6. Is the brightest point in the frame where the player should look?
7. Does gameplay stay readable at the darkest lighting state in the game?
