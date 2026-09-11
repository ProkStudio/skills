---
name: blender-lighting-and-rendering
description: Light scenes and render them in Blender with Cycles or EEVEE without guesswork. Use whenever the user asks how to light a character product interior or exterior, how to use an HDRI, what three-point lighting is, how to get soft or hard shadows, which light type and size to use, what colour temperature to pick, why a render is noisy grainy blotchy or full of fireflies, how many samples to use, how denoising works, how to set light bounces and clamping, why EEVEE looks different from Cycles, how to configure EEVEE Next raytracing shadows and light probes, how to choose focal length and depth of field, how to compose a shot, which render passes to output, how to add bloom or glare, or which file format and settings to use for stills and animation. Covers light types and sizes, ratios and motivation, colour temperature, HDRI and sky workflows, interior lighting and portals, Cycles sampling denoising light paths and performance, EEVEE Next raytracing shadow jitter overblur and shadow pool, camera lenses and depth of field, composition, render passes cryptomatte and compositing, and output formats for stills and sequences.
version: 1.0.0
---

# Lighting and rendering

Lighting is the difference between a model and an image. Almost every "my render looks bad" problem
is lighting, exposure or colour management - not render settings.

## When to use

- Lighting a character, product, interior, exterior or full scene.
- Choosing between Cycles and EEVEE, and configuring either.
- Fixing noise, fireflies, blotches, slow renders or wrong-looking shadows.
- Choosing focal length, depth of field and framing.
- Setting up passes, cryptomatte, compositing and final output.

Colour management (AgX, view transforms, which formats bake the look) lives in
`../blender-materials-and-texturing/references/color-management.md` and applies to everything here.

## Ask first

1. **What is the deliverable?** Still, turntable, animation, or real-time preview. This sets engine
   and sample budgets.
2. **What mood and time of day?** Lighting decisions are narrative before they are technical.
3. **Hardware and time budget?** GPU model and how long a frame may take.
4. **Which engine, and is that negotiable?** EEVEE for speed and iteration, Cycles for accuracy.
5. **Will it be composited or graded?** If yes, output EXR with passes rather than a baked PNG.

## Core rules

1. **Light with intent.** Decide what the image is about, then light that.
2. **Softness comes from apparent size.** A big light close to the subject is soft; a small or
   distant one is hard. Wattage does not change softness.
3. **Motivate your lights.** Every light should plausibly come from something: window, lamp, sky,
   fire, screen.
4. **Expose first, then judge colour.** Use False Color; most "washed out" renders are simply
   over-exposed.
5. **Contrast ratios beat absolute values.** Key to fill around 2:1 to 8:1 depending on mood.
6. **Noise is a sampling problem with a cause.** Find the cause (small lights, caustics, high
   roughness bounces) instead of raising samples blindly.
7. **Denoise as a finishing step**, not as a way to hide a badly lit scene.
8. **Render animations as image sequences**, never straight to video.

## Workflow

**Step 0 - decide deliverable, engine, mood, and reference.**

**Step 1 - block the lighting** with one key light. Get the subject reading correctly before adding
   anything else. See `references/light-setups.md`.

**Step 2 - add fill, rim and practicals**, each with a reason, checking the ratio after each.

**Step 3 - set exposure** and verify with False Color.

**Step 4 - camera**: focal length, height, framing, depth of field. See
   `references/camera-and-composition.md`.

**Step 5 - engine settings**: samples, bounces, raytracing or shadow settings. See
   `references/cycles-and-eevee.md`.

**Step 6 - passes and compositing**: choose passes, add glare and grade. See
   `references/output-and-compositing.md`.

**Step 7 - final render**: test frames, then the full job with the correct format and naming.

## References

| File | Read it for |
| --- | --- |
| `references/light-setups.md` | Light types and when to use each, size vs softness, three-point and its variants, ratios, colour temperature table, HDRI and sky workflows, interior lighting and portals, product and character setups, common lighting mistakes |
| `references/cycles-and-eevee.md` | Engine comparison, Cycles sampling/denoising/light paths/clamping/performance, EEVEE Next raytracing, shadow jitter overblur and filter, shadow pool, volumetrics, light probes, when each engine is the wrong choice |
| `references/camera-and-composition.md` | Focal length behaviour and choices, sensor and framing, depth of field and f-stop, motion blur, composition principles, aspect ratios and resolution, camera animation basics |
| `references/output-and-compositing.md` | Render passes and cryptomatte, view layers, EXR multilayer, compositor recipes (glare, grade, fog, defocus), denoise nodes, output formats for stills and sequences, naming, render time control |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-materials-and-texturing/SKILL.md` | Material response, colour management details |
| `../blender-fundamentals/SKILL.md` | Scale, units and clipping problems affecting lighting |
| `../blender-geometry-nodes/SKILL.md` | Procedural scene dressing and instancing |
| `../blender-rigging-and-animation/SKILL.md` | Animated shots and motion blur |
| `../../game/2d/vfx-and-lighting-2d/SKILL.md` | The 2D equivalent of light and shadow design |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Flat, boring render | One frontal light, no ratio, no rim | Move the key off-axis, build a ratio, add separation |
| Washed-out image | Over-exposure under a filmic transform | Lower exposure; check with False Color |
| Noisy render even at high samples | Small bright lights, caustics, glossy interreflections | Enlarge lights, raise Filter Glossy, clamp indirect |
| Bright single-pixel fireflies | Extreme indirect samples | Clamp Indirect, enlarge light sources, denoise |
| Blotchy patches after denoising | Too few samples for the denoiser to work with | Raise samples; enable denoising data passes |
| Shadows look blurry or detached in EEVEE | Shadow resolution, overblur and filter settings | Tune shadow settings; enable jitter where affordable |
| Dark artifacts or banding in EEVEE shadows | Shadow pool too small for the scene | Increase the shadow pool size |
| EEVEE glass or refraction is black | Screen-space raytracing cannot see off-screen content | Enable raytracing, add a fallback, or render in Cycles |
| Render is far too slow | Too many bounces, subdivision, volumetrics, 4K textures | Reduce bounces, use Simplify, limit textures, use instances |
| Video output unusable | Rendered straight to a compressed video and interrupted | Render PNG/EXR sequences, encode afterwards |

## Answering style

- Give light sizes in metres and distances relative to the subject, plus colour temperatures in K.
- Name the physical cause of noise before suggesting more samples.
- Say explicitly which engine a setting belongs to; EEVEE and Cycles do not share most of them.
- Recommend exposure and False Color checks before any colour or saturation advice.
