# Landforms and scale

## Slope ratios (computed)

| Rise:run | Angle | Use |
| --- | --- | --- |
| 1:6 | 9.5 deg | Meadow, farmland, buildable ground |
| 1:4 | 14.0 deg | Gentle foothill, park, garden |
| 1:3 | 18.4 deg | Standard hillside, terraced fields |
| 2:3 | 33.7 deg | Steep grassy slope, alpine pasture |
| 1:1 | 45.0 deg | Rock slope, needs stone showing through |
| 3:2 | 56.3 deg | Broken rock face with ledges |
| 2:1 | 63.4 deg | Cliff with ledges and vegetation pockets |
| 3:1 | 71.6 deg | Sheer cliff, strata fully exposed |
| Vertical | 90 deg | Fresh cliff, quarry, karst tower - always with scree below |

Mix at least three ratios in any slope taller than 20 blocks.

## Scale reference

| Feature | Height / size | Notes |
| --- | --- | --- |
| Garden mound | 3-6 | Enough to hide a wall or frame a path |
| Hill | 10-25 | One dominant, one secondary crest |
| Large hill / fell | 25-45 | Tree line effects start to read |
| Mountain | 50-120 | Needs spurs, cirques, bare rock above ~y110 |
| Mountain range | 3-7 peaks over 150-400 blocks | Peaks differ in height by 15%+ |
| Cliff (coastal) | 15-40 | Strata bands, undercut, sea stacks |
| Canyon | 30-80 deep, 40-150 wide | Terraced walls, talus, river at the bottom |
| Plateau / mesa | 20-60 | Flat top, stepped sides, capstone layer |
| Island (small) | 30-60 across | Beach one side, rock the other |
| Island (large) | 150-400 across | Needs its own interior terrain and water |
| Dune | 5-15 | Asymmetric: gentle windward, steep leeward |

Build height limits: y-64 to y319 in 1.18+. A 100-block mountain from sea level (y63) still
leaves 150 blocks of sky - use it, tall terrain reads better than wide terrain.

## Landform catalogue

### Rolling hills

Overlapping domes of different sizes, never tangent. Valleys between them carry a stream or a
path. Ratio 1:3 to 1:4, surface grass with coarse dirt on the steeper flanks.

### Alpine mountain

Ridgelines radiating from a summit like a starfish (3-5 spurs), cirques (bowl-shaped hollows)
between them, scree fans below, bare stone above the tree line, snow above ~y140 in cold
biomes. Steeper on one side than the other.

### Fjord / glacial valley

U-shaped valley floor, near-vertical walls 40-80 high, flooded to sea level, hanging valleys
with waterfalls on the side walls, flat sediment terraces at the head.

### Karst / tower hills

Vertical limestone towers (calcite, diorite, smooth stone) 20-50 high with flat tops and heavy
vegetation, undercut bases, caves and arches punched through. Spacing irregular, never a grid.

### Mesa / plateau

Hard capstone layer (2-4 blocks of a distinct material) over softer banded rock, stepped sides
with 2-5 block benches, deep vertical gullies cutting back into the rim, talus skirt at 1:2.

### Canyon

Start with the river, then cut. Walls terrace in 3-8 block benches, strata bands continuous
across both walls (they were one rock), side canyons entering at angles, boulders in the river.

### Badlands

Banded terracotta strata, hoodoos and spires left standing, dry channels, sparse vegetation,
steep gullies with fan deposits.

### Volcano

Asymmetric cone with a breached crater, hardened lava flows (blackstone, basalt, magma) running
downslope in narrow tongues, ash fields (gravel, coarse dirt), older eroded flanks with
vegetation on one side.

### Desert dunes

Asymmetric ridges: windward 1:4, leeward 1:1, crests curving in parallel chains, blowouts and
exposed sandstone between them, dead bushes and cacti only in the hollows.

### Wetland / delta

Almost no relief: 1-2 block variation, braided water channels, islands of rooted dirt and mud,
reeds (sugar cane, tall grass), dead trees, clay and mud banks.

### Island

One high side (rock, cliffs, wind-exposed, sparse plants) and one low side (beach, lagoon,
dense plants). Underwater slope continues the shape - never a vertical drop at the shoreline
unless the cliff continues below.

### Cave mouth / sinkhole

Collapsed rim with boulders inside, light falling into the throat, vegetation ring at the edge
feeding on the light, stalactites (pointed dripstone) below, water seeping down one wall.

## Massing procedure

1. **Lines** - place a single line of blocks along every ridge crest and valley floor, at final
   height. Walk it. Fix the plan before adding volume.
2. **Sections** - at 20-30 block intervals, build the cross-section profile (concave low,
   convex high) from ridge to valley.
3. **Fill** - connect the sections, keeping the slope ratios per zone.
4. **Break** - remove and add 3-8 block patches along every edge so no line stays clean.
5. Only then: strata, surface, erosion, water, planting.

## Anti-patterns

- Symmetrical peaks; a single peak with no spurs.
- Ridge crests running due north-south or east-west along the block grid.
- Same slope from base to summit.
- Terrain that stops at a straight edge where the edit ended.
- Mountains that are wide domes instead of tall masses (players read height, not volume).
- Flat valley floors with no stream, path or sediment.
