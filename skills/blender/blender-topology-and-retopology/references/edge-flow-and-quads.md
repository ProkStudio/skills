# Edge flow, faces and poles

## Face types in context

| Face type | Subdivision | Deformation | Real-time render | Bake source |
| --- | --- | --- | --- | --- |
| Quad | Required | Required | Fine (triangulated anyway) | Fine |
| Triangle | Causes artifacts | Poor at bends | Native GPU primitive | Fine |
| N-gon | Unpredictable | Bad | Triangulated unpredictably | Fine on flat faces |

What this means in practice:

- The GPU renders triangles. A shipped game asset is all triangles regardless of how you modelled it.
- Triangles are harmless on a flat, static, non-subdivided surface. They are a problem on curvature,
  at deformation zones, and under subdivision.
- N-gons are fine as a temporary state and on truly flat faces, but they break bevels, subdivision
  and predictable triangulation. Do not ship them on curved surfaces.
- "All quads" is a means, not a goal. Chasing it on a bake-only high-poly is wasted effort.

## Loops and rings

- **Edge loop**: a continuous path of edges through 4-valence vertices. Select with Alt+click.
- **Face loop / edge ring**: the band of faces alongside a loop. Select with Ctrl+Alt+click.
- Loops let you select, scale and slide whole bands of geometry, which is why loop-based topology is
  fast to edit and triangle soup is not.
- A loop is broken by any pole it passes through - that is how you control where loops terminate.

Loop operations worth knowing:

| Operation | Shortcut | Use |
| --- | --- | --- |
| Loop Cut | Ctrl+R | Add a loop; scroll for multiple |
| Edge Slide | G, G | Move a loop along the surface |
| Bridge Edge Loops | Edge menu | Connect two open loops |
| Grid Fill | Face menu | Fill an even-numbered boundary with quads |
| Checker Deselect | Select menu | Remove every other loop to halve density |
| Dissolve Edges | X > Dissolve | Remove edges without leaving vertices |

## Poles and valence

Valence = number of edges meeting at a vertex.

| Valence | Name | Behaviour |
| --- | --- | --- |
| 3 | Triangle pole (E-pole) | Mild; common at corners and loop terminations |
| 4 | Regular | Ideal; loops pass through cleanly |
| 5 | Star pole (N-pole) | Acceptable; used to redirect flow |
| 6+ | High-valence pole | Pinches visibly under subdivision |

Rules for poles:

- You cannot avoid poles on a closed surface that changes loop direction. Plan them.
- Put poles on flat or low-curvature areas, hidden from key highlights.
- Never put poles inside a deformation zone (elbow crease, mouth corner, knee).
- Standard flow-redirection patterns use pairs of 3- and 5-poles; they are the vocabulary of clean
  topology.

## Loop termination patterns

When a detail area needs more density than its surroundings, terminate the extra loops deliberately:

- **Triangle-pair termination**: two triangles merged into a quad diamond, ending a loop on a flat
  surface.
- **Diamond/3-pole**: a quad rotated 45 degrees to absorb a loop.
- **Loop redirect (5-pole)**: turn a loop 90 degrees to follow a new form.
- Never let a loop simply stop mid-face: that leaves an N-gon or a T-junction, which is the classic
  source of shading dents.

## Density rules

1. **Density follows curvature.** Tight curves need more quads; flat areas need almost none.
2. **Density follows deformation.** Joints need loops even if the surface is smooth.
3. **Density follows camera distance.** A background asset can be a quarter of the resolution.
4. **Keep quads roughly square** in the areas that matter; long thin quads stretch shading and
   textures.
5. **Avoid sudden density jumps**; transition over 2-3 rows using termination patterns.

## Local re-flow recipes

| Problem | Recipe |
| --- | --- |
| N-gon on a curved surface | Delete the face, rebuild with quads using F and Grid Fill |
| Triangle in a deforming area | Merge it into a neighbour and re-route the loop |
| 6+ pole | Dissolve one of the edges into a neighbouring quad; often converts to a 5-pole plus 3-pole pair |
| Too much density in one patch | Checker Deselect on loops, then dissolve |
| Circular hole with a fan of triangles | Add a surrounding loop, then convert the fan to a quad ring |
| Two meshes to join | Bridge Edge Loops after matching vertex counts |
| Uneven loop spacing | Select loops, Mesh > Sort Elements or use Loop Tools > Space |

Loop Tools (bundled add-on) provides Circle, Relax, Space, Flatten and Bridge, which handle most
re-flow chores faster than doing it by hand.

## Review checklist

1. Face types appropriate to the mesh's purpose.
2. No loop terminating mid-face.
3. No pole above 5 edges on a visible curved surface.
4. No pole inside a deformation zone.
5. Quad proportions reasonable where curvature or texture matters.
6. Density transitions handled with termination patterns.
7. Subdivide-once test shows no pinching.
