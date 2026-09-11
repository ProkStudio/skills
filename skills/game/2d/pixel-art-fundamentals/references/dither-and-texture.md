# Dithering, texture and the detail budget

## Dither patterns

Dithering interleaves two colours to fake a third. It is a tool for gradients and material
suggestion under a colour constraint, not a shading style.

| Pattern | Layout | Use |
| --- | --- | --- |
| 50% checker | Alternating pixels | The midpoint between two ramp steps |
| 25% / 75% | Every fourth pixel | Softer transition, longer gradients |
| Graduated | Dense near one colour, sparse near the other | Skies, large metal, long cloth |
| 2x2 Bayer | Ordered 4-level matrix | Retro DOS/Amiga feel, very regular |
| Irregular / hand | Clusters placed by eye | Stone, dirt, rust - texture rather than gradient |

One hard rule: dither only between two *adjacent* colours on the same ramp. Dithering between
distant colours produces visible speckle, not a blend.

## When dithering helps

- Large flat areas that need a gradient: skies, walls, water, big metal plates.
- A hard colour constraint (4-shade Game Boy, 16-colour palette) where you cannot add a step.
- Deliberate period style - late-80s/early-90s PC and Amiga art is dither-forward.
- Material texture: rust, gravel, sand, old stone.

## When dithering hurts

- Sprites below roughly 32 px. There is no room; it reads as noise.
- Anything that moves or scales. Dither "crawls" and shimmers, and a dither pattern that changes
  phase between animation frames flickers - keep the pattern locked to the object, not the frame.
- Areas behind UI text, or icons at 1:1. Dither becomes flat grey when downscaled.
- When you can afford one more palette colour instead. A real intermediate colour beats a dithered
  fake almost every time.

## Texture recipes

Texture is not random pixels; it is a repeatable motif at a chosen density.

| Surface | Recipe |
| --- | --- |
| Rough stone | Clusters of 2-4 darker pixels at irregular spacing, a few lighter chips on top edges, AO in the joints |
| Brick | Offset rows, 1 px darker mortar, vary 2-3 bricks per row by one value, never texture every brick |
| Wood plank | 1 px grain lines parallel to the plank, 1-2 knots as small dark clusters with a lighter halo |
| Thatch / straw | Short diagonal 2 px strokes in two values, denser at the bottom edge |
| Cloth | Fold lines only, following the body's turn; no surface texture below 48 px |
| Fur | Broken silhouette (1-2 px spikes) plus 2-3 value clumps, not individual hairs |
| Metal plate | Flat fills, hard value jumps, rivets as single accent pixels on a regular grid |
| Rust / damage | Irregular clusters that break panel edges, warmer hue, always at edges and low points |
| Sand / gravel | Sparse 1 px dots in two values on a flat base, density gradient toward slopes |
| Grass (top-down) | 2-3 value patches in blobs of 4-9 px, plus a few 1 px blades on silhouette edges |

## Noise vs texture

Noise is pixels that belong to no cluster and follow no motif. The test: squint, or downscale to
50%. Texture survives as a tonal impression; noise turns into flat mush or visible dirt.

If a sprite looks "dirty", count the single-pixel islands. Merge them into clusters, or delete them.

## The detail budget

Spend roughly 60% of your effort on silhouette, 30% on the big value shapes, 10% on detail. Detail
goes where the eye goes: face, hands, weapon, the object's identifying feature. Uniform detail
across a sprite reads as busy and, paradoxically, as less detailed - there is no hierarchy to guide
the eye.

A useful discipline: after finishing, delete the least important 20% of the detail pixels. Most
sprites improve.
