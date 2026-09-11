# Bake troubleshooting

## Diagnostic table

| Artifact | Real cause | Fix |
| --- | --- | --- |
| Black patches or holes | Rays miss the high-poly: extrusion / ray distance too small | Increase extrusion and Max Ray Distance, or use a cage |
| Random dark speckles | Rays hitting the low-poly itself, or coincident surfaces | Increase extrusion slightly; separate the pair in space |
| Detail from another part appearing | Ray distance too large, or nearby geometry | Reduce distance; explode the bake by matched pairs |
| Skewed, sheared detail | Ray directions not perpendicular to the surface (interpolated normals) | Use a cage; add supporting geometry to the low-poly; split the UV/normals there |
| Wavy, rippling gradients on flat areas | Low-poly's smoothed normals differ from the flat high-poly surface | Mark the area sharp plus a UV seam, or add support loops |
| Visible seams on the model | Margin too small, or hard edge without a UV seam | Increase bake margin; make every sharp edge a seam |
| Hard shading break where it should be smooth | Sharp edge or split normals on the low-poly | Clear sharp, re-bake; remember UV seams cost split vertices |
| Baked normals too strong / embossed | High-poly bevels too large, or baking geometry that should be shape | Reduce high-poly bevel width; reconsider what belongs in the map |
| Normal map looks flat / has no detail | Baked from the low-poly to itself, or wrong Selected to Active order | High-poly selected first, low-poly active, Selected to Active on |
| Green channel inverted (bumps look like dents) | Engine expects the other tangent convention | Flip the green channel, or set the exporter/engine option |
| Colour shifts / washed-out data maps | Image colour space set to sRGB instead of Non-Color | Set Non-Color on all data maps |
| Banding in a height map | 8-bit output | Bake to 16 or 32-bit float |
| Noisy AO | Too few samples | Raise samples to 128-256 |
| AO too dark in crevices, or missing contact shadow | Baked without the surrounding geometry, or with the wrong distance | Bake AO with the whole high-poly assembly present |
| Mirrored half has inverted detail | Mirrored tangent space with overlapping UVs | Offset mirrored islands by one UV tile, or bake unique halves |
| Seams appear only at distance | Padding lost in mipmaps | Increase padding and margin; consider disabling mips for atlases |
| Bake missing on some faces | Faces outside 0-1 UV space, overlapping islands, or no material/image assigned | Fix UVs; verify the image node is active |
| Everything is pink in the engine | Missing texture / wrong path | Relink; export textures alongside the mesh |

## Tangent space and green-channel conventions

- **Tangent space** normal maps are relative to the surface: they survive deformation and tiling. Use
  them for characters, tiling surfaces and anything animated.
- **Object space** normal maps are relative to the object: slightly better quality on rigid props,
  but they break under deformation.
- Blender bakes tangent-space normal maps in the **OpenGL** convention: +Y, green pointing up.
- Engines differ: DirectX-convention engines (Unreal being the common example) expect **-Y**, green
  pointing down, so the green channel must be flipped. Unity uses the OpenGL convention.
- Do not trust memory for a given engine version: bake a test sphere with an obvious raised bump,
  view it in the engine, and see whether the bump reads as raised or sunken. That test takes two
  minutes and settles it permanently.
- Flip green wherever is most maintainable: in the texturing tool's export preset, in a small image
  processing step, or in the engine's import settings - but choose one place and document it.

## Skew, and how to avoid it

Skew appears when the low-poly's interpolated normal at a point is not perpendicular to the
high-poly surface - typically on chamfers, cylinders with few sides, and long thin faces.

Remedies in order of preference:

1. **Use a cage** built from the low-poly and smoothly inflated.
2. **Add geometry** to the low-poly where the surface changes direction most.
3. **Split normals / add UV seams** at strong angle changes, so interpolation does not cross them.
4. **Bake at higher resolution** and accept a little skew where it is not visible.
5. Use a dedicated baker (Substance, Marmoset, xNormal) with skew-correction painting if the asset
   demands it.

## Verification routine

1. View the normal map at 100% zoom; look for black pixels, hard lines and smears.
2. Apply the maps to the low-poly and rotate it in Material Preview with a bright HDRI.
3. Compare low-poly-with-maps against the high-poly side by side, same lighting, same angle.
4. Check silhouette: nothing in a normal map changes the outline, so the low-poly must already carry
   the silhouette.
5. Test in the target engine early - conventions and colour spaces are engine-side decisions.
6. Inspect at grazing angles, where normal-map errors are most visible.

## Pre-texturing checklist

1. Normal map clean at 100% zoom: no black pixels, no skew where the camera looks.
2. AO baked with the full assembly, no missing contact shadows.
3. All data maps in Non-Color space.
4. Height maps 16-bit or higher.
5. Green-channel convention matched to the target engine and documented.
6. Padding and margin consistent.
7. Map names follow the project convention.
8. Verified in the target engine, not only in Blender.
