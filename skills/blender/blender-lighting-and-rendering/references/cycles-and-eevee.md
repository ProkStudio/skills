# Cycles and EEVEE

## Engine comparison

| | Cycles | EEVEE Next (4.2+) |
| --- | --- | --- |
| Method | Path tracing | Rasterisation plus screen-space and raytraced effects |
| Accuracy | Physically accurate | Approximate, greatly improved over legacy EEVEE |
| Speed | Seconds to hours per frame | Milliseconds to seconds |
| Refraction | True | Screen-space; off-screen content is missing |
| SSS | Accurate random walk | Approximated |
| Volumetrics | Accurate | Fast, resolution-limited |
| Displacement | True geometric | Bump only |
| Caustics | Yes (with effort) | No |
| Best for | Final renders, product, VFX, anything physically critical | Previews, animation, stylised work, motion graphics, deadlines |

Blender 5.0 made EEVEE material compilation dramatically faster (notably on NVIDIA with Vulkan) and
added EEVEE view-layer overrides for material, world and sample settings, which makes multi-layer
EEVEE setups practical.

## Cycles: sampling

| Setting | Guidance |
| --- | --- |
| Max Samples | 128-512 for most stills with denoising; 1000+ for heavy interiors or caustics |
| Noise Threshold (adaptive sampling) | 0.01 default; lower (0.005) for cleaner, higher (0.02-0.05) for faster |
| Min Samples | Leave automatic unless adaptive sampling stops too early |
| Time Limit | Useful for animation: cap per-frame time instead of samples |
| Denoise (render) | On, OpenImageDenoise on CPU or OptiX on NVIDIA |
| Denoise (viewport) | On, with a low start-sample for fast feedback |
| Denoising passes (Albedo, Normal) | Enable - they preserve texture detail through denoising |

Denoising is not free: it softens fine detail and can smear at low sample counts. Give the denoiser
enough signal - blotchy output means samples, not denoiser settings, are the problem.

## Cycles: light paths

| Setting | Default-ish | Notes |
| --- | --- | --- |
| Total bounces | 12 | Raise for glass-heavy or interior scenes |
| Diffuse | 4 | 6-12 for interiors, 2 for speed on exteriors |
| Glossy | 4 | Raise for mirrored/metal-heavy scenes |
| Transmission | 12 | Thick glass needs high values or it goes black |
| Volume | 0-2 | Raise for smoke, clouds, atmosphere |
| Transparent | 8 | Overlapping alpha (foliage, hair cards) needs more |
| Clamp Direct | 0 (off) | Rarely needed |
| Clamp Indirect | 0, or 3-10 to kill fireflies | Lower values flatten indirect light, so use the highest value that removes fireflies |
| Filter Glossy | 0-1 | Blurs glossy rays to tame caustic noise |
| Fast GI Approximation | Off | Approximates distant bounces; big speedups, less accuracy |

Caustics: enable Filter Glossy and consider per-object Caustics Cast/Receive settings for shadow
caustics. Refractive caustics remain the noisiest phenomenon in path tracing - budget for it.

## Cycles: performance

- **Device**: GPU Compute with OptiX/HIP/Metal as available; check preferences for the right backend.
- **Persistent Data**: on for animation - keeps the scene in memory between frames, trading RAM for
  speed.
- **Simplify**: cap viewport and render subdivision, texture size limits, and child particle counts.
- **Instances**: linked duplicates and geometry-node instances cost almost no extra memory.
- **Light Tree**: keep enabled when the scene has many lights; it samples them far more efficiently.
- **Textures**: 4K everywhere is the usual memory hog; limit sizes for background objects.
- **Volumes**: expensive; reduce step rate and resolution before raising samples.
- **Tiling**: only matters when GPU memory is short; large tiles are faster when memory allows.

## EEVEE Next: raytracing

The Raytracing panel replaced most of legacy EEVEE's fake effects:

| Setting | Purpose |
| --- | --- |
| Screen Tracing | Traces rays against the depth buffer for reflections, refraction and GI |
| Resolution / Precision | Quality vs speed of the traced effects |
| Denoising (Spatial, Temporal, Bilateral) | Cleans traced results; temporal needs several frames or samples |
| Fast GI Approximation | Cheap ambient bounce when full tracing is too slow |
| Clamping | Limits bright traced samples to reduce flicker |

Limitations to state plainly: screen-space tracing cannot see what is off-screen or behind objects,
so reflections and refractions of off-screen content fall back to probes or the world. That is the
main reason EEVEE glass and mirrors look wrong compared with Cycles.

## EEVEE Next: shadows

Shadows are now virtual shadow maps, configured per light and globally:

| Setting | Effect |
| --- | --- |
| Shadow (per light) | Enables shadow casting |
| Jitter | Randomises shadow sampling for soft, accurate penumbra; costs performance and disables shadow-map caching |
| Overblur | Widens the shadow slightly to hide aliasing at the cost of contact sharpness |
| Filter | PCF-style softening of the shadow edge |
| Resolution Limit (scene) | Caps shadow map detail; raise for crisp contact shadows |
| Shadow Pool (memory) | Global memory for shadow maps; too small produces dark artifacts and missing shadows |

If shadows show blocky darkness or drop out in a complex scene, increase the shadow pool before
touching anything else.

## EEVEE Next: other settings

| Setting | Notes |
| --- | --- |
| Samples (render / viewport) | Temporal accumulation; more samples clean up jitter and traced noise |
| Volumes | Resolution, step rate and max depth; volumetric quality is resolution-bound |
| Light Probes (Sphere, Plane, Volume) | Provide off-screen reflection and irradiance data; bake them for interiors |
| Clamping | Limits world and surface brightness to reduce flicker |
| Motion Blur | Accumulation-based; needs enough steps |
| Film > Transparent | Same as Cycles |
| Bloom | Removed from EEVEE Next - use the compositor's Glare node |

Light probes matter: without a Sphere probe, interior reflections fall back to the world and look
wrong. Plane probes give accurate mirror-like reflections on flat surfaces.

## Choosing wrongly

| Situation | Wrong choice | Why |
| --- | --- | --- |
| Jewellery, crystal, liquids | EEVEE | Needs true refraction and caustics |
| 2000-frame animation on a laptop | Cycles at 1000 samples | Render time is the deliverable's real constraint |
| Product shot for a client colour approval | EEVEE with default probes | Reflection and GI accuracy matter |
| Stylised short with flat shading | Cycles | Paying for accuracy nobody sees |
| Architectural interior walkthrough | Cycles without Persistent Data and Simplify | Avoidable per-frame cost |

## Render settings checklist

1. Engine chosen for the deliverable, not by habit.
2. Resolution and frame range set correctly, including the percentage scale.
3. Cycles: adaptive sampling threshold set, denoising with data passes enabled.
4. Cycles: bounces tuned to the scene (interiors up, exteriors down); clamp indirect only if needed.
5. EEVEE: raytracing enabled, light probes placed and baked, shadow pool sufficient.
6. Persistent Data and Simplify configured for animation.
7. Test-rendered a single representative frame at full resolution before committing.
