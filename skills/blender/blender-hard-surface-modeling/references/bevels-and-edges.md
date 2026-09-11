# Bevels, support loops and creases

## Modifier bevel vs destructive bevel

| Approach | Pros | Cons |
| --- | --- | --- |
| Bevel modifier | Non-destructive, width and segments stay editable, works with weights | Struggles on complex intersections; can fail near tight geometry |
| Ctrl+B in edit mode | Full control, handles awkward intersections | Destructive; changes topology permanently |
| Bevel weights + modifier | Per-edge control with global tuning | Requires setting weights; remember weights are a separate edge attribute |

Practical default: Bevel modifier with Limit Method **Weight**, plus edge bevel weights set where you
want rounding. Angle limiting is fine for simple objects but catches edges you did not intend on
anything complex.

## Key bevel modifier settings

| Setting | What it does | Typical use |
| --- | --- | --- |
| Amount | Bevel width in metres (respects object scale) | 0.001-0.003 m for manufactured edges |
| Segments | Number of bevel divisions | 1-2 for real-time, 2-4 for close-up renders, 1 for subdivision support |
| Limit Method | Angle / Weight / Vertex Group / None | Weight for control, Angle 30-60 degrees for quick passes |
| Profile | Shape of the bevel section | 0.5 round, 1.0 sharp chamfer, under 0.5 concave |
| Clamp Overlap | Prevents bevels from overlapping and self-intersecting | Keep on unless you need exact width |
| Miter Outer/Inner | Behaviour where bevels meet | Miter Outer Arc for cleaner corners on boxy shapes |
| Harden Normals | Bakes flat shading into the bevel's neighbours | Hard-surface without subdivision; needs smooth shading |
| Material Index | Assigns a material to bevel faces | Edge wear masks, painted-metal chips |

Notes:

- Bevel width is in world metres, so **object scale must be applied** or widths lie.
- Vertex mode bevel (Vertices instead of Edges) rounds corners, useful for plate corners.
- Two bevel modifiers are legitimate: a wide one for large rounding, a narrow one for the hard edge.

## Support loops for subdivision

When using Subdivision Surface, sharpness comes from geometry density near the edge:

- A loop pair close to an edge holds it tight; loops further away produce a softer round.
- Spacing rule of thumb: distance between support loop and edge is roughly the radius of the rounding
  you want.
- Support loops must **not** cross other loops at odd angles or terminate in the middle of a face -
  that is what creates pinching.
- Use Ctrl+R (loop cut) with even spacing, or add one Bevel modifier segment before subdivision to
  generate support geometry automatically.
- Keep the cage all quads. A triangle or N-gon next to a support loop shows up as a shading dent.

## Creases vs geometry

| Technique | Result | When |
| --- | --- | --- |
| Edge crease (Shift+E) | Subdivision pulls the surface to the edge, no extra geometry | Quick sharpening, mechanical shapes, low-poly cages |
| Support loops | Full control of the rounding profile | Anything that will be rendered close, or baked |
| Bevel modifier before subdivision | Automatic support geometry | Hard-surface pipelines, fast iteration |

Creases are cheap but blunt: they produce infinitely sharp corners that can look CG, and they behave
differently in engines and other DCC apps. For final assets, geometry beats creases.

## Bevelling after booleans

- Boolean first, bevel after. Bevelling before a cut leaves the cut edges sharp and the bevel
  mangled.
- Boolean results often contain N-gons and coplanar faces; the Bevel modifier tolerates them poorly.
  Clean the intersection (merge by distance, dissolve stray edges, re-flow the immediate area) before
  bevelling.
- On complex intersections, reduce Segments to 1-2 and enable Clamp Overlap; a heavy bevel is the
  usual cause of black smears at boolean corners.
- If the modifier bevel refuses to behave, bevel those specific edges destructively and move on.

## Real-time vs render bevels

- **Real-time**: 1 segment, tiny width, plus Weighted Normal; or no bevel geometry at all and a
  baked normal map from the high-poly (`../../blender-uv-and-baking/SKILL.md`).
- **Render**: 2-4 segments, or subdivision. In Cycles, a Bevel shader node can round edges at shading
  time without geometry - useful for large scenes, not a substitute for real bevels in close-ups.

## Edge pass checklist

1. Object scale applied before setting bevel widths.
2. Every hard edge has some rounding - no razor-sharp edges on manufactured objects.
3. Bevel widths chosen in millimetres, consistent across the object.
4. Clamp Overlap on, or widths verified not to overlap.
5. Support loops all quads, evenly spaced, no loose ends.
6. Boolean intersections cleaned before bevelling.
7. Checked with a reflective matcap for smears and pinching.
