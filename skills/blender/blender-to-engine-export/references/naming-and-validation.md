# Naming, batching and validation

## Naming conventions

One convention, applied everywhere. A common prefix-based scheme:

| Type | Pattern | Example |
| --- | --- | --- |
| Static mesh | `SM_<category>_<name>_<variant>` | `SM_prop_barrel_01` |
| Skeletal mesh | `SK_<name>` | `SK_hero_knight` |
| Skeleton | `SKEL_<name>` | `SKEL_hero_knight` |
| Animation clip | `A_<character>_<action>_<variant>` | `A_knight_run_fwd` |
| Material | `M_<name>` | `M_wood_oak_painted` |
| Material instance | `MI_<name>` | `MI_wood_oak_red` |
| Texture | `T_<name>_<map>` | `T_barrel_01_N` |
| Collision | `UCX_<mesh>_01` | `UCX_SM_prop_barrel_01_01` |
| LOD | `<mesh>_LOD1` | `SM_prop_barrel_01_LOD1` |

Map suffixes: `_BC` or `_D` base colour, `_N` normal, `_R` roughness, `_M` metallic, `_AO` occlusion,
`_ORM` packed, `_E` emissive, `_H` height, `_MSK` mask.

Rules:

- Lowercase or a single consistent case; never mixed.
- No spaces, no accents, no `#`, `%` or other characters that break paths.
- Zero-padded numbers (`_01`, not `_1`) so sorting works.
- Describe content, not history: `barrel_wood_01`, not `barrel_final_new_v2`.
- Keep names identical between Blender and the engine so reimports match.

## Folder structure

```
project/
  source/                 # .blend working files
    props/
    characters/
  export/                 # exported meshes
    props/
    characters/
  textures/
    props/
    characters/
  reference/
```

- Source and export separated, so an export folder can be wiped and regenerated.
- Mirror the engine's content folder structure in `export/` to make importing trivial.
- One .blend per asset for props; one per character (plus animation files) for characters.
- Use relative paths inside .blend files (File > External Data > Make Paths Relative).

## Batch export

| Approach | When |
| --- | --- |
| Export presets in the exporter | Any manual workflow; saves the settings once |
| Collection-per-asset plus a small Python script | Dozens of assets; full control over names and paths |
| Blender's `bpy.ops.export_scene.*` in a script | Automation and CI; drive from a list or folder walk |
| Batch-export add-ons | Convenience layer over the same operators |
| Command line (`blender -b file.blend -P export.py`) | Pipelines and build servers |

A workable scripted pattern: one collection per asset, named exactly as the exported file should be;
the script iterates collections, isolates each, applies the preset, and writes to `export/` mirroring
the collection hierarchy. Keep the script in the repo next to the source files.

Whatever the mechanism: export deterministically. If two people export the same asset, the files
should be identical.

## Pre-export validation

1. **Transforms**: all applied; scale 1, 1, 1; rotation zero; origin at the intended pivot.
2. **Scale**: dimensions match reality in metres.
3. **Geometry**: no loose verts/edges, no interior faces, no zero-area faces, no duplicate vertices.
4. **Normals**: recalculated outside; face-orientation overlay clean; sharp edges marked.
5. **Modifiers**: intentionally applied or intentionally left; subdivision resolved.
6. **UVs**: present, inside 0-1 where required, no unintended overlaps; second channel if the engine
   bakes light.
7. **Materials**: correct slot count, named by convention, no unused slots.
8. **Textures**: named by convention, relative paths, correct colour spaces.
9. **Triangle count**: within budget, recorded per LOD.
10. **Extras**: LODs, collision, sockets present and named.
11. **Rig** (if any): single armature, root at origin, deform bones only, influences limited,
    constraints baked.
12. **File hygiene**: orphan data purged, collections named, nothing stray in the export selection.

## Post-import verification

1. Scale checked against an in-engine reference object.
2. Orientation and forward axis correct.
3. Pivot where expected; the asset sits on the floor and rotates around the right point.
4. Shading correct: hard edges hard, smooth edges smooth, no faceting.
5. Normal map orientation correct (test with a strong directional light).
6. Material slots mapped as expected.
7. Collision present and behaving; no invisible walls.
8. LODs switching without visible popping.
9. Animation clips playing at the right length and frame rate, loops seamless.
10. Performance sane: draw calls, triangle count, texture memory within budget.

## Import error decoder

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| "Mesh has no UVs" / lightmap warning | Missing UV channel | Unwrap; add a lightmap channel |
| "Degenerate tangent bases" | Overlapping or zero-area UVs/faces | Fix UVs and geometry |
| "Too many bone influences" | Weights exceed the engine budget | Limit Total and normalise |
| "Non-uniform scale detected" | Unapplied scale | Apply transforms |
| "Multiple root bones" | More than one top-level bone | Restructure to a single root |
| "Smoothing groups missing" | FBX smoothing option set to Off/Normals Only | Export with Face or Edge smoothing |
| Import is empty | Wrong object types or nothing selected | Check exporter include/object-type options |
| Duplicate materials created on reimport | Material names changed between exports | Freeze names by convention |
| Textures not found | Absolute or packed paths | Make paths relative; export textures separately |
| Animation length wrong | Frame range or frame rate mismatch | Match scene frame rate and export range |

## Delivery checklist

1. One asset exported, imported and verified end to end before batching.
2. Export settings saved as a preset or a script in the repo.
3. Naming convention followed for meshes, materials, textures and clips.
4. Source and export folders separated; paths relative.
5. Budgets recorded: triangles, material slots, texture resolutions.
6. Known caveats documented (e.g. green-channel flipping, unit settings).
7. The source .blend saved with the export setup intact.
