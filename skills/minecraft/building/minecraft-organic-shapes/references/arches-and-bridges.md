# Arches, vaults, tunnels and bridges

## Semicircular arch rise table

For an arch of odd span `S`, the intrados follows the top half of a circle of diameter `S`.
Each list gives the rise above the springline for each column from the **edge to the centre**
(mirror for the other half). "Rise" = number of blocks of clear height added above the
springline at that column.

| Span | Column rises (edge -> centre) | Crown rise |
| --- | --- | --- |
| 5 | 2,3,3 | 3 |
| 7 | 2,3,4,4 | 4 |
| 9 | 3,4,5,5,5 | 5 |
| 11 | 3,4,5,6,6,6 | 6 |
| 13 | 3,5,6,6,7,7,7 | 7 |
| 15 | 3,5,6,7,7,8,8,8 | 8 |
| 17 | 3,5,7,7,8,8,9,9,9 | 9 |
| 21 | 4,6,7,8,9,10,10,11,11,11,11 | 11 |

So a semicircular arch of span S needs about `(S+1)/2` blocks of rise plus the pier height, and
1-2 blocks of masonry above the crown before the wall or deck starts.

## Arch types and when to use them

| Type | Profile rule | Reads as |
| --- | --- | --- |
| Flat / lintel | Full blocks spanning, 1-2 thick | Modern, Japanese, cheap utility |
| Corbelled | Each course steps in 1 from both sides until they meet | Primitive, dwarven, ancient |
| Segmental | Take the arch table but start 2-3 rows into the circle (lower rise) | Roman bridges, cellars, tunnels |
| Semicircular | Table above | Roman, Renaissance, aqueducts |
| Horseshoe | Semicircular but continue the curve 1-2 blocks below the springline | Moorish, desert |
| Pointed (Gothic) | Two arcs struck from centres inside the span: build each half as a quarter circle of radius `S-2`, meeting at a keystone above the centre | Gothic, cathedral, elven |
| Ogee / onion | Pointed arch with the top third curving back out | Fantasy, Venetian, oriental |
| Parabolic | Column rise increases by a constant difference (1,3,5,7...) | Catenary bridges, organic/alien |

## Building an arch cleanly

1. Build the two piers/jambs in full blocks to the springline.
2. Place the intrados (inner curve) with full blocks using the rise table.
3. Add the **voussoir ring**: one block thick, in a contrasting block, following the curve -
   this is what makes an arch read as an arch.
4. Put the **keystone** at the crown, one block taller or in the accent block.
5. Smooth: stairs under the curve pointing into the opening where the step is 1 block; upside
   down stairs (`half=top`) for the soffit inside a deep arch.
6. Fill the spandrels (the triangles between adjacent arches) with the field material and
   optionally a small round window (`oculus`) in each.

## Arcades

- Bay rhythm: pier width 2-3, span 4-7, repeated 3+ times; a pier is never thinner than
  1/4 of the span for a masonry look.
- End the arcade with a wider pier or a solid wall, never with a half arch.
- Vary the rhythm on long runs: A-B-A-B-A with one taller central bay reads as designed.

## Vaults and tunnels

- **Barrel vault:** extrude the arch profile along the length; ribs every 4-6 blocks in a
  contrasting block.
- **Groin vault:** intersect two barrel vaults of the same span; the diagonal ribs follow
  a 1:1 step and meet at a central boss block.
- **Tunnel:** segmental arch profile, 2-3 blocks of cover above the crown, timbering every
  3-4 blocks (log frames), floor of a different material, drainage channel on one side.
- Lighting in vaults: hide the source in the rib recess or behind the springline cornice.

## Bridges

Proportions that work:

| Bridge type | Span between piers | Deck thickness | Parapet |
| --- | --- | --- | --- |
| Foot bridge | 5-9 | 1-2 | fences or walls, 1-2 high |
| Road bridge | 9-15 | 2-3 | 1-2 high with posts every 4-6 |
| Aqueduct | 7-13 | 3-4 (channel inside) | channel walls 1-2 with a 1-2 wide water run |
| Rail/industrial | 11-21 | 2-3 + truss | truss above deck, iron bars/walls |

Rules:

- Pier spacing 1-1.5x the arch span; piers get a batter (1 block wider at the base) and a
  cutwater (a wedge pointing upstream) when they stand in water.
- The deck must be thicker than the parapet; a 1-thick deck always looks like paper.
- Always add: a slight camber (the centre 1-2 blocks higher than the ends), abutments where the
  bridge meets land, and a material change at the transition.
- Wear and use: worn path blocks in the wheel lines, moss/vines under the arches, lanterns on
  posts every 6-8 blocks, a shrine or a toll house at one end.
- Suspension: towers of 2-3 block width, main cable as a catenary of chains or walls (drop the
  cable 1 block per 2-3 horizontally at the towers, flattening toward mid-span), hangers every
  2-3 blocks, stiffening truss under the deck.
- Covered bridge: treat it as a building on a deck - roof from
  `../../minecraft-architecture/references/roofs.md`.

## Connection warning

Never write connection blockstates (`north=`, `east=`, `up=`) for fences, walls, panes or bars
in bridge parapets. Place them and let the game connect, and reload chunks (F3+A) after bulk
commands. See `../../minecraft-architecture/references/block-connection-rules.md`.
