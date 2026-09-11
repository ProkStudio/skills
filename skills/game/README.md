# Game skills

Skills for making games: art, design, and the technical glue between them.

## Structure

```
skills/game/
  2d/          2D game art and interface skills
  minecraft/   Minecraft building skills (see note below)
```

> **Note on `minecraft/`**: the Minecraft skills currently still live at `skills/minecraft/`. Moving
> a directory is a single git operation but cannot be done through the GitHub file API, so run this
> locally once:
>
> ```bash
> git mv skills/minecraft skills/game/minecraft
> git commit -m "Move minecraft skills under game/"
> git push
> ```
>
> Every cross-link inside that tree is relative, so nothing breaks after the move.

## 2D art and interface skills

| Skill | Use it for |
| --- | --- |
| [pixel-art-fundamentals](2d/pixel-art-fundamentals/SKILL.md) | Canvas size and pixel density, clean lines and anti-aliasing, shading and form, dithering and texture, critique of a sprite |
| [color-and-palettes](2d/color-and-palettes/SKILL.md) | Ramps and hue shifting, building a limited palette, contrast and readability, known palettes and palette swaps |
| [sprite-animation](2d/sprite-animation/SKILL.md) | Frame budgets and timing, walk/run/jump cycles pose by pose, attack anatomy and hit feel, spritesheets and pivots |
| [tilesets-and-environments](2d/tilesets-and-environments/SKILL.md) | Tile grids and autotiling schemes, seamless tiles, breaking repetition, parallax and depth, level composition |
| [vfx-and-lighting-2d](2d/vfx-and-lighting-2d/SKILL.md) | Effect anatomy and frame budgets, 2D lighting and shadows, hit-stop, screen shake, juice per player action |
| [game-ui-and-hud](2d/game-ui-and-hud/SKILL.md) | HUD layout and UI classes, widgets and all their states, fonts and icons, menu navigation, accessibility |
| [game-art-pipeline](2d/game-art-pipeline/SKILL.md) | Base resolution and integer scaling, pixel-perfect rendering, atlases and export, engine import settings, naming and versioning |

## Suggested reading order

1. **pixel-art-fundamentals** - the drawing craft everything else assumes.
2. **color-and-palettes** - pick the palette before producing assets.
3. **sprite-animation** - characters and anything that moves.
4. **tilesets-and-environments** - the world the characters move through.
5. **vfx-and-lighting-2d** - mood and feedback on top of that world.
6. **game-ui-and-hud** - the layer the player reads under pressure.
7. **game-art-pipeline** - read this early if art already looks wrong in engine.

Shortcuts by symptom:

| Problem | Start here |
| --- | --- |
| "Sprite looks flat / muddy / noisy" | `2d/pixel-art-fundamentals/references/critique-checklist.md` |
| "Colours look dull or muddy" | `2d/color-and-palettes/references/ramps-and-hue-shifting.md` |
| "Animation looks robotic or floaty" | `2d/sprite-animation/references/timing-and-spacing.md` |
| "Level looks like graph paper" | `2d/tilesets-and-environments/references/grids-and-autotiling.md` |
| "Combat feels weak" | `2d/vfx-and-lighting-2d/references/juice-and-feedback.md` |
| "UI looks amateur" | `2d/game-ui-and-hud/references/widgets-and-states.md` |
| "Art is blurry / shimmering in engine" | `2d/game-art-pipeline/references/pixel-perfect-rendering.md` |

## Skill layout

Each skill follows the same shape:

```
<skill-name>/
  SKILL.md              # when to use, what to ask, workflow, failure modes
  references/*.md       # the detailed material, loaded on demand
```

`SKILL.md` stays short enough to read in full; the `references/` files carry the tables, numbers and
step-by-step procedures.

## Conventions

- Frontmatter: `name` must equal the folder name, `description` under 1024 characters, `version`
  following semver.
- Links between skills are relative: `../<skill>/SKILL.md` from a sibling `SKILL.md`, and
  `../../<skill>/references/<file>.md` from inside a `references/` file.
- Every skill lists concrete numbers (frame counts, px sizes, contrast ratios) rather than adjectives.
- Validate the repo after edits with `python scripts/validate_skills.py` (this has not been run for
  the skills added here, since they were pushed through the GitHub API rather than from a clone).
