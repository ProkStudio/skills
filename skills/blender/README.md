# Blender skills

Ten skills covering 3D modelling in Blender end to end: scene setup, modelling, sculpting, UVs and
baking, materials, lighting and rendering, procedural geometry, rigging and animation, and export to
game engines.

Each skill is a folder with a `SKILL.md` (rules, workflow, failure modes) and a `references/` folder
with the detailed material. Read the `SKILL.md` first; open a reference only when you need the
detail.

## Version baseline

The skills are written against **Blender 5.2 LTS** (July 2026) and stay valid for 4.2 LTS and newer.
The changes that break old tutorials most often:

| Change | Version | What it means |
| --- | --- | --- |
| AgX is the default view transform | 4.0 | Renders look desaturated compared to old Filmic tutorials; Filmic is deprecated |
| Principled BSDF reorganised | 4.0 | Specular became IOR Level, Clearcoat became Coat, Sheen reworked |
| Bone collections replaced armature layers | 4.0 | Tutorials using the 32 layers and the M shortcut need translating |
| Mesh Auto Smooth checkbox removed | 4.1 | Use Object > Shade Auto Smooth, which adds a Smooth by Angle modifier |
| Musgrave texture removed | 4.1 | Folded into Noise Texture fractal types |
| EEVEE Next | 4.2 | New raytracing, shadow and light settings; Bloom removed in favour of the compositor Glare node |
| Brushes became assets | 4.3 | Brushes live in the asset shelf, not a fixed list |

Where behaviour is version-sensitive, the skills say so instead of asserting one answer.

## The skills

| Skill | Covers | References |
| --- | --- | --- |
| [`blender-fundamentals`](blender-fundamentals/SKILL.md) | Units and real-world scale, transforms and origins, objects vs data-blocks, linked duplicates and collections, the modifier stack and non-destructive habits, file hygiene and versions | `scene-and-units.md`, `objects-and-datablocks.md`, `modifiers-and-nondestructive.md`, `file-hygiene-and-versions.md` |
| [`blender-hard-surface-modeling`](blender-hard-surface-modeling/SKILL.md) | Blocking with primitives, proportions, bevels and edge weighting, booleans and cutter workflows, subdivision, support loops and shading control | `blocking-and-forms.md`, `bevels-and-edges.md`, `booleans-and-cutters.md`, `subdivision-and-shading.md` |
| [`blender-topology-and-retopology`](blender-topology-and-retopology/SKILL.md) | Edge flow and quads, poles and loops, topology that deforms, remesh and retopology tools, cleanup and diagnostics | `edge-flow-and-quads.md`, `deformation-topology.md`, `remesh-and-retopo-tools.md`, `cleanup-and-diagnostics.md` |
| [`blender-sculpting`](blender-sculpting/SKILL.md) | Blockout and big forms, dyntopo vs voxel remesh vs multires, the brush kit that actually matters, detail passes and handoff to retopology | `blockout-and-forms.md`, `geometry-strategies.md`, `brush-kit.md`, `detail-and-handoff.md` |
| [`blender-uv-and-baking`](blender-uv-and-baking/SKILL.md) | Seam placement and unwrapping, texel density and packing, bake recipes for normal AO curvature and ID maps, bake troubleshooting | `seams-and-unwrapping.md`, `texel-density-and-packing.md`, `baking-recipes.md`, `bake-troubleshooting.md` |
| [`blender-materials-and-texturing`](blender-materials-and-texturing/SKILL.md) | Principled BSDF and PBR values, node graphs and masking, colour management and AgX, concrete surface recipes | `principled-and-pbr.md`, `nodes-and-masks.md`, `color-management.md`, `surface-recipes.md` |
| [`blender-lighting-and-rendering`](blender-lighting-and-rendering/SKILL.md) | Light setups and colour temperature, Cycles vs EEVEE Next settings, cameras and composition, output formats and compositing | `light-setups.md`, `cycles-and-eevee.md`, `camera-and-composition.md`, `output-and-compositing.md` |
| [`blender-geometry-nodes`](blender-geometry-nodes/SKILL.md) | Fields and domains, instancing and scattering, generators and curves, reusable patterns and debugging | `fields-and-domains.md`, `instancing-and-scattering.md`, `generators-and-curves.md`, `patterns-and-debugging.md` |
| [`blender-rigging-and-animation`](blender-rigging-and-animation/SKILL.md) | Armatures, bone placement and roll, weighting and deformation fixes, IK/FK constraints and drivers, animation craft and curves, game rigs and baking | `armatures-and-weights.md`, `controls-and-constraints.md`, `animation-craft.md`, `game-rigs-and-export.md` |
| [`blender-to-engine-export`](blender-to-engine-export/SKILL.md) | Engine unit and axis conventions, glTF vs FBX vs USD, exporter settings, LODs and collision, naming and validation | `scale-and-orientation.md`, `formats-and-settings.md`, `lods-and-collision.md`, `naming-and-validation.md` |

## Reading order

For someone learning 3D modelling in order:

1. `blender-fundamentals` - scale, transforms, data-blocks, modifiers. Everything else assumes this.
2. `blender-hard-surface-modeling` - the modelling toolkit on concrete objects.
3. `blender-topology-and-retopology` - why meshes shade and deform the way they do.
4. `blender-sculpting` - organic forms and the sculpt-to-retopo loop.
5. `blender-uv-and-baking` - UVs, texel density, baked maps.
6. `blender-materials-and-texturing` - surfaces and colour management.
7. `blender-lighting-and-rendering` - making it look like something.
8. `blender-geometry-nodes` - procedural work once the manual workflow is understood.
9. `blender-rigging-and-animation` - movement.
10. `blender-to-engine-export` - delivery.

For a game asset, the practical path is 1 > 2/4 > 3 > 5 > 6 > 9 > 10, with 7 used for portfolio
renders.

## Shortcuts by symptom

| Symptom | Go to |
| --- | --- |
| Imported model is 100x too big or rotated 90 degrees | `blender-to-engine-export/references/scale-and-orientation.md` |
| Simulation, bevels or depth of field behave strangely | `blender-fundamentals/references/scene-and-units.md` |
| Dark smudges or pinching near bevels after subdivision | `blender-hard-surface-modeling/references/subdivision-and-shading.md` |
| Boolean leaves a mess | `blender-hard-surface-modeling/references/booleans-and-cutters.md` |
| Surface shades badly with no visible modelling error | `blender-topology-and-retopology/references/cleanup-and-diagnostics.md` |
| Elbow, knee or shoulder collapses when posed | `blender-topology-and-retopology/references/deformation-topology.md` then `blender-rigging-and-animation/references/armatures-and-weights.md` |
| Sculpt cannot hold detail or the file crawls | `blender-sculpting/references/geometry-strategies.md` |
| Texture looks stretched or inconsistent between objects | `blender-uv-and-baking/references/texel-density-and-packing.md` |
| Baked normal map has seams, waves or black areas | `blender-uv-and-baking/references/bake-troubleshooting.md` |
| Metal looks like plastic, or glass looks wrong | `blender-materials-and-texturing/references/principled-and-pbr.md` |
| Render looks washed out or desaturated | `blender-materials-and-texturing/references/color-management.md` |
| Render is noisy or takes forever | `blender-lighting-and-rendering/references/cycles-and-eevee.md` |
| Scattered instances look repetitive or tank performance | `blender-geometry-nodes/references/instancing-and-scattering.md` |
| Node tree works on one object and breaks on another | `blender-geometry-nodes/references/patterns-and-debugging.md` |
| Animation looks floaty | `blender-rigging-and-animation/references/animation-craft.md` |
| Animation or constraints do not export | `blender-rigging-and-animation/references/game-rigs-and-export.md` |
| Shading, materials or textures wrong after import | `blender-to-engine-export/references/formats-and-settings.md` |

## Conventions in these skills

- Metric units, real-world scale, metres. Every measurement is stated with its unit.
- Numbers are given as ranges with the reason behind them, not as magic values.
- Version-dependent behaviour is labelled with the version.
- Each `SKILL.md` ends with a failure-mode table: symptom, real cause, fix.
- Each reference ends with a checklist you can run before calling the work done.

## Related skill sets in this repo

| Set | Use |
| --- | --- |
| [`../game/README.md`](../game/README.md) | 2D game art: pixel art, palettes, sprite animation, tilesets, VFX, UI/HUD, art pipeline |
| [`../minecraft/README.md`](../minecraft/README.md) | Minecraft building: architecture, palettes, interiors, organic shapes, settlements, terraforming, redstone, version history |

The export, naming and pipeline material here pairs directly with
[`../game/2d/game-art-pipeline/SKILL.md`](../game/2d/game-art-pipeline/SKILL.md), and the animation
principles pair with [`../game/2d/sprite-animation/SKILL.md`](../game/2d/sprite-animation/SKILL.md).

## Notes

- These skills are documentation, not scripts: there is nothing to run, and no add-on is required
  beyond what ships with Blender (Rigify is bundled).
- `scripts/validate_skills.py` in the repo root checks skill folder names, frontmatter and
  description length. It has not been run against this folder locally; run it before relying on the
  catalog.
- If this set should live under the game umbrella instead, one command moves it:
  `git mv skills/blender skills/game/3d/blender`. All links inside the folder are relative, so only
  the cross-links to `../game/` and `../minecraft/` would need adjusting.
