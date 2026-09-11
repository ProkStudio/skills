# Spritesheets, pivots and export

## Sheet layout

| Layout | When |
| --- | --- |
| One row per animation, frames left to right | Default; easy to read and hand-edit |
| One column per direction, rows per animation | Top-down and eight-direction sets |
| Packed atlas with metadata | Many odd-sized sprites; requires a packer and JSON |

Rules:

- Uniform cell size within a sheet. Variable cells save memory and cost hours of debugging.
- Size the cell for the *largest* frame including smears and weapon extension, then centre
  everything in it. Cropping frames individually breaks alignment.
- Keep the same frame order everywhere: idle, walk, run, jump, fall, land, attack, hit, death.
- Leave 1-2 px of transparent padding around each cell, or extrude edge pixels, to prevent atlas
  bleeding (`../../game-art-pipeline/references/atlases-and-export.md`).

## Pivots and anchors

- Characters: pivot at the centre of the feet. Everything lines up on ground contact.
- Projectiles and effects: pivot at the visual centre, or at the muzzle/contact point if it attaches.
- Held items: define an explicit hand anchor in a fixed pixel position per frame; note it in the
  sheet's metadata or with a 1 px marker pixel on a separate layer.
- Never change the pivot mid-set. If a frame needs the character taller, extend the cell upward,
  not the pivot.
- Snap pivots to whole pixels. A half-pixel pivot plus a camera at a fractional position is the
  classic source of "my sprite shimmers".

## Naming and tagging

```
character_knight_idle_01.png
character_knight_walk_01..08.png
knight.aseprite        # source, with one tag per animation
knight.png             # exported sheet
knight.json            # frame durations, tags, pivots
```

- Lowercase, underscore-separated, zero-padded frame numbers.
- One source file per character with tagged frame ranges beats dozens of loose PNGs.
- Tag names match the state names in code, exactly. "attack_heavy" in art and "HeavyAttack" in code
  guarantees a mapping table nobody maintains.

## Per-frame durations

Store durations with the art, not in code. Aseprite frame durations survive into its JSON export,
and every engine can read them via a small importer. If durations live in code, animators cannot
iterate without a programmer - which in practice means timing never gets fixed.

A minimal export from the command line looks like:

```
aseprite -b knight.aseprite --sheet knight.png --data knight.json \
  --format json-array --sheet-pack --inner-padding 1 \
  --filename-format "{tag}_{tagframe}"
```

Check the exact flags with `aseprite --help`; they change between versions.

## Root motion versus code movement

- Default: the sprite animates in place, code moves the entity. Simple, predictable, but requires
  the stride length of the walk cycle to match the movement speed or the character skates.
- Stride matching: distance travelled per cycle = movement speed x cycle duration. If a 8-frame
  walk at 12 fps covers 0.67 s and the character moves 40 px/s, the cycle must cover about 27 px -
  roughly 13 px per step.
- Baked-in displacement (root motion) suits dashes, lunges and attacks that should move the
  character exactly as drawn. Then code must not add its own translation for those frames.

## Consistency across frames

- Keep the palette fixed. A single off-palette pixel in one frame flickers.
- Lock dither and texture patterns to the form, not the frame, or they crawl.
- Redraw rather than transform: rotating or scaling a pixel frame ruins the grid
  (`../../pixel-art-fundamentals/references/canvas-and-density.md`).
- Check the set by playing it at 3x speed - drift, pops and stray pixels appear immediately.

## Handoff checklist

1. Uniform cell size, padding, one row per animation.
2. Pivot documented and identical across the set.
3. Tags match code state names.
4. Durations exported with the sheet.
5. Sheet tested in engine at 1:1 with point filtering.
6. Source file committed alongside the export.
