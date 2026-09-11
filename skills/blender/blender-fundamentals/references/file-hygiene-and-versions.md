# Files, assets and Blender versions

## Folder layout

```
project/
  blend/
    prop_barrel_v003.blend
    prop_barrel_v003.blend1        (Blender's auto backup)
  textures/
    barrel_basecolor.png
    barrel_normal.png
  refs/
    photos/, blockout.png
  export/
    prop_barrel.glb
  renders/
    barrel_turntable_0001.png
```

- Keep textures external and referenced with **relative paths** (`//../textures/`). File > External
  Data > Make Paths Relative.
- Pack textures only for handoff or archiving (File > External Data > Pack Resources); packed files
  balloon in size and hide what the asset actually depends on.
- Report missing textures with File > External Data > Report Missing Files; fix with Find Missing
  Files.

## Versioning

- Number files: `asset_v001.blend`, `asset_v002.blend`. Never `final`, `final2`, `final_real`.
- Blender writes a `.blend1` backup of the previous save automatically (Preferences > Save & Load >
  Save Versions). Raise it to 2-3 if disk space allows.
- Autosave (Preferences > Save & Load) writes temporary files; recover with File > Recover > Auto
  Save or Last Session after a crash.
- Git works for .blend files only with LFS, and binary files cannot be merged: one owner per file,
  or explicit locking. Commit exports and textures alongside so a checkout is usable.
- Save a new version before: applying modifiers, remeshing, decimating, retopologising, rigging, or
  any "let me just try something" experiment.

## Keeping files small and clean

1. **Purge orphans**: File > Clean Up > Unused Data-Blocks (recursive). Removes materials, images,
   node groups and meshes nobody references.
2. **Check for fake users** (shield icon) holding data alive on purpose; clear them if unintended.
3. **Unpack resources** if the file was packed and you no longer need it self-contained.
4. **Delete sculpt multires levels** you will never use again, after baking.
5. **Remove duplicate materials** (`mat_steel.001`, `.002`) by reassigning slots to one data-block.
6. **Outliner > Blender File / Orphan Data** views show what is actually in the file, which is the
   fastest way to find the 400 MB nobody wanted.

## Asset libraries

- Mark any object, material, node group, world or pose as an asset (right click > Mark as Asset); it
  then appears in the Asset Browser.
- Preferences > File Paths > Asset Libraries points at a folder of .blend files. Every marked asset
  inside becomes available for drag and drop.
- Give assets a catalog, description and preview; an unlabelled library is unusable within a month.
- Dragging in from a library can append or link, depending on the Asset Browser's import method.
  Link plus Library Override is the pipeline-friendly choice.

## Blender release landscape

The 5 series covers 2025-2027. Relevant releases:

| Version | Released | Notes |
| --- | --- | --- |
| 5.2 LTS | 14 July 2026 | Current stable LTS; long-term support target |
| 5.1 | 17 March 2026 | Libraries aligned with VFX Platform 2026, Python 3.13 |
| 5.0 | 18 November 2025 | Much faster material compilation, updated viewport MatCaps |
| 4.5 LTS | 15 July 2025 | Previous LTS; still common in pipelines |
| 4.2 LTS | 16 July 2024 | EEVEE Next introduced; support ended July 2026 |

Choosing a version:

- **Studio or team work**: pin to an LTS (currently 5.2 LTS) and upgrade deliberately.
- **Solo work chasing features**: the latest stable release is fine, but never upgrade mid-project.
- **Addons decide it in practice**: check that every addon you depend on supports the version first.
- Blender opens older files but not newer ones. A file saved in 5.2 may not open in 4.5, so agree on
  a version before sharing files.
- Big things to know when reading older tutorials: AgX replaced Filmic as the default view transform
  in 4.0 (Filmic is deprecated), the Principled BSDF was reorganised in 4.0, and EEVEE Next replaced
  the old EEVEE in 4.2 with different settings and much better shadows and raytracing.

## Handoff checklist

1. All objects and data-blocks named; no `Cube.001`.
2. Transforms applied where required; scale 1, 1, 1.
3. Textures external with relative paths, or packed on purpose.
4. Orphan data purged; file size sane.
5. Collections reflect what the recipient needs (high, low, cages, refs).
6. A README or note in-file stating scale, units, target engine and version used.
7. Exports regenerated from the current file, not from an older one.
