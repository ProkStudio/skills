# Brushes, masking and filters

## Brush organisation in recent versions

From Blender 4.3 onward, brushes are **assets**: they live in asset libraries and appear in the asset
shelf instead of a fixed brush list. Practical consequences:

- Custom brushes are saved as assets and reused across files.
- Older tutorials referring to a brush dropdown map to the asset shelf.
- Per-brush settings (strength, radius, falloff, alpha, stroke method) work the same as before.

Always-relevant modifiers on any brush: Ctrl inverts the effect, Shift temporarily switches to
Smooth, F sets radius, Shift+F sets strength, and the stroke method (Space, Dots, Drag Dot,
Anchored, Airbrush, Curve) changes behaviour more than most people expect.

## Primary-form brushes

| Brush | Behaviour | Typical strength |
| --- | --- | --- |
| Grab | Moves geometry like clay, no falloff on the grabbed island | 1.0 |
| Elastic Deform | Volume-preserving push/pull, great for big organic moves | 0.5-1.0 |
| Snake Hook | Pulls out new forms - horns, tentacles, hair strands | 0.5-0.8 |
| Draw Sharp | Cuts sharp creases and indents | 0.3-0.6 |
| Clay Strips | Builds mass in flat slabs; the workhorse of blocking | 0.4-0.7 |
| Clay | Softer mass building | 0.4-0.6 |
| Inflate | Adds volume along normals | 0.2-0.4 |
| Pose | Rotates a limb from a virtual pivot, for reposing | 1.0 |
| Boundary | Deforms along an open boundary (bends a plane's edge) | 0.5-1.0 |

## Secondary-form and refinement brushes

| Brush | Behaviour | Typical strength |
| --- | --- | --- |
| Flatten | Averages toward a plane - defines facets | 0.3-0.6 |
| Scrape / Fill | Cuts below / fills above the plane | 0.3-0.6 |
| Multiplane Scrape | Scrapes two planes at once, leaving a crisp ridge | 0.4-0.7 |
| Crease | Pinches and pulls in, for creases and seams | 0.3-0.6 |
| Pinch / Magnify | Draws geometry toward the stroke - sharpens edges | 0.2-0.5 |
| Blob | Inflates spherically, for fat and lumps | 0.3-0.5 |
| Layer | Raises a constant-height plateau, good for panels and patches | 0.3-0.6 |
| Nudge | Slides surface detail sideways | 0.5 |
| Slide Relax | Slides vertices to relax topology without changing form | 0.3-0.5 |
| Smooth | Averages - use sparingly | 0.2-0.5 |
| Rotate | Twists the masked/unmasked region | 0.5 |

## Detail brushes

| Brush | Use |
| --- | --- |
| Draw with an alpha texture | Pores, scales, fabric weave, stamped detail |
| Draw Sharp with small radius | Fine wrinkles, cracks, stitch lines |
| Crease at low strength | Skin folds, cloth seams |
| Clay Strips at small radius | Layered wrinkles that read as volume, not scratches |
| Cloth brush | Fabric folds simulated locally, with pinning |
| Mask + Mesh Filter > Inflate | Raised patches, blisters, panel offsets |
| Paint brush (Color Attribute) | Blocking colour directly on the sculpt |

Texture and alpha tips: set the texture mapping to **Area Plane** or **Random** rather than Tiled to
avoid a visible grid, and vary rotation. Uniform alpha tiling is the most recognisable form of
artificial detail.

## Masking

| Action | How |
| --- | --- |
| Paint a mask | Mask brush (M in the default keymap) |
| Box / Lasso mask | Box Mask and Lasso Mask tools |
| Invert mask | Ctrl+I |
| Clear mask | Alt+M |
| Smooth / sharpen / grow / shrink mask | Mask menu, or Mask Filter |
| Mask by cavity | Mask menu > Mask by Cavity - isolates crevices |
| Mask from Face Set | Face Sets menu |

**Auto-masking** (in the brush settings) is the underused power feature:

- **Topology**: affects only the connected island under the cursor - stops the brush grabbing the
  other side of a thin form.
- **Face Sets**: confines the stroke to the Face Set under the cursor - the cleanest way to sculpt
  hard boundaries.
- **Boundary edges / Face Set boundary**: fades the effect near boundaries.
- **Cavity**: limits the stroke to concave or convex areas - excellent for wear and grime-like
  detail.
- **View Normal / Occlusion**: limits to surfaces facing the view.

## Face Sets

- Face Sets are named regions of the sculpt: like polygroups, they drive visibility, masking and
  some brushes.
- Create with the Draw Face Sets brush, or generate from masks, boundaries, materials or topology
  (Face Sets menu > Init Face Sets).
- Use them to: isolate a body part (hide the rest), constrain brushes with auto-masking, extract a
  piece of geometry (Face Set Extract), or keep hard boundaries crisp.
- Face Sets survive Voxel Remesh reprojection, which makes them the safest organisational tool during
  a remesh-heavy sculpt.

## Filters

| Filter | Use |
| --- | --- |
| Mesh Filter > Smooth | Global smoothing at a controllable amount |
| Mesh Filter > Sharpen | Re-crisps detail after too much smoothing |
| Mesh Filter > Inflate / Scale | Global volume changes |
| Mesh Filter > Relax Topology | Evens out geometry without changing shape |
| Mesh Filter > Random | Adds controlled surface noise |
| Cloth Filter | Simulates gravity, inflation, expansion over the whole mesh - fast cloth-like forms |
| Color Filter | Adjusts Color Attributes (hue, saturation, value) |

Filters respect masks, so mask first and filter second for local control without brush strokes.

## Symmetry and radial options

- Mirror X/Y/Z toggles in the top bar; Tiling and Radial options live in the Symmetry panel.
- **Radial symmetry** around an axis is how you sculpt rosettes, gears, shells and flowers.
- Symmetry is relative to the object origin, and to local axes - apply rotation if it mirrors
  diagonally.

## Brush selection cheat sheet

| Goal | Brush |
| --- | --- |
| Move a whole form | Elastic Deform or Grab |
| Build up mass | Clay Strips |
| Define a flat plane | Flatten, then Scrape |
| Sharpen an edge or ridge | Pinch, Multiplane Scrape, Crease |
| Pull out a horn | Snake Hook, then remesh |
| Cut a crease | Draw Sharp inverted, or Crease |
| Even out lumps | Mesh Filter > Smooth at low strength, not brush spam |
| Reposition a limb | Pose brush |
| Add fabric folds | Cloth brush or Cloth Filter |
| Add pores/scales | Draw with an alpha, Area Plane mapping |
| Fix over-smoothed detail | Mesh Filter > Sharpen, then rebuild planes |
