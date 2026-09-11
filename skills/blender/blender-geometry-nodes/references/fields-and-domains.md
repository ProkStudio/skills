# Fields, attributes and domains

## The field model

A **field** is a function waiting for a context: "the noise value at this point", "1 if this face is
selected". It has no value until a node evaluates it on real geometry.

Socket shapes tell you what is going on:

| Shape | Meaning |
| --- | --- |
| Round dot | Single value only |
| Diamond | Field-capable, currently a single value |
| Diamond with a dot inside | Field-capable and currently receiving a field |

If a link is refused, the target needs a single value while the source is a field. Resolve it by:

- Using the field inside a node that evaluates it (Set Position, Store Named Attribute, Distribute
  Points on Faces density, any Selection input).
- **Capture Attribute** to freeze a field on a domain before geometry changes.
- **Attribute Statistic** or **Sample Index** to reduce a field to one value.

## Field inputs worth knowing

| Node | Provides |
| --- | --- |
| Position | Per-element position |
| Normal | Per-element normal |
| Index | Element index (unstable under topology change) |
| ID | Stable random identifier on points, when present |
| Radius | Point/curve radius |
| Named Attribute | Any stored attribute by name |
| Random Value | Random per element, with a Seed and an ID input |
| Scene Time | Frame or seconds, for animation |
| Curve Parameter / Tangent / Tilt | Curve-specific fields |
| Edge Angle / Face Area / Is Face Planar / Shortest Edge Paths | Topology measurements |
| Texture nodes | Procedural values driven by Position |

## Domains

| Domain | Elements | Typical attributes |
| --- | --- | --- |
| Point | Vertices, control points, point-cloud points | position, radius, ID, custom masks |
| Edge | Mesh edges | crease, sharp, bevel weight |
| Face | Mesh faces | material index, smooth flag, area-based masks |
| Face Corner | Per-face vertex references | UVs, split normals, vertex colours in some forms |
| Curve | Whole splines | cyclic, resolution, per-spline randomness |
| Instance | Each instance | transform-related and per-instance attributes |
| Layer | Grease Pencil layers | layer-level data |

Rules:

- UVs live on **face corners**, which is why treating them as point data produces wrong results.
- Storing to a different domain than the source triggers implicit interpolation: point to face
  averages, face to point averages the adjacent faces. Both lose sharpness.
- The Spreadsheet has one tab per domain. If a value is missing, you are probably reading the wrong
  one.

## Storing and reading

| Node | Use |
| --- | --- |
| Store Named Attribute | Write a named attribute on a chosen domain and data type |
| Named Attribute | Read it back, anywhere downstream or in a shader |
| Capture Attribute | Freeze a field's current values so later topology changes do not re-evaluate it |
| Remove Named Attribute | Clean up before output; stray attributes bloat files and exports |
| Attribute Statistic | Min, max, mean, sum, standard deviation over a domain |
| Accumulate Field | Running totals along an index order |
| Sample Index / Sample Nearest / Sample Nearest Surface | Read a value from another geometry |
| Geometry Proximity | Distance and closest position to another geometry |
| Raycast | Hit position, normal and attributes from a target surface |
| Interpolate Curves / Sample Curve | Curve-specific sampling |

Naming conventions that save pain:

- Prefix project attributes, e.g. `gn_density`, `gn_mask_road`, so they are obvious in the
  Spreadsheet.
- Data types matter: Float, Vector, Color, Boolean, Int, Quaternion, Matrix. Reading with the wrong
  type silently gives odd results.
- Attributes starting with a dot are internal; do not rely on them.
- Shaders can read named attributes with the Attribute node - this is how procedural masks reach
  materials.

## Selections

Most nodes have a **Selection** input. It takes a boolean field, and it is the cleanest way to act on
part of a geometry:

- `Normal > Separate XYZ > Z > Greater Than 0.5` to affect only up-facing faces.
- `Named Attribute ("mask") > Greater Than 0.5` to use a painted vertex group or attribute.
- `Face Area > Greater Than x` to act only on large faces.
- `Position > Separate XYZ > Z > Less Than 0` to affect geometry below a height.

Vertex groups read as float attributes by name; that makes weight painting a practical mask authoring
tool for node setups.

## Common field errors decoded

| Message or behaviour | Meaning | Fix |
| --- | --- | --- |
| "Field cannot be evaluated in this context" | A field was fed to a socket with no geometry context | Move the field inside a node that evaluates it, or capture it |
| Value becomes a constant unexpectedly | The field got captured earlier than intended | Move Capture Attribute later in the chain |
| Attribute disappears after a node | Node does not propagate that domain/type | Store before, read after; or reorder |
| Everything is the same random value | Random Value has no ID input and a single evaluation context | Feed ID or Index explicitly |
| Mask affects the wrong elements | Domain interpolation | Store the mask on the domain you will use it on |

## Domain checklist

1. Know which domain each attribute is on, and say so when explaining a setup.
2. Verify in the Spreadsheet, on the right domain tab.
3. Use ID rather than Index for anything random that must stay stable.
4. Capture fields before topology changes when the values must not follow.
5. Remove temporary named attributes before output.
6. Use vertex groups and painted attributes as masks instead of hardcoded numbers.
