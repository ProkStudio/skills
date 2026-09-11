# Tools and workflow

Pick the tooling in Step 0 and deliver in that format. Terrain is where tool choice changes the
answer most.

## Order of operations (all tools)

1. Mark the edit boundary (wool) and note sea level and existing build heights.
2. Ridgelines and valley floors as lines.
3. Bulk volume (brush, `/fill`, or hand).
4. Smooth pass - **before** strata and surface.
5. Strata bands in exposed faces.
6. Surface layer by slope and aspect.
7. Erosion: scree, gullies, crest rounding, overhangs, boulders.
8. Water: channels sealed, then filled.
9. Planting in three layers.
10. Seam pass at the boundary, then F3+A to reload chunks.

Skipping 4 before 5 is the most common mistake: smoothing after strata deletes the bands.

## Vanilla / survival

- **Bulk removal:** TNT for rock (cheap in creative, viable in survival with a duper),
  Efficiency V + Haste beacon for stone, water bucket + gravel/sand for fast clearing (flowing
  water breaks gravity blocks into items).
- **Bulk placement:** dirt/stone from a farm or a mine; scaffolding to reach height fast;
  water elevators for vertical movement.
- Survival-friendly sequencing: do the heavy vertical work first while the scaffolding is up,
  then detail downward.
- Tell the user the rough block count per stage - a 40x40 hill 15 blocks tall is roughly
  8-12k blocks, which is the difference between an evening and a week.

## Commands (vanilla, no mods)

- `/fill x1 y1 z1 x2 y2 z2 <block>` - max 32768 blocks per command; split large volumes.
- `/fill ... replace <filter>` - e.g. replace only air, or only stone.
- `/fill ... hollow` or `outline` for shells.
- `/clone x1 y1 z1 x2 y2 z2 dest` - duplicate a hand-built hill or rock, then rotate the copy
  by hand so it does not read as a clone.
- `/setblock` for single corrections.
- Commands leave **perfectly straight edges** - always follow with a manual break-up pass.
- Gravity blocks placed by command do not fall until updated; a block update (or F3+A) drops
  them, which is either a trick or a trap.

## WorldEdit / FAWE

Core terrain kit:

| Command | Use |
| --- | --- |
| `//brush sphere <block> <r>` (`//br s`) | Bulk volume; hold with `//mask` to limit |
| `//brush cylinder <block> <r> <h>` | Plateaus, benches, flat pads |
| `//brush smooth <size> <iterations>` | The main smoothing tool; 1-2 iterations at a time |
| `//brush gravity <r>` | Drops floating blocks - cleans up after sphere work |
| `//mask <block>` / `//gmask` | Restrict the brush, e.g. `//gmask >air` to paint only exposed surfaces |
| `//replace <from> <to>` | Strata and surface swaps inside a selection |
| `//overlay <block>` | Lay a surface layer on top of whatever is exposed |
| `//naturalize` | Grass/dirt/stone layering in a selection - a fast Step 6 |
| `//smooth <iterations>` | Selection-wide smoothing |
| `//deform` | Mathematical warping for large-scale shaping |
| `//sphere`, `//hsphere`, `//cyl`, `//hcyl`, `//pyramid` | Primitives for rocks and towers |
| `//set <pattern>` with percentages | `//set 60%gravel,25%cobblestone,15%stone` for scree mixes |
| `//stack`, `//move` | Extend ridges, shift a landform |
| `//undo` / `//redo` | Always announce that terrain work is iterative |

FAWE extras worth naming: `//br erode`, `//br splatter`, `//br layer`, `//br scatter`, and
`//paste -e` for schematics with entities.

Pattern trick: use percentage patterns for every natural mix instead of placing single blocks
by hand, then break the result up manually in the 10% of places the player will stand.

## Axiom (creative, in-game editor)

- Sculpt, blend, erode and flatten brushes with live preview - closest thing to a terrain
  sculptor inside Minecraft.
- Best for: large organic landforms, blending an edit into existing terrain, quick iteration on
  silhouette.
- Still needs the manual passes: strata, surface variety, scree, planting.

## WorldPainter (out-of-game, whole maps)

- Heightmap-based: paint elevation, then apply biome and layer brushes, then export the world.
- Best for: continents, islands, mountain ranges, custom maps where terrain comes before builds.
- Workflow: rough heightmap -> biomes -> ground cover layers -> export -> in-game detail pass
  for everything within 60 blocks of a viewpoint or a build.
- Caveat: exported terrain is smooth and uniform; it always needs in-game erosion and strata
  where the player walks.

## Litematica / schematics

Useful for terrain in one specific way: build a rock, a tree or a cliff module once, save it,
then paste variations (rotated, mirrored, partially buried) instead of repeating the work. Vary
at least 20% of the blocks of each paste so the repetition does not read.

## Housekeeping

- **F3+A** reloads chunks after bulk edits so grass, water, light and leaf decay update.
- **F3+G** shows chunk borders - never let a terrain feature edge align with one.
- Work in a copy of the world, or at least `//undo`-safe steps, before large edits.
- Check the result from ground level, from 60 blocks up, and at night before calling it done.
