---
name: blender-to-engine-export
description: Export Blender assets to game engines and other tools so they arrive at the right scale orientation and quality. Use whenever the user asks how to export to Unity Unreal Godot or a web viewer, whether to use glTF or FBX or OBJ or USD, why an imported model is 100 times too big or too small, why it is rotated ninety degrees or lying on its side, what apply transform and units scale do, how to handle axis conventions and forward directions, how to export smooth shading custom normals or hard edges, how to set up LODs collision meshes material slots and texture naming, how to export animation and skinned characters, how to batch export many assets, or how to validate an asset before handing it to an engine. Covers per-engine unit and axis conventions with concrete numbers, the FBX exporter options including the experimental apply transform caveat, glTF settings, scale and orientation debugging, LOD generation ratios, collision mesh conventions, material and texture naming, triangulation and normals, and a pre-export validation checklist.
version: 1.0.0
---

# Export to engines

Export problems are almost never mysterious: they are unit mismatches, axis conventions, unapplied
transforms, or normals. Fix them in the source file, once, and every future export behaves.

## When to use

- Exporting meshes, characters or scenes to Unity, Unreal, Godot, a web viewer or another DCC tool.
- Choosing a format: glTF, FBX, OBJ, USD, Alembic.
- Debugging scale, rotation, flipped or dark-looking imports.
- Setting up LODs, collision meshes, sockets and material slots.
- Exporting skinned characters and animation clips.
- Establishing naming conventions and a batch-export process.

## Ask first

1. **Which engine and version?** Units and axes differ, and importer defaults change between
   versions.
2. **What is the asset?** Static prop, modular kit piece, skinned character, or a whole scene.
3. **Does the project have conventions already?** Follow them over any generic advice.
4. **Are textures exported with the mesh or handled separately?** Most pipelines handle them
   separately.
5. **Do LODs and collision need to come from Blender**, or are they generated in-engine?
6. **Animation included?** That changes format and settings materially.

## Core rules

1. **Model at real-world scale in metres** and apply all transforms. This removes most export
   problems before they exist.
2. **Know the target's conventions**: Unity is Y-up with 1 unit = 1 m, Unreal is Z-up with 1 unit =
   1 cm, Godot is Y-up with 1 unit = 1 m, glTF is Y-up in metres.
3. **Prefer glTF where the engine supports it well.** Its axis and unit conventions are defined by
   the format, so there is less to get wrong.
4. **Do not rely on FBX "Apply Transform"** for animated or skinned assets: it is flagged
   experimental and is known to misbehave with armatures and animations. Fix the source instead.
5. **Origins and orientation are content decisions**: origin at the base or the pivot point, forward
   axis consistent across the whole library.
6. **Triangulate deliberately** (modifier or exporter) so the engine's triangulation matches what you
   saw.
7. **Name everything by convention** - meshes, materials, textures, LODs, collision, sockets.
8. **Validate one asset end to end** before batch-exporting a hundred.

## Workflow

**Step 0 - confirm target conventions** and project naming rules.

**Step 1 - clean the source**: applied transforms, correct scale, origin placed, unused data purged.
   See `references/scale-and-orientation.md`.

**Step 2 - finalise shading**: normals, sharp edges, smooth-by-angle, UVs, material slots. See
   `references/formats-and-settings.md`.

**Step 3 - build extras**: LODs, collision meshes, sockets. See `references/lods-and-collision.md`.

**Step 4 - choose the format** and configure the exporter for the target.

**Step 5 - export one asset** and import it into the engine.

**Step 6 - verify** scale against an in-engine reference, orientation, shading, materials, and
   animation. See `references/naming-and-validation.md`.

**Step 7 - batch the rest** using a saved preset or a script, then spot-check.

## References

| File | Read it for |
| --- | --- |
| `references/scale-and-orientation.md` | Per-engine unit and axis tables, forward-axis conventions, applying transforms, origin placement, the 100x and 0.01x problems, rotation fixes with and without Apply Transform, scene scale settings, debugging routine |
| `references/formats-and-settings.md` | glTF vs FBX vs OBJ vs USD vs Alembic, exporter options that matter, FBX scale options and the experimental apply-transform caveat, normals and smoothing, triangulation, material slots, texture packing and paths, animation export settings |
| `references/lods-and-collision.md` | LOD ratios and generation methods, Decimate modes, LOD naming conventions per engine, collision primitives and convex hulls, collision naming, sockets and attachment points, pivot and modular-kit rules |
| `references/naming-and-validation.md` | Naming conventions for meshes materials textures and clips, folder structure, batch export approaches, a full pre-export validation checklist, post-import verification, common import errors decoded |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-fundamentals/SKILL.md` | Scene units, transforms and file hygiene |
| `../blender-topology-and-retopology/SKILL.md` | Triangle budgets and clean geometry |
| `../blender-uv-and-baking/SKILL.md` | UVs, texel density and baked maps |
| `../blender-materials-and-texturing/SKILL.md` | Channel packing and material setup |
| `../blender-rigging-and-animation/SKILL.md` | Skinned characters, baking, animation clips |
| `../../game/2d/game-art-pipeline/SKILL.md` | Project-wide naming, versioning and export discipline |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Model imports 100x too large or 1/100 the size | Unit mismatch (metres vs centimetres) | Set the exporter's scale option, or match the engine's unit scale on import |
| Model is rotated 90 degrees | Z-up vs Y-up conventions | Set the exporter's up/forward axes, or pre-rotate and apply in the source |
| Object is offset from where it should be | Origin not at the intended pivot | Move the origin in Blender before exporting |
| Scale is fine but children are wrong | Parent had unapplied non-uniform scale | Apply transforms through the hierarchy |
| Shading looks faceted or blotchy | Custom normals or smoothing not exported | Enable smoothing/normals export; keep sharp edges marked |
| Hard edges look soft or vice versa | Smoothing type mismatch (face vs edge vs smoothing groups) | Choose the exporter's smoothing option the engine expects |
| Normal map looks inverted | Green channel convention mismatch | Flip green for DirectX-style engines |
| Materials arrive as one grey material | Material slots or export options wrong | One slot per material, correct exporter material settings |
| Textures missing in engine | Absolute paths or unpacked files | Export textures separately with relative paths, or embed them |
| Animation missing | Constraints not baked, or animation export disabled | Bake Action, then enable the animation options |
| Mesh appears inside-out in places | Flipped normals | Recalculate normals outside before export |
| Extra empties and cameras imported | Exporter object types left at defaults | Limit the exported object types, or export only selected |

## Answering style

- State the engine's unit and axis convention with numbers before giving export settings.
- Prefer fixing the source file over compensating with exporter options.
- Give the exact exporter option names and values.
- Insist on one verified test import before batch work.
