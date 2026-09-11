# Surface recipes

Starting values, not final answers. Every recipe assumes the Principled BSDF and real-world scale,
and every one needs variation added on top.

## Metals

| Surface | Metallic | Roughness | Base colour | Extra |
| --- | --- | --- | --- | --- |
| Polished chrome | 1.0 | 0.02-0.05 | #C4C5C5 | Needs an HDRI with shapes to reflect |
| Brushed aluminium | 1.0 | 0.25-0.4 | #D0D2D3 | Anisotropic roughness along the brush direction |
| Cast iron | 1.0 | 0.5-0.7 | #6E6E6E | Heavy surface noise, pitting via bump |
| Gold | 1.0 | 0.05-0.25 | #FFD86F | Roughness variation makes it read as real metal |
| Copper, oxidised | mask | 0.3 / 0.8 | #F7BFA5 / #4E9C87 patina | Patina is a dielectric layer: metallic 0 in those areas |
| Painted steel | 0.0 | 0.3-0.5 | paint colour | Metallic 1.0 only where paint has chipped, via curvature mask |
| Rusted steel | mask | 0.7-0.9 rust | #6B3A21 | Rust is dielectric, rough, with height variation |

Key point: paint, rust, dirt and patina on metal are **dielectric layers**, so they are metallic 0 in
those masked areas - not a mid metallic value everywhere.

## Painted and plastic surfaces

| Surface | Setup |
| --- | --- |
| Car paint | Base colour, metallic 0, roughness 0.35; add Coat 1.0 with Coat Roughness 0.03-0.1; optional flakes via a high-frequency Voronoi into the normal |
| Glossy plastic | Metallic 0, roughness 0.15-0.3, IOR 1.45-1.5; slight colour variation |
| Matte plastic | Roughness 0.5-0.7; fine bump grain; slight sheen on worn edges |
| Rubber | Roughness 0.6-0.8, IOR 1.5, very dark albedo (40-60 sRGB), subtle dust in recesses |
| Painted wood | Wood grain in the bump, paint colour on top, wear revealing wood at edges |
| Enamel / ceramic | Roughness 0.05-0.15, Coat for the glaze, slight SSS for thin porcelain |

## Wood, stone, concrete

| Surface | Setup |
| --- | --- |
| Wood, finished | Wave texture with distortion for grain; colour variation between early/late wood; roughness 0.25-0.4; Coat for varnish |
| Wood, raw/weathered | Roughness 0.6-0.8; stronger grain bump; grey-shifted albedo; splits via sharpened Voronoi |
| Concrete | Blotchy large noise in albedo; roughness 0.7-0.9 with wet-patch variation; fine grain bump; cracks from Voronoi Distance to Edge |
| Marble | Albedo veins (stretched noise), roughness 0.05-0.2 polished, SSS radius a few millimetres |
| Granite | Voronoi cells with per-cell colour variation; roughness 0.3-0.5 polished, 0.8 raw |
| Brick | Brick texture or tiling map for layout; per-brick colour variation; mortar rougher and lighter |
| Asphalt | Dark albedo (50-70); roughness 0.8-0.9; gravel bump; wear polish in tyre tracks |

## Glass, water, liquids

| Surface | Setup |
| --- | --- |
| Window glass | Transmission 1.0, roughness 0, IOR 1.5, real thickness; Cycles preferred |
| Frosted glass | Transmission 1.0, roughness 0.2-0.4 |
| Coloured glass | Transmission 1.0 plus Volume Absorption inside the mesh (colour + density), not a tinted base colour |
| Water surface | Transmission 1.0, IOR 1.33, roughness 0; ripples via a normal from layered noise |
| Deep water | Water surface plus Volume Absorption/Scatter for depth colour |
| Wet surface | Reduce roughness in puddle masks, darken albedo slightly, add Coat |
| Ice | Transmission with IOR 1.31, internal bubbles via volume, surface roughness variation |

## Skin, organic

| Surface | Setup |
| --- | --- |
| Human skin | Base colour from texture, SSS weight 0.2-0.5 with radius roughly 0.01/0.004/0.002 m, roughness 0.4-0.6 with wetter lips and eye corners, Coat very low for sebum sheen |
| Fine skin detail | Pores and micro wrinkles via a baked normal plus subtle bump; never a uniform pattern |
| Eyes | Cornea as a separate transmissive surface over an iris with its own roughness; the sclera needs SSS |
| Leaves | Translucency via SSS or a Translucent BSDF mix; veins in normal and albedo; roughness 0.3-0.6 with a waxy Coat |
| Fur / hair | Principled Hair BSDF in Cycles; melanin-driven colour; check the render engine's hair support |
| Wax, candle | Strong SSS with a radius of centimetres, roughness 0.3-0.5 |

## Fabric

| Surface | Setup |
| --- | --- |
| Cotton | Roughness 0.85-0.95, Sheen 0.1-0.3, weave normal at real thread scale, slight SSS for thin cloth |
| Velvet | Sheen 0.5-1.0 with Sheen Roughness low, dark albedo, strong view-dependent falloff |
| Silk | Roughness 0.2-0.4 with anisotropy along the weave, Sheen low |
| Denim | Diagonal twill normal, roughness 0.8, colour variation and worn lighter edges |
| Leather | Roughness 0.35-0.6 with polish on raised grain, pebbled normal, slight Coat |
| Wool knit | Large-scale knit normal or displacement, roughness 0.9, Sheen for fibre glow |

## Emissive and screens

| Surface | Setup |
| --- | --- |
| Glowing sign | Emission colour plus Strength 5-50 depending on exposure; the mesh lights the scene in Cycles |
| Screen / display | Emission with the image plugged in; add a subpixel grid normal for close-ups; a faint reflective Coat for realism |
| LED indicator | Small emissive face, Strength high, plus a glass cover with slight roughness |
| Neon tube | Emissive cylinder plus a transparent glass tube; bloom in the compositor, not in the shader |
| Hot metal | Blackbody node driving emission colour by temperature (1000-2000 K), masked to the hot area |

Emission strength depends on exposure: tune it against the scene's lighting, not to an absolute
number, and verify with False Color that it is not clipping.

## Applying any recipe

1. Start from the values above.
2. Add large-scale albedo variation (noise, texture, per-instance hue shift).
3. Add roughness variation - the single biggest realism gain.
4. Add geometry-derived wear: edges polished or chipped, recesses dirty, top surfaces dusty.
5. Add micro surface detail via bump at low strength.
6. Verify under an HDRI with recognisable shapes, at grazing angles.
7. Compare against the photographic reference, not against memory.
