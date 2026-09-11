# Lines, edges and anti-aliasing

At low resolution the edge *is* the drawing. Two sprites with identical shading read as amateur and
professional purely by how their edges are built.

## Jaggies

A jaggie is an irregular step in a line or curve: a run of 2 pixels, then 1, then 3, for no reason.
The eye reads it as a dent.

Rules:

- Use a regular step pattern. Straight diagonals: 1-1-1-1 (45 degrees), 2-2-2-2 (about 27 degrees),
  3-3-3-3, or 1-2-1-2 for a shallow curve.
- Within one curve, step lengths should change monotonically: 4-3-2-1-1 is a clean quarter circle,
  4-1-3-2 is noise.
- No "doubles": two pixels sticking out where the pattern calls for one, usually left behind by a
  freehand stroke or the line tool.
- Avoid a 1 px step between two long runs; it reads as a bump. Merge it into a neighbour.

## Line thickness

- Sprites up to 32 px: 1 px lines only. A 2 px line eats 6% of a 32 px silhouette.
- Larger work can use 2 px for the outer contour and 1 px inside, but keep it a rule, not a mood.
- Never let a line thicken and thin by accident; taper only on purpose (brush strokes, hair tips).

## Outline styles

| Style | How | Reads as |
| --- | --- | --- |
| Hard black | Solid black around the whole silhouette | Arcade, cartoon, maximum readability on any background |
| Dark tone | Outline is a dark version of the adjacent fill colour | Softer, painterly, still readable |
| Selective (selout) | Outline present on shadow side, dropped or lightened on lit side | Volume and light in the contour itself; the classic "pro" look |
| No outline | Silhouette defined by value contrast against the background | Modern, needs tight control of background values |
| Light rim | A bright 1 px rim on the lit edge, dark elsewhere | Backlight, glow, night scenes |

One rule per project. Mixing hard black characters with outline-free props is the second most
common coherence failure after mixed pixel densities.

Black is a choice, not a default. Pure black (#000) against a coloured world can feel like a hole;
a very dark version of the scene's shadow hue usually sits better. See
`../../color-and-palettes/references/readability-and-contrast.md`.

## Anti-aliasing

AA means placing intermediate-value pixels at a step so the eye smooths the edge.

- AA in the direction of the slope: a shallow (near-horizontal) slope gets horizontal AA pixels, a
  steep slope gets vertical ones. AA across the wrong axis makes the line fatter, not smoother.
- One intermediate step for small sprites; two for 64 px and above. Three is a gradient, not AA.
- AA the *inside* of a silhouette freely. Be careful AA-ing the outer contour of a moving sprite:
  intermediate pixels are tuned to one background colour and become a visible halo on others. If
  the sprite moves over varied backgrounds, either skip outer AA or keep it inside the outline.
- Never AA into transparency for sprites that will sit on unknown backgrounds unless the engine
  composites with proper alpha and you accept the soft edge.
- Do not AA 45 degree diagonals - they are already the cleanest line the grid can make.
- Do not AA every edge. AA is punctuation: use it on curves and shallow slopes that read as ragged.

## Banding

Banding is two ramp steps running parallel along the same diagonal, producing a thick stripe that
flattens form. It is the most common shading edge defect.

Fixes:

- **Band compression**: squeeze the intermediate step into a short segment instead of letting it
  run the whole length of the edge.
- Vary the run lengths of neighbouring bands so their boundaries are not parallel.
- Rotate the direction of the transition so the value change crosses the form instead of hugging it.
- Remove a value. Two clean steps beat three banded ones.

## Drawing curves without fighting the tool

- Use a 1 px pencil. Soft or textured brushes produce semi-transparent pixels that pollute a
  fixed palette.
- Do not use the line tool for curves longer than about 8 px - it produces uneven step patterns.
  Draw the curve as 3-4 straight segments with decreasing step lengths, then clean the joints.
- Draw the big shape, then erase into it, rather than nibbling outward.
- Flip the canvas horizontally now and then: asymmetric errors jump out immediately.
- Zoom to 100% every few minutes. Edge decisions only make sense at display size.

## Orphan pixels and clusters

A lone pixel surrounded by a different colour reads as dirt unless it is a deliberate accent (an
eye, a rivet, a star). In textured areas keep clusters of 2 or more pixels. If a sprite looks
"dusty", count the single-pixel islands and merge them.
