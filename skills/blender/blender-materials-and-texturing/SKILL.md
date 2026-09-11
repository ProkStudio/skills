---
name: blender-materials-and-texturing
description: Build physically plausible materials in Blender and texture assets so they hold up in render and in engine. Use whenever the user asks how to set up the Principled BSDF, what metallic roughness IOR or specular values to use, why a material looks like plastic or looks flat or washed out, how to make metal wood glass skin fabric or emissive surfaces, how to build procedural textures and node masks, how to add edge wear dirt and grunge from curvature and ambient occlusion, how to use baked maps in a shader, the difference between bump normal and displacement, how to texture paint in Blender, how to organise node groups and texture sets, or how colour management view transforms and AgX affect the look. Covers the Principled BSDF after its 4.0 reorganisation, PBR albedo and roughness discipline, IOR reference values, procedural noise and Voronoi patterns including the removal of Musgrave, mask building from geometry attributes, decals and trim sheets, texture paint setup, and colour management with AgX Standard Raw False Color and Khronos PBR Neutral plus which file formats bake the view transform.
version: 1.0.0
---

# Materials and texturing

A material is a set of physical claims about a surface: how much light bounces, how rough it is, what
it is made of. Believable materials come from plausible values plus variation, not from stacking
nodes.

## When to use

- Setting up or fixing a Principled BSDF material.
- Deciding metallic, roughness, IOR, transmission and subsurface values.
- Building procedural textures, masks, wear and grunge.
- Wiring baked maps (normal, AO, roughness, ID) into a shader.
- Texture painting inside Blender.
- Diagnosing plastic, flat, washed-out or noisy-looking materials.
- Understanding view transforms, AgX, and why saved images look different from the viewport.

## Ask first

1. **Render engine?** Cycles and EEVEE support different features (real refraction, SSS quality,
   raytraced reflections).
2. **Real-time or offline?** Engine-bound assets need baked PBR maps in a fixed channel layout;
   renders can use procedural setups freely.
3. **Is the asset baked or procedural?** Baked textures and procedural node setups need different
   organisation.
4. **Reference?** "Metal" is fifty different materials. Ask which one.
5. **Close-up or background?** Decides map resolution, displacement vs normal, and how much variation
   is worth authoring.

## Core rules

1. **Metallic is nearly binary.** A surface is metal or it is not; 0.3 metallic is almost never
   physically meaningful (painted or dusty metal is a dielectric coating over metal, which is a mask,
   not a middle value).
2. **Base colour is albedo only.** No baked lighting, no shadows, no AO painted in.
3. **Roughness carries the story.** Uniform roughness is the number-one cause of CG-looking surfaces.
   Vary it with masks.
4. **Use IOR, not guesswork**, for dielectrics; the Principled BSDF's specular behaviour is IOR-driven
   since 4.0.
5. **Detail hierarchy applies to textures too**: large colour variation, medium wear patterns, fine
   surface texture.
6. **Build masks from geometry** - curvature, AO, position, normal direction - so wear lands where
   physics would put it.
7. **Know your view transform.** AgX changes contrast and highlight saturation; judging colour without
   knowing the transform wastes time.
8. **Organise as node groups** with exposed inputs, one per reusable material.

## Workflow

**Step 0 - reference**: find photographs of the actual material, including close-ups and worn areas.

**Step 1 - base PBR values**: base colour, metallic, roughness, IOR. See
   `references/principled-and-pbr.md`.

**Step 2 - wire the baked maps** if the asset was baked, in the correct colour spaces.

**Step 3 - break up uniformity**: large-scale colour and roughness variation via noise or textures.

**Step 4 - build wear masks** from curvature, AO, height and position. See
   `references/nodes-and-masks.md`.

**Step 5 - add surface detail**: bump or normal for micro texture, displacement only where the
   silhouette matters.

**Step 6 - check under proper lighting**: an HDRI with real highlights, and the project view
   transform. See `references/color-management.md`.

**Step 7 - finalise**: name materials, group nodes, verify ranges, export or document the maps.

## References

| File | Read it for |
| --- | --- |
| `references/principled-and-pbr.md` | Principled BSDF inputs after the 4.0 reorganisation, metallic/roughness discipline, albedo ranges, IOR reference table, subsurface, transmission, coat, sheen, emission, EEVEE vs Cycles differences |
| `references/nodes-and-masks.md` | Texture coordinates and mapping, procedural textures (Noise after the Musgrave removal, Voronoi, Wave, Gradient), Color Ramp, mask building from curvature/AO/position, bump vs normal vs displacement, node groups, decals and trim sheets |
| `references/color-management.md` | View transforms (AgX, Standard, Filmic Log, Raw, False Color, Khronos PBR Neutral), which formats bake the transform, texture colour spaces, exposure and look control, common washed-out and oversaturated cases |
| `references/surface-recipes.md` | Concrete starting values for metals, painted surfaces, plastics, wood, stone, concrete, glass, water, skin, fabric, foliage, emissive and screens, with the variation that makes each read |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-uv-and-baking/SKILL.md` | Producing or fixing the maps a material consumes |
| `../blender-lighting-and-rendering/SKILL.md` | Lighting, engine settings, output formats |
| `../blender-geometry-nodes/SKILL.md` | Procedural geometry and attributes feeding shaders |
| `../blender-to-engine-export/SKILL.md` | Channel packing, material slots, engine material setup |
| `../../game/2d/color-and-palettes/SKILL.md` | Colour theory and palette construction |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Everything looks like plastic | Uniform roughness, no variation, wrong metallic | Vary roughness with masks; set metallic correctly |
| Metal looks grey and dull | Metal needs an environment to reflect | Add an HDRI or reflective surroundings |
| Material looks washed out | AgX unsaturating highlights, or over-exposure | Adjust exposure and pre-transform contrast; check the view transform |
| Colours too saturated in the saved file | View transform baked into an LDR format | Check format: EXR/HDR/DPX ignore the view transform, PNG/JPEG bake it |
| Textures look dark or faded | Wrong colour space on the image node | sRGB for colour, Non-Color for data |
| Normal map has no effect | Missing Normal Map node, or wrong colour space | Insert Normal Map node, set image to Non-Color |
| Surface looks embossed and fake | Bump strength too high | Reduce strength; micro detail is subtle |
| Glass renders black | EEVEE without raytracing/refraction settings, or no light behind it | Enable the needed settings or use Cycles |
| Skin looks like wax | Subsurface radius wrong for the scale, no variation | Set radius in metres for the model's real scale |
| Wear looks painted on | Mask not derived from geometry | Build masks from curvature, AO and position |

## Answering style

- Give concrete numeric starting values, then say what to vary and why.
- Distinguish Cycles and EEVEE behaviour when it matters.
- State the assumed Blender version when naming Principled BSDF inputs, since they were renamed in
  4.0.
- Point to a physical explanation (dielectric vs conductor, IOR, coating) rather than a slider habit.
