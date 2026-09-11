# Topology for deformation

## The principle

A mesh bends by moving vertices. If there are no vertices where the bend happens, the surface
collapses, creases wrongly, or intersects itself. So: **put loops where motion happens, oriented
along the direction of the crease.**

Two orientations matter:

- **Loops across the joint** (perpendicular to the limb) allow bending.
- **Loops around the joint** (following the muscle form) keep the silhouette during the bend.

## Loop counts per joint

| Area | Minimum loops | Comfortable | Notes |
| --- | --- | --- | --- |
| Elbow / knee | 3 across the bend | 4-5 | Bias loops toward the inside of the bend |
| Shoulder | 3-4 radial | 5-6 | Hardest joint; loops should follow the deltoid |
| Hip | 3-4 | 5 | Needs loops that wrap from the thigh into the pelvis |
| Wrist / ankle | 2-3 | 4 | Also carries twist |
| Finger joint | 2 | 3 | Real-time hands often use 2 |
| Neck | 3 | 4-5 | Rotation plus bend |
| Spine segment | 2-3 per bone | 4 | Even spacing along the torso |
| Mouth corner | radial loops | 3+ rings | See face section |
| Eyelid | 2-3 rings | 4 | Must slide over the eyeball |

For real-time assets, halve the comfortable numbers and rely on good weighting; for film-quality
deformation, use the higher counts plus corrective shape keys.

## Limb topology

- Loops perpendicular to the limb's length, evenly spaced, denser at joints.
- Keep a consistent loop count around the limb's circumference (8, 12 or 16 typical) so loops can run
  uninterrupted from wrist to shoulder.
- Poles on the limb belong on the least-visible, least-deforming side.
- The crease side of a joint (inside of elbow, back of knee) needs loops closer together than the
  stretch side.

## Torso and shoulders

- The shoulder girdle is where most character topology fails. Loops should radiate from the armpit
  around the deltoid, not run straight across the chest into the arm.
- Keep a loop following the collarbone and one around the armpit; they form the boundary between
  torso flow and arm flow.
- The chest and back want loops that follow the pectoral and scapula forms so that raising an arm
  does not smear the silhouette.

## Face topology

The face is loop-driven because it is muscle-driven:

- **Concentric rings around the eyes** (orbicularis oculi) - at least 3 rings, 4 for film.
- **Concentric rings around the mouth** (orbicularis oris) - at least 3 rings; the mouth corner is
  the highest-stress area on the face.
- **A loop following the nasolabial fold**, connecting the nose wing to the mouth corner.
- **Loops along the jaw and around the chin**, so speaking and chewing do not smear.
- Eyelid rings must be dense enough to slide over the eyeball without intersecting it.
- Keep poles at the bridge of the nose, the temples, behind the ear, under the jaw - never at the
  mouth corner or eye corner.
- Ear topology is usually a separate patch stitched into the head; it barely deforms, so its loop
  flow serves shape, not motion.

## How skinning interacts with topology

- Good topology reduces, but does not replace, good weights. Bad topology cannot be fixed with
  weights at all.
- A joint needs at least one loop that sits **at** the rotation point; the loops either side carry
  the falloff.
- Corrective shape keys (driven by bone rotation) fix the last 10%: elbow volume, shoulder shape,
  crotch and armpit intersections.
- For real-time, remember the engine's bone-influence limit (commonly 4 per vertex); dense loop
  clusters at joints help distribute those influences smoothly.

## Testing deformation

1. Add a quick armature with a couple of bones, or use Simple Deform (Bend) for a cheap test.
2. Bend the joint to its realistic extreme and 20% beyond.
3. Look for: collapse, self-intersection, silhouette loss, texture smearing, shading pinch.
4. Check both the crease side and the stretch side.
5. Twist the limb 90 degrees; twisting reveals insufficient loops faster than bending.
6. Fix topology first, weights second, corrective shapes third.

## Deformation checklist

1. Loops exist at every joint that bends, with the minimum counts above.
2. Loops are oriented along the crease, not across it.
3. No poles or triangles inside deformation zones.
4. Loop density biased toward the inside of each bend.
5. Face rings present around eyes and mouth.
6. Limb loop counts consistent so loops run uninterrupted.
7. Tested at extreme bend and twist before rigging properly.
