# Nodes, procedural textures and masks

## Coordinates and mapping

| Texture Coordinate output | Behaviour | Use |
| --- | --- | --- |
| UV | Uses the mesh's UV map | Baked textures, anything authored in UV space |
| Object | Object-space coordinates; follows the object | Procedural detail that should move with the object |
| Generated | Normalised bounding-box space | Quick gradients, scale-independent patterns |
| Normal | Surface normal direction | Directional masks (up-facing dust) |
| Camera / Window | View-relative | Screen-space effects, matte tricks |
| Reflection | Reflection vector | Fake reflection gradients |

Pair it with the **Mapping** node for location, rotation and scale. For texturing without UVs, an
Object-coordinate box or triplanar projection works well on props and terrain.

Image Texture settings that matter: Extension (Repeat / Extend / Clip / Mirror), Interpolation
(Closest for pixel art and ID maps, Cubic for smooth data), and Alpha mode for decals.

## Procedural textures

| Node | Produces | Notes |
| --- | --- | --- |
| Noise Texture | Fractal noise, multiple dimensions | Since 4.1 it absorbed Musgrave: fBM, Multifractal, Hybrid Multifractal, Ridged, Hetero Terrain types |
| Voronoi Texture | Cells, distance fields, edges | F1/F2/Smooth F1/Distance to Edge/N-Sphere Radius; the workhorse for scales, cracks, stones, cobbles |
| Wave Texture | Bands and rings with distortion | Wood grain, ripples, stripes |
| Gradient Texture | Linear/radial/spherical ramps | Masks, falloff, blends |
| Magic / Checker / Brick | Patterned utility textures | Checker for UV checks, Brick for masonry |
| White Noise | Per-element random values | Randomising instances or faces via Object Info / attributes |
| Musgrave | **Removed in 4.1** | Use Noise Texture's fractal types instead |

Combine, do not settle for one: real surfaces are layered. A convincing concrete is large-scale
blotchiness (Noise, low detail) plus medium stains (Voronoi Smooth F1) plus fine grain (Noise, high
detail, tiny scale) plus cracks (Voronoi Distance to Edge, sharpened by a Color Ramp).

## Shaping values

| Node | Use |
| --- | --- |
| Color Ramp | The main tool: remap any value, set contrast, posterise with Constant interpolation |
| Map Range | Precise numeric remapping with clamping |
| Math | Multiply/Add for strength, Power for contrast, Greater/Less Than for hard masks |
| Mix (Color) | Blend two inputs by a factor or mask; the generic Mix node replaced the old MixRGB |
| RGB Curves | Fine tonal control on masks and colour |
| Hue/Saturation/Value | Colour variation per instance or region |
| Separate/Combine Color | Channel-level work, unpacking ORM maps |
| Bump / Normal Map | Convert height or normal data into shading normals |
| Displacement | True displacement in Cycles (requires the material's Displacement setting) |

## Geometry-derived masks

These make wear land where physics would put it:

| Source | Node | Produces |
| --- | --- | --- |
| Curvature | Geometry > Pointiness (into a tight Color Ramp) | Convex edges and concave crevices |
| Occlusion | Ambient Occlusion node | Dirt in recesses |
| Rounded shading | Bevel node (Cycles) | Softened edges without geometry |
| Height / position | Texture Coordinate > Object or Generated, Separate XYZ | Water lines, dust accumulation by height, gradient fades |
| Up-facing surfaces | Geometry > Normal > Separate XYZ, Z channel | Dust, snow, moss on top surfaces |
| Baked maps | AO/curvature images | Reliable, resolution-dependent masks |
| Attributes | Attribute / Color Attribute node | Painted masks, geometry-node attributes, Face Sets converted to data |

Pointiness needs a very narrow Color Ramp to be useful, and it is mesh-density dependent - a coarse
mesh gives a coarse mask. For production, bake curvature and AO instead of relying on live nodes.

## Wear and grunge recipe

1. **Edge wear**: curvature mask > sharpen with Color Ramp > multiply by a noise breakup > use to mix
   in exposed metal (metallic 1, lower roughness).
2. **Recess dirt**: AO mask > Color Ramp > mix in a darker, rougher, dustier material.
3. **Directional streaks**: Noise stretched on one axis via Mapping scale > mask below rain-shadow
   areas.
4. **Top-surface dust**: normal Z mask > multiply by noise > mix in a light, very rough layer.
5. **Water line / splash zone**: height gradient > Color Ramp with a hard edge, plus noise
   distortion.
6. **Variation per instance**: Object Info > Random > Hue/Saturation, so a hundred crates are not
   identical.

Always break a clean procedural mask with noise. Perfect edge wear along every bevel reads as a
filter, not as damage.

## Bump vs normal vs displacement

| Technique | Cost | Silhouette | Use |
| --- | --- | --- | --- |
| Bump (height) | Cheapest | No change | Micro detail, grain, pores |
| Normal map | Cheap | No change | Baked detail from a high-poly |
| Displacement (Cycles) | Expensive, needs subdivision | Real | Close-ups, terrain, heavy relief |
| Bump + Normal combined | Cheap | No change | Baked detail plus fine procedural grain |

To combine: plug the Normal Map node output into the Bump node's Normal input, then the Bump output
into the shader's Normal. Keep bump strength low (0.05-0.3 for micro detail).

True displacement in Cycles requires the material setting Displacement (or Displacement and Bump),
plus adaptive subdivision or dense geometry.

## Organisation

- **Node groups** for anything reused: a wear-mask group, a triplanar mapping group, a fabric
  material group. Expose only the inputs that matter.
- **Frames and labels**: name frames by intent ("edge wear", "base colour variation").
- **Reroute nodes** to keep long connections readable.
- Keep a single "look control" area of exposed values at the left of the tree; tweaking a material
  should not require hunting through fifty nodes.
- Name materials by material, not by object, and reuse data-blocks instead of duplicating.

## Decals, trims and projection

| Technique | How | Use |
| --- | --- | --- |
| Mesh decal | Floating geometry with an alpha-blended material | Signs, panel labels, damage patches |
| Decal projection via node | Project From View UVs, or Object coordinates and an image with Clip extension | Logos, graffiti, stencils |
| Trim sheet | One texture of reusable strips; UVs snapped onto them | Architecture, modular kits |
| Atlas material | Many small textures in one image | Prop sets, mobile |
| Detail/tiling second UV | A second UV channel scaled up for fine texture | Micro detail on large surfaces |

For real-time work, mesh decals and trim sheets are how you get high perceived detail with small
textures. Check the engine's decal support before committing.

## Texture painting in Blender

1. Unwrap first; painting without UVs produces unusable results.
2. Texture Paint mode, add a new image texture per channel you intend to paint (base colour,
   roughness, mask).
3. Enable **Bleed** in the paint settings to paint across seams, and paint from multiple angles.
4. Use stencils and the Clone brush for photo detail; use masks (Face Sets, vertex groups, or
   selection masking) to constrain strokes.
5. Save images explicitly - painted images are not saved with the .blend unless packed.
6. For heavy texturing work, a dedicated tool (Substance Painter, ArmorPaint, Quixel Mixer-style
   apps) is far faster; Blender painting is best for touch-ups, masks and stylised work.

## Node checklist

1. Coordinates chosen deliberately (UV vs Object vs Generated).
2. Procedural layers at three scales minimum.
3. Masks derived from geometry, then broken up with noise.
4. Data images set to Non-Color; colour images sRGB.
5. Bump strength subtle; displacement only where needed.
6. Reusable logic in named node groups with exposed controls.
7. Per-instance variation wired where objects repeat.
