# Detail passes and handoff

## Detail principles

1. **Direction**: every wrinkle, fold and pore follows something - muscle, gravity, growth, wear.
   Random direction reads as noise.
2. **Hierarchy within detail**: a few large folds, more medium ones, many small ones. Roughly a 1:3:9
   progression in count, with decreasing depth.
3. **Variation**: vary depth, length and spacing. Uniform anything reads as CG.
4. **Breathing room**: leave smooth areas. Detail reads by contrast with smoothness.
5. **Depth discipline**: real skin detail is fractions of a millimetre; cloth folds are centimetres.
   Sculpt at real depth or it looks like elephant hide.
6. **Detail supports form.** If detail is fighting the form, the form is wrong.

## Detail pass order

| Pass | Content | Brush scale |
| --- | --- | --- |
| 1 | Large folds and major wrinkles | Big, low strength |
| 2 | Secondary wrinkles branching from pass 1 | Medium |
| 3 | Fine wrinkles, cross-hatching | Small |
| 4 | Micro texture (pores, weave, grain) | Alpha texture or noise filter |
| 5 | Damage and asymmetry (scars, nicks, wear) | Varied |

Work pass by pass over the whole model, not region by region to completion - otherwise density and
style drift across the sculpt.

## Recipes

**Skin**

- Fat pads and volume first (Blob, Inflate), then bone landmarks re-established (Flatten, Crease).
- Expression lines follow the facial muscles: nasolabial fold, crow's feet radiating from the eye
  corner, forehead lines perpendicular to the frontalis pull.
- Pores: alpha texture with Area Plane mapping, very low strength, varied size by zone (larger on
  nose and cheeks, smaller on eyelids). Never uniform.
- Finish with Mesh Filter > Sharpen at a small amount to recover crispness lost to smoothing.

**Cloth**

- Folds start where fabric is pinned or compressed: shoulders, elbows, waist, knees.
- Use the Cloth brush or Cloth Filter for believable fold chains, then refine with Crease and Draw
  Sharp.
- Fold cross-sections are asymmetric: sharp on the compression side, soft on the stretch side.
- Add thickness at hems and seams; a zero-thickness edge is the giveaway of a sculpted-cloth fake.

**Hard surface in sculpt mode**

- Use Face Sets plus Face Set auto-masking to keep boundaries crisp.
- Trim tools (Box/Lasso Trim), Line Project and Layer brush give mechanical shapes.
- Sharpen with Multiplane Scrape; do not rely on Pinch alone.
- Accept that a sculpted mechanical form is a bake source, not a modelled asset.

**Creature scales and horn/keratin**

- Block the scale rows with Draw Face Sets or a guide curve, then stamp with an alpha.
- Scale size should change with body region and follow the direction of growth.
- Keratin (horns, nails, beaks) has growth ridges perpendicular to the growth direction, with
  irregular spacing.

## Handoff to a usable asset

**Route A - game or animation asset**

1. Finish the sculpt; save a version.
2. Voxel Remesh if the sculpt is non-manifold or self-intersecting.
3. Retopologise (`../../blender-topology-and-retopology/SKILL.md`): loops at joints, budget
   respected.
4. UV unwrap the low-poly (`../../blender-uv-and-baking/SKILL.md`).
5. Bake normal, AO and curvature from high to low. Cage and ray distance matter here.
6. Texture the low-poly; rig and animate as needed.

**Route B - render straight from the sculpt**

1. Keep the sculpt as-is; use Multires render levels for detail.
2. Use Face Sets or material assignment for shading regions.
3. Colour with Color Attributes or procedural/triplanar materials - full UVs are optional.
4. Watch memory: a 10M-triangle sculpt with subsurface scattering is a heavy render.

**Route C - 3D print**

1. Voxel Remesh to guarantee a watertight manifold mesh.
2. Check wall thickness and overhangs (3D-Print Toolbox, Mesh Analysis overlay).
3. Keep detail above the printer's resolution - fine pores will not print.
4. Split into parts with Trim tools, add keys/pegs, and export STL or 3MF at real scale.

## Normal vs displacement

| Map | Stores | Use |
| --- | --- | --- |
| Normal map | Shading direction only | Real-time and most renders; no silhouette change |
| Bump / height | Greyscale height | Cheap micro detail, layered on top of normals |
| Displacement | Real geometric offset | Film-quality close-ups, silhouette-changing detail |
| Vector displacement | Offset in 3D, can overhang | Detail that folds over itself, like heavy folds |

For a sculpt, bake **normal + AO + curvature** at minimum; add displacement only where the silhouette
matters and the renderer can afford subdivision at render time.

## Handoff checklist

1. Sculpt saved as its own version, untouched thereafter.
2. Mesh manifold if it is going to boolean, print or bake.
3. Detail depth verified at real scale.
4. Retopologised mesh has deformation loops where needed.
5. Low-poly UVs made after all remeshing.
6. Bakes checked for skewing and ray-distance artifacts.
7. Triangle counts and texture resolutions inside the target budget.
