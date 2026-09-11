# Controls, constraints and rig ergonomics

## IK and FK

| Mode | Behaviour | Best for |
| --- | --- | --- |
| FK (forward kinematics) | Rotate each bone in the chain | Arcs, free motion, arms in the air, tails |
| IK (inverse kinematics) | Move the end, the chain solves | Feet on the ground, hands on a surface, contact poses |

IK setup:

1. Add an IK target bone (usually unparented or parented to a control), not part of the deform chain.
2. Add an **Inverse Kinematics** constraint to the last bone of the chain (e.g. the shin), Target =
   the IK control, **Chain Length = 2** for a two-bone limb.
3. Add a **pole target** bone in front of the knee or behind the elbow to control the chain's plane,
   and adjust Pole Angle until the limb matches its rest orientation.
4. Use IK Stretch (bone stretch settings) only if the style allows stretching.
5. Limit rotations on the middle joint (Limit Rotation constraint or bone IK limits) so knees and
   elbows cannot invert.

IK/FK switching: duplicate the chain into IK and FK sets, then have the deform chain use **Copy
Transforms** constraints from both, with a driver on the influence so 0 = FK and 1 = IK. Expose that
driver as a custom property on a visible control bone.

**Spline IK** drives a bone chain along a curve - the standard solution for tails, tentacles,
ropes and spines that must follow a path.

## Constraint catalogue

| Constraint | Real use |
| --- | --- |
| Copy Location / Rotation / Scale | Partial or full transform copying; the building block of IK/FK blending and twist distribution |
| Copy Transforms | Full transform matching; snapping, IK/FK blends |
| Child Of | Dynamic parenting: picking up and dropping props |
| Limit Location / Rotation / Scale | Guard rails: keep knees from inverting, sliders in range |
| Limit Distance | Keep a control within a radius, e.g. eye targets |
| Transformation | Map one transform to another with custom ranges; mechanical relationships |
| Inverse Kinematics | Limb chains |
| Spline IK | Chains along curves |
| Damped Track / Track To / Locked Track | Aim a bone at a target: eyes, guns, heads |
| Follow Path | Motion along a curve, with Follow Curve for orientation |
| Armature (constraint) | Weighted multi-bone influence, useful for ribbon and helper setups |
| Stretch To | Squash and stretch along a target, muscle and rubber-hose effects |
| Shrinkwrap | Keep a control on a surface |
| Action | Drive a whole action from one transform; mechanical and facial setups |

Target spaces (World, Custom, Pose, Local) determine behaviour. When a constraint "jumps", a space
mismatch is the usual explanation.

## Drivers

- Right-click a property > Add Driver, then edit it in the Drivers editor.
- Variable types: Transform Channel (a bone's rotation/location), Single Property (a custom
  property), Distance, Rotational Difference.
- Use a **custom property** on a control bone (e.g. `ik_fk`, `foot_roll`, `fist`) as the animator's
  interface, then drive the real mechanics from it.
- Prefer scripted-expression-free drivers where possible; a mapping curve in the Drivers editor is
  easier to debug than an expression.
- Drivers do not export to engines. They are authoring tools; bake the result.

## Custom shapes and display

1. Model simple wireframe widgets (circles, cubes, arrows, text) in a hidden collection.
2. Assign per bone in Bone Properties > Viewport Display > Custom Object, with scale and offset
   adjustments.
3. Use **Wireframe** display for controls so they do not obscure the mesh.
4. Colour-code by side and function using bone colours (per-bone and per-collection colours are
   available since 4.0): left one hue, right another, centre a third, IK controls distinct.
5. Hide deform and mechanism bones from the animator entirely.

## Bone collections

Blender 4.0 replaced the fixed 32 armature layers with **bone collections**:

- Create named collections (`controls_arm.L`, `deform`, `mechanism`, `face`) and assign bones.
- Collections can be nested (hierarchy support arrived in 4.1) and have their own colours.
- Toggle visibility per collection, which is how an animator reduces clutter.
- Solo/visibility state can be saved with the file, so deliver the rig with a sane default: controls
  visible, deform and mechanism hidden.

If a tutorial talks about armature layers and the M shortcut for moving bones between them, translate
it to bone collections.

## Rigify

- A bundled add-on that generates a full rig from a metarig: bipeds, quadrupeds, faces, wings and
  more.
- Workflow: add a metarig, fit its bones to the mesh (this is the part that decides quality),
  generate, then skin the mesh to the generated rig's deform bones.
- Strengths: fast, feature-rich, standard controls, IK/FK switching, twist handling.
- Costs: complex generated structure, harder to debug, heavy for games (needs baking and cleanup
  before export).
- For game characters, many studios build a simple custom rig for export and use a Rigify-style rig
  only for animation, baking the result onto the export skeleton.

## Ergonomics

A rig is finished when an animator can work without asking questions:

1. Only controls are selectable; deform and mechanism bones are hidden or locked.
2. Controls have custom shapes at readable sizes and colours by side.
3. Bone collections are organised and named, with a sensible default visibility.
4. Custom properties (IK/FK, foot roll, fist, stretch) are on obvious bones.
5. Rotation modes chosen deliberately: quaternion for freely rotating bones, Euler (usually XYZ) for
   single-axis readable controls.
6. Transform locks applied to axes that should never move.
7. A reset-to-rest path exists (Alt+G/R/S works because rest is the neutral pose).
8. Limits prevent impossible poses.
9. The rig is tested by posing a full action, not just single joints.

## Constraint troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| Bone jumps when a constraint is added | Non-zero offset between current and target transforms | Clear the offset, use Copy Transforms, or set the correct space |
| IK limb flips at full extension | No pole target, or a perfectly straight rest chain | Add a pole target; bend the rest pose slightly |
| Pole makes the limb rotate oddly | Wrong Pole Angle | Adjust Pole Angle in 90-degree steps, then fine-tune |
| Child Of misbehaves | Inverse matrix not set | Use Set Inverse; re-set it if the parent moves |
| Driver does nothing | Wrong variable space or channel | Check Transform Channel axis and space in the Drivers editor |
| Rig slows down badly | Long constraint chains, heavy subdivision, simulation | Disable subdivision while animating; simplify mechanisms |
