# Patterns, debugging and handoff

## Debugging routine

1. **Viewer node** (Ctrl+Shift+Click a node) shows that node's output in the viewport and drives the
   Spreadsheet.
2. **Spreadsheet editor**: pick the object, the node-tree evaluation stage, and the domain tab. Look
   at actual counts and values.
3. **Element counts** are the fastest sanity check: 0 points means the problem is upstream.
4. **Mute nodes** (M) to bisect the tree; find the last node where data is still correct.
5. **Hover a socket** to see its inspection value or field status.
6. **Check the domain tabs** before believing an attribute is missing.
7. **Simplify the input**: test on a single plane or a cube before a full terrain.
8. **Watch the modifier's timing** in the spreadsheet or with a simple before/after viewport test to
   find the slow branch.

## Error decoder

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Empty output | Selection is all false, or geometry consumed by a node | Viewer down the chain; check selections |
| Sockets will not link | Field into a single-value socket | Capture the field, or evaluate it in place |
| Values averaged unexpectedly | Cross-domain interpolation | Store on the target domain explicitly |
| Instances invisible in render | Instances hidden, or the source object hidden in render | Check object visibility flags; Object Info does not need the source visible if instanced correctly |
| Random values identical | No ID input, single evaluation context | Feed ID or Index into Random Value |
| Attribute missing downstream | Node does not propagate it | Store before, read after |
| Simulation gives different results | Scrubbing rather than playing from the start | Play from the start frame or bake |
| Viewport fine, render heavy/crashes | Render density higher than viewport, or realize at render | Reduce render density; keep instances |
| Exporter produces nothing | Instances not realized | Realize or apply the modifier before export |
| Slow after a small change | A proximity, raycast or boolean now runs per element | Reduce element count before the expensive node |

## Pattern library

| Ask | Chain |
| --- | --- |
| Scatter rocks on terrain | Distribute Points on Faces (Poisson) > Align Rotation to Vector (Normal) > Rotate Instances (random Z) > Instance on Points (Collection Info, Pick Instance) |
| Grass field | Distribute Points (high density, Random) > Instance on Points (grass blade) > random Z rotation and scale; reduce viewport density |
| Ground-conformed props | Grid > Raycast down onto terrain > Set Position (hit position) > Instance on Points with hit normal alignment |
| Procedural fence | Curve > Resample by Length > Instance on Points (post) + Curve to Mesh (rails) |
| Cables between points | Curve Line or Bezier Segment per pair > Set Position with a downward sag via Curve Parameter > Curve to Mesh |
| Building blockout | Grid > Extrude Mesh per face with random offsets > Scale Elements > Set Material by height mask |
| Noise displacement | Set Position with Offset = Normal x Noise Texture value |
| Melt / flatten effect | Set Position lerping Z toward 0 by a mask or time |
| Exploding mesh | Mesh to Points > Instance on Points (fragment) > Translate Instances by random direction x time |
| Honeycomb / hex grid | Grid > Dual Mesh > Scale Elements > Extrude |
| Crowd placement | Points from a mask > Instance on Points (Collection Info, Pick Instance) > per-instance random attribute for material variation |
| Fake LODs | Switch on Is Viewport, or proximity to the camera choosing between proxy and hero instance |
| Wear/dirt mask for shading | Compute a field, Store Named Attribute, read it in the shader with the Attribute node |
| Camera-frustum culling | Position transformed relative to the camera, Delete Geometry outside a bounding test |

## Performance order of operations

Optimise in this order:

1. **Reduce element count** as early as possible in the tree; every later node pays for it.
2. **Keep instances** and avoid Realize.
3. **Move expensive nodes after filters**, not before (proximity, raycast, boolean, simulation).
4. **Lower viewport density** with a Switch on Is Viewport.
5. **Avoid booleans** on dense meshes; use instancing or pre-made cut geometry.
6. **Cap repeat iterations** and bake simulations.
7. **Simplify** (scene Simplify limits subdivision and child counts too).
8. **Bake or apply** when the setup is final and no longer needs to be procedural.

## Handoff

| Destination | What to do |
| --- | --- |
| Keep procedural in Blender | Group, label, expose inputs, save as an asset |
| Render heavy scenes | Keep instances; Cycles and EEVEE both handle instancing efficiently |
| Hand to another artist | Node group as an asset, documented inputs, example file |
| Engine export | Apply the modifier (or Realize) to produce real geometry, then follow `../../blender-to-engine-export/SKILL.md` |
| Sculpt or edit the result | Apply the modifier; procedural output is not editable in edit mode |
| Cache for animation | Bake simulation zones; consider Alembic export for heavy caches |

Before applying, save a version with the procedural setup intact. Applied geometry cannot be
re-parameterised.

## Final checklist

1. Tree built from named groups with exposed, sensible inputs.
2. Viewer-verified at each major stage.
3. Domains explicit; temporary attributes removed.
4. Random values seeded by ID.
5. Instances preserved; viewport density reduced.
6. Performance measured, not guessed.
7. Handoff decided: procedural asset, applied mesh, or baked cache.
8. Procedural version saved before any apply.
