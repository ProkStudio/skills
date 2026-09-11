# Booleans and cutters

## Solvers

| Solver | Behaviour | Use |
| --- | --- | --- |
| Exact | Robust, handles coplanar faces and complex intersections, slower | Default choice |
| Fast | Quicker, fails on coplanar and near-degenerate geometry | Heavy meshes where Exact stalls |

Exact solver options worth knowing:

- **Self Intersection**: needed when the operand intersects itself; slower but fixes many failures.
- **Hole Tolerant**: helps when the input is not perfectly closed, at a performance cost.

## Requirements for a reliable boolean

1. **Both meshes should be manifold and closed.** Open edges produce holes and spikes.
2. **No coplanar faces.** Offset the cutter by a fraction of a millimetre so the surfaces are not
   exactly flush.
3. **The cutter must fully pass through** the target when cutting a hole - do not end a cutter exactly
   on the surface.
4. **No doubled vertices** in either mesh. Merge by Distance first.
5. **Consistent normals**, all facing outward, on both meshes.
6. **Reasonable density.** A 200k-triangle cutter against a 5-poly plane is asking for trouble.

## Cutter organisation

- Keep all cutters in a dedicated collection (`x_cutters/`), excluded from renders and from the view
  layer when not in use.
- Name cutters after what they do: `x_cut_vent_a`, `x_cut_screwhole_01`.
- Display cutters as Wire or Bounds so they do not obscure the model.
- Keep the Boolean modifiers live as long as possible - a cutter you can move is worth far more than
  a hole you must rebuild.
- Use one cutter object containing many disjoint pieces (all the screw holes at once) to keep the
  modifier stack short.
- Cutters can be linked duplicates: one vent shape reused twelve times updates everywhere.

## Typical boolean uses

| Goal | Setup |
| --- | --- |
| Round hole | Cylinder cutter, Difference, passing fully through |
| Panel line | Thin box or extruded profile, Difference, 1-2 mm deep |
| Inset plate | Duplicate the surface region, solidify, Union or Difference |
| Vent slots | One cutter object with an array of slots |
| Trimmed intersection | Union of two masses, then clean the seam and bevel |
| Stamped text | Text object converted to mesh, solidified, Difference |

## Cleanup after a boolean

Boolean output is topologically ugly by design. Depending on the target:

- **Baking high-poly**: leave it. Nobody sees the topology; only the shading matters.
- **Subdivision or deformation**: the result is unusable as-is. Re-flow the intersection by hand, or
  retopologise (`../../blender-topology-and-retopology/SKILL.md`).
- **Real-time asset**: dissolve stray edges, merge by distance, remove interior faces, then check
  triangle count.

Standard cleanup sequence:

1. Merge by Distance (M > By Distance), threshold 0.0001-0.001 m.
2. Select All by Trait > Interior Faces, delete.
3. Recalculate Normals Outside (Shift+N).
4. Dissolve leftover edges that split flat surfaces pointlessly (X > Dissolve Edges).
5. Check Face Orientation overlay - no red faces.
6. Statistics overlay: verify the triangle count did not explode.

## Boolean failure diagnosis

| Symptom | Cause | Fix |
| --- | --- | --- |
| Nothing happens | Cutter not intersecting, or wrong operation | Check overlap and Difference/Union/Intersect |
| Hole punched through the wrong side | Cutter normals inverted | Recalculate normals on the cutter |
| Spikes or stray faces at the cut | Non-manifold input, doubled verts | Merge by distance, close the mesh |
| Whole face disappears | Coplanar faces | Offset the cutter by 0.0001-0.001 m |
| Jagged, stair-stepped cut | Low-resolution cutter on a curved surface | Increase cutter segments |
| Extremely slow | Exact solver on dense meshes, Self Intersection on | Decimate the cutter, or switch to Fast |
| Bevel breaks after the boolean | N-gons and tight angles at the seam | Clean the seam, reduce bevel segments |
| Shading dents around a hole | Long thin triangles radiating from the hole | Add a surrounding loop, or re-flow the area |

## Alternatives to booleans

| Instead of | Consider |
| --- | --- |
| Cutting a hole in a subdivision cage | Modelling the hole with quads and support loops |
| Boolean panel lines on a deforming mesh | Modelled insets, or a baked normal/height map |
| Boolean text | A decal, or baked height detail |
| Dozens of boolean screw holes on a low-poly | Floater geometry baked into the normal map |
| Boolean to trim a silhouette | Bisect (Ctrl+R / Bisect tool) with Clear Inner/Outer |

For real-time assets especially, the cheapest hole is often no hole: model the surface flat and bake
the detail (`../../blender-uv-and-baking/references/baking-recipes.md`).
