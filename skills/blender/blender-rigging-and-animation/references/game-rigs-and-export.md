# Game rigs and animation export

## What engines require

| Requirement | Reason |
| --- | --- |
| One armature per character | Importers expect a single skeleton root |
| A single root bone at the origin, axis-aligned | Root motion, attachment, retargeting |
| Applied transforms, object scale 1, 1, 1 | Avoids double transforms and scale drift |
| Deform bones only in the exported hierarchy | Control and mechanism bones confuse importers |
| Limited influences per vertex (commonly 4) | Runtime skinning budget |
| Normalised weights | Undefined behaviour otherwise |
| No constraints or drivers at runtime | They do not export; bake instead |
| Uniform scale on bones (ideally none) | Non-uniform bone scale is poorly supported |
| Consistent naming with `.L` / `.R` or `_l` / `_r` | Retargeting and mirroring tools |

Influence budgets differ: four bones per vertex is the classic default (and Unity's common setting),
while Unreal supports more (eight or twelve in UE5 configurations). Confirm the project's setting
rather than assuming, then enforce it with Weights > Limit Total.

Bone count: modern engines handle a few hundred bones, but every bone costs animation memory and
CPU. Typical budgets: 50-80 bones for a simple character, 100-160 with fingers and facial bones,
more only for hero characters.

## Rig structure for export

```
root                (at world origin, Y or Z forward per engine)
  pelvis
    spine_01 ... neck_01, head
    thigh_l > calf_l > foot_l > ball_l
    clavicle_l > upperarm_l > lowerarm_l > hand_l > fingers
```

- Keep the export skeleton clean and flat in purpose: no IK controls, no widgets, no helpers that the
  engine does not need. Twist bones are fine and often desirable.
- If you animate on a complex rig (Rigify or custom), bake onto a clean export skeleton via Copy
  Transforms constraints plus Bake Action.
- Attachment points (weapon sockets) can be extra bones parented to hands or spine; name them
  obviously (`socket_weapon_r`).

## Root motion

Two approaches:

| Approach | Setup | Engine side |
| --- | --- | --- |
| In-place animation | Character animates without translating; root stays still | Engine moves the character via code/navigation |
| Root motion | The root bone carries the forward translation and turning | Engine extracts root motion from the clip |

For root motion:

1. Animate the root bone's translation and yaw to match the actual movement.
2. Keep the root bone on the ground plane, at the character's centre of mass footprint.
3. Do not put bounce or vertical noise on the root unless the engine expects it.
4. Ensure the first frame has the root at the origin if the engine requires it.
5. Verify the motion curve is smooth - root jitter shows up as character stutter.

## Baking

Constraints, drivers and IK do not export. Bake them:

1. Select the armature, enter pose mode, select the bones to bake.
2. Pose > Animation > **Bake Action** with:
   - Visual Keying on (captures constrained results),
   - Clear Constraints if baking onto the same rig,
   - Only Selected Bones as appropriate,
   - the correct frame range and step (1).
3. Bake onto the **export skeleton** rather than destroying the animation rig, by constraining export
   bones to animation bones and baking those.
4. After baking, run Clean Keyframes to remove redundant keys, then spot-check the result against the
   original.
5. Keep the unbaked animation file as the source of truth.

Bake shape-key animation separately if the engine consumes blend shapes; verify the exporter's shape
key and animation options together.

## FBX vs glTF for animation

| | FBX | glTF 2.0 |
| --- | --- | --- |
| Skinning | Supported | Supported |
| Multiple animations | "All Actions" or NLA strips | Multiple animations from actions/NLA |
| Blend shapes | Supported | Supported (morph targets) |
| Axis conversion | Manual settings needed | Defined by the format |
| Engine support | Universal in Unity/Unreal | Universal on web, good in Godot and Unity/Unreal via plugins |
| Gotchas | Apply Transform is experimental and known to misbehave with armatures and animation; Use Mesh Modifiers prevents shape key export | Fewer axis problems; check the exporter's animation mode and sampling settings |

Practical guidance: prefer glTF where the engine supports it well, because fewer conventions are
left undefined. Use FBX when the studio pipeline or the engine's importer demands it, and do not
rely on FBX's experimental transform options for animated characters - fix the source instead.

Always export a test with one short clip and verify in-engine before exporting fifty clips.

## Exporting multiple clips

| Strategy | How |
| --- | --- |
| One file per clip | Export the armature with a single active action; simplest to manage, easiest for version control |
| All actions in one file | Exporter's all-actions option; convenient but produces large files and name collisions |
| NLA strips | Each strip becomes a clip; good control over ranges and names |
| Separate skeleton and clips | Export the skinned mesh once, then animation-only files referencing the same skeleton |

Naming matters downstream: `char_hero_run_fwd`, `char_hero_idle_01`. Keep clip names stable, because
engine state machines reference them.

## Retargeting

- Retargeting maps one skeleton's animation onto another. It works well when bone names, orientations
  and proportions are close.
- Give the rig a standard naming scheme and a T- or A-pose matching the target skeleton's reference
  pose.
- Blender-side options include constraint-based retargeting (Copy Rotation per bone plus Bake Action)
  and add-ons; engine-side options include Unreal's IK Rig/Retargeter and Unity's Humanoid avatar.
- Consistent bone roll is what makes retargeting behave; inconsistent roll produces twisted limbs.
- Mocap data usually needs cleanup: filter noise, fix foot sliding, then bake.

## Validation checklist

1. Object transforms applied; armature and mesh scale 1, 1, 1.
2. Single armature, single root bone at the origin.
3. Only deform bones exported; controls and widgets excluded.
4. Influences limited to the engine's budget and normalised.
5. No constraints or drivers left on exported bones - all baked.
6. Bone count within budget.
7. Animations named per convention, ranges correct, cycles looping exactly.
8. Root motion behaviour matching the engine's expectation.
9. A test clip imported in-engine and verified for scale, orientation and skinning.
10. Source .blend kept with the unbaked animation rig.
