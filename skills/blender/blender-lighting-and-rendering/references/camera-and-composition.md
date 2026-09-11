# Camera and composition

## Focal length

Blender's default camera uses a 36 mm sensor width, so focal lengths match full-frame photography.

| Focal length | Character | Use |
| --- | --- | --- |
| 12-18 mm | Extreme wide, heavy distortion | Cramped interiors, dramatic scale, stylised |
| 24-35 mm | Wide, environmental | Architecture, establishing shots, environments |
| 50 mm | Near-human perspective | Neutral, documentary feel |
| 85 mm | Compressed, flattering | Portraits, character close-ups |
| 100-135 mm | Strong compression | Product detail, isolated subjects |
| 200 mm+ | Telephoto, flat layers | Distant subjects, stacked-plane compositions |

Perspective is controlled by camera **distance**, not focal length: a wide lens up close exaggerates
noses and foreshortening, a long lens far away flattens features. Choose the look, then move the
camera and set the lens to frame it.

Orthographic cameras remove perspective entirely - useful for technical, isometric and
texture-reference renders. Orthographic Scale replaces focal length.

## Depth of field

| Setting | Effect |
| --- | --- |
| Focus Object | Locks focus to an object; safest for animation |
| Focus Distance | Manual focus distance in metres |
| F-Stop | Lower = shallower depth of field (f/1.2-f/2.8 shallow, f/8-f/16 deep) |
| Blades / Rotation / Ratio | Bokeh shape: blades give polygonal bokeh, ratio gives anamorphic ovals |

Notes:

- DOF depends on real scale. At the wrong scene scale, f/2.8 can blur everything or nothing.
- Shallow DOF on a small product needs a physically plausible distance, or it reads as a miniature.
- In Cycles, DOF is traced and costs samples; in EEVEE it is post-processed and can show artifacts at
  object edges.
- Compositor Defocus with a Z pass is an alternative that keeps flexibility, but it handles
  overlapping depths poorly.

## Framing and composition

Principles that carry most images:

1. **One clear subject.** Decide what the eye should land on first and give it the most contrast.
2. **Rule of thirds** as a starting grid; centre framing for symmetry and confrontation.
3. **Leading lines** guide the eye - edges, light shafts, roads, shadows.
4. **Negative space** gives the subject room; cramped framing feels accidental unless intentional.
5. **Foreground, midground, background** create depth; one layer alone flattens the image.
6. **Silhouette check**: squint or blur the image; the composition should still read.
7. **Value grouping**: group similar values into a few big shapes rather than scattering contrast.
8. **Camera height tells a story**: low reads powerful, high reads vulnerable or observational.

Use Blender's camera overlays: Composition Guides (thirds, golden ratio, centre, diagonals), Safe
Areas for broadcast, and Passepartout to darken the outside of frame.

## Depth cues

| Cue | How to add it |
| --- | --- |
| Atmospheric perspective | Mist pass or a thin volumetric; distant objects lose contrast and shift to sky colour |
| Overlap | Arrange objects so they occlude each other |
| Size gradient | Repeat similar objects at receding scales |
| Focus falloff | Depth of field |
| Light falloff | Let distant areas fall darker or hazier |
| Warm/cool separation | Warm foreground, cool distance |

## Resolution and aspect

| Aspect | Resolution examples | Use |
| --- | --- | --- |
| 16:9 | 1920x1080, 3840x2160 | Video, general |
| 2.39:1 | 2048x858, 3840x1608 | Cinematic widescreen |
| 4:5 / 1:1 | 1080x1350 / 1080x1080 | Social posts |
| 9:16 | 1080x1920 | Vertical video |
| 3:2 / 4:3 | 3000x2000 / 2048x1536 | Print-like stills |

- Render at final resolution for judging; the percentage scale is for tests only.
- Print work needs a target size and DPI: 300 DPI at A4 is roughly 3508x2480 px.
- Keep the resolution percentage at 100% for the final; halving it halves apparent sharpness and
  changes how DOF and noise read.

## Motion and animation basics for camera

- Real cameras move on a dolly, crane or handheld rig. Perfect linear moves feel synthetic; add slow
  ease in and out.
- Use a camera rig: an Empty parent for the dolly, a second for the head, so you can animate
  translation and rotation independently.
- Track to a target with a Track To or Damped Track constraint for locked-on subjects.
- Motion blur: enable it in Render Properties; shutter around 0.5 matches a standard 180-degree
  shutter at your frame rate.
- Handheld feel: a subtle noise modifier on rotation F-curves, amplitude small (fractions of a
  degree).
- Check for gimbal problems on long rotating shots; a rig with separate empties avoids most of them.

## Camera checklist

1. Lens chosen for the desired perspective, then the camera moved to frame.
2. Real-world scale verified so DOF behaves.
3. Focus on the intended subject, ideally via Focus Object.
4. Composition guides used; subject clearly dominant.
5. Three depth layers present, or a deliberate flat design.
6. Final resolution and aspect set, percentage at 100%.
7. Motion blur and shutter set for animated shots.
