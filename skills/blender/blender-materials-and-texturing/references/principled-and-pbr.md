# Principled BSDF and PBR values

## The node after the 4.0 reorganisation

Blender 4.0 rebuilt the Principled BSDF into grouped panels. What changed in practice:

- Inputs are organised into panels: Base, Subsurface, Specular, Transmission, Coat, Sheen, Emission,
  plus Thin Film in later 4.x releases.
- The old **Specular** slider is now **IOR Level** inside the Specular panel; the physical **IOR**
  input drives dielectric reflectance directly.
- **Clearcoat** became **Coat** (with its own roughness, IOR and tint).
- **Sheen** gained roughness and tint controls, aimed at fabric.
- **Subsurface** is radius-based with a Random Walk default and a Scale value.
- **Transmission** simplified to a weight, using the main IOR and roughness.

When reading older tutorials: "set Specular to 0.5" means the default dielectric response, which is
now simply IOR 1.45-1.5 with IOR Level at 0.5.

## The three values that matter most

| Input | Meaning | Discipline |
| --- | --- | --- |
| Base Color | Albedo: the colour of diffusely reflected light | No lighting, no shadow, no AO baked in |
| Metallic | Conductor (1.0) vs dielectric (0.0) | Binary in practice; use masks, not middle values |
| Roughness | Microsurface scatter | Never uniform; this is where realism lives |

### Albedo ranges

Real-world dielectric albedo rarely exceeds the extremes. In 8-bit sRGB terms:

| Material | sRGB value (approx) |
| --- | --- |
| Fresh snow | 230-245 |
| White paint | 210-230 |
| Concrete, dry | 130-170 |
| Weathered wood | 90-130 |
| Asphalt, dry | 50-70 |
| Charcoal / soot | 25-40 |
| Vegetation (green leaf) | 60-100 |

Nothing natural is pure 0 or pure 255. Pure white albedo bounces impossible amounts of light and
blows out GI; pure black kills all bounce and reads as a hole.

Metals do not use arbitrary albedo - their base colour **is** their reflectance:

| Metal | Base colour (linear, approx sRGB hex) |
| --- | --- |
| Iron / steel | #C0C0BE - slightly cool grey |
| Aluminium | #D0D2D3 |
| Chrome | #C4C5C5 |
| Silver | #F7F4EB |
| Gold | #FFD86F |
| Copper | #F7BFA5 |
| Brass | #E6C27A |
| Titanium | #C1BAB0 |

### Roughness by material

| Surface | Roughness |
| --- | --- |
| Polished chrome, mirror | 0.0-0.05 |
| Polished car paint (under clearcoat) | 0.1-0.2 |
| Brushed metal | 0.25-0.4 |
| Smooth plastic | 0.2-0.35 |
| Matte paint | 0.5-0.7 |
| Rough concrete, stone | 0.7-0.9 |
| Unfinished wood | 0.6-0.8 |
| Fabric (cotton) | 0.8-0.95 |
| Rubber | 0.6-0.8 |
| Dry skin | 0.4-0.6 with wet areas lower |

Always add variation: a roughness map, a noise mix, or a curvature-driven polish on edges. Even a
0.05 range of variation transforms how a surface reads.

## IOR reference

| Material | IOR |
| --- | --- |
| Air | 1.0 |
| Water | 1.33 |
| Ice | 1.31 |
| Skin | ~1.4 |
| Plastic (generic) | 1.45-1.5 |
| Glass (window) | 1.45-1.52 |
| Quartz | 1.54 |
| Sapphire | 1.77 |
| Diamond | 2.42 |
| Default dielectric | 1.45-1.5 |

Metals are conductors; their IOR is complex and handled by the Metallic model, so do not tune IOR for
metal.

## Subsurface scattering

- Use for skin, wax, marble, milk, leaves, thin plastic, jade.
- **Radius is in metres** and must match the model's real scale. Typical human skin radii sit around
  0.01 / 0.004 / 0.002 m for red/green/blue - red travels furthest, which is why ears and fingers glow
  red.
- Random Walk is the accurate method in Cycles; EEVEE approximates SSS and behaves differently, so
  verify in the engine you will render with.
- Vary SSS with a mask: thin areas (ears, nostrils, fingers, leaf edges) scatter more.
- Waxy skin is almost always a radius-vs-scale mismatch plus too little roughness variation.

## Transmission, coat, sheen

| Feature | Use | Notes |
| --- | --- | --- |
| Transmission | Glass, water, liquids, gems | Needs correct IOR; roughness frosts the glass |
| Coat | Car paint, varnish, lacquer, wet look | A separate glossy layer over the base; its own roughness and IOR |
| Sheen | Velvet, peach fuzz, cloth edge glow | Subtle; high values look like lint |
| Thin Film | Iridescence: soap bubbles, oil slicks, anodised metal | Thickness and IOR driven |
| Emission | Screens, lights, glow | Strength above 1.0 makes it a light source in Cycles |

Glass practicalities:

- Solid glass needs real thickness; a single plane refracts wrongly.
- In Cycles, enable enough transmission bounces in Light Paths or thick glass goes black.
- In EEVEE Next, refraction relies on raytracing/screen-space settings; off-screen content cannot be
  refracted, so use a reflection/world fallback.
- Coloured glass is coloured by absorption through volume, not by base colour - use a Volume
  Absorption inside the mesh for accuracy.

## Wiring baked maps

| Map | Node | Colour space |
| --- | --- | --- |
| Base colour | Image Texture > Base Color | sRGB |
| Roughness | Image Texture > Roughness | Non-Color |
| Metallic | Image Texture > Metallic | Non-Color |
| Normal | Image Texture > Normal Map node > Normal | Non-Color |
| AO | Multiply into base colour (sparingly) or into a mask | Non-Color |
| Height | Bump node, or Displacement output | Non-Color |
| ORM packed | Separate Color > channels to AO/Rough/Metal | Non-Color |

AO should not be multiplied into base colour for a physically-lit render - the renderer computes
occlusion. Use it for masks, for real-time assets where the engine expects it, or very lightly to
reinforce contact.

## EEVEE vs Cycles differences worth knowing

| Feature | Cycles | EEVEE Next |
| --- | --- | --- |
| Refraction | Accurate | Screen-space, needs raytracing enabled |
| SSS | Accurate random walk | Approximated |
| Volumetrics | Accurate, slow | Fast, resolution-limited |
| Displacement | True geometric displacement | Bump only |
| Light bounces | Full path tracing | Raytracing plus fast GI approximation |
| Shader nodes | All supported | A few unsupported or approximated |

Build materials in the engine you will ship with. A material tuned in Cycles can look wrong in EEVEE
and vice versa.

## Value checklist

1. Metallic is 0 or 1, with masks for coatings.
2. Albedo inside plausible ranges, no lighting baked in.
3. Roughness varied by a map or mask.
4. IOR set from the reference table for dielectrics.
5. SSS radius in metres, matching the model's scale.
6. Data maps set to Non-Color.
7. Checked under an HDRI with real highlights.
8. Material named descriptively (`mat_steel_painted`, not `Material.003`).
