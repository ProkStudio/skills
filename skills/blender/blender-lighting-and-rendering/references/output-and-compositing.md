# Passes, compositing and output

## Render passes worth enabling

| Pass | Contains | Use |
| --- | --- | --- |
| Combined | The final beauty render | Base image |
| Z / Depth | Per-pixel distance | Defocus, fog, depth grading |
| Mist | Normalised 0-1 distance (set range in World > Mist Pass) | Easier atmospheric fog than raw Z |
| Normal | Surface normals | Relighting tricks, edge detection |
| Position | World position | Advanced masking and relighting |
| Ambient Occlusion | Contact darkening | Subtle contact reinforcement |
| Diffuse / Glossy / Transmission (Direct, Indirect, Color) | Light components | Rebalancing light in comp without re-rendering |
| Emission | Emissive contribution | Isolating glows for the Glare node |
| Environment | World background | Replacing or grading the background |
| Shadow Catcher | Shadows on transparent film | Compositing CG onto plates |
| Cryptomatte (Object, Material, Asset) | Per-object/material mattes | Accurate selections in comp - the best masking tool available |
| Denoising Data (Albedo, Normal, Depth) | Denoiser inputs | Denoising in comp instead of at render time |
| AOV (custom) | Any value from the shader | Custom masks, IDs, wear maps |

Cryptomatte is the pass most people forget and most often need. Enable it on any shot that will be
graded or have elements isolated.

## View layers

- Use view layers to split a scene (character / environment / effects) for separate control.
- Each view layer can include/exclude collections, apply holdouts and indirect-only flags.
- EEVEE view-layer overrides (material, world, samples) in Blender 5.0 make layer-based EEVEE setups
  viable, which previously required Cycles.
- Keep layer names meaningful; they appear in the compositor and in the EXR channels.

## Compositor recipes

| Goal | Nodes |
| --- | --- |
| Bloom / glare | Glare node (Bloom or Fog Glow mode), often fed from the Emission pass, mixed additively at low strength |
| Grade | Color Balance (lift/gamma/gain), RGB Curves, Hue Correct |
| Atmospheric fog | Mist pass > Color Ramp > Mix with a sky colour |
| Depth of field in post | Defocus node with Z pass (watch edge artifacts) |
| Vignette | Ellipse Mask > Blur > Multiply |
| Chromatic aberration | Lens Distortion node with Dispersion, very small values |
| Film grain | Noise texture or the Sequencer's grain; keep it subtle and resolution-aware |
| Sharpen | Filter node (Sharpen) at low strength, or Glare Streaks off |
| Denoise in comp | Denoise node fed by Denoising Data passes |
| Isolate an object | Cryptomatte node, pick objects, use as a mask |
| Light rays | Sun Beams node from the bright source position |

Keep the comp minimal and physically motivated. Heavy post-processing usually compensates for a
lighting problem better solved in 3D.

## Output formats

| Deliverable | Format | Settings |
| --- | --- | --- |
| Final still, web | PNG 8-bit, or JPEG quality 90+ | View transform baked in |
| Still for print | PNG/TIFF 16-bit | Correct resolution and colour space |
| Compositing / grading | OpenEXR Multilayer, 16 or 32-bit, ZIP or DWAA | View transform NOT baked in |
| Animation frames | PNG (16-bit) or EXR sequence | Numbered files; resumable |
| Delivered video | FFmpeg container MP4, H.264, high quality, or ProRes for editing | Encode from a rendered sequence |
| Alpha over a plate | PNG RGBA or EXR with Film > Transparent | Check premultiplied vs straight alpha |

Rules:

1. **Never render an animation straight to MP4.** A crash loses everything and you cannot re-render a
   single frame.
2. Render PNG or EXR sequences, then encode with the Video Sequencer or ffmpeg.
3. EXR keeps scene-linear data with no view transform applied; PNG/JPEG/TIFF bake the transform in.
4. Use frame numbering with padding (`shot01_####.png`) and one folder per shot or version.
5. Match the output frame rate to the scene frame rate, and set it before animating.

## Controlling render time

| Lever | Typical saving |
| --- | --- |
| Denoising instead of brute-force samples | Large |
| Lower noise threshold only where needed | Moderate |
| Reduce diffuse/glossy bounces | Moderate to large on interiors |
| Simplify: subdivision and texture limits | Large in dense scenes |
| Persistent Data for animation | 10-30% on many scenes |
| Instances instead of copies | Large memory saving |
| Cut volumetrics or lower their resolution | Very large |
| Render at 100% but crop test regions (Render Region) | Large during iteration |
| Time Limit per frame | Predictable animation budgets |

Measure before optimising: the render statistics (and the per-pass timings in Cycles) tell you where
the time goes. Guessing usually targets the wrong thing.

## Delivery checklist

1. Frame range, frame rate and resolution confirmed.
2. Passes enabled for the intended comp work, including Cryptomatte.
3. Output path and naming convention set, with padding.
4. Format chosen with the view-transform behaviour in mind.
5. A single test frame reviewed at 100% before the full render.
6. Colour management consistent across all shots.
7. Sequence encoded to video only after all frames exist.
8. Backups: .blend version saved alongside the render output.
