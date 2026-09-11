# Domes, spheres and caps

A sphere is a vertical stack of circles whose diameter changes on a **non-linear** schedule:
almost no change near the equator, big steps near the crown. Linear shrinking gives a cone;
shrinking too early gives a pancake. The tables below are computed, not eyeballed.

## Dome layer diameters (springline -> crown)

Each value is the circle diameter of one layer, starting at the widest layer. Build each layer
with the row widths from `circles-and-cylinders.md`.

| Dome D | Layers from springline to crown | Height |
| --- | --- | --- |
| 9 | 9,9,9,7,5 | 5 |
| 11 | 11,11,11,9,7,5 | 6 |
| 13 | 13,13,13,11,11,9,5 | 7 |
| 15 | 15,15,15,13,13,11,9,5 | 8 |
| 17 | 17,17,17,15,15,13,13,9,5 | 9 |
| 21 | 21,21,21,21,19,19,17,15,13,11,7 | 11 |
| 25 | 25,25,25,25,23,23,21,21,19,17,15,11,7 | 13 |
| 31 | 31,31,31,31,29,29,29,27,27,25,23,21,19,17,13,7 | 16 |

Note the pattern: the first 3-4 layers do not shrink at all (that is the 10-15% of height that
makes a dome look spherical), then steps of 2, then 2-4 near the crown. The crown is closed
with a 5x5 or 7x7 cap - finish it with slabs, a lantern structure, or an oculus.

## Full sphere layer diameters (bottom -> top)

| Sphere D | Layers |
| --- | --- |
| 7 | 3,5,7,7,7,5,3 |
| 9 | 5,7,9,9,9,9,9,7,5 |
| 11 | 5,7,9,11,11,11,11,11,9,7,5 |
| 13 | 5,9,11,11,13,13,13,13,13,11,11,9,5 |
| 15 | 5,9,11,13,13,15,15,15,15,15,13,13,11,9,5 |
| 17 | 5,9,13,13,15,15,17,17,17,17,17,15,15,13,13,9,5 |
| 21 | 7,11,13,15,17,19,19,21,21,21,21,21,21,21,19,19,17,15,13,11,7 |
| 25 | 7,11,15,17,19,21,21,23,23,25,25,25,25,25,25,25,23,23,21,21,19,17,15,11,7 |
| 31 | 7,13,17,19,21,23,25,27,27,29,29,29,31,31,31,31,31,31,31,29,29,29,27,27,25,23,21,19,17,13,7 |

Odd diameters only: a sphere needs a centre block to be symmetrical in all three axes.

## Build order that actually works

1. Mark the centre and the springline ring (the widest layer) on the ground or on the drum.
2. Build **4 ribs** (N, E, S, W great-circle quarter arcs) using the dome layer heights, then
   **4 more** at 45 degrees. Ribs are a temporary or permanent structure - in many styles they
   stay as the visible dome ribs.
3. Fill layer by layer between the ribs using the row widths table. Work from the springline up.
4. Check the silhouette from 4 sides, fix any layer that drifts by 1.
5. Smooth: stairs facing out on layers where the diameter drops by 2; slabs where the profile
   goes flatter (near the springline). Interior: upside-down stairs for the soffit.
6. Finish the crown: oculus (open ring with a glass or open hole), lantern (small cylinder with
   windows and its own mini dome), or a finial (fence posts + end rod + lightning rod).

## Dome variants

- **Hemisphere:** the table above as-is.
- **Shallow / saucer dome:** take the dome table and delete the first 2-3 non-shrinking layers,
  starting from the first layer that shrinks. Rises about half as much.
- **Stilted dome:** cylinder drum of 3-8 layers at the springline diameter, then the dome. The
  drum is where windows go; almost every good Minecraft dome has one.
- **Onion dome:** springline layers *grow* by 2 for 2-3 layers (bulge), hold, then shrink
  quickly with increasing steps, ending in a tall narrow neck and a finial. Sequence example
  for a 13-wide base: 13,15,15,15,13,11,9,7,5,3,3,1 with a fence spike above.
- **Ribbed / melon dome:** build the 8 ribs in the accent block, then infill each web 1 block
  recessed from the rib line. Instant medieval/Byzantine read.
- **Geodesic / glass dome:** use the same layer table but place the shell in glass with a
  full-block rib grid every 4-5 blocks; keep the ribs on the 8 symmetry lines so they meet at
  the crown.
- **Square-to-round transition:** to put a round dome on a square room, use pendentives - fill
  each corner of the square with a quarter dome (stairs stepping inward layer by layer) until
  the opening is the circle you need, or simply set the drum on a 45-degree chamfered octagon.

## Scale guidance

| Room span | Dome diameter | Typical total rise (drum + dome) |
| --- | --- | --- |
| 7-9 | 9-11 | 8-12 |
| 11-13 | 13-15 | 12-18 |
| 15-17 | 17-21 | 18-26 |
| 21+ | 25-31 | 28-45 |

A dome under 9 wide is a hat, not a dome - use a cone or a hip roof instead.

## Interior of a dome

- Light the shell indirectly: hidden light in the springline cornice and in the oculus ring.
- Coffers: recess every second web panel by 1 block in a grid; costs nothing, reads rich.
- A painted-ceiling effect: use 3-4 blocks of the same hue family in irregular patches
  (e.g. lapis, blue concrete, blue terracotta, blue glazed terracotta highlights).
- Cross-reference `../../minecraft-interiors/references/lighting.md` for hidden fixtures.

## WorldEdit

- `//sphere <block> <r>` / `//hsphere` centred on the player; `//sphere stone 10,6,10` for an
  ellipsoid.
- `//hemisphere` does not exist - build `//hsphere` then `//set air` on the lower half with a
  cuboid selection.
- `//g` (generate) with `(x^2+y^2+z^2)^0.5 < 1` style formulas for exotic shells, toruses:
  `//g glass (0.6-(x^2+z^2)^0.5)^2+y^2 < 0.1^2`.
- Bulk placement skips block updates - reload chunks with F3+A afterwards.
