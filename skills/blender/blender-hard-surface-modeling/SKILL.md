---
name: blender-hard-surface-modeling
description: Model hard-surface objects in Blender - props, weapons, vehicles, machinery, architecture, furniture - so shapes read well and shading stays clean. Use whenever the user is box modelling, asks how to block out an object, how to bevel edges properly, how to add support loops, how to use booleans without breaking the mesh, how subdivision surface modelling works, why their model has dark smudges, pinching, wavy reflections or shading artifacts, why a bevel looks uneven, or how to cut panel lines, holes, screws and greebles. Covers reference gathering and blockout with primitives at real dimensions, primary secondary and tertiary forms, edge flow and silhouette, destructive versus modifier bevels, bevel weights and clamp overlap, support loop spacing for subdivision, creases versus geometry, boolean solvers and cutter management, non-manifold cleanup, custom normals and Smooth by Angle, weighted normals, and a diagnostic table for every common shading artifact.
version: 1.0.0
---

# Hard-surface modelling

Hard-surface modelling is a shape problem first and a shading problem second. Get the silhouette and
form hierarchy right, then keep the surface clean enough that light behaves predictably on it.

## When to use

- Building props, weapons, vehicles, machinery, furniture, architecture, sci-fi panels.
- Blocking out an object and deciding where detail goes.
- Bevelling, support loops, subdivision setups, creases.
- Cutting holes, panel lines, vents, screws, greebles with booleans.
- Dark smudges, pinching, wavy highlights or other shading artifacts.

Scene setup and transform hygiene come from `../blender-fundamentals/SKILL.md`; deeper topology
theory is in `../blender-topology-and-retopology/SKILL.md`.

## Ask first

1. **What is it for?** Close-up hero render, background prop, or a real-time asset with a triangle
   budget? This sets subdivision, bevel density and boolean freedom.
2. **Real-world dimensions** of the object and its details (a screw head is 6-10 mm, a panel gap
   is 1-3 mm). Details modelled at the wrong size are the main reason props look like toys.
3. **Will it be baked?** A high-poly for baking can be messy topologically; a deforming or
   subdivision-ready mesh cannot.
4. **Reference available?** Hard surface without reference produces vague, plastic shapes.
5. **Subdivision or bevel-only?** Two different disciplines: subdivision needs quad cages and support
   loops; bevel-only needs weighted normals and tight control of the bevel modifier.

## Core rules

1. **Blockout before detail.** Match proportions and silhouette with primitives at real dimensions
   before a single bevel.
2. **Work in form hierarchy**: primary masses, then secondary breakups (panels, plates, cuts), then
   tertiary detail (screws, vents, decals). Never start at tertiary.
3. **Silhouette carries the read.** If the outline is boring, surface detail will not save it.
4. **Bevels are what make an object look manufactured.** No perfectly sharp edge exists in the real
   world; a 1-3 mm bevel on every hard edge is the single biggest realism upgrade.
5. **Keep the mesh manifold.** No holes, no interior faces, no doubled vertices, no inverted normals.
6. **Detail density must be consistent.** Mixed density - one area with 200 bolts and another bare -
   reads as unfinished, not as contrast.
7. **Shading artifacts are geometry telling you something.** Fix the geometry, do not hide it with
   smooth shading.

## Workflow

**Step 0 - reference and dimensions.** Real object sizes, at least 3 reference angles, and a scale
   figure in the scene.

**Step 1 - blockout** with primitives at correct dimensions; judge proportion and silhouette from
   the camera you will actually render. See `references/blocking-and-forms.md`.

**Step 2 - primary forms.** Convert the blockout into clean base shapes, all quads where
   subdivision is planned, transforms applied.

**Step 3 - secondary forms**: panel splits, insets, plates, cut-outs. Booleans go here, with cutters
   kept live. See `references/booleans-and-cutters.md`.

**Step 4 - edges.** Bevel weights or angle-limited bevels; support loops if subdividing. See
   `references/bevels-and-edges.md`.

**Step 5 - tertiary detail**: screws, vents, rivets, cables, decals - as linked duplicates or
   floaters, not modelled into the mesh, when it will be baked.

**Step 6 - shading pass**: Smooth by Angle or weighted normals, check with a reflective matcap, hunt
   artifacts. See `references/subdivision-and-shading.md`.

**Step 7 - cleanup**: merge by distance, recalculate normals, check Face Orientation overlay, remove
   interior faces, apply transforms.

## References

| File | Read it for |
| --- | --- |
| `references/blocking-and-forms.md` | Reference setup, blockout method, primary/secondary/tertiary hierarchy, real detail dimensions, silhouette and proportion checks, greeble and panel-line design |
| `references/bevels-and-edges.md` | Modifier vs destructive bevel, bevel weights, segments and profiles, clamp overlap, miters, support-loop spacing, creases vs geometry, bevel after boolean |
| `references/booleans-and-cutters.md` | Exact vs Fast solver, cutter organisation, manifold requirements, self-intersection, boolean cleanup, common boolean failures and their fixes |
| `references/subdivision-and-shading.md` | Subdivision cage rules, poles and pinching, Smooth by Angle and custom normals in 4.1+, weighted normals, matcap checking, full shading-artifact diagnostic table |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-fundamentals/SKILL.md` | Scale, transforms, modifier stack order, file structure |
| `../blender-topology-and-retopology/SKILL.md` | Edge flow theory, cleanup, remeshing, deforming topology |
| `../blender-uv-and-baking/SKILL.md` | Unwrapping the finished model, baking high to low |
| `../blender-materials-and-texturing/SKILL.md` | Materials, wear, panel-line masks |
| `../blender-to-engine-export/SKILL.md` | Triangle budgets, LODs, export settings |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Model looks like a toy | Details modelled at the wrong physical size | Model details in millimetres from reference |
| Dark smudges near edges | Bevel too wide for the geometry, or overlapping bevel | Reduce width, enable Clamp Overlap, add support geometry |
| Wavy or blotchy highlights | Non-planar quads, N-gons on flat faces | Make faces planar; triangulate or re-flow the area |
| Pinching after subdivision | Poles or tight loops too close together | Move loops apart, reduce pole valence, use creases |
| Bevel looks uneven across the object | Object scale not 1, 1, 1 | Apply scale |
| Boolean leaves holes or spikes | Non-manifold input, coplanar faces | Make both meshes solid, offset the cutter slightly |
| Flat faces show shading gradients | Smooth shading with no angle limit | Shade Auto Smooth / Smooth by Angle, or weighted normals |
| Black facets in render | Inverted normals | Recalculate normals; check Face Orientation overlay |
| Detail reads as noise | Uniform density, no quiet areas | Cluster detail, leave breathing space |

## Answering style

- Give real dimensions in millimetres for details, metres for masses.
- Propose a non-destructive route (modifiers, live cutters) before a destructive one.
- When diagnosing shading, name the geometric cause, not just the fix.
- Distinguish advice for subdivision workflows from bevel-only workflows; they are not interchangeable.
