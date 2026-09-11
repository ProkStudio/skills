# Blockout, forms and detail sizing

## Reference setup

- Collect at least front, side and three-quarter views, plus close-ups of the details you will model.
- Load references as Image Empties (Add > Image > Reference) in a `refs/` collection, set to
  front/side orthographic, opacity around 0.5, and locked.
- Put a scale figure or a known object (a 1.7 m human, a 0.33 l can) in the scene. Nearly every
  "proportions feel off" problem is a scale problem.
- Note the real dimensions in a text object in the file. Guessed dimensions produce toy-like models.

## Blockout

1. Build the object from primitives at correct dimensions - cubes, cylinders, spheres - one per
   major mass.
2. Judge from the camera you will render from, in perspective, not from an orthographic view.
3. Fix proportions now. Every hour spent fixing proportions later costs ten.
4. Keep the blockout in its own collection; it is your measuring stick for the rest of the project.
5. Only then convert masses into clean base meshes.

Useful blockout habits:

- Model half and mirror when the object is symmetric.
- Use the N-panel Dimensions field rather than dragging.
- Snap with vertex/face snapping and the 3D cursor for exact placement.
- Check the silhouette by pressing into solid shading with a flat material, or by looking at the
  object against a bright backdrop.

## Form hierarchy

| Level | What it is | Typical size relative to object | Examples |
| --- | --- | --- | --- |
| Primary | The masses that define the silhouette | 100-30% | Body, barrel, chassis, roof |
| Secondary | Breakups of the primary surfaces | 30-5% | Panels, plates, hatches, insets, grilles |
| Tertiary | Small surface detail | under 5% | Screws, rivets, cables, labels, weld seams |

Rules:

- Finish each level before starting the next. Tertiary detail on wrong primary forms is wasted work.
- Vary the rhythm within each level: repeated identical panels look like a texture, not an object.
- Keep 20-40% of the surface quiet. Detail reads because of the empty space around it.
- Tertiary detail should cluster around function: fasteners near joins, cables near ports, wear near
  handles and edges.

## Real detail dimensions

Model details at plausible physical sizes:

| Detail | Real size |
| --- | --- |
| Panel gap / seam | 1-3 mm |
| Chamfer / bevel on a manufactured edge | 0.5-3 mm |
| Screw head (M3-M6) | 5.5-10 mm across |
| Rivet head | 4-12 mm |
| Sheet metal thickness | 0.8-3 mm |
| Plywood / MDF panel | 12-18 mm |
| Cable (power) | 5-12 mm diameter |
| Hydraulic line | 8-25 mm |
| Button (machine) | 10-20 mm |
| Lettering on a plate | 4-10 mm cap height |

A 3 cm bevel on a 1 m box looks like injection-moulded plastic at 10x scale; a 2 mm bevel on the
same box reads as machined metal.

## Panel lines and cuts

- Panel lines should follow function: where parts would be manufactured separately, where something
  must open, where stress concentrates.
- Avoid symmetrical grids of identical panels; group them with varying sizes and one dominant break.
- Terminate lines deliberately - into a corner, a fastener, or another line. Lines that stop in the
  middle of a surface look accidental.
- Depth matters: a 1-2 mm inset with a bevel catches light; a flat texture line does not, at close
  range.

## Greebles and mechanical plausibility

- Every shape should imply a purpose: cooling, access, fastening, reinforcement, routing.
- Reuse a small kit of parts (bolts, vents, clamps, boxes) as linked duplicates; a coherent kit
  reads as engineering, while random shapes read as noise.
- Match the technology level: riveted plate and CNC-milled housing do not belong on the same object
  unless the story says so.
- Scale greebles to the object - a 3 m mech and a 30 cm drone cannot share the same bolt size.

## Blockout review checklist

1. Dimensions match the reference, verified in the N-panel.
2. Silhouette is readable from the render camera, in perspective.
3. Primary forms finished before any bevels or details.
4. Scale figure present in the scene.
5. Detail sizes chosen in millimetres from real references.
6. Quiet areas deliberately preserved.
7. Symmetry handled with a Mirror modifier rather than duplicated geometry.
