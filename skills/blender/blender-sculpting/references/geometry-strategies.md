# Dyntopo, Multires and Voxel Remesh

Three ways to get resolution, with different trade-offs. Choosing wrongly costs hours.

## Comparison

| | Dyntopo | Multiresolution | Voxel Remesh |
| --- | --- | --- | --- |
| How it works | Adds/removes triangles under the brush | Subdivision levels on a clean base | Rebuilds the whole surface from a volume |
| Topology | Triangles, uneven | Quads inherited from the base | Even quad grid, ignores form flow |
| Needs a good base | No | Yes | No |
| Keeps low-res control | No | Yes - switch levels freely | No |
| Big shape changes | Good | Poor at high levels | Good (re-remesh as needed) |
| Free-form growth (horns, limbs) | Excellent | Impossible | Good with Snake Hook + remesh |
| Data layers (UVs, groups) | Lost/mangled | Preserved | Discarded |
| Bake to maps | Via retopo + bake | Bake from Multires directly | Via retopo + bake |
| Performance ceiling | Drops fast with fine detail | Best for very high detail | Heavy at small voxel sizes |
| Typical use | Exploration, creatures, concepting | Production characters, film detail | Sculpt cleanup, reshaping, printing |

## Dyntopo

- Toggle in sculpt mode (default keymap Ctrl+D) or from the Dyntopo panel.
- Detail types: **Relative** (screen-space, density depends on zoom), **Constant** (fixed world
  detail - most predictable), **Brush** (scales with brush size), **Manual** (only on flood fill).
- Detail Size is the main dial. Small values plus a large brush will destroy performance instantly.
- **Collapse Short Edges** keeps triangle counts sane; without it, density only grows.
- Detail Flood Fill re-tessellates the whole mesh to the current detail setting - useful, and
  destructive to finer detail.
- Key limitation: any stroke re-tessellates the area it touches at the current detail size, so
  coarse-detail strokes wipe out fine detail you already sculpted there.
- Dyntopo output is triangle soup. Fine for a bake source or a print, useless as final deforming
  topology.

## Multiresolution

- Add the Multires modifier, then Subdivide to create levels. Catmull-Clark for smooth, Simple to
  keep the base shape, Linear for straight subdivision.
- Sculpt at any level; changes at a low level propagate to higher ones, which is the whole point:
  fix proportions at level 1 with detail intact at level 5.
- Requires a clean, mostly-quad, evenly distributed base mesh. Triangles, N-gons and uneven density
  all show up amplified at high levels.
- **Apply Base** pushes low-level sculpt changes into the base mesh. **Rebuild Subdivisions** can
  reconstruct levels for a mesh whose base matches.
- Each level multiplies face count by 4: a 10k-quad base becomes 40k, 160k, 640k, 2.5M, 10M. Plan
  levels, do not add them reflexively.
- Sculpt detail can be baked out with the bake option for multires displacement, or by baking
  high-to-low in the usual way (`../../blender-uv-and-baking/SKILL.md`).
- Cannot grow new appendages; topology is fixed by the base.

## Voxel Remesh

- Sculpt mode: Ctrl+R remeshes; the interactive voxel-size gizmo (R in the default keymap) previews
  density.
- Produces a watertight manifold mesh of even density - excellent for continuing to sculpt and for
  3D printing.
- **Discards object data layers** (UV maps, vertex groups, custom normals), but can reproject **Face
  Sets** and **Color Attributes**.
- Adaptivity reduces density on flat regions; Fix Poles cleans up some pole artifacts.
- Ignores form flow, so it is never final deformation topology.
- Best at fixing self-intersections and overlapping geometry, because it only sees the volume.
- Voxel size is a real-world length: halving it roughly quadruples face count. 0.01 m on a human is
  already very heavy.

## A practical combined pipeline

1. Block out on a primitive; **Voxel Remesh** coarsely (large voxel size) each time you reshape.
2. Keep remeshing progressively finer as secondary forms appear.
3. When the form is settled and you want fine detail with the ability to go back, retopologise or use
   **Quad Remesh**, then add **Multires** and sculpt detail on levels.
4. Use **Dyntopo** only for exploratory growth or one-off bake sources.
5. Save a version before every remesh. Every one of them is destructive.

## Performance and limits

- Sculpting is CPU and RAM bound; the viewport draw cost dominates at high counts.
- Rough comfort zones on mainstream hardware: up to ~2M triangles is smooth, 5-10M is workable with
  care, 20M+ needs hiding, masking and patience.
- Ways to keep it fast:
  - Hide what you are not sculpting (Shift+H / Face Sets visibility).
  - Lower Multires viewport level while working; raise for detail passes.
  - Turn off overlays, shadows and cavity in the viewport; use a Matcap.
  - Use Constant detail in Dyntopo and enable Collapse Short Edges.
  - Split a complex character into separate objects (head, body, clothing, props).

## Cleanup tools during sculpting

| Tool | Use |
| --- | --- |
| Box / Lasso Trim | Cut away chunks of the sculpt directly, remeshing the cut |
| Line Project | Slice the sculpt flat along a line |
| Mask + Mesh Filter | Inflate, smooth, sharpen or relax only the unmasked area |
| Sculpt > Symmetrize | Force one side onto the other |
| Mesh Filter > Smooth / Sharpen | Global smoothing or sharpening without brush strokes |
| Simplify brush (Dyntopo) | Reduce local density without changing shape |
| Remesh modifier | Non-destructive voxel remesh when you need the source kept |

## Strategy checklist

1. Purpose known (render / game / print / bake source).
2. Strategy chosen deliberately, not by habit.
3. Version saved before each remesh or Apply Base.
4. Multires base mesh is clean quads with even density.
5. Dyntopo detail set to Constant with Collapse Short Edges when used.
6. Triangle count within the machine's comfort zone.
7. UVs and vertex groups created **after** all remeshing, never before.
