# Mesh cleanup and diagnostics

## The five-minute cleanup pass

Run this before judging any mesh, and before UVs, baking, rigging or export:

1. **Merge by Distance** - Edit mode, A, M > By Distance (0.0001-0.001 m). Reports how many were
   merged.
2. **Recalculate Normals Outside** - Shift+N. Check with the Face Orientation overlay (blue = out,
   red = flipped).
3. **Delete interior faces** - Select > All by Trait > Interior Faces, then X > Faces.
4. **Delete loose geometry** - Select > All by Trait > Loose Geometry, then delete.
5. **Check non-manifold** - Select > All by Trait > Non Manifold (in vertex or edge mode).
6. **Degenerate geometry** - Mesh > Clean Up > Degenerate Dissolve removes zero-area faces and
   zero-length edges.
7. **Statistics overlay** - verify vertex, face and triangle counts are in the range you expect.

Mesh > Clean Up also offers Decimate Geometry, Delete Loose, Limited Dissolve, Make Planar Faces,
Split Non-Planar Faces and Fill Holes - all useful, all destructive, so save a version first.

## Non-manifold geometry

Non-manifold means the surface could not exist as a real solid. Common forms:

| Form | Description | Consequence |
| --- | --- | --- |
| Boundary edge | Edge with one face (a hole) | Boolean failures, print failures, light leaks |
| Wire edge | Edge with no faces | Export garbage, selection confusion |
| T-junction | Edge shared by 3+ faces | Shading errors, boolean chaos |
| Interior face | Face inside the volume | Bake errors, wasted triangles, black patches |
| Zero-area face | Degenerate face | Normal and bake artifacts |
| Duplicate vertices | Unwelded seam | Faceted shading, cracks in engines |
| Inverted normals | Face pointing inward | Black facets, wrong boolean results |

Non-manifold matters for booleans, 3D printing, volumetric effects and baking. For a plain rendered
surface with no cuts, a boundary edge is often harmless - judge by purpose.

## Overlays and analysis tools

| Tool | Reveals |
| --- | --- |
| Face Orientation overlay | Flipped normals (red) |
| Statistics overlay | Vert/edge/face/tri counts, selected counts |
| Wireframe overlay on shaded view | Which geometry causes an artifact |
| Chrome / reflective matcap | Shading smears, dents, pinching |
| Mesh Analysis (Overlay > Mesh Analysis) | Overhang, thickness, intersections, distortion, sharpness - aimed at 3D printing but useful generally |
| 3D-Print Toolbox add-on | Manifold, thin walls, sharp angles, overhangs, volume, with one-click select of offenders |
| Edit-mode Select All by Trait | Non-manifold, loose, interior, faces by sides |
| Select Faces by Sides | Find all triangles or all N-gons instantly |

## Finding specific problems fast

| Goal | Method |
| --- | --- |
| Find all N-gons | Select > Select All by Trait > Faces by Sides > Greater Than 4 |
| Find all triangles | Faces by Sides > Equal To 3 |
| Find high-valence poles | Select Similar (Shift+G) by amount of connecting edges, from a known pole |
| Find hidden duplicate vertices | Merge by Distance and read the reported count |
| Find holes | Select > All by Trait > Non Manifold, edge mode |
| Find inverted normals | Face Orientation overlay |
| Find long thin faces | Mesh Analysis > Distortion, or visual scan with wireframe |
| Find unapplied scale | N-panel, or Object > Apply > Scale and watch dimensions |

## Reading the statistics

- Compare **triangle** count, not face count, when talking budgets - a quad is two triangles, an
  N-gon is unpredictable.
- A sudden count jump after a boolean or bevel is a warning, not a success.
- For real-time work, note that UV seams, sharp edges and material boundaries split vertices at
  render time, so the engine's vertex count exceeds Blender's. Fewer seams and fewer sharp edges mean
  fewer real vertices.

## Repair recipes

| Problem | Repair |
| --- | --- |
| Holes in a mesh that should be solid | Select boundary (Select > All by Trait > Non Manifold), F to fill, then re-flow, or Mesh > Clean Up > Fill Holes |
| Faceted shading on a smooth surface | Merge by Distance, then Shade Auto Smooth |
| Black faces in render | Recalculate normals outside; if mixed, check for interior faces |
| Boolean-mangled seam | Dissolve stray edges, merge by distance, rebuild the corner by hand |
| Scan mesh with noise and holes | Voxel Remesh to close it, then retopologise key areas |
| CAD import with millions of triangles | Decimate Planar, then manual cleanup of visible edges |
| Mesh with mixed normals after mirroring | Apply scale, then Shift+N |
| Cracks appearing only in the engine | Unwelded vertices at the seam, or a normals export setting |

## Pre-handoff checklist

1. Merge by Distance run, count noted.
2. Normals recalculated; Face Orientation clean.
3. No interior faces, loose geometry or zero-area faces.
4. Non-manifold checked; remaining cases justified by purpose.
5. N-gon and triangle counts known and appropriate.
6. Triangle count within budget.
7. Scale applied, transforms sane.
8. Chrome matcap inspection done at grazing angles.
