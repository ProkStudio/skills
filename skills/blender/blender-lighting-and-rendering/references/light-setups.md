# Light setups

## Light types

| Type | Behaviour | Use |
| --- | --- | --- |
| Point | Omnidirectional from a sphere of given radius | Bulbs, candles, small practicals |
| Sun | Parallel rays; only angle matters, not position | Daylight; Angle controls shadow softness (0.526 degrees is real sun) |
| Spot | Cone with blend and size | Lamps, stage light, controlled pools of light |
| Area | A rectangle, square, disc or ellipse | Softboxes, windows, screens, bounce cards - the workhorse |
| World / HDRI | Environment light from all directions | Base ambient, realistic reflections |
| Emissive mesh | Any geometry acting as a light | Neon, screens, complex shapes (heavier to sample) |

## Softness

Shadow softness depends on the light's **apparent size** from the subject:

- Double the light's size, or halve its distance, and shadows get softer.
- A 1 m area light at 1 m is soft; the same light at 10 m is nearly hard.
- The Sun lamp's Angle parameter is the sun's angular diameter: 0.526 degrees for a real sun, larger
  for hazy skies.
- Hard shadows read as harsh, dramatic, sunny, artificial; soft shadows read as gentle, overcast,
  flattering.

Intensity falls off with the inverse square of distance for point-like sources, so moving a light
closer makes it both softer and much brighter - compensate with power.

## Three-point lighting and its variants

| Light | Purpose | Typical placement |
| --- | --- | --- |
| Key | Main shaping light | 30-45 degrees off camera axis, 15-45 degrees above eye level |
| Fill | Controls shadow density | Opposite side, lower intensity, larger and softer |
| Rim / back | Separates subject from background | Behind and above, often cooler or warmer than the key |

Ratios (key to fill, measured in exposure stops or relative power):

| Ratio | Mood |
| --- | --- |
| 1:1 | Flat, commercial, clinical |
| 2:1 | Gentle, friendly |
| 4:1 | Standard dramatic portrait |
| 8:1 | Moody, noir |
| Key only | Harsh, isolated, threatening |

Useful additions: a practical (a visible in-scene light), a background light, a bounce card (an area
light or actual white plane), and a kicker (low side rim).

## Colour temperature

| Source | Kelvin |
| --- | --- |
| Candle flame | 1800-1900 K |
| Tungsten bulb | 2700-3200 K |
| Warm LED | 3000 K |
| Neutral LED / fluorescent | 4000-4500 K |
| Midday sun | 5200-5800 K |
| Overcast sky | 6500-7500 K |
| Blue sky / shade | 8000-12000 K |
| Computer screen | ~6500 K |

Use the Blackbody node to get physically correct colours from a temperature. Warm/cool contrast is
the cheapest way to make lighting interesting: warm key plus cool fill, or the reverse.

## HDRI workflow

1. Load an HDRI into the World shader via Environment Texture.
2. Rotate it with a Mapping node to place the sun and bright shapes where you want highlights.
3. Control strength in the background shader, not by scaling the render exposure.
4. To hide the HDRI but keep its lighting: use Film > Transparent, or a Light Path node to show a
   different colour to camera rays only.
5. Add a real Sun lamp when you need crisp shadows; many HDRIs are too low-resolution in the sun
   region for sharp shadow edges.
6. HDRIs alone rarely finish an image - they provide ambience and reflections, and you still shape
   with lamps.

For procedural skies, the Sky Texture node (Nishita model) gives physically based sun position,
turbidity, dust and altitude controls, and pairs naturally with a Sun lamp aligned to the same
direction.

## Interiors

- Interiors are light-transport problems: most illumination is indirect.
- Put an area light just outside each window, sized to the window, pointing in. This is the single
  most effective interior trick.
- Increase diffuse bounces (6-12) so light reaches deep into the room.
- Bright walls and ceilings do the work; dark interiors need far more samples.
- Add practicals (lamps, screens, fires) for local warmth and interest.
- Expect noise in corners; denoising and a slightly larger light source help more than samples.
- In Cycles, portals are no longer needed as a separate feature; the light tree and MIS handle
  window lighting well when you use area lights at the openings.

## Exteriors

- Sun plus sky, then adjust the sun's angle for time of day: low sun (5-20 degrees elevation) gives
  long shadows and warm light; high sun is harsh and unflattering.
- Golden hour is warm sun (3000-4000 K) plus cool blue sky fill - a strong built-in colour contrast.
- Overcast is a huge soft source: a very large area light or a uniform grey sky, minimal directional
  shadow.
- Atmosphere sells depth: a mist pass, a thin volumetric, or fog in the compositor.

## Product lighting

- Start with a large soft key at 45 degrees, plus a big fill card opposite.
- Add a top or rim light to define the top edge; add gradient reflections with long thin area lights
  (strip lights) to describe curvature on glossy surfaces.
- Control what reflects: for glossy products, you are lighting the reflections, not the surface.
- Use a neutral view transform (or Khronos PBR Neutral) when the product's real colour matters.
- Keep the background separate: a gradient backdrop plus a light aimed only at it.

## Character lighting

- Define the face with the key: short-side lighting slims, broad-side widens, Rembrandt (small
  triangle under the eye) is the classic portrait.
- Keep light out of the eye sockets' shadow - eyes need a catchlight.
- Add a rim to separate hair from the background; hair without a rim reads as a silhouette blob.
- Skin needs enough exposure to show subsurface warmth, and soft light to avoid harsh specular.
- For stylised characters, fewer and cleaner lights read better than complex naturalistic setups.

## Common mistakes

| Mistake | Result | Fix |
| --- | --- | --- |
| Light directly at the camera axis | Flat, shadowless | Move 30-45 degrees off axis |
| All lights the same colour | Lifeless | Introduce warm/cool contrast |
| Tiny lights far away | Hard shadows and heavy noise | Enlarge or move closer |
| No rim or separation | Subject merges with background | Add a back light or darken the background |
| Boosting strength instead of exposure | Clipped highlights | Set exposure globally, keep plausible light values |
| Unmotivated lights | Uncanny look | Tie each light to a visible or implied source |
| Lighting to the viewport, not the render | Surprises at render time | Judge in rendered view with the final transform |

## Lighting checklist

1. The image's subject is the brightest, most contrasted area.
2. Key placed off-axis; ratio chosen deliberately.
3. Every light has a plausible motivation.
4. Warm/cool contrast present unless deliberately monochrome.
5. Exposure verified with False Color.
6. Shadows read at the intended hardness.
7. Subject separated from the background.
8. Checked at final resolution, with the final view transform.
