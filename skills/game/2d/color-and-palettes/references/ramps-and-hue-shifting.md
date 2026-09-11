# Ramps and hue shifting

A ramp is the ordered set of colours used to shade one material. Palettes are made of ramps, not of
individual colours.

## Anatomy of a 5-step ramp

| Step | Value | Saturation | Hue |
| --- | --- | --- | --- |
| Highlight | Very light | Low-ish | Shifted toward the light's hue (warm sun: yellow) |
| Light | Light | Medium | Slightly toward the light |
| Base | Mid | Highest of the ramp | The material's own hue |
| Shadow | Dark | Medium-high | Shifted toward the ambient/shadow hue (cool sky: blue-violet) |
| Deep / occlusion | Darkest | Medium | Further toward ambient, sometimes toward the scene's darkest hue |

Three steps (light, base, shadow) is enough for small sprites. Five is the practical maximum before
the ramp starts to look like a gradient.

## How far to shift

Starting points, to taste:

- **Hue**: 15-40 degrees of rotation per step. Small shifts (15) read as natural; large shifts (40+)
  read as stylised and are common in modern pixel art.
- **Value**: keep steps roughly even but slightly compressed at the ends - the gap between base and
  shadow can be larger than between light and highlight.
- **Saturation**: peak in the midtones, fall off at both ends. Fully saturated darks look like
  plastic; fully saturated lights look like neon.

Direction depends on the light story:

| Light | Highlights shift toward | Shadows shift toward |
| --- | --- | --- |
| Warm sun | Yellow / orange | Blue / violet |
| Overcast | Pale blue-white | Warm grey / brown |
| Moonlight | Cyan / pale blue | Deep blue / purple |
| Torch or fire | Orange / yellow-white | Blue-green, cold |
| Neon / sci-fi | The neon's own hue | Complement of the neon |

## Bounce light and reflected colour

The bottom of the shadow side usually catches light bouncing off the ground. One step lighter, hue
shifted toward whatever is under the object (green over grass, orange over sand). One pixel of it
sells depth better than another highlight on the lit side.

## Why identical value patterns still read as different metals

Gold, silver, copper and steel share the same value structure: dark core shadow, mid body, sharp
near-white specular. Only the hue path differs - gold swings orange-to-brown in shadow, silver
swings blue, copper swings red-brown, steel stays almost neutral with a cool shadow. If a metal
looks wrong, the hue path is the problem, not the values.

## Ramp mistakes

| Mistake | Result | Fix |
| --- | --- | --- |
| Darkening only (value slider) | Dull, grey, "dirty" shadows | Rotate hue toward ambient, keep saturation up |
| Adding white for highlights | Chalky, washed-out lights | Shift toward the light's hue before adding value |
| Same hue shift for every material | Everything looks plastic and related | Vary shift direction per material |
| Evenly spaced everything | Mechanical, no focus | Compress steps near the extremes, leave one bigger jump at the terminator |
| Ramps that never meet | Palette balloons to 60 colours | Share endpoints - see `palette-construction.md` |
| Pure black shadow, pure white highlight | Kills the colour story, blows out detail | Use the darkest ambient-tinted colour and a tinted near-white |

## Practical construction

1. Pick the base colour of the material at full intent (the colour someone would name it).
2. Build the shadow step: drop value about 25-35%, rotate hue 20-30 degrees toward the ambient,
   keep or raise saturation slightly.
3. Build the light step: raise value about 20%, rotate 15-25 degrees toward the light's hue, drop
   saturation slightly.
4. Add the deep step only where two forms meet, and the highlight only on glossy materials.
5. Check the ramp in greyscale: the steps must be clearly distinguishable. If two steps have the
   same value, you have a decoration, not a ramp.
