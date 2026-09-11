# Light, value and form

Colour is decoration; value is structure. A sprite with correct values reads in black and white,
and a sprite that does not read in black and white will not be saved by colour.

## Decide the light, then never drift

Write the light direction down for the project: "upper left, 45 degrees" is the most common default
because it reads instantly and matches how most engines draw drop shadows. Every asset - characters,
props, tiles, UI panels - obeys it. Mixed light directions across a tileset produce the
characteristic "asset pack salad" look.

Also decide the light's *character*: hard sunlight (short ramps, sharp terminators, strong cast
shadows) or overcast/ambient (long ramps, soft terminators, almost no cast shadow).

## Value structure

| Sprite size | Values to use |
| --- | --- |
| 8-16 px | 2-3: base, shadow, and one accent |
| 24-32 px | 3-4: light, base, shadow, plus contact shadow or specular |
| 48-64 px | 4-5: highlight, light, base, shadow, deep/contact shadow |
| 96+ px | 5-7, and a real risk of muddiness - keep the extremes far apart |

Block values in before colour. Two rules keep it clean: the lightest light and the darkest dark each
touch a small area, and the base value owns most of the sprite.

## The shadow family

- **Form shadow** - the part of the object turned away from the light. Soft boundary (the terminator).
- **Cast shadow** - thrown by the object onto something else. Harder edge, darker, shaped by the
  receiving surface. Always ground a character with one, even a 3 px ellipse.
- **Contact / occlusion shadow** - the darkest value, only where two surfaces meet: under an arm,
  where a boot meets ground, inside a crack. One pixel of it fakes enormous depth.
- **Bounce light** - one step lighter, hue-shifted toward the ambient colour, on the shadow side's
  bottom edge. This is what makes shadows look transparent rather than painted on.

## Pillow shading and how to kill it

Pillow shading is shading that follows the silhouette inward: dark rim, light centre, everywhere.
It happens when the artist shades "edges" instead of "planes", and it makes everything look like a
cushion.

Fix:

1. Choose a light direction.
2. Imagine the object as a box or cylinder. Mark which planes face the light and which do not.
3. Shade the planes, not the outline. Whole regions change value at once, along the form's turn.
4. Keep the value change *asymmetric*: the light side is bigger or smaller than the shadow side,
   never a symmetrical ring.

## Hard and soft edges

- A tight radius (a sharp fold, a cube corner) gets an abrupt value change - no intermediate step.
- A broad round form (a shoulder, a helmet dome) gets one intermediate step, sometimes dithered.
- Use edge quality as information: sharp = hard material, soft = cloth, skin, cloud.

## Specular highlights

- Small, bright, sparse. 1-3 px on a 32 px sprite.
- Only on glossy materials: metal, glass, wet surfaces, polished leather, eyes.
- One primary specular per object. A highlight on every surface reads as glitter.
- Place it where the surface faces the light most directly, offset toward the viewer.

## Material cheat sheet

| Material | Ramp | Signature detail |
| --- | --- | --- |
| Matte cloth | Long, low contrast | Fold lines 1 px, no specular, ambient occlusion in creases |
| Skin | Short ramp, warm base | Soft terminator, slightly warmer at thin parts (ears, fingers) |
| Metal | Very high contrast, non-linear | Dark core shadow, bright near-white specular, hard edges, reflected light band |
| Glass | Mostly background colour | Dark thin rim, 1-2 hard highlights, brighter where thick |
| Wood | Low contrast | 1 px grain lines following the plank, knots as small clusters |
| Stone | Mid contrast, clustered | Chipped corners, AO in cracks, avoid regular texture |
| Foliage | 2 greens plus dark gap | Clumped blobs, never per-leaf detail below 32 px |
| Water | Few values, horizontal | Banded shapes, bright specular row, transparency by showing what is under |
| Gold vs silver | Same value pattern | Hue separates them: gold shifts to orange in shadow, silver to blue |

## Triage at very small sizes

At 16 px tall you have room for a silhouette, two values and one accent. Decide what the object
*is for* and keep only that: a healer's staff, a knight's helmet crest, a merchant's bag. Cutting
detail is not a compromise at this size - it is the technique.

## Self-check

- Desaturate: do figure and background still separate?
- Is there exactly one light direction?
- Is the darkest dark only in contact areas, and the lightest light only on the lit-most plane?
- Is the base value still the majority of the sprite?
- Does the shadow side have one step of bounce light?
