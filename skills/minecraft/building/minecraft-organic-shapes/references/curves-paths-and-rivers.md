# Curves in plan: paths, roads, rivers, shorelines, terraces

## The one rule everybody breaks

**Never run an organic line straight for more than ~7 blocks.** Beyond that the eye reads a
ruler. Break it with a 1-block jog, a width change, or a curve. (This applies to paths,
rivers, shorelines, hedges, cliff edges - not to buildings or engineered roads.)

## Curve construction

A curve in plan is a sequence of straight runs of *different* lengths with 1-block steps
between them. Uniform steps read as a diagonal, uniform runs read as a staircase.

- Gentle curve: runs of 5-7 with single steps.
- Medium curve: runs of 3-4.
- Tight curve: runs of 1-2 (use only for switchbacks and small details).
- Blend: 6,5,4,3,2,2,3,4,5,6 gives a smooth arc that enters and leaves straight - the standard
  "road bend".
- For an S-curve, mirror a blend sequence; never place two bends of the same radius in a row.

## Path and road widths

| Use | Width | Notes |
| --- | --- | --- |
| Garden / desire line | 1-2 | Irregular edges, mostly dirt path blocks |
| Village lane | 3 | 1 centre + 2 shoulders, occasional 4-wide widening |
| Town street | 5 | 3 travel + 1 walkway each side (slabs) |
| Main road / avenue | 7-9 | Central crown, gutters, tree line |
| Highway / causeway | 9-13 | Engineered: straight runs allowed, but bends need 9+ radius |

Construction layers: base (coarse dirt/gravel), surface (dirt path, gravel, cobble, stone
bricks depending on era), edge (slabs, stone walls, grass with flowers), then wear - swap 10%
of the surface for a partner block in patches of 2-4.

## Making a path look used

- Widen at junctions, gates, wells and shop fronts; narrow between buildings.
- Puddles (1-block water in a 1-deep dip), ruts (path blocks in two parallel lines), spilled
  material near workshops, moss and grass creeping in at the edges of quiet lanes.
- Kerbs: slabs or stone walls only where the settlement is wealthy; villages get no kerbs.
- Steps on slopes: 2-3 stair blocks then a 2-3 block landing; for a road use ramps of slabs
  (half-step) instead of full steps so carts "could" pass.
- Lighting: lanterns on fence posts or wall posts every 8-10 blocks, offset from the path edge,
  not centred.

## Slopes and terraces

- Grade: 1 block rise per 3-4 horizontal for comfortable walking; 1 per 2 feels steep; 1 per 1
  is a stair.
- Switchbacks on steep ground: runs of 7-12 with 3x3 landings at the turns, retaining wall on
  the uphill side, drop-off planted on the downhill side.
- Terraces: retaining walls of 2-4 blocks, each terrace 4-8 deep, walls stepped in plan (never
  one long straight wall), stairs linking terraces at irregular intervals.
- Retaining wall recipe: base course of a heavier block, field of the main stone, coping of
  slabs; add weep holes, a vine or two, and one collapsed section for age.

## Rivers and streams

- Width: stream 2-4, river 6-12, big river 15-30. Vary the width along the course by +/-30%.
- Depth: 1 at the inside of bends and in riffles, 2-4 in the outer bends and pools. Never a
  uniform depth; never a 1-deep river wider than 6.
- Bed material: gradient of dirt/gravel/clay/sand, with a patch of stone or granite where the
  current would scour. Add seagrass, kelp only in the deeper parts, lily pads in slow water.
- Banks: undercut the outer bend (overhang the grass 1 block), build a gentle gravel/sand
  beach on the inner bend - this asymmetry is what makes a river read as flowing.
- Meanders: radius 8-20, alternating, with the wavelength roughly 10-14x the river width.
  Add an oxbow or an island every few bends.
- Edge treatment: coarse dirt and dirt path where feet and water wear the grass, roots (logs
  and fences), fallen trees, rocks in clusters of 3.
- Waterfalls: widen the channel just above the drop, break the lip with 2-3 rocks, put a plunge
  pool 3-4 deep below, mist with cobwebs or white stained glass only if the style allows.

## Lakes and shorelines

- Outline first with a single line of a marker block, following the 7-block rule, then flood.
- Shelve the bottom: 1-deep for 2-4 blocks from shore, then step down; a lake with vertical
  walls always looks like a hole.
- Coves and points: at least one of each per 30 blocks of shore. A round pond is a bug unless
  it is man-made.
- Reeds and life: sugar cane in clumps of 2-5 at the water edge, lily pads offshore, dead bush
  and gravel on the dry side, driftwood logs half in the water.

## Walls, hedges and fences on terrain

- Follow the contour: step the wall with the ground, keep the coping continuous, never leave a
  floating segment or a buried base.
- Break the top line: a tower or gate every 20-40 blocks, a collapsed section, a gate posts.
- Hedges: leaf blocks with 1-block irregularity on top, mixed leaf types, gaps with a gate.

## WorldEdit helpers

- `//brush sphere <block> <r>` with `//mask` for terrain work; `//brush smooth` for slopes.
- `//curve` (with `//sel convex`) draws a spline through selected points - ideal for a road
  centreline or a river thalweg; then widen with brushes.
- `//deform` and `//naturalize` fix a raw cut; `//flora`, `//forest` for planting.
- Always finish by hand: the last 10% of irregularity is what sells it.
