# Armatures and weighting

## Before the first bone

1. Mesh at real-world scale, transforms applied, scale 1, 1, 1.
2. A- or T-pose with slightly bent limbs (a perfectly straight limb gives IK no plane to solve in).
3. Loops at every joint: `../../blender-topology-and-retopology/references/deformation-topology.md`.
4. Symmetric mesh, mirrored cleanly, so weights can be mirrored.
5. Separate objects for clothing, hair and props decided up front.

## Bone placement

| Joint | Where the bone joint goes |
| --- | --- |
| Hip / pelvis root | At the pelvis centre, slightly above the crotch |
| Spine | 3-5 bones following the real curvature, not a straight line |
| Neck / head | Neck base at the top of the shoulders; head pivot between the ears at ear-canal height |
| Shoulder / clavicle | From near the spine out to the shoulder ball |
| Upper arm | At the shoulder's rotation centre, inside the deltoid mass |
| Elbow | At the bony hinge, slightly back from the arm's centreline |
| Wrist | At the wrist crease; add forearm twist bones between elbow and wrist |
| Fingers | Three bones per finger at the visible knuckle creases |
| Thigh | At the hip ball joint, inside the pelvis, not at the skin surface |
| Knee | At the hinge, slightly forward |
| Ankle / foot | Ankle at the joint; foot bone to the ball; toe bone from ball to tip |

Rules:

- Check placement in front, side and perspective views; a correct front view with a wrong side view
  is the most common error.
- Put joints at rotation centres, which are usually inside the volume, not on the surface.
- Keep limb chains slightly bent so the IK solver has a well-defined plane.
- Use Snap to face/vertex and X-mirror editing to keep both sides identical.

## Roll and orientation

- Bone roll defines the local axes. Inconsistent roll makes rotations feel random and IK poles
  misbehave.
- Use Armature > Bone Roll > Recalculate Roll with a sensible reference (Global +Z, View Axis, or
  Active Bone) for whole chains.
- Keep the same convention across the rig: for example, bone Y along the bone, Z pointing "up" or
  "out" consistently on every limb.
- Verify with the axes overlay enabled in the armature display settings.
- For game engines, consistent roll makes retargeting and IK setups much less painful.

## Hierarchy and naming

```
root
  hips
    spine_01 > spine_02 > spine_03 > neck > head
    thigh.L > shin.L > foot.L > toe.L
    thigh.R > shin.R > foot.R > toe.R
    clavicle.L > upperarm.L > forearm.L > hand.L > finger bones
```

- Suffix mirrored bones `.L` / `.R`. Blender uses that suffix for symmetrize, mirrored weight paint
  and flipped poses.
- Number chains with padding (`spine_01`) so sorting behaves.
- Separate **deform** bones (skinned) from **control** bones (animated) and from **mechanism** bones
  (helpers). Only deform bones should have vertex groups.
- Disconnect bones (Alt+P > Disconnect) where a chain should not inherit translation while keeping
  the parent relationship.
- Turn off Inherit Rotation / Inherit Scale where a bone must stay stable (e.g. some twist and helper
  bones).

## Skinning

1. Select mesh, then armature, Ctrl+P > **With Automatic Weights** (or With Empty Groups for full
   manual control).
2. This adds an Armature modifier; keep it after generative modifiers that create the base shape and
   before Corrective Smooth.
3. Enable **Preserve Volume** (dual quaternion skinning) to reduce the classic twist-collapse, with
   the caveat that it behaves differently at extreme rotations.
4. Add a **Corrective Smooth** modifier (Length Weight or Simple) to clean up automatic-weight
   artifacts without hand painting everything.
5. Test immediately: rotate every joint to its extreme and look for collapse, pinching and
   candy-wrapper twisting.

For mechanical rigs, parent parts directly to bones (Ctrl+P > Bone) instead of skinning; rigid parts
should not deform at all.

## Weight painting

| Tool / option | Use |
| --- | --- |
| Draw brush | Add or subtract weight; keep strength low and build up |
| Blur brush | Smooth harsh transitions |
| Smear / Average | Even out a region |
| Gradient tool | Linear or radial falloff across a limb |
| Weights > Normalize All | Make weights per vertex sum to 1 |
| Weights > Limit Total | Cap influences per vertex (4 for most engines) |
| Weights > Smooth | Algorithmic smoothing across the whole group |
| Weights > Mirror | Copy the weights across `.L` / `.R` |
| Weights > Transfer Weights (Data Transfer) | Copy weights from another mesh, e.g. body to clothing |
| X Mirror option | Paint both sides at once |
| Auto Normalize | Keeps weights summing to 1 while painting |
| Front Faces Only | Avoids painting through the mesh |
| Overlay > Zero Weights | Reveals unweighted vertices |

Painting order that works:

1. Start from automatic weights - hand-painting from zero is rarely worth it.
2. Fix the **big** transitions first: hips, shoulders, spine.
3. Work joint by joint, posing the joint to its extreme while painting.
4. Aim for smooth gradients across three loops at a joint: roughly 100% / 50% / 0%.
5. Mirror when one side is finished.
6. Run Normalize All, then Limit Total to the target budget, then Normalize All again.
7. Check for zero-weight vertices and stray influences (a hand bone affecting the hip is common with
   automatic weights).

## Deformation fixes

| Problem | Fix |
| --- | --- |
| Candy-wrapper twist on the forearm | Two or three twist bones between elbow and wrist, each with Copy Rotation from the hand at a fraction (0.33/0.66) on the bone's Y axis |
| Shoulder collapse | Clavicle bone taking part of the rotation, plus a helper bone driven at 50% of the arm rotation |
| Hip crease | Extra loops, softer weights, and a helper bone for the thigh's front |
| Volume loss on bends | Preserve Volume, Corrective Smooth, or corrective shape keys |
| Knee/elbow pinch | Three loops across the joint and weights distributed over all three |
| Clothes intersecting the body | Transfer weights from the body, then adjust; Shrinkwrap-based fitting; or Cloth simulation |
| Jaw/neck stretching | Head pivot placed correctly; a separate jaw bone |

## Corrective shape keys

1. Pose the rig into the problem position.
2. Create a shape key, sculpt the correction on the posed result (enable the sculpt/edit-on-pose
   workflow, or model the fix and use it as a key).
3. Add a **driver** on the shape key value, using the driving bone's rotation as the variable
   (Transform Channel, Rotation, correct axis, in the right space).
4. Set the driver's mapping so the key reaches 1.0 at the extreme pose and 0 at rest.
5. Keep corrective keys few and targeted: elbows, knees, shoulders, hips, jaw.

Corrective shape keys export to engines as blend shapes only if the engine and exporter support
driving them; in games it is more common to bake the correction into the skinning or accept the
artifact.

## Weighting checklist

1. Every vertex has a total weight of 1 and belongs to at least one group.
2. No vertex exceeds the influence budget.
3. Weights mirrored and symmetric.
4. No stray influences from distant bones.
5. Every joint tested at its extreme, both directions.
6. Twist bones handling forearm and shin rotation.
7. Corrective smoothing or shape keys only where genuinely needed.
8. Clothing weights transferred rather than painted from scratch.
