---
name: minecraft-settlements
description: Plan and build believable Minecraft settlements for Java 1.21+ - hamlets, villages, towns, cities, harbours, mining camps, fortresses, elven or desert settlements, server spawn hubs and city districts. Use whenever the user wants more than one building on a site, asks how to make a village or city look alive rather than like a row of identical houses, needs street layout, road hierarchy, districts, plot subdivision, public squares, walls and gates, landmarks, or wants an existing town to feel older and more organic. Covers site reading, centre-first layout, road widths, zoning ratios, plot staking, building mix and variation, history layering, props of daily life, villager and mob-proofing mechanics, and a staged build order for survival or creative.
version: 1.0.0
---

# Minecraft Settlements

A settlement is not a collection of houses; it is a **plan** with a centre, a road hierarchy,
districts, and a history. Players who build "10 houses" get a showroom. Players who build the
plan first get a town.

**Target:** Java Edition 1.21+, creative or survival, single player or server.

**Companion skills:**
- `../minecraft-architecture/SKILL.md` - every individual building (massing, facade, roof, palette).
- `../minecraft-interiors/SKILL.md` - the insides, once the shell list is fixed.
- `../minecraft-organic-shapes/SKILL.md` - roads, bridges, terraces, river banks, domes.

## Non-negotiables

1. **Ask 2-3 questions first** (Step 0). Scale, era/style and site change everything.
2. **Centre first, then roads, then plots, then buildings.** Never start with a house.
3. **The terrain decides the plan.** Roads follow contours, the centre sits on the flattest
   spot or the best landing, the wealthy quarter takes the high ground.
4. **Road hierarchy is mandatory.** At least three widths (main / secondary / alley). A town
   where every street is 3 wide reads as a maze.
5. **No two identical neighbouring buildings**, and no building type reused more than ~3 times
   per district without a changed roof, footprint or accent.
6. **Every settlement needs a reason to exist**: river crossing, mine, harbour, shrine, trade
   road, fortress. State it, then let it shape the plan.
7. **Stake out before building.** Mark roads and plot corners with a cheap block (wool,
   terracotta, concrete) and walk the plan first.
8. **Include life, not just buildings**: market stalls, laundry, carts, wells, crates, gardens,
   graveyard, lighting, signage.

## Step 0 - Ask 2-3 questions

1. **Scale** - hamlet (5-8 buildings), village (10-25), town (25-60), city (60+ / districts)?
2. **Style and era** - offer 2-3 concrete options (medieval European, Japanese, nordic,
   desert, steampunk, modern) and match `../minecraft-architecture/styles/`.
3. **Site and purpose** - flat plains, valley, hillside, coast, island, nether? Survival town
   that must work with villagers and mob-proofing, or a cinematic build?

Optional: available area in blocks, placement method (hand / WorldEdit), whether an existing
village must be absorbed.

Restate the brief in 2-3 lines, including the settlement's reason to exist, then plan.

## Step 1 - Read the site

- Walk it. Note: flattest area, highest point, water access, river crossings, existing roads or
  villages, biome transitions, resources (mine, forest, farmland).
- Assign: **centre** (flat + accessible), **landmark site** (high or visible - church, keep,
  lighthouse, pagoda), **dirty functions** (downhill/downstream/downwind - tannery, smelter,
  farms), **expansion direction** (where the town grows next).
- Decide how much terraforming is allowed. Prefer adapting: terraces, retaining walls,
  stepped streets (see `../minecraft-organic-shapes/references/curves-paths-and-rivers.md`).

## Step 2 - Centre and landmark

Place the heart first: a market square, a well, a crossroads, a temple forecourt or a harbour
quay. Size: 7x7 for a hamlet, 11x15 for a village, 15x25+ for a town, with at least one side
defined by an important building.

Then fix 1-3 **landmarks** visible from outside: church/temple tower, keep, clock tower,
lighthouse, great tree, windmill. Landmarks terminate street views - point roads at them.

## Step 3 - Road skeleton

Read `references/layout-and-roads.md`. Lay the main road through or past the centre, then
secondary streets, then alleys. Hierarchy:

| Level | Width | Notes |
| --- | --- | --- |
| Main road / high street | 5-9 | Through the settlement, links the gates, widens at the square |
| Secondary street | 3-5 | Serves plot rows, connects districts |
| Alley / lane | 1-3 | Behind blocks, service access, stairs on slopes |

Prefer T-junctions to 4-way crossings in organic towns; use a grid only where the culture or
the terrain justifies it (colonial, Roman, modern, reclaimed flat land).

## Step 4 - Districts and program

Read `references/districts-and-program.md`. Assign land use and check the mix - a town needs
more than houses. Target ratios by area:

- Residential 50-60%
- Commercial / market 10-15%
- Civic & religious 10%
- Industrial / agricultural 15%
- Green & public space 10%

Each district gets its own density, building height range and one palette shift.

## Step 5 - Plots

Read `references/plots-and-building-mix.md`. Subdivide the blocks between streets into plots
*before* building: vary widths (5-11), keep depths consistent per row, mark the corners.
Corner plots get the special buildings. Leave 2-4 gaps for gardens, yards, wells and stalls.

## Step 6 - Buildings with variation

Build in **passes**, not one house at a time:

1. Footprints and floor counts for the whole district (silhouette pass).
2. Roofs for the whole district (check the roofscape from a distance - vary ridge directions).
3. Facades and palettes (2-3 block palette per district with per-building accents).
4. Details, then interiors for the buildings the player will enter.

Use `../minecraft-architecture/references/variation-engine.md` for the per-building variation,
and keep height mixed: tallest at the centre and along the main road, lowest at the edges.

## Step 7 - Public space, infrastructure, life

- Square: well/fountain/statue, stalls, benches, trees, a notice board (signs/item frames).
- Street furniture: lanterns every 8-10, hitching posts, barrels, crates, carts, laundry lines,
  flower boxes, signage over shop doors (hanging signs).
- Infrastructure: wall and gates, bridges, docks and cranes, mill, aqueduct or wells, drainage,
  graveyard, stables, guard posts.
- Farms and pastures on the outskirts, with fences following the contour and irregular field
  shapes.

## Step 8 - Age the town

Read `references/growth-and-history.md`. Add the chronology: an old crooked core, a newer
regular quarter, the line of a demolished wall as a ring road, patched masonry, a ruin, an
abandoned plot, wear on the busiest paths. This step is what separates a town from a diorama.

## Step 9 - QA before delivering

- [ ] Reason to exist is visible in the plan (crossing, harbour, mine, shrine).
- [ ] Centre reads as the centre: widest space, best buildings, most traffic.
- [ ] Three road widths present; roads follow terrain; every road ends at something.
- [ ] Land-use ratios roughly met; the town has civic, commercial and productive buildings.
- [ ] No two identical neighbours; no type repeated more than 3 times per district.
- [ ] Height mix: centre tall, edges low; roofscape varied in ridge direction.
- [ ] Plots fully used or intentionally empty (garden, yard, ruin) - no accidental gaps.
- [ ] Public space furnished; street lighting continuous (and spawn-safe on survival).
- [ ] Transition to nature: fields, orchards, tracks, scattered outbuildings - no hard edge.
- [ ] Survival extras: villager beds paired with workstations, mob-proof lighting (light level
      1+ on all walkable blocks), gates closable, iron golem spawn conditions understood.
- [ ] Silhouette checked from 3 approach directions and from above.

## Delivery format

Deliver a **staged plan**, not a pile of houses:

1. Stake-out list: road centrelines, square outline, plot corners (marker block + coordinates
   or relative layout sketch in text/ASCII).
2. District table: name, land use, palette, height range, building list.
3. Plot table: plot id, width x depth, building type, floors, roof type, notes.
4. Build order: roads -> terracing -> landmark shells -> district silhouettes -> roofs ->
   facades -> public space -> details -> interiors -> ageing.
5. Block palette list per district, plus the marker blocks to remove at the end.

For WorldEdit users mention `//stack` for repeating plot walls, `//brush` for terrain, and
`//copy`/`//paste` with rotation for reusing a building type (then edit 20% of it by hand).

End with 2-3 levers: "turn the north quarter into docks", "add a ring road on the old wall
line", "raise the temple 4 blocks so it closes the main street view".

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Looks like a row of houses" | No centre, no hierarchy, buildings first | Steps 2-3: centre, landmark, three road widths |
| "Feels empty / too spread out" | Plots too big, streets too wide | Tighten to 3-5 wide streets, plots 5-9 wide, party walls in the core |
| "All buildings look the same" | One footprint and roof repeated | Step 6 passes + variation engine; vary ridge direction and floor count |
| "Grid feels lifeless" | Perfect grid with 4-way crossings | T-junctions, offset blocks, curved edge streets, terrain-driven breaks |
| "No sense of place" | No landmark, no reason to exist | One tall landmark closing the main view + an economic reason |
| "Town ends abruptly" | Hard edge at the wall/last house | Fields, orchards, outbuildings, tracks, ruins beyond the edge |
| "Doesn't look old" | Uniform materials, no wear | Step 8: layered chronology, patched walls, worn paths, one ruin |
| "Mobs spawn inside my village" | Dark alleys and interiors | Light level 1+ everywhere walkable; check roofs, yards, docks |
| "Villagers won't work / breed" | Beds or workstations missing or unreachable | 1 bed + 1 workstation per villager, within pathable range |

## References

| File | Read it when |
| --- | --- |
| `references/layout-and-roads.md` | Street layout, widths, junctions, squares, walls, terrain |
| `references/districts-and-program.md` | What buildings a settlement needs, zoning, ratios by scale |
| `references/plots-and-building-mix.md` | Subdividing blocks, plot sizes, variation, density, heights |
| `references/growth-and-history.md` | Ageing, chronology, props of daily life, villager mechanics |
