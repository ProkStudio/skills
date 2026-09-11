# Scale and orientation

## Engine conventions

| Target | Up axis | Forward | Handedness | 1 unit |
| --- | --- | --- | --- | --- |
| Blender | +Z | -Y (front view looks along +Y) | Right-handed | 1 m (default unit scale 1.0) |
| Unity | +Y | +Z | Left-handed | 1 m |
| Unreal Engine | +Z | +X | Left-handed | 1 cm |
| Godot | +Y | -Z | Right-handed | 1 m |
| glTF 2.0 | +Y | +Z (per format definition) | Right-handed | 1 m |
| USD | Configurable (commonly +Y) | Scene-defined | Right-handed | Scene-defined (metersPerUnit) |
| Three.js / web | +Y | -Z | Right-handed | Scene-defined, usually 1 m |

Two conclusions follow:

1. **Blender to Unity/Godot/glTF is a Z-up to Y-up conversion.** A 90-degree rotation exists
   somewhere; either the exporter does it or you do.
2. **Blender to Unreal is a unit conversion**, not an up-axis one: both are Z-up, but 1 m in Blender
   is 100 units in Unreal. Unreal's FBX importer normally handles this; verify rather than assume.

## Forward axis conventions

Pick one forward direction for your whole library and never deviate:

- A common choice for characters and props is **-Y forward** in Blender (facing the default front
  view), which maps to the engine's forward after conversion.
- Unreal projects often standardise on **+X forward** in the source file, matching the engine.
- Whatever you choose, document it and check every asset against it. A library with mixed forward
  axes forces per-asset fixes forever.

Check the convention with a simple test: export a cube with an arrow shape, import it, and see which
way the arrow points relative to the engine's forward.

## Apply transforms first

Before any export:

1. Object > Apply > **All Transforms** (or Rotation & Scale at minimum) so scale is 1, 1, 1 and
   rotation is zero.
2. Fix parent hierarchies: an unapplied non-uniform scale on a parent produces skewed children.
3. Clear delta transforms (they are invisible in the sidebar's main fields but still apply).
4. Reset the mesh's own transform relative to the intended pivot by placing the origin.

Why this matters: exporters bake object transforms differently. An asset whose scale is already 1 and
whose rotation is already zero exports identically through almost any path.

## Origin placement

| Asset | Origin |
| --- | --- |
| Props standing on the floor | At the base, centred in footprint |
| Wall / modular kit pieces | At a grid corner, so pieces snap predictably |
| Doors, levers, wheels | At the rotation axis |
| Characters | Between the feet, at the floor plane |
| Attachable props (weapons) | At the grip point |
| Decals / planes | At the centre |

Set it with Object > Set Origin > Origin to Geometry / to 3D Cursor (place the cursor precisely first,
using snapping). Getting this right removes an entire class of in-engine placement pain.

## Scene scale settings

| Setting | Where | Effect |
| --- | --- | --- |
| Unit System / Unit Scale | Scene Properties > Units | Defines what 1 Blender unit means; keep Metric with Unit Scale 1.0 and length in metres unless there is a strong reason |
| Exporter Scale | FBX/glTF export panel | Multiplies exported coordinates |
| FBX Apply Scalings | FBX export | `FBX_SCALE_NONE` / `FBX_SCALE_UNITS` / `FBX_SCALE_CUSTOM` / `FBX_SCALE_ALL` - controls whether the scale goes into FBX units or into the transforms |
| Importer scale | Engine side | Unity's FBX "Convert Units" / scale factor, Unreal's Import Uniform Scale, Godot's import scale |

Rule: change **one** of these, not several. Scale bugs are nearly always two compensating settings
fighting each other.

## Fixing a 90-degree rotation

Three valid approaches, in order of preference:

1. **Let the exporter convert.** In the FBX exporter set Up and Forward axes to the target's
   convention; glTF handles it by definition. This is the least invasive option and the safest for
   animated assets.
2. **Author in the target's orientation** in the source file: build the asset so that after the
   exporter's default conversion it lands correctly. Verify once, then reuse.
3. **Pre-rotate and apply**: rotate the object -90 degrees on X, apply rotation, and export without
   further conversion. This is the classic Unity trick, but it makes the Blender file itself
   unintuitive and can complicate rigs, so use it only for static meshes and only if the project
   standardises on it.

About the FBX **Apply Transform** option (`bake_space_transform`): it bakes the space conversion into
the mesh data. It is marked experimental in Blender and is known to misbehave with armatures and
animation. Do not use it on skinned or animated assets; for static meshes, test it once and keep the
result only if the whole library uses the same approach.

## Debugging routine

When an import looks wrong, work through this in order:

1. **Measure in-engine** against a known reference (a 1 m cube, or a character capsule). Note the
   exact factor: 100x, 0.01x, 2.54x (inches), or something else.
2. **Check Blender's Unit Scale** and the object's scale values in the N-panel.
3. **Check applied transforms** on the object and all its parents.
4. **Check the exporter's scale and axis settings**, then the importer's.
5. **Export a test cube** of exactly 1 m and import it. If the cube is right and the asset is not,
   the problem is in the asset, not the pipeline.
6. **Check for double conversion**: exporter converting units and importer also converting.
7. **Check the origin** if only the placement is off but the size is right.
8. **Check the hierarchy** if children misbehave while parents are fine.

Record the working combination of settings in the project readme as soon as you find it, including
exporter and importer values.

## Why real-world scale matters beyond import

- Physics: mass, gravity and collision behave correctly only at real scale.
- Depth of field and camera focal lengths assume real dimensions.
- Simulations (cloth, fluid, smoke) are scale-sensitive.
- Texel density is defined per metre, so scale drift silently ruins consistency.
- Lighting falloff and light units are physical.

## Checklist

1. Unit system Metric, Unit Scale 1.0, lengths in metres.
2. Asset dimensions match reality (check the N-panel Dimensions).
3. All transforms applied; scale 1, 1, 1; rotation zero.
4. Origin at the intended pivot.
5. Forward-axis convention matches the project standard.
6. Exporter axis and scale options set for the target once, then saved as a preset.
7. A 1 m test cube verified in-engine.
8. The working settings documented.
