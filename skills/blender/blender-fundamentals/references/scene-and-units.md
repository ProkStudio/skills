# Scene setup, units and transforms

## Units

- Scene Properties > Units: system Metric, Unit Scale 1.0, Length in metres.
- 1 Blender unit = 1 metre at Unit Scale 1.0. The default cube is 2 m on a side.
- Do **not** change Unit Scale to work at a different size; change the model instead. Unit Scale is
  for extreme cases (astronomical or microscopic scenes) and confuses downstream tools.

Reference sizes for blocking:

| Subject | Size |
| --- | --- |
| Door | 0.9 x 2.05 m |
| Ceiling height, residential | 2.4-2.7 m |
| Chair seat height | 0.45 m |
| Table height | 0.75 m |
| Kitchen counter height | 0.9 m |
| Adult human | 1.7-1.85 m |
| Car | ~4.5 x 1.8 x 1.45 m |
| Stair riser / tread | 0.17 / 0.28 m |
| Brick | 0.25 x 0.12 x 0.065 m |

Block with these and lighting, camera lenses and depth of field behave like the real world.

## Why real scale matters

| System | What breaks at the wrong scale |
| --- | --- |
| Bevel, solidify, displace | Absolute widths become meaningless |
| Physics (rigid body, cloth, fluid) | Gravity is 9.81 m/s^2; a 100x model falls like a feather |
| Depth of field and focal length | Lens maths is metric; DOF becomes unusable |
| Light falloff and exposure | Inverse-square falloff needs metres |
| Texture and texel density | Density is measured per metre |
| Engine import | Unity, Godot and Unreal all assume metres (Unreal displays centimetres) |

## Clipping

- Viewport clip start/end: N-panel > View tab. Camera clipping: camera data properties.
- Geometry vanishing as you zoom in means clip start is too large; distant geometry vanishing means
  clip end is too small.
- Z-fighting and flickering surfaces usually come from an extreme start/end ratio. Raise clip start
  rather than pushing clip end further out.
- Landscapes and cities need a larger clip end; jewellery and mechanical detail need a smaller clip
  start.

## Transform hygiene

Every object carries location, rotation and scale.

- **Scale must be 1, 1, 1** for predictable modelling. Resize in object mode, then Object > Apply >
  Scale. Non-uniform scale is the most common cause of uneven bevels and broken normals on export.
- **Rotation**: apply it when local axes should match world axes - important for arrays, mirrors and
  engine export.
- **Location**: keep the origin somewhere meaningful. Origin placement *is* rigging for simple props.
- Apply All Transforms bakes everything into the mesh and discards placement information, so do it
  knowingly.
- Negative scale (from mirroring) inverts normals. Apply scale, then recalculate normals outside.

## Origins and pivots

- Object > Set Origin: to geometry, to centre of mass, or to the 3D cursor.
- Snap the 3D cursor to a vertex, edge or face first (Shift+S) for exact placement.
- Rotating parts (wheels, hinges, turrets) need the origin on the axis of rotation.
- Props for engines usually want the origin at the base, centred in X and Y
  (`../../blender-to-engine-export/references/scale-and-orientation.md`).

## Scale symptom table

| Symptom | Check |
| --- | --- |
| Bevel amount differs between similar objects | Object scale |
| Modifier widths behave unpredictably | Object scale, unit scale |
| Simulation runs at the wrong speed | Scene scale in metres |
| Texture repeats at a different rate per object | Non-uniform or unapplied scale |
| Sharp shading breaks after mirroring | Negative scale on one axis |
| Object imports rotated 90 degrees | Unapplied rotation plus axis convention |
| Normals inverted after scaling | Negative scale; apply, then recalculate normals |

## Starting-file checklist

1. Units metric, Unit Scale 1.0.
2. Default cube, light and camera deleted or repurposed deliberately.
3. Render engine chosen; view transform set (AgX is the default since 4.0).
4. Clip start/end appropriate for the subject size.
5. Collections created for the project's logical groups.
6. File saved with a version number in the name before real work starts.
