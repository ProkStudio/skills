# Seams and unwrapping

## Where seams belong

Rank candidate edges by how well they hide a break:

1. **Hard edges and silhouette corners** - a 90-degree corner hides a seam almost perfectly.
2. **Material or colour boundaries** - the texture already changes there.
3. **Concave creases and inner corners** - light rarely hits them.
4. **Undersides, backs, and areas the camera never sees.**
5. **Natural breaks in the subject**: panel gaps, garment seams, hairlines, joint creases.

Avoid seams:

- Across large flat lit surfaces.
- Straight through a face's features or the centre of a character's front.
- In deformation zones on characters, where stretching exposes the break.
- Where a tiling pattern must continue unbroken.

Per asset type:

| Asset | Typical seam plan |
| --- | --- |
| Box-like prop | Seams on all hard corners; unfold like a cardboard box |
| Cylinder / pipe | One seam along the length on the hidden side, plus caps |
| Character body | Inside legs and arms, under the chin/back of head, around joints, centre back |
| Head | Behind the ears, along the hairline, back of the neck; keep the face one island |
| Clothing | Follow real garment seams |
| Hard-surface machine | Per-part islands, following manufactured panel splits |
| Terrain / walls | Grid-aligned strips for tiling, or trim-sheet UVs |

## Seams and hard edges

For normal baking, the rule is: **every hard (sharp) edge should be a UV seam.** If a hard edge is
not split in UV space, the baker cannot store the normal discontinuity and you get gradient smearing
and visible shading errors.

The reverse is a good default too: mark UV seams as sharp. Extra seams cost split vertices, so keep
them purposeful. Blender's Edge > Mark Sharp and UV > Mark Seam are separate attributes - set both.

## Unwrap methods

| Method | Behaviour | Use |
| --- | --- | --- |
| Unwrap - Angle Based | Balances angle distortion; the default | General purpose, organic and hard surface |
| Unwrap - Conformal | Minimises overall stretch, can twist islands | Simple islands, when Angle Based skews |
| Unwrap - Minimum Stretch | Newer solver aimed at reducing stretch overall | Dense organic islands where stretch matters most |
| Smart UV Project | Automatic seams by angle threshold | Bake-only high-polys, blockouts, quick props |
| Follow Active Quads | Continues a quad grid from an active face | Pipes, roads, cloth strips, anything grid-like |
| Cube / Cylinder / Sphere Projection | Primitive projections | Boxes, pipes, domes |
| Lightmap Pack | Packs every face with padding | Lightmap UV channels |
| Project From View | Uses the current camera view | Decals, planar surfaces, matte-painting style |

Angle Based is the right default. Smart UV Project is a fine tool for meshes nobody will texture by
hand - it is a poor choice for hero assets because its islands are fragmented.

## Checking distortion

1. Assign a **checker texture** (UV Grid or Color Grid from the image new-texture presets) and look
   for squares that are not square.
2. Use the UV editor's **Display Stretch** overlay (area or angle) - blue is good, red is distorted.
3. Compare squares across the whole asset to eyeball consistent texel density.
4. Rotate around the model in Material Preview; distortion shows up in motion more than in stills.

Fixes for distortion:

- Add a seam so the island can flatten.
- Use UV > Relax (Minimize Stretch, or Loop Tools/UVPackmaster-style relax) with pinned boundaries.
- Pin (P) key vertices and re-unwrap so the solver respects them.
- Split a cone or dome into segments instead of forcing one island.

## Straightening and cleanup

| Operation | Use |
| --- | --- |
| UV > Align / Straighten | Make an island's edge perfectly horizontal or vertical |
| Follow Active Quads | Build a straight grid along a strip |
| Pin (P) / Unpin (Alt+P) | Lock vertices before re-unwrapping |
| Live Unwrap | Re-unwrap continuously while moving pinned points |
| UV > Average Islands Scale | Equalise texel density across islands |
| Select Similar / Select Split | Manage islands quickly |
| Snap to pixel / Rip & Weld (V / Alt+M) | Fine layout control |

Straight islands matter for: trims and tiling textures, hand-painted details, text and decals,
anything read at a glance. Organic islands rarely need straightening.

## Layout patterns

- **One island per logical part** for hard surface; easier to texture, easier to bake.
- **Symmetry**: mirror halves can share UV space (overlapping) to double effective resolution - but
  only if baked lighting or unique detail is not required. For mirrored islands, offset them by one
  UV tile so bakers treat them correctly.
- **Grouping**: keep islands of the same material adjacent; it makes masking and hand-painting sane.
- **Orientation**: keep the up direction of the asset consistent across islands so gradients and
  directional textures work.

## Multiple UV channels

- UV maps are per-mesh data layers; a mesh can have several.
- Common setups: channel 1 = main texture UVs; channel 2 = lightmap UVs (non-overlapping, padded);
  channel 3 = detail/tiling UVs or decal projection.
- Engines reference channels by index or name - keep names identical across assets
  (`UVMap`, `UVLightmap`) or the importer picks the wrong one.

## Unwrap checklist

1. Topology final before unwrapping.
2. Seams placed on hidden, hard, or material-boundary edges.
3. Every sharp edge is a seam.
4. Checker texture shows square squares everywhere that matters.
5. Islands straightened where direction matters.
6. Average Islands Scale applied, then density verified against the project standard.
7. Mirrored/overlapping islands handled deliberately, offset by a tile if needed.
8. UV channel names consistent.
