# Circles, rings, cylinders, cones

## The rule behind the tables

A block at grid cell `(x, z)` belongs to a circle of diameter `D` when the distance from the
cell **centre** to the circle centre is `<= D/2`. All tables below are computed with that
rule. Other generators differ by one block at the corners; pick one rule and stay with it so
every floor of a tower matches.

- **Odd D** - one centre block, a true axis, symmetrical doors and keystones. Use for towers,
  rotundas, wells, anything with a centre pillar or a single entrance on the axis.
- **Even D** - a 2x2 centre, no axis. Use for bases wrapped around a 2x2 shaft, or when the
  inner room wants even dimensions.
- Below D=7 a "circle" is a rounded square: D=5 gives 3,5,5,5,3. Do not fight it - either
  embrace the octagon or go bigger.

## Filled circle row widths

Each line lists the widths of the **top half of the rows**, centred. Mirror the list (without
repeating the last row for odd D) to get the bottom half. Total rows = D.

| D | Top-half row widths (centre the rows) |
| --- | --- |
| 5 | 3,5,5 |
| 6 | 4,6,6 |
| 7 | 3,5,7,7 |
| 8 | 4,6,8,8 |
| 9 | 5,7,9,9,9 |
| 10 | 4,8,8,10,10 |
| 11 | 5,7,9,11,11,11 |
| 12 | 4,8,10,10,12,12 |
| 13 | 5,9,11,11,13,13,13 |
| 14 | 6,8,10,12,14,14,14 |
| 15 | 5,9,11,13,13,15,15,15 |
| 16 | 6,10,12,14,14,16,16,16 |
| 17 | 5,9,13,13,15,15,17,17,17 |
| 18 | 6,10,12,14,16,16,18,18,18 |
| 19 | 7,11,13,15,17,17,19,19,19,19 |
| 20 | 6,10,14,16,16,18,18,20,20,20 |
| 21 | 7,11,13,15,17,19,19,21,21,21,21 |
| 23 | 7,11,15,17,19,19,21,21,23,23,23,23 |
| 25 | 7,11,15,17,19,21,21,23,23,25,25,25,25 |
| 27 | 7,13,15,19,21,21,23,25,25,25,27,27,27,27 |
| 29 | 7,13,17,19,21,23,25,25,27,27,27,29,29,29,29 |
| 31 | 7,13,17,19,21,23,25,27,27,29,29,29,31,31,31,31 |
| 33 | 9,13,17,21,23,25,27,27,29,29,31,31,33,33,33,33,33 |

For an **outline** (ring) circle, place the filled rows and then remove everything more than
1 block inside the perimeter - or simply place, per row, only the first and last block of the
row width, plus the full run on the flat top/bottom rows.

## Quarter-arc run notation

Useful when placing by hand: `width x rows` from the top of the circle downward (top half only).

| D | Arc runs |
| --- | --- |
| 7 | 3x1  5x1  7x2 |
| 9 | 5x1  7x1  9x3 |
| 11 | 5x1  7x1  9x1  11x3 |
| 13 | 5x1  9x1  11x2  13x3 |
| 15 | 5x1  9x1  11x1  13x2  15x3 |
| 17 | 5x1  9x1  13x2  15x2  17x3 |
| 19 | 7x1  11x1  13x1  15x1  17x2  19x4 |
| 21 | 7x1  11x1  13x1  15x1  17x1  19x2  21x4 |
| 25 | 7x1  11x1  15x1  17x1  19x1  21x2  23x2  25x4 |
| 31 | 7x1  13x1  17x1  19x1  21x1  23x1  25x1  27x2  29x3  31x4 |

Read it as: "top row 7 wide, then one row 13 wide, ... then 4 rows at full width". The
straight side of the circle is the last entry, and it is always the longest run - that is why
large circles read as round while small ones read as octagons.

## Cylinders and towers

- Stack the same circle for a straight cylinder; the vertical joint lines are invisible if the
  texture is patched (2-5 block patches of a partner block).
- **Base flare:** add a ring of D+2 for the bottom 1-2 layers, capped with stairs facing out.
- **String courses:** a ring of a contrasting block (or slabs overhanging by nothing, stairs
  overhanging by 1) every 4-6 layers; it breaks the vertical monotony.
- **Taper:** drop the diameter by 2 every 6-10 layers, and hide each step behind a string
  course so the transition looks deliberate.
- **Openings in round walls:** a window in a curved wall wants a flat jamb - use full blocks
  for both sides of the opening, and keep openings on the 4 or 8 symmetry lines so they land on
  the flat runs of the circle rather than on a corner step.
- **Stairs inside a tower:** a spiral of stair blocks around a 1x1 or 2x2 newel; for D=9 the
  spiral wants 8 or 12 steps per full turn (rise 1 per step), plus a landing every turn.
- **Roof cap:** cone (see below), dome (`domes-and-spheres.md`), or a conical stair cap: ring of
  stairs facing in, each layer D-2, until D<=3, then a lightning rod or a fence finial.

## Cones and spires

- Cone = stack of circles with the diameter dropping on a fixed schedule. A pleasant medieval
  spire drops 2 in diameter every 2 layers; a steep witch-hat drops 2 every 3-4 layers.
- Vary the drop schedule to change the profile: constant drop = straight cone, increasing drop
  near the top = concave (needle), decreasing drop = convex (bell).
- Smooth the outer surface with stairs facing out on the layers where the diameter drops.
- Break every spire with at least one of: a ring cornice, a dormer, a flag/lightning rod, a
  change of material in the top third.

## Ellipses and arbitrary curves

- **Ellipse:** build the two half-arcs with different radii - use the top half of the circle
  table for diameter A on the long axis and stretch by repeating the widest rows N times in
  the middle. Repeating rows is what makes an ellipse instead of a circle.
- **Squashed dome plan / oval room:** two half circles of diameter D joined by a straight
  section L (a stadium shape). This is far easier to build cleanly than a true ellipse and
  reads the same in game.
- **Diagonal lines** (for chamfers and 45-degree walls): slope table, rise:run -> angle.
  1:1 = 45.0 deg, 1:2 = 26.6, 1:3 = 18.4, 1:4 = 14.0, 2:3 = 33.7, 3:4 = 36.9, 2:1 = 63.4,
  3:1 = 71.6, 4:1 = 76.0. Mix two neighbouring slopes to approximate an angle between them.

## Commands and WorldEdit

- `//cyl <block> <radius> <height>` and `//hcyl` for hollow; radius `r` produces diameter
  `2r+1` (odd) - for an even diameter use `//cyl` with two radii (`//cyl stone 5,4 10`).
- `/fill` works per ring row; write one `/fill` per row width, which is why the row-width table
  is the useful form for commands.
- After any bulk placement, reload chunks (F3+A) so fences, panes, walls and bars re-connect.
