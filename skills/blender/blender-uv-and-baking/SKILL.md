---
name: blender-uv-and-baking
description: Unwrap UVs and bake maps in Blender so textures land at the right density and bakes come out clean. Use whenever the user asks where to put UV seams, which unwrap method to use, how to fix stretched or distorted UVs, how to pack or pin a UV layout, what texel density is and how to keep it consistent, how many texture sets or UDIM tiles to use, how to bake a high-poly onto a low-poly, how to bake normal ambient occlusion curvature or ID maps, what a cage and ray distance do, why a bake has black spots seams skewed detail or wavy artifacts, or which normal-map convention an engine expects. Covers seam placement logic, Smart UV Project versus Angle Based versus Conformal unwrapping, checker and stretch checking, packing and margins, the texel density formula with worked examples, atlases trim sheets and UDIM, Selected to Active baking, cage and extrusion setup, bake margin and padding, tangent versus object space and green channel direction, plus a full bake artifact diagnostic table.
version: 1.0.0
---

# UVs and baking

UVs decide how much texture resolution every surface gets and where the texture breaks. Baking
transfers detail from a heavy mesh onto a light one. Both are mechanical crafts with clear rules -
nearly every "weird texture" problem traces back to one of them.

## When to use

- Unwrapping any model that will be textured.
- Fixing stretched, rotated, overlapping or wasteful UV layouts.
- Deciding texture resolution, texel density, number of texture sets or UDIM tiles.
- Baking high-poly detail onto a low-poly: normal, AO, curvature, ID, position maps.
- Diagnosing bake artifacts: black spots, visible seams, skewed detail, waviness.
- Preparing maps for a specific engine or texturing tool.

Scale must be correct first - see `../blender-fundamentals/references/scene-and-units.md`.

## Ask first

1. **Target resolution and budget?** One 2K set, four 4K sets, or UDIM tiles - this changes every
   other decision.
2. **Real-world size of the asset?** Texel density is meaningless without it.
3. **Real-time or offline render?** Real-time wants packed atlases and no overlap; offline can use
   UDIM and overlapping tiling.
4. **Which texturing tool?** Substance, Blender, Mari and hand-painting have different expectations
   for seams, padding and map sets.
5. **Which engine?** Normal-map green-channel direction and texture naming depend on it.
6. **Will it tile or be unique?** Trim sheets and tiling materials need entirely different UVs from
   unique-baked assets.

## Core rules

1. **Seams go where they hide**: hard edges, silhouette breaks, material changes, inside concave
   areas, under overhangs, along the back or the underside.
2. **Every UV island should be as flat and as undistorted as possible.** Check with a checker
   texture, not by eye.
3. **Texel density should be consistent across the asset and the scene.** px/m = texture resolution
   divided by real-world size in metres.
4. **UV seams cost real vertices.** Fewer seams means fewer split vertices in the engine.
5. **Hard edges need UV seams** (and every UV seam should ideally be a hard edge) for correct normal
   baking.
6. **Bake with a cage or sensible extrusion.** Ray distance problems cause most bake artifacts.
7. **Margin/padding must match the mip and compression plan** - too little padding bleeds, too much
   wastes space.
8. **Never scale UVs non-uniformly** unless you intend stretched texel density.

## Workflow

**Step 0 - finish the model.** UVs made before topology is final will be redone.

**Step 1 - mark seams** deliberately; mark the same edges sharp. See
   `references/seams-and-unwrapping.md`.

**Step 2 - unwrap** with the appropriate method, then check distortion with a checker texture.

**Step 3 - straighten and relax** key islands (trims, pipes, panels) so texture direction is clean.

**Step 4 - set texel density** to the project standard and verify it per object. See
   `references/texel-density-and-packing.md`.

**Step 5 - pack** with the right margin, grouping islands by material and importance.

**Step 6 - bake** high to low with cage and ray distance configured. See
   `references/baking-recipes.md`.

**Step 7 - inspect the bake** at 100% zoom, fix causes rather than painting over symptoms. See
   `references/bake-troubleshooting.md`.

## References

| File | Read it for |
| --- | --- |
| `references/seams-and-unwrapping.md` | Seam placement logic per asset type, unwrap methods compared, checker and stretch checks, straightening, pinning, live unwrap, seams vs hard edges, common layout patterns |
| `references/texel-density-and-packing.md` | Texel density formula and worked table, choosing resolutions, packing and margins, atlases, trim sheets, UDIM, multiple texture sets, overlapping and mirrored UVs |
| `references/baking-recipes.md` | Selected to Active setup, per-map recipes (normal, AO, position, ID, height, curvature), cage and extrusion, bake margin, multires baking, float vs 8-bit output, naming conventions |
| `references/bake-troubleshooting.md` | Every common bake artifact with its geometric cause and fix, tangent space and green-channel conventions, verification method, engine-side checks |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-topology-and-retopology/SKILL.md` | The low-poly needs fixing before UVs |
| `../blender-sculpting/SKILL.md` | Producing the high-poly detail you are baking |
| `../blender-materials-and-texturing/SKILL.md` | Using the baked maps in materials |
| `../blender-to-engine-export/SKILL.md` | Exporting meshes and textures to an engine |
| `../../game/2d/game-art-pipeline/SKILL.md` | Atlas, naming and export conventions on the 2D side |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Texture stretched on some faces | Distorted UV island | Re-unwrap, relax, add a seam |
| Texture resolution varies across the asset | Inconsistent texel density | Set density per island group with a common standard |
| Visible seam lines in the render | Padding too small, or seam in a lit area | Increase margin, move seams to hidden edges |
| Normal map shows hard shading breaks at seams | UV seams not marked sharp, or averaged normals mismatch | Mark seams sharp; bake with matching normals |
| Bake has black blotches | Ray distance too short, or overlapping geometry | Use a cage, increase extrusion, separate parts |
| Baked detail looks skewed or smeared | Low-poly normals differ strongly from the high-poly surface | Add supporting geometry, use a cage, split UVs |
| Baked normals look inverted in the engine | Wrong green-channel convention | Flip green for DirectX-style engines |
| Wasted texture space | Bad packing, no rotation, huge margins | Repack, allow rotation, right-size the margin |
| Texture flickers at distance | No padding for mipmaps | Increase margin, disable mips for atlases where appropriate |

## Answering style

- Always ask for the asset's real-world size and target resolution before giving density advice.
- State texel density as px/m and show the arithmetic.
- Name the geometric cause of bake artifacts, then the fix.
- Call out engine-specific conventions explicitly instead of assuming one.
