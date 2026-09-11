---
name: blender-topology-and-retopology
description: Judge and fix mesh topology in Blender, and rebuild clean meshes over messy or sculpted ones. Use whenever the user asks what good topology is, whether triangles and N-gons are acceptable, what a pole is, how edge loops should flow, why a mesh deforms badly at elbows shoulders or knees, why subdivision pinches, how to retopologise a sculpt, when to use Voxel Remesh versus Quad Remesh or Quadriflow, how to use the Remesh modifier, Poly Build, Shrinkwrap and snapping for manual retopology, how to reduce polygon count sensibly, or how to clean up non-manifold geometry, duplicate vertices, inverted normals and interior faces. Covers quads triangles and N-gons in context, edge loops and rings, pole valence and where poles may live, loop layout for faces and joints, quad density and even spacing, Voxel versus Quadriflow remeshing with their real limitations, manual retopology tooling and overlays, decimation and LOD reduction, triangulation for export, and a full diagnostic checklist for broken meshes.
version: 1.0.0
---

# Topology and retopology

Topology is how a mesh's faces are arranged. It matters for exactly three reasons: how the surface
shades, how it deforms, and how it subdivides. Outside those three, "bad" topology is often perfectly
fine - and insisting on all-quads everywhere wastes time.

## When to use

- Deciding whether a mesh's topology is good enough for its purpose.
- Fixing deformation problems at joints, faces, or anywhere a mesh bends.
- Diagnosing subdivision pinching and shading errors caused by topology.
- Retopologising a sculpt or a messy boolean mesh.
- Choosing between Voxel Remesh, Quad Remesh/Quadriflow, manual retopology, or decimation.
- Cleaning non-manifold meshes, duplicate vertices, inverted normals, interior faces.

## Ask first

1. **What will the mesh do?** Static prop, deforming character, subdivision surface, bake source, or
   3D print. Each has different topology requirements - a bake source needs almost none.
2. **Is there a polygon or triangle budget?**
3. **Will it be subdivided?** Subdivision demands quads; real-time rendering does not.
4. **Does it deform?** If yes, joints and expression areas need deliberate loops.
5. **How was it made?** Sculpt, boolean modelling, scan, or CAD import - each implies a different
   retopology route.

## Core rules

1. **Topology serves a purpose.** Judge it against deformation, subdivision and shading, not against
   an aesthetic ideal.
2. **Quads for anything that deforms or subdivides.** Triangles are fine on static, non-subdivided
   geometry and are what the GPU renders anyway.
3. **N-gons are acceptable only on genuinely flat surfaces**, and even then they break bevels and
   subdivision.
4. **Poles are unavoidable; placement is the skill.** Keep them off curved highlight areas and away
   from deforming zones.
5. **Loops should follow form and motion**: around eyes and mouth, around joints, along the length of
   a limb.
6. **Even quad density** where curvature and deformation happen; sparse where the surface is flat.
7. **Remeshing is not retopology.** Automatic remeshers give you workable geometry, not good
   deformation topology.
8. **Clean before you judge.** Duplicate vertices and inverted normals masquerade as topology
   problems.

## Workflow

**Diagnosing an existing mesh**

**Step 0 - clean**: merge by distance, recalculate normals, delete interior faces, check non-manifold
   (Select > All by Trait). See `references/cleanup-and-diagnostics.md`.

**Step 1 - classify the purpose** (static / deforming / subdivided / bake source / print).

**Step 2 - measure**: face-type counts, pole locations, density variation.

**Step 3 - fix locally** where possible: re-flow a corner, dissolve a stray edge, move a pole.
   Full retopology is a last resort. See `references/edge-flow-and-quads.md`.

**Retopologising a sculpt**

**Step 4 - decide the route**: Voxel Remesh for sculpt continuation, Quad Remesh/Quadriflow for a
   subdivision base, manual retopology for anything that deforms or must be efficient. See
   `references/remesh-and-retopo-tools.md`.

**Step 5 - build the new mesh** with Poly Build or plane extrusion, snapping to the surface, using
   the retopology overlay and Shrinkwrap where helpful.

**Step 6 - lay out deformation loops** explicitly at joints and expression areas. See
   `references/deformation-topology.md`.

**Step 7 - verify**: subdivide once and look for pinching, test-deform with a quick armature or
   Simple Deform, and check shading with a chrome matcap.

## References

| File | Read it for |
| --- | --- |
| `references/edge-flow-and-quads.md` | Quads/tris/N-gons in context, loops and rings, poles and valence, loop termination, density rules, local re-flow recipes |
| `references/deformation-topology.md` | Loop layout for elbows, knees, shoulders, hips, face; loop counts per joint; how skinning interacts with topology; testing deformation |
| `references/remesh-and-retopo-tools.md` | Voxel vs Quad (Quadriflow) remesh with documented limitations, Remesh modifier, manual retopology tools, snapping and overlays, Shrinkwrap, decimation and LODs, triangulation |
| `references/cleanup-and-diagnostics.md` | Non-manifold, duplicates, interior faces, normals, zero-area faces, loose geometry, statistics reading, mesh-analysis overlays, 3D-print checks |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-hard-surface-modeling/SKILL.md` | Building hard-surface shapes, bevels, booleans |
| `../blender-sculpting/SKILL.md` | Creating the high-poly form you are retopologising |
| `../blender-uv-and-baking/SKILL.md` | Unwrapping and baking high to low |
| `../blender-rigging-and-animation/SKILL.md` | Skinning the mesh you just built loops for |
| `../blender-to-engine-export/SKILL.md` | Triangle budgets, LODs, triangulation on export |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Elbow collapses when bent | Too few loops across the joint | 3+ loops at the bend, evenly spaced |
| Shoulder tears or folds badly | Loops not following the deltoid form | Re-flow loops radially around the joint |
| Subdivision pinches at a point | High-valence pole | Reduce to 4-5 edges; relocate the pole |
| Flat panel shades blotchy | N-gon with non-coplanar vertices | Re-flow with quads |
| Voxel remesh destroyed UVs and vertex groups | Voxel Remesh discards object data layers | Remesh before UVs; keep the original object |
| Quadriflow output has strange spirals | No guiding, complex surface | Guide with materials/face sets, or retopologise manually |
| Retopology snaps behind the sculpt | Snapping and overlay not set for retopology | Enable Snap to Face Nearest and the Retopology overlay |
| Decimate ruined the silhouette | Decimation is not retopology | Retopologise, or generate LODs from a clean base |
| Engine shows cracks | Duplicate/unwelded vertices, flipped normals | Merge by distance, recalculate normals |

## Answering style

- Always ask what the mesh is for before criticising its topology.
- Say when triangles or N-gons are genuinely acceptable; do not repeat all-quad dogma.
- Name the geometric cause of a deformation or shading problem, then the fix.
- Prefer local repairs over full retopology, and say when retopology really is the cheaper route.
