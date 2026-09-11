# Generators, curves and zones

## Curve workflows

The most productive corner of Geometry Nodes. Core chain:

```
Curve (input or Curve Line/Circle/Quadratic Bezier) > Resample Curve > Curve to Mesh
                                                                          ^
                                                             Profile curve (Circle, Quadrilateral, custom)
```

| Node | Use |
| --- | --- |
| Curve to Mesh | Sweeps a profile along a curve - pipes, cables, rails, ropes, roads |
| Resample Curve | Controls segment count (Count, Length, or Evaluated) |
| Curve to Points | Points along a curve for instancing (fence posts, lights, sleepers) |
| Fill Curve / Grid Fill | Caps a closed curve into a face |
| Curve Tangent / Normal / Parameter | Fields for orientation and gradients along the curve |
| Trim Curve | Cuts a curve by factor or length - growth animation |
| Set Curve Tilt / Radius | Twist and taper along the length |
| Curve of Point / Endpoint Selection | Selecting parts of splines |
| Mesh to Curve / Curve to Mesh | Round-tripping edges and splines |
| Subdivide Curve / Smooth by Angle | Density and smoothing |

Recipes:

| Goal | Chain |
| --- | --- |
| Cable or pipe | Curve > Resample > Curve to Mesh with a Circle profile; Set Curve Radius for taper |
| Fence | Curve > Resample (by Length) > Instance on Points (post); plus Curve to Mesh for rails |
| Road | Curve > Curve to Mesh with a flat quad profile; store UVs from Curve Parameter |
| Rope | Multiple curves offset and twisted (Set Curve Tilt) then Curve to Mesh |
| Vine growth | Trim Curve driven by Scene Time or a value; instance leaves on the remaining points |
| Railing | Curve to Mesh for the handrail plus Curve to Points for balusters |
| Chain | Curve to Points plus alternating rotated link instances via Index and a modulo |

## Mesh generation nodes

| Node | Use |
| --- | --- |
| Extrude Mesh | Extrude points, edges or faces, with per-element offset and selection |
| Subdivide Mesh / Subdivision Surface | Density and smoothing |
| Dual Mesh | Turns faces into vertices - hex grids from triangles, Voronoi-like panels |
| Mesh Boolean | Difference, union, intersect; slow on dense geometry |
| Split Edges / Merge by Distance | Topology cleanup inside a tree |
| Scale Elements | Scale faces or edges individually - panel insets |
| Triangulate | Prepare for export or specific effects |
| Mesh to Points / Points to Vertices | Convert between representations |
| Mesh to Volume / Volume to Mesh | Remesh-like effects, metaball fusion |
| Set Position | The universal deformer: displace by noise, textures, proximity or math |
| Set Shade Smooth | Shading control on generated faces |

A standard procedural panelling pattern: `Grid > Dual Mesh > Scale Elements (per-face, random) >
Extrude Mesh (per-face, random offset) > Set Shade Smooth (off)`.

## Zones

| Zone | Introduced | Use |
| --- | --- | --- |
| Simulation Zone | 3.6 | State carried frame to frame: growth, physics-like behaviour, accumulation |
| Repeat Zone | 4.0 | Fixed iteration counts: fractals, stacking, iterative subdivision |
| For Each Geometry Element Zone | 4.3 | Per-element processing with independent geometry per element |

Zone practices:

- Keep iteration counts low while building; raise them at the end.
- Simulation zones depend on playback from the start frame; scrubbing backwards gives wrong states.
- Bake simulation zones (the modifier's bake controls) before rendering an animation, so frames are
  deterministic.
- Repeat zones multiply cost linearly: 50 iterations of a heavy branch is 50x the work.
- For Each Element is powerful and expensive; prefer field-based solutions when they express the same
  thing.

Newer releases continue to add node-group capabilities (gizmos for in-viewport controls, bundles and
closures for richer group interfaces). Check the release notes of the version in use before promising
a feature exists.

## Node groups and exposed controls

1. Select the working part of the tree and press Ctrl+G to group it.
2. In the group's interface panel, set socket types, min/max, defaults, subtypes (distance, angle,
   factor) and descriptions.
3. Order inputs by importance; group them into panels where the version supports it.
4. Name the group for what it does (`GN_Scatter_Forest`, not `NodeGroup.003`).
5. Keep single-purpose groups and compose them, rather than one giant tree.
6. Mark reusable groups as assets so they appear in the asset browser for other files.

A generator is finished when someone else can drive it with only the exposed inputs.

## Node tools

Since Blender 4.0, a geometry node group can be a **tool**: it runs on the selected geometry in edit
mode like a built-in operator.

- Set the group's type to Tool; it then receives the edit-mode selection.
- Useful for repeatable modelling operations: custom bevel patterns, panel cuts, symmetry helpers,
  batch selections.
- Tools can be assigned to menus and shortcuts, and shipped as assets.
- Tools run destructively on the mesh, unlike modifier node trees.

## Materials and UVs on generated geometry

- Use **Set Material** inside the tree, on the relevant selection, before joining streams.
- Material Index is a face attribute; you can set it per face with a selection.
- Generated geometry has no UVs unless you create them: store a Vector attribute on the face-corner
  domain, or derive UVs from Curve Parameter and a cross-section coordinate for swept meshes.
- For shading, read named attributes in the shader with the Attribute node - the standard route for
  procedural masks and per-instance randomness.

## Generator checklist

1. Built from small, named node groups.
2. Inputs exposed with sensible defaults, ranges and subtypes.
3. Curve-based where a path drives the shape.
4. Materials set inside the tree.
5. UVs authored if the asset will be textured.
6. Zone iteration counts and simulation bakes handled.
7. Tested on more than one input shape before being called reusable.
