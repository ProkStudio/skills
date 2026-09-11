---
name: minecraft-terraforming
description: Shape believable Minecraft terrain in Java 1.21+ - mountains, ridges, valleys, cliffs, canyons, plateaus, islands, hills, dunes, rivers, lakes, waterfalls, beaches, caves and biome transitions. Use whenever the user wants to terraform or landscape, fix flat or blocky ground, remove a superflat platform, blend a build into a hillside, join two biomes, carve a river or a lake, raise a mountain or an island, build a garden or a park, or make vanilla worldgen look hand-made. Covers slope ratios, three-layer rock strata, erosion and scree, noise and smoothing rules, surface material blending, vegetation layering with custom trees, water features with correct flow distances, and a staged WorldEdit, Axiom and WorldPainter workflow with vanilla-only and survival fallbacks.
version: 1.0.0
---

# Minecraft Terraforming

Terrain is a build. It gets massing, silhouette, materials and detail passes exactly like
architecture - and it is finished when it looks like the world was always that way.

**Target:** Java Edition 1.21+. Gated blocks (tuff 1.21, pale moss 1.21.4, leaf litter and dry
grass 1.21.5) are marked; verify anything else in
`../../building/minecraft-block-palettes/references/version-gates.md`.

**Companions:**

| Skill | Takes over when |
| --- | --- |
| `../../building/minecraft-architecture/references/terrain-integration.md` | The joint between one building and the ground |
| `../../building/minecraft-organic-shapes/SKILL.md` | Individual rocks, cliffs, custom trees, statues, curve maths |
| `../../building/minecraft-settlements/SKILL.md` | Terrain that has to carry roads, plots and districts |
| `../../building/minecraft-block-palettes/SKILL.md` | Which surface and stone blocks exist in the user's version |

## Non-negotiables

1. **Ask 2-3 questions first** (Step 0) - scale, tooling and whether the world is survival or
   creative change every later decision.
2. **Never deliver a single smooth cone or dome of dirt.** Terrain needs a dominant ridge, a
   secondary spur and a broken outline, same as a building's massing.
3. **No 45-degree everything.** Pick slope ratios per zone from `references/landforms.md`.
   Uniform slope is the #1 tell of hand-raised terrain.
4. **Three vertical layers minimum**: bedrock/stone strata, subsurface (dirt, coarse dirt,
   gravel), surface (grass, podzol, moss, sand). A grass skin over a stone lump reads as fake.
5. **Erode after you build.** Scree at the foot of every cliff, softened ridgelines, rounded
   plateau edges. `references/erosion-and-detail.md`.
6. **No single-block noise.** Isolated blocks scattered on a slope look like a rash; use patches
   of 3-8 blocks with feathered edges.
7. **Water obeys physics**: water spreads 7 blocks horizontally from a source, lava 3 in the
   Overworld and 7 in the Nether. Design channels around that, not against it.
8. **Answer in the user's language**, with English block ids in brackets so commands work.

## Step 0 - Ask 2-3 questions

Default trio:

1. **Scale and purpose** - "a 30x30 garden around a house, a 200-block mountain range, or a
   whole island?"
2. **Tooling** - vanilla hand-placing, commands, WorldEdit/FAWE, Axiom, or WorldPainter for a
   whole map? This changes the entire delivery format.
3. **Site and mood** - which biome, what is already there, what must survive the edit
   (existing builds, spawn, farms)?

Swap in: survival or creative (survival means shovel/pickaxe economics and TNT), whether the
terrain serves a build or is the subject, reference real landscape (alpine, fjord, karst,
badlands, atoll), and render or gameplay priority.

## Step 1 - Read the site

Before touching anything, note: the dominant terrain line (ridge or shore), existing water
level, biome boundaries, sun direction for the main view, and where the player will stand.
Terraform for that viewpoint first.

Mark the footprint with a temporary block (wool) so the edit has boundaries. Terrain edits
without an edge always creep and never blend.

## Step 2 - Massing

Read `references/landforms.md` and pick a landform, then lay the skeleton:

- Draw ridgelines and valley floors as **lines first**, at final height, before any volume.
- One dominant mass (~60% of the height), one secondary (~30%), a few minor spurs (~10%).
- Ridgelines bend and branch; they never run straight for more than ~10 blocks.
- Valleys are V-shaped near peaks and U-shaped downstream - water widens them as it descends.
- Silhouette test: look at the black outline against the sky. If it is one hump, redesign.

## Step 3 - Slopes and profile

Assign a slope per zone (`references/landforms.md` has the ratio table):

| Zone | Ratio | Angle | Reads as |
| --- | --- | --- | --- |
| Valley floor, meadow | 1:6 to flat | <10 deg | Walkable, buildable |
| Foothill | 1:3 | 18.4 deg | Gentle, plantable |
| Main slope | 1:2 | 26.6 deg | Alpine, still climbable |
| Steep face | 1:1 | 45 deg | Rock, needs stone showing |
| Cliff | 2:1 to vertical | 63-90 deg | Exposed strata, scree below |

Concave at the bottom, convex at the top - a real hill flares out as it meets the plain. A
straight-line profile from base to peak is the second-biggest tell after uniform slope.

## Step 4 - Strata and materials

Read `references/erosion-and-detail.md`. Rock is layered, not homogeneous: horizontal bands of
2-5 blocks of stone, andesite, granite, diorite, tuff (1.21+) and deepslate below y=0, with the
bands bending as the terrain bends. Surface material follows slope and aspect: grass on gentle
and north faces, coarse dirt and gravel on steep ones, bare stone above the tree line.

## Step 5 - Erosion pass

The pass that separates hand-made from generated:

- Scree/talus fans of gravel and cobble at the foot of every cliff, widest below gullies.
- Gullies and dry channels down the fall line, 2-4 wide, deeper as they descend.
- Rounded ridge crests and plateau edges (1-2 block step-back per layer).
- Undercut cliffs and overhangs - at least one per 30 blocks of cliff face.
- Boulders detached from the parent rock, 3-8 blocks, half-buried, clustered near the cliff.

## Step 6 - Water

Read `references/water-and-coasts.md`. Rivers meander, lakes have varied depth and a shelf,
waterfalls need a plunge pool and spray vegetation, coasts alternate beach, rock and wetland.

## Step 7 - Planting and biome blending

Read `references/biomes-and-planting.md`. Vegetation is three layers (canopy, shrub, ground
cover), clustered by species, denser in valleys and on shaded slopes, absent from ridges and
exposed rock. Biome transitions need a mixed zone of 10-20 blocks, never a straight seam.

## Step 8 - QA before delivering

- [ ] Silhouette has a dominant mass, a secondary mass and a broken outline.
- [ ] No uniform slope; profile is concave low, convex high.
- [ ] Three vertical material layers present; strata visible in every exposed face.
- [ ] Scree at every cliff foot; at least one overhang per major face.
- [ ] No isolated single-block noise; patches are 3-8 blocks with soft edges.
- [ ] Water flows correctly, no floating source blocks, no 1-block flat-bottom lakes.
- [ ] Vegetation clustered, layered, with negative space left open.
- [ ] Biome seams blended over 10+ blocks.
- [ ] Edit blends into untouched terrain at the boundary - stand at the seam and check.
- [ ] Chunks reloaded (F3+A) after bulk placement so grass, water and light update.

## Delivery format

Adapt to the tooling from Step 0:

- **Hand-placed / survival** - stage order, block counts per stage, and a "do this first"
  sequence: ridgelines -> volume -> strata -> surface -> erosion -> water -> planting. Give
  heights as y-values relative to the existing ground, and tell the user which tools
  (shovel with Efficiency, TNT for bulk removal, water buckets for rapid gravel clearing).
- **Commands** - `/fill` and `/clone` for bulk moves, with the warning that `/fill` edges are
  always visible and need a manual erosion pass.
- **WorldEdit / FAWE / Axiom** - brush, mask and smoothing recipes from
  `references/tools-and-workflow.md`, in the order they should be applied.
- **WorldPainter** - heightmap and layer workflow for whole-map work, then in-game detailing.

Always end with 2-3 concrete levers: "raise the secondary ridge 6 blocks", "push the river
mouth 10 blocks east to open a delta".

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Looks like a pile of dirt" | No ridgeline skeleton | Step 2 - lines before volume |
| "Looks like a pyramid / cone" | Uniform slope from base to peak | Step 3 - vary ratio per zone, concave-convex profile |
| "Terrain looks like plastic" | One surface block, no strata | Step 4 - three layers, bent bands |
| "Mountain looks new / raw" | No erosion pass | Step 5 - scree, gullies, overhangs, boulders |
| "Blocky staircase edges" | `/fill` or brush edges left raw | Smooth pass + manual patches, `references/tools-and-workflow.md` |
| "Noise looks like measles" | Single scattered blocks | Patches of 3-8, feathered |
| "Lake looks like a swimming pool" | Flat bottom, hard edge | Varied depth, shelf, gravel/clay shore |
| "River is a canal" | Straight channel, constant width | Meanders, undercut outer bends, varied width |
| "Biomes cut with a knife" | No transition zone | 10-20 block mixed zone, matching plants both sides |
| "Grass on vertical walls" | Surface layer applied to cliffs | Stone and gravel on anything above 45 degrees |
| "Build now floats above the new ground" | Terraformed after building | Re-cut the foundation into the new surface, fill voids |

## References

| File | Read it when |
| --- | --- |
| `references/landforms.md` | Choosing and massing a landform, slope ratios, scale tables |
| `references/erosion-and-detail.md` | Strata, scree, gullies, surface blending, the detail pass |
| `references/water-and-coasts.md` | Rivers, lakes, waterfalls, coasts, wetlands, underwater |
| `references/biomes-and-planting.md` | Vegetation layering, custom trees, biome transitions, parks |
| `references/tools-and-workflow.md` | WorldEdit/FAWE/Axiom/WorldPainter recipes, survival workflow |
