# Baking recipes

## Setup: Selected to Active

The standard high-to-low bake in Blender (Cycles):

1. Render engine: **Cycles** (baking lives in Render Properties > Bake).
2. Low-poly: UV unwrapped, with an image texture node in its material holding a new blank image.
3. Select the **high-poly first**, then shift-select the **low-poly last** so the low-poly is active.
4. Enable **Selected to Active**.
5. Set **Extrusion** and **Max Ray Distance**, or use a **Cage** object.
6. Choose the bake type, set Margin, then Bake.

Notes:

- The image must be assigned in the active material's node tree and selected as the active node.
- Bake resolution comes from the image, not from render settings; samples come from the render
  settings.
- For clean AO and other ray-traced maps, 64-256 samples is usually plenty; normal maps need very few
  samples because they are not noisy.
- Place high and low in the same location, overlapping. Bake by parts (in matched pairs) for complex
  assets to avoid cross-contamination.

## Cage, extrusion and ray distance

| Control | What it does | Guidance |
| --- | --- | --- |
| Extrusion | Pushes ray origins outward along the low-poly normals | Start at 2-5x the largest gap between low and high |
| Max Ray Distance | How far rays travel before giving up | Slightly more than the biggest high-to-low distance |
| Cage object | A separate inflated copy of the low-poly used as ray origin | Best quality; eliminates skew on curved/complex shapes |

Making a cage:

1. Duplicate the low-poly.
2. Add Displace or Shrink/Fatten (Alt+S) to inflate it until it fully encloses the high-poly.
3. Keep the **same topology and vertex order** as the low-poly; the cage cannot be a different mesh.
4. Smooth-shade it and remove sharp edges - the cage's job is to give smoothly varying ray
   directions.

Too-small distances cause black patches (rays miss the high-poly); too-large distances cause detail
from the wrong part of the mesh bleeding in.

## Map-by-map recipes

| Map | Bake type | Settings that matter |
| --- | --- | --- |
| Normal | Normal | Space: Tangent for meshes that deform or tile; Object for fixed props. Swizzle +X +Y +Z for OpenGL |
| Ambient occlusion | Ambient Occlusion | Samples 64-256; bake from the high-poly with the whole asset present |
| Height / displacement | Position, or a Displacement bake from Multires | Use 16/32-bit float output; 8-bit banding is severe |
| Curvature | No native bake type - use Geometry > Pointiness into Emit, or bake in a texturing tool | Pointiness needs a Color Ramp to be usable |
| ID / material mask | Emit with flat emission colours per material, or Diffuse with Color only | Use pure, distinct, unlit colours |
| Diffuse / base colour | Diffuse with Direct and Indirect disabled | Keeps flat albedo without lighting |
| Roughness / metallic | Roughness, or Emit with the value wired to emission | Bake into non-colour data |
| Emission | Emit | Good for transferring any arbitrary value via emission |
| Thickness | Ambient Occlusion with inverted normals on the high-poly | Hack, but works for SSS masks |
| Lightmap / combined | Combined | Needs a second non-overlapping UV channel |
| Multires sculpt detail | Bake from Multires (Normals or Displacement) | Same object, no high/low pair needed |

## Margin

- **Margin** in the Bake panel expands the baked island edges outward so bilinear filtering and mips
  do not sample empty space.
- Margin Type **Adjacent Faces** (continues the neighbouring island's data) generally beats **Extend**
  (smears the edge pixel) for normals and AO.
- Match the margin in pixels to the padding you allowed when packing; padding without margin is
  wasted space, and margin without padding bleeds between islands.

## Output settings

| Map type | Bit depth | Colour space |
| --- | --- | --- |
| Normal | 8-bit acceptable, 16-bit better | Non-Color |
| AO, roughness, metallic, masks | 8-bit | Non-Color |
| Height / displacement | 16 or 32-bit float (EXR, or 16-bit PNG) | Non-Color |
| Base colour / albedo | 8-bit | sRGB |
| ID maps | 8-bit PNG, no compression artifacts | sRGB, but with flat colours |

Always save as PNG, TIFF or EXR - never JPEG. Compression artifacts in a normal map produce visible
shading noise.

Remember that PNG/JPEG/TIFF outputs bake in the view transform, while EXR/HDR/DPX do not. For
data maps, set the image to Non-Color and keep the bake out of display-referred space.

## Naming

Use one convention and stick to it:

```
<asset>_<set>_<map>.<ext>
barrel_main_basecolor.png
barrel_main_normal.png
barrel_main_orm.png        (packed occlusion/roughness/metallic)
barrel_main_height.exr
```

Packed channel maps (ORM, or AO+Rough+Metal) save texture slots in engines; pack them in the
texturing tool or a small compositing step, and document the channel order.

## Baking helpers

- **Floaters**: detail geometry (bolts, vents, panel lines) hovering just above the surface. They bake
  into the normal map without needing to exist in the low-poly. Keep them in an `x_floater_`
  collection.
- **Split by material for ID maps**: the fastest way to get clean masks for texturing.
- **Explode the bake**: separate matching high/low pairs in space so nearby geometry cannot
  contaminate rays. Move pairs together, never independently.
- **Bake by parts**: for large assets, bake in groups and composite the results.
- **Test at low resolution** (512 px) first; a full 4K bake to discover a ray-distance mistake is a
  waste of time.

## Bake checklist

1. Low-poly UVs done, packed, with padding matching the intended margin.
2. Every sharp edge is a UV seam.
3. High and low aligned, both with applied transforms and scale 1, 1, 1.
4. Cage or extrusion configured and verified to enclose the high-poly.
5. Floaters in place, high-poly triangulation irrelevant but shading clean.
6. Image created at the target resolution with the correct colour space.
7. Test bake at low resolution reviewed before the full bake.
8. Maps named by convention and saved in a lossless format.
