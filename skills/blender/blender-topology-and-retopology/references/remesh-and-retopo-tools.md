# Remeshing, retopology and reduction

## Choosing a route

| Situation | Route |
| --- | --- |
| Continue sculpting, need even density | Voxel Remesh |
| Need a quad base for Subdivision or Multires | Quad Remesh (Quadriflow) |
| Character or anything that deforms | Manual retopology |
| Real-time asset with a triangle budget | Manual retopology, or a clean base plus LODs |
| Scan or CAD import to clean up | Remesh, then manual repair of key areas |
| Just needs fewer triangles for a background prop | Decimate |
| 3D print, watertight required | Voxel Remesh |

## Voxel Remesh

Blender's Voxel Remesh rebuilds the surface from a volume:

- Produces a **manifold** (watertight) mesh with even density - ideal for continuing a sculpt or for
  printing.
- Output is mostly quads in a grid pattern that ignores the form's flow: it is **not** good
  deformation topology.
- **Discards object data layers** - UV maps, vertex groups, custom normals are lost. Remesh before you
  invest in UVs.
- Can reproject **Face Sets** and **Color Attributes**, so sculpt organisation and painted colour can
  survive.
- Controlled by Voxel Size (smaller = more detail and much heavier) and Adaptivity (reduces density
  on flat areas). Shortcut in sculpt mode: Ctrl+R with a preview of voxel size.
- Good at fixing intersecting and overlapping geometry, because it only cares about the volume.

## Quad Remesh (Quadriflow)

- Field-aligned quad remesher: slower than voxel, but much better quality output.
- Produces few poles and loops that broadly follow curvature - a good base for Subdivision or
  Multires.
- **Not** intended for cleaning intersecting geometry (use Voxel for that first).
- **Not** recommended as final topology for a deforming character: it does not know where your joints
  or expression lines are.
- Can produce strange spiral loop patterns on complex surfaces without guidance; guiding by material
  or symmetry options helps.
- Options include target face count/edge length, symmetry axes, and preserving sharp edges - test the
  presets, results vary greatly per mesh.

## Remesh modifier

- Does voxel-style remeshing non-destructively in the stack (Voxel, Blocks, Smooth, Sharp modes).
- Useful for procedural or iterative work where you want to keep the source shape editable.
- Same caveat: the result's topology serves shape, not deformation.

## Third-party auto-retopology

- **Quad Remesher** (Exoside) is a paid add-on that produces noticeably better field-aligned quads
  than Quadriflow, with edge-guide and density-painting control. It is the practical choice for
  studios doing heavy retopology.
- Automatic tools still do not place deformation loops. For hero characters, manual retopology or
  heavy manual correction remains standard.

## Manual retopology toolkit

| Tool | Use |
| --- | --- |
| Poly Build tool | Click to place quads directly on the surface; the core retopology tool |
| Extrude + snapping | Build strips of quads along forms |
| Snap: Face Nearest | Snapping mode that keeps new vertices glued to the reference surface, even when moved |
| Snap: Face with Project Individual Elements | Older workflow; projects vertices onto the surface |
| Retopology overlay | Draws the retopo mesh in front of the reference so it does not z-fight |
| Shrinkwrap modifier | Keeps a whole low-poly mesh stuck to the high-poly while you edit |
| Mirror modifier with clipping | Retopologise one half only |
| Grid Fill / Bridge Edge Loops | Close large regions quickly |
| Loop Tools > Relax | Even out a patch after rough placement |

A practical manual retopology setup:

1. High-poly in its own collection, selectable but not editable; set to display as solid.
2. New empty mesh object, Mirror modifier (with clipping) plus Shrinkwrap targeting the high-poly.
3. Enable Snap to Face Nearest and the Retopology overlay.
4. Lay down the major loops first: silhouette, joints, eye and mouth rings, panel boundaries.
5. Fill the regions between them, keeping quads roughly even.
6. Apply Shrinkwrap at the end (or keep it live if the high-poly stays around).

Order of work: **define flow, then fill.** Retopologising by filling from a corner produces flow that
follows nothing.

## Reduction: decimate and LODs

| Decimate mode | Behaviour | Use |
| --- | --- | --- |
| Collapse | Ratio-based edge collapse; makes triangles | Background props, LOD2+ |
| Un-Subdivide | Reverses subdivision steps; keeps quads | Meshes that came from subdivision |
| Planar | Merges coplanar faces within an angle | Boolean-heavy hard surface, CAD cleanup |

- Decimate is reduction, not retopology: the flow is gone, deformation is compromised, UVs distort.
- For LODs, decimate from a clean base mesh, verify the silhouette at the distance the LOD appears,
  and keep UV seams intact (enable Preserve UV boundary-type options where available).
- Typical LOD ratios: LOD1 at 50-60%, LOD2 at 25-30%, LOD3 at 10-15% of LOD0 triangles.

## Triangulation for export

- Engines triangulate on import anyway, but doing it yourself makes the result deterministic and
  matches what you baked against.
- Prefer the exporter's triangulation option, or a Triangulate modifier at the very bottom of the
  stack, so the editable mesh stays quads.
- Beauty method gives nicer triangles for shading; Fixed is predictable. Keep N-gons out first -
  triangulating an N-gon is where surprise shading comes from.

## Retopology checklist

1. Purpose decided before choosing a method.
2. Original high-poly kept untouched in its own collection.
3. Voxel remesh done before UVs, never after.
4. Quadriflow output reviewed for spirals and pole placement.
5. Deformation loops placed manually, whatever tool generated the base.
6. Density appropriate to camera distance and budget.
7. Triangulation handled at export, not in the working mesh.
