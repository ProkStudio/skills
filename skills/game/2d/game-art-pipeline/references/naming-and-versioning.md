# Folders, naming and versioning

## Folder structure

Separate sources from exports so nobody edits a generated file:

```
art/                      # sources, never loaded by the engine
  characters/
    player/player.aseprite
    slime/slime.aseprite
  tilesets/
    forest.aseprite
  ui/
    panels.aseprite
    icons.aseprite
  vfx/
  palettes/
    project.gpl
assets/                   # exports, loaded by the engine
  characters/
    player.png
    player.json
  tilesets/
    forest.png
  ui/
  vfx/
tools/
  export_all.sh
  validate_palette.py
```

Alternative for engines with strict asset folders (Unity `Assets/`, Godot `res://`): keep `art/`
outside the engine folder, or exclude it from import so sources are not processed.

## Naming conventions

- Lowercase, hyphens or underscores, never spaces or non-ASCII characters.
- Pattern: `category_subject_variant_state_frame`, for example
  `enemy_slime_green_walk_03.png`, `ui_panel_dialogue.png`, `tile_forest_grass.png`.
- Zero-pad frame numbers so they sort correctly: `01`, `02`, ... `10`.
- Animation tag names must match the state names used in code, exactly.
- Do not encode sizes or dates in filenames (`icon_32_v2_final.png` always becomes a lie); let the
  folder and version control carry that information.

## Source-file hygiene

- One source file per subject with tagged animations, not dozens of loose files.
- Named layers and layer groups; delete scratch layers before committing.
- Keep the palette in the file (and in the repo as a separate palette file).
- Document the canvas size and pivot convention in the file (a note layer works).
- Never scale or rotate inside the source file; keep it at authoring resolution.

## Version control for binary art

- Binary files cannot be merged. Two people editing the same `.aseprite` means one of them loses
  work: agree on ownership per file, or lock files.
- Use Git LFS (or the engine's own asset server) for `.psd`, `.aseprite`, large PNGs and audio.
  Without LFS, repository size grows with every export.
- Commit both sources and exports if the engine needs the exports at build time; otherwise generate
  exports in CI and gitignore them. Pick one policy and write it down.
- Commit messages should name the asset and the change: "player: add 8-frame run cycle".
- Tag milestone builds so art can be rolled back with the code that expects it.

## Automation

Three small scripts remove most pipeline friction:

1. `export_all` - regenerate every sheet and atlas from sources, deterministically.
2. `validate` - check canvas sizes, palette conformance, naming pattern, presence of metadata files.
3. `report` - list texture memory per scene and flag assets not referenced anywhere.

Run validation in CI on pull requests; art problems found automatically are cheap, art problems found
in a build review are not.

## Handoff to programmers

Provide with every asset:

- Canvas/cell size and pixel scale.
- Pivot/anchor position.
- Animation tags with frame ranges and durations.
- 9-slice insets and inner padding for UI.
- Collision or interaction notes if the art implies them (platform surfaces, hitbox extents).
- Palette file and whether palette swapping is expected.

## Review checklist before merging art

1. Correct canvas size and pixel density for its class.
2. On-palette (validation script passes).
3. No stray pixels, no accidental anti-aliasing, no semi-transparent edges in strict projects.
4. Pivot consistent with the rest of the set.
5. Naming matches the convention; frames zero-padded.
6. Metadata file exported alongside the image.
7. Tested in engine at 1:1 and at the maximum supported scale.
8. Tested over the busiest background, and in the darkest lighting state.
9. Source file committed, layers named, no scratch layers.
10. No engine settings changed silently as part of the art commit.
