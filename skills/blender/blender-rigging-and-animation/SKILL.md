---
name: blender-rigging-and-animation
description: Rig characters and props in Blender and animate them so the motion reads and the rig survives export. Use whenever the user asks how to build an armature, how to place and name bones, how to parent and skin a mesh, how to weight paint or fix bad weights, how IK and FK work and how to switch between them, which constraints to use for controls, how to make custom bone shapes and organise bone collections, how to use Rigify, how to fix a collapsing shoulder elbow or knee, how to animate a walk cycle or a jump, how to work in the graph editor with F-curves and interpolation, how to use the NLA editor, how to add corrective shape keys, how to bake constraints into keyframes, or how to make a rig and its animations export cleanly to a game engine. Covers armature construction and bone roll, weighting workflows and influence limits, IK FK constraints drivers and rig ergonomics, bone collections after the 4.0 layer replacement, the animation principles that matter in 3D, blocking to spline workflow, curve and handle discipline, action and NLA organisation, corrective shapes, and game-rig rules including root motion baking and per-vertex influence budgets.
version: 1.0.0
---

# Rigging and animation

A rig is a user interface for deformation. An animation is a set of poses with deliberate timing.
Both fail for the same reason: skipping the boring setup that makes the interesting work possible.

## When to use

- Building an armature and skinning a character, creature or mechanical prop.
- Fixing weights, collapsing joints, or deformation that breaks under rotation.
- Setting up IK/FK, constraints, drivers, custom shapes and control hierarchies.
- Animating cycles, actions, cameras or props.
- Working in the graph editor, dope sheet or NLA.
- Preparing a rig and its animations for a game engine.

Topology for deformation comes first - see `../blender-topology-and-retopology/SKILL.md`. If the mesh
has no loops at the joints, no rig will save it.

## Ask first

1. **Where does it end up?** Film-style rigs can use anything; game rigs are constrained by engine
   rules.
2. **Biped, quadruped, mechanical, or something else?** Determines the joint plan and whether Rigify
   fits.
3. **Who animates it?** A rig for yourself and a rig for a team have different ergonomics.
4. **Facial animation needed?** Bones, shape keys, or both.
5. **Is the mesh final?** Reweighting after a mesh change costs real time.
6. **Frame rate and shot length?** Sets keyframe density and blocking strategy.

## Core rules

1. **Name bones properly from the start**: descriptive plus `.L` / `.R` suffixes, so symmetry,
   mirroring and engine tools work.
2. **Bones go where joints rotate**, not where they look neat. Place them from reference and check in
   three views.
3. **Roll matters.** Consistent bone roll makes rotations predictable and IK poles behave.
4. **Weights are hierarchical**: get large smooth influence right before painting details.
5. **Limit influences** for games (commonly four per vertex) and normalise weights.
6. **Rig ergonomics are part of the deliverable**: custom shapes, bone collections, sensible control
   counts, no animator ever selecting a deform bone.
7. **Pose, then time, then polish.** Blocking first, curves later.
8. **Constraints do not export.** Bake actions before exporting to an engine.

## Workflow

**Step 0 - check the mesh**: applied transforms, real scale, loops at joints, T- or A-pose.

**Step 1 - build the armature**: joint placement, roll, hierarchy, naming. See
   `references/armatures-and-weights.md`.

**Step 2 - skin and weight**: automatic weights, then correction, then limits and normalisation.

**Step 3 - test deformation** through the extremes before adding any controls.

**Step 4 - add controls**: IK/FK, constraints, drivers, custom shapes, bone collections. See
   `references/controls-and-constraints.md`.

**Step 5 - block the animation** in stepped mode: key poses and timing only. See
   `references/animation-craft.md`.

**Step 6 - spline and polish**: curves, arcs, overlap, follow-through, contact fixes.

**Step 7 - deliver**: organise actions, bake where needed, export per the engine's rules. See
   `references/game-rigs-and-export.md`.

## References

| File | Read it for |
| --- | --- |
| `references/armatures-and-weights.md` | Bone placement per joint, roll, hierarchy and naming, parenting and the Armature modifier, automatic vs manual weights, weight painting tools, influence limits, deformation fixes, corrective shape keys |
| `references/controls-and-constraints.md` | IK and FK, pole targets, IK/FK switching, the constraint catalogue with real uses, drivers, custom bone shapes, bone collections and colours after 4.0, Rigify, rig ergonomics checklist |
| `references/animation-craft.md` | The principles that actually change a shot, blocking to spline workflow, walk and run cycle structure, graph editor and handle discipline, arcs and overlap, holds, frame rates, actions and NLA organisation |
| `references/game-rigs-and-export.md` | Game rig constraints, bone budgets and influence limits, root motion, baking constraints and actions, FBX vs glTF for animation, retargeting, per-engine notes, validation checklist |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-topology-and-retopology/SKILL.md` | Deformation topology needs fixing |
| `../blender-sculpting/SKILL.md` | Sculpting corrective shapes or posed versions |
| `../blender-to-engine-export/SKILL.md` | Export settings, scale and axis conventions |
| `../blender-lighting-and-rendering/SKILL.md` | Rendering animation, motion blur, output |
| `../../game/2d/sprite-animation/SKILL.md` | The 2D counterpart: timing, cycles, spritesheets |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Shoulder or hip collapses when rotated | Too few loops, weights too tight, no helper bone | Add loops, soften weights, add a twist/helper bone |
| Elbow or knee pinches | No loops at the joint, weights split across the wrong edge | Add support loops, reweight across three loops |
| Wrist twists like a rubber tube | No twist bone distributing rotation | Add forearm twist bones with a Copy Rotation at 0.5 |
| Mesh stretches oddly at extremes | Automatic weights left unedited | Manual paint, Limit Total, Normalize All |
| Parts of the mesh do not move | Vertices with zero weight, or missing from the vertex group | Weight paint with Select Zero Weight / Normalize |
| Rig is unusable by others | Deform bones selectable, no custom shapes, no collections | Hide deform bones, add shapes, organise collections |
| IK limb flips or snaps | No pole target, or bad bone roll | Set a pole target; fix roll; use Recalculate Roll |
| Animation looks floaty | Bezier interpolation everywhere, no holds, no contrast in timing | Sharpen curves, add moving holds, vary spacing |
| Rotations jitter or gimbal-lock | Euler rotation on a spinning bone | Use quaternions for bones, Euler for readable single-axis controls |
| Export has no animation | Constraints not baked, or wrong exporter options | Bake Action; check the exporter's animation settings |
| Engine complains about influences | More than four weights per vertex | Limit Total to the engine's budget and normalise |

## Answering style

- Name the bone, the constraint and the exact setting rather than describing it vaguely.
- Separate rig problems (deformation, controls) from animation problems (timing, curves).
- For game work, state the engine's constraint (bone count, influences, root motion) explicitly.
- Recommend testing deformation at extremes before any polish work.
