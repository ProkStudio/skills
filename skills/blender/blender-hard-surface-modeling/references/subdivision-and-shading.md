# Subdivision, normals and shading artifacts

## Subdivision cage rules

Subdivision Surface (Catmull-Clark) smooths a control cage. The cage decides everything:

- **All quads.** Triangles and N-gons subdivide into irregular patches and show as dents.
- **Even quad proportions.** Very long thin quads produce visible stretching on curved surfaces.
- **Poles**: vertices where an unusual number of edges meet. 3- and 5-edge poles are normal and
  unavoidable; 6+ poles pinch badly. Keep poles on flat areas, never on a curved highlight.
- **Loops must be continuous.** A support loop that ends mid-surface creates a pole exactly where it
  terminates.
- **Corner handling**: three loops meeting at a corner is fine; stacked loops within a fraction of a
  millimetre are not.

Settings:

- Viewport levels 1-2, Render levels 2-3. Higher is rarely visible and always slower.
- Use Optimal Display to see the cage rather than the subdivided wireframe.
- Limit Surface off/on affects how the cage displays in edit mode; it does not change the render.

## Smooth shading and normals

Blender 4.1 removed the old mesh **Auto Smooth** checkbox. The current workflow:

- **Object > Shade Smooth** makes everything smooth.
- **Object > Shade Auto Smooth** adds a **Smooth by Angle** modifier (a geometry-nodes based
  modifier) with an angle threshold - edges sharper than the angle render as hard.
- **Shade Flat** per face, or the **Sharp** edge attribute, marks specific edges hard.
- Custom split normals from imported files still exist and can be cleared with Mesh > Normals >
  Clear Custom Split Normals Data.

On older files and tutorials, "enable Auto Smooth at 30 degrees" means "Shade Auto Smooth with a 30
degree angle" in 4.1 and later.

**Weighted Normal** modifier (needs smooth shading and Keep Sharp) redistributes normals by face
area, which removes most gradient artifacts on bevelled hard-surface models. It is the standard
finishing touch for bevel-only workflows, and must sit after Bevel in the stack.

**Harden Normals** inside the Bevel modifier achieves something similar for the bevel faces only; do
not enable both blindly - test which one gives a cleaner result on your mesh.

## Checking shading properly

Solid grey viewport hides everything. Check with:

1. **A reflective matcap** (Viewport Shading > Matcap, chrome or reflective one). Smears and dents
   become obvious.
2. **A glossy material** in rendered view, with an HDRI that has bright shapes in it.
3. **Wireframe overlay** over the shaded surface, to see which geometry causes an artifact.
4. **Face Orientation overlay** for inverted normals (red = flipped).
5. **Statistics overlay** to catch geometry explosions.
6. **Grazing angles**: rotate the view until light skims the surface; that is where flaws show.

## Artifact diagnostic table

| Artifact | Geometric cause | Fix |
| --- | --- | --- |
| Dark smudge along an edge | Bevel wider than nearby geometry allows, overlapping bevel | Reduce width, enable Clamp Overlap, add space |
| Dent or pucker at a point | High-valence pole (6+) | Re-flow to 4-5 edges per vertex; move the pole off the highlight |
| Wavy highlight on a flat panel | Non-planar quads | Flatten the face (S, Z, 0 on axis) or triangulate the area |
| Blotchy patches on a flat surface | N-gon with vertices not coplanar | Re-flow with quads, or add support loops |
| Triangular shading dent next to a hole | Long thin triangles fanning from the hole | Add a circular support loop around the hole |
| Hard seam where shading should be smooth | Sharp edge marked, or split normals present | Clear sharp/split normals, adjust the smooth angle |
| Black facets in render | Inverted normals | Shift+N recalculate outside |
| Faceted look despite smooth shading | Duplicate vertices splitting the surface | Merge by Distance |
| Pinching after subdivision | Support loops too close, or loops crossing | Space loops, keep loops continuous |
| Surface visibly stretched | Extremely elongated quads | Add loops to even out proportions |
| Shading breaks only after mirroring | Negative scale | Apply scale, recalculate normals |
| Edges look soft in the engine but sharp in Blender | Custom normals or smooth angle not exported | Check export normals settings (`../../blender-to-engine-export/SKILL.md`) |

## Choosing your workflow

| Workflow | Cage | Edge sharpness | Best for |
| --- | --- | --- | --- |
| Subdivision | All quads, low density, support loops | Loops or creases | Organic-mechanical hybrids, hero renders, anything that deforms |
| Bevel-only + weighted normals | Any reasonable quad/tri mix | Bevel modifier, 1-2 segments | Real-time assets, fast iteration, boolean-heavy design |
| High-poly for baking | Whatever shades correctly | Bevel or subdivision, heavy | Normal-map source for a low-poly |

Do not mix mindlessly: a boolean-heavy mesh with N-gons will never subdivide cleanly, and a
subdivision cage is a poor real-time asset without retopology or decimation.

## Final shading checklist

1. All quads where subdivision is used.
2. No poles above 5 edges on curved surfaces.
3. All flat faces genuinely planar.
4. Normals recalculated outside; Face Orientation clean.
5. No duplicate vertices.
6. Smooth by Angle or Weighted Normal configured, not both fighting each other.
7. Verified with a chrome matcap at grazing angles.
