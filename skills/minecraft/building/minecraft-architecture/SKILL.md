---
name: minecraft-architecture
description: Design and build non-generic Minecraft architecture for Java 1.21+. Use whenever the user wants to build, design, improve or critique anything in Minecraft - house, base, camp, castle, fortress, wall, tower, village, town, city, farm, tech build, shop, bridge, interior or decoration - or asks to make a build prettier, less boxy, more detailed, more varied, or in a named style such as medieval fantasy, Japanese, modern minimal, nordic rustic or steampunk industrial. Covers massing and silhouette, a roof catalogue that replaces the default stair gable, block palettes and texturing, facade depth and detailing, terrain integration, interiors, settlement layout, an anti-sameness variation engine, and fixes for glass panes, iron bars, fences and walls that render as lone disconnected posts. Always asks 2-3 clarifying questions before building.
version: 1.0.0
---

# Minecraft Architecture

Build principles, not blueprints. Decide every design question deliberately from the
context, then hand the player a plan they can actually place block by block.

**Target:** Java Edition 1.21+ (creative, unlimited blocks). Blocks from 1.20-1.21 such as
bamboo planks, cherry wood, tuff bricks, chiseled/grate/bulb copper, decorated pots and
pale oak are fair game; say so when a block is version-gated.

## Non-negotiables

1. **Ask 2-3 questions first** (Step 0). Never start building on a one-line prompt.
2. **Never deliver a box.** A single rectangular volume with one roof is a failure, even
   when the detailing is good.
3. **Choose the roof on purpose** from `references/roofs.md`. A single unbroken stair run
   from eave to ridge on every building is the #1 tell of generated builds.
4. **Roll the variation matrix** (`references/variation-engine.md`) and state the rolled
   combination. Two builds in one session must not share footprint + roof + accent.
5. **Palette in tiers**, never one material per surface. See `references/palette-and-texture.md`.
6. **Never write connection blockstates** (`north=`, `east=`, `up=`) for panes, bars, walls
   or fences in commands, and frame pane windows with full blocks. See
   `references/block-connection-rules.md`.
7. **Answer in the user's language**, with block names the user can find in the creative
   inventory (English block ids in brackets when the chat language is not English).

## Step 0 - Ask 2-3 questions

Pick the 2-3 questions whose answers would most change the design, and no more. Never ask
something the user already answered. Offer a default for each so the user can say "just do
it" and get a good build anyway.

Default trio when nothing is known:

1. **What and how big** - "cottage for one player, manor, or 40-block keep?"
2. **Style** - offer 2-3 concrete options from `styles/` fitting the request.
3. **Site** - biome, flat or slope, existing neighbours to match.

Swap in these when more relevant:

- **Purpose/program** - what has to fit inside (storage, farms, portal, 6 beds)?
- **Placement method** - hand-placed in creative, `/setblock` + `/fill`, or WorldEdit? This
  changes the delivery format and the block-update warnings.
- **Must-match** - an existing build, palette or world save to blend with.
- **Freedom** - "may I change the terrain / add outbuildings?"
- **Interior** - full interior or shell only?

After the answers, restate the brief in 2-3 lines, then design.

## Step 1 - Brief and constraints

Write down, explicitly: build type, style, footprint budget, height budget, floor count,
site shape, placement method, interior yes/no. Everything downstream references this.

Scale discipline: a 1-wide door and 3-high walls read as a doll house. For anything above
cottage scale use 2-wide entries, 4-5 block interior floor heights, and detail motifs that
scale with the building (a 30-block keep needs 2-3 block cornices, not more 1-block trim).

## Step 2 - Massing and silhouette

Read `references/massing-and-silhouette.md`.

Short version: footprint is never a single rectangle (L, T, U, cross, or a core plus
satellites). Break the volume into a dominant mass (~60%), a secondary mass (~30%) and
small attachments (~10%). One element must break the height line by at least 1.5x. Test the
build as a black silhouette against the sky - if the outline is a rectangle, redesign before
placing a single detail block.

## Step 3 - Structure and openings

Decide the structural logic before decoration, then let decoration express it:

- Corner and bay columns (logs, pillars, quoins) on a repeating rhythm of 3-5 blocks.
- Floor lines readable from outside (string course, beam band, material change).
- Window rhythm as a pattern, e.g. A-B-A per bay, not one window every block.
- Load path that makes sense - overhangs sit on brackets, upper floors on beams.

Window openings 2 wide or more when a glass surface is wanted; 1-wide openings always look
like posts (that is the pane rule, not a bug).

## Step 4 - Roof

Read `references/roofs.md` and pick a roof type that fits the span, style and silhouette.
At least one of: changed pitch, dormer, hip, valley, chimney, ridge cap or overhang must
break the roof plane. An L/T footprint from Step 2 gives valleys for free.

## Step 5 - Palette

Read `references/palette-and-texture.md` and the chosen file in `styles/`. Lock a base
(~60%), secondary (~30%), accent (~10%), plus trim and glass/light blocks. Within each tier
use 2-3 blocks of similar value and different texture, placed in irregular patches of 2-5
blocks - never a checkerboard, never uniform noise.

## Step 6 - Depth and detail

Read `references/facade-depth-and-detail.md`. Depth comes from offsets in and out of the
wall plane (recessed windows, protruding plinth and pilasters, cornices, overhangs), not
from sprinkling decoration on a flat wall. Keep roughly two thirds of every surface calm so
the detailed third reads.

## Step 7 - Terrain and surroundings

Read `references/terrain-integration.md`. No flattened square pad, no floating corners.
Foundation follows the ground, paths and planting tie the build to the site, and the
building orientation follows the dominant terrain line rather than the compass.

## Step 8 - Interior

Read the interiors section of `references/build-types.md`. Ceiling structure, floor zoning,
a focal point per room, hidden lighting, and interior windows that line up with the exterior
openings.

## Step 9 - QA before delivering

Run this checklist and fix what fails:

- [ ] Top-down outline is not a rectangle; silhouette has 3+ height steps.
- [ ] Roof is not one continuous stair run; roof plane is broken at least once.
- [ ] 3+ material tiers; no surface is a single flat material.
- [ ] Wall plane offset in and out at least twice per facade.
- [ ] Base course present; no floating or half-buried corners; terrain not flattened.
- [ ] Pane/fence/wall runs connect - full-block jambs, no explicit blockstates, reload
      chunks with F3+A after bulk placement.
- [ ] Light sources hidden or stylistically justified; interior lit.
- [ ] Variation matrix combination stated and different from the previous build.
- [ ] Interior windows match exterior openings.

## Delivery format

Adapt to the placement method from Step 0:

- **Hand-placed (default)** - a short design brief (massing, roof, palette, motifs) plus a
  build order in stages: footprint -> base course -> structure -> walls -> openings -> roof
  -> details -> terrain -> interior. Give dimensions and layer counts ("eave at y+5, roof
  rises 1 per 2 blocks over 8"), plus the block list per tier. Coordinates only when the
  user gave some.
- **Commands** - `/fill` and `/setblock` lines for the bulk shapes only, with rotation states
  for stairs/logs spelled out, and connection states deliberately omitted.
- **WorldEdit** - brush/selection workflow plus the block-update warning from
  `references/block-connection-rules.md`.

Always end with 2-3 concrete variation levers the user can pull ("swap the gambrel for a
half-hip", "push the wing 3 blocks east") instead of a generic offer to help.

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "It made me a box" | No massing step | Step 2 - footprint shape and 3-mass split before anything else |
| "Every roof is a staircase" | Default 45 degree stair gable | `references/roofs.md` - pick by span, vary pitch, break the plane |
| "All my houses look the same" | Same skeleton, different textures | `references/variation-engine.md` - roll footprint, roof, height, motif, not just materials |
| "Looks flat / like a texture pack demo" | Detail applied on an unbroken plane | Step 6 - offsets, plinth, cornice, recesses first |
| "Panes and fences are lone posts" | Explicit blockstates, no block update, or non-solid neighbours | `references/block-connection-rules.md` |
| "Build floats on a flat square" | Terrain flattened for convenience | Step 7 - stepped foundation, retaining walls, planting |
| "Palette is muddy" | Too many materials, no value contrast | Step 5 - 3 tiers, contrast by value first |
| "Big build feels small" | Detail motifs not scaled | Step 1 - scale anchors, 2-3 block trim on large masses |

## References

Read on demand, not all at once:

| File | Read it when |
| --- | --- |
| `references/massing-and-silhouette.md` | Any new build, before placing blocks |
| `references/roofs.md` | Choosing or fixing a roof |
| `references/palette-and-texture.md` | Choosing blocks, fixing muddy or flat colours |
| `references/facade-depth-and-detail.md` | Walls, windows, entrances, trim |
| `references/block-connection-rules.md` | Panes, bars, fences, walls, chains, or any bulk/command placement |
| `references/terrain-integration.md` | Siting the build, slopes, paths, planting |
| `references/build-types.md` | Houses, castles, villages, farms, tech builds, interiors |
| `references/variation-engine.md` | Anything repeated - villages, districts, multiple requests |
| `styles/<style>.md` | Style chosen in Step 0 |

Styles available: `medieval-fantasy`, `japanese`, `modern-minimal`, `nordic-rustic`,
`steampunk-industrial`. If the user asks for a style with no file, build the closest one and
say which principles you transferred.
