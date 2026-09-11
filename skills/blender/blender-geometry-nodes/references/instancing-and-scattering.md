# Instancing and scattering

## Instancing basics

The core chain:

```
Geometry > Distribute Points on Faces > Instance on Points > Group Output
                                            ^
                              Object Info (As Instance) / Collection Info
```

| Node | Role |
| --- | --- |
| Object Info | Brings in another object; enable **As Instance** to keep it cheap |
| Collection Info | Brings in a collection; **Separate Children** exposes each child as a pickable instance |
| Instance on Points | Places instances, with Rotation, Scale, Pick Instance and Instance Index |
| Rotate Instances / Scale Instances / Translate Instances | Per-instance transforms after placement |
| Realize Instances | Converts instances into real geometry (expensive) |
| Join Geometry | Merges geometries into one stream |
| Set Material | Assigns a material inside the tree |

Instances are references: a thousand instances of a 50k-triangle rock cost roughly one rock in memory.
Realizing them costs fifty million triangles of real data. Keep instances until something genuinely
needs real geometry - an exporter, a boolean, a per-element attribute you cannot express otherwise.

To pick randomly between several assets: Collection Info with Separate Children, then Instance on
Points with **Pick Instance** enabled and Instance Index driven by `Random Value (Integer)` seeded by
ID.

## Scattering on a surface

| Setting | Effect |
| --- | --- |
| Distribute Method: Random | Fast, allows clustering and overlaps |
| Distribute Method: Poisson Disk | Enforces a minimum distance; use for non-overlapping scatter |
| Density | Points per square metre - scale-dependent, so check your units |
| Density Max / Density Factor | For Poisson: the upper bound and the per-point mask |
| Seed | Change to re-roll the layout |

Density masks - feed a field into Density (Random) or Density Factor (Poisson):

- A painted vertex group via Named Attribute: the most controllable option.
- A texture (Noise, Voronoi, image) for natural clumping.
- A slope mask: `Normal > Separate XYZ > Z`, ramped, so nothing grows on cliffs.
- A height mask: `Position > Separate XYZ > Z`, ramped, for tree lines and shorelines.
- A distance mask: `Geometry Proximity` from a path or building collection, so nothing grows on roads.

## Natural-looking variation

| Variation | How |
| --- | --- |
| Random rotation around Z | `Random Value (Float, 0 to 2pi)` into a Combine XYZ Z, feeding Rotation |
| Random scale | `Random Value (Float, 0.8 to 1.3)` into Scale; use non-uniform vectors sparingly |
| Align to surface normal | Align Rotation to Vector (or Align Euler to Vector) using the sampled Normal, then add random Z spin |
| Slight tilt for organics | Mix the normal alignment with world up at 60-90%, so trees are mostly upright |
| Colour or material variation | Store a random attribute per instance and read it in the shader |
| Clumping | Scatter clump centres, then scatter again around them |
| Size-density link | Larger instances in sparser areas via a shared mask |

Alignment order matters: align to the normal first, then apply the random spin around the local axis,
otherwise the spin fights the alignment.

## Collision and exclusion

| Goal | Technique |
| --- | --- |
| Do not overlap each other | Poisson Disk with a minimum distance at least the instance footprint |
| Keep off roads/paths | Geometry Proximity to the path geometry > Greater Than distance > Selection or density factor |
| Keep out of buildings | Proximity to building collection, or a painted exclusion mask |
| Keep on the ground | Raycast down onto the terrain, use the hit position to Set Position |
| Avoid steep slopes | Normal Z mask |
| Keep inside a boundary | Point-in-volume test via Mesh to Volume / proximity sign, or a mask texture |

For ground conforming: scatter on a flat grid, then Raycast straight down onto the terrain and use
the hit position and hit normal for position and alignment. That gives clean control and works when
the terrain itself is procedural.

## Performance

| Lever | Effect |
| --- | --- |
| Keep instances unrealized | The single biggest saving |
| Lower viewport density, full density at render | Use a Switch driven by Is Viewport |
| Use low-poly proxies in the viewport | Switch between proxy and hero asset |
| Camera culling | Delete points outside the frustum via a proximity/position mask, or keep it simple with a bounding volume |
| Distance culling | Proximity to the camera object, delete beyond a radius |
| Cap point counts | Check the Spreadsheet's point count; 100k instanced points is fine, 10M is not |
| Avoid per-instance booleans | Booleans on dense geometry are the classic freeze cause |
| Bake heavy scatter | Apply the modifier or export to a cached file when the layout is final |

A practical ceiling: instanced scatter scales into the millions of instances, but every node that
must process each point (proximity, raycast, sampling) multiplies cost. Measure by muting branches
(M) and watching the viewport.

## Scatter checklist

1. Real-world scale confirmed - density is per square metre.
2. Assets have origins at their base and applied transforms.
3. Poisson disk used where overlap matters.
4. Density driven by a mask, not uniform.
5. Rotation aligned to the surface, then randomised.
6. Scale varied within plausible limits.
7. Exclusion zones respected (paths, buildings, water).
8. Instances not realized; viewport density reduced.
9. Materials assigned inside the tree or on the source objects.
