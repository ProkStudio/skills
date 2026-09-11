---
name: blender-fundamentals
description: Set up Blender projects correctly and work non-destructively before modelling anything. Use whenever the user is starting a Blender project or asks about scene scale and units, why bevels or physics or depth of field behave strangely, why an object looks wrong after scaling, how objects relate to mesh data-blocks, how to organise collections and instances, when to apply a modifier versus keeping the stack live, how to link or append between files, which Blender version or LTS to use, or how to keep .blend files clean, packed and versioned. Covers the unit system and real-world scale, transform hygiene with applied scale and rotation, object versus mesh data and shared data-blocks, collections, instancing and linked duplicates, modifier stack order and the non-destructive mindset, empties and parenting, folder layout, asset libraries, packed textures, orphan purge, autosave and version numbering, plus the current Blender release landscape. Always asks what the model is for and which Blender version is in use before giving settings.
version: 1.0.0
---

# Blender fundamentals

Most "why is Blender doing this?" problems come from three things: wrong scale, unapplied transforms,
and destructive edits that cannot be undone two hours later. Fixing those three habits prevents more
pain than any modelling technique.

## When to use

- Starting a project: scene setup, units, folder structure, file naming.
- Bevels, physics, particles, depth of field, lighting falloff or texture projection behave oddly.
- Objects arrive in an engine at the wrong size or rotation.
- Questions about object versus mesh data, linked duplicates, collections, instancing.
- Deciding when to apply a modifier and when to keep the stack live.
- Organising files, asset libraries, links, or version control for .blend files.

## Ask first

1. **What is the model for?** Render, game asset, 3D print, or animation. The target decides scale
   discipline, topology rules and export needs.
2. **Which Blender version?** Names and defaults move between releases; pipelines pin to LTS.
3. **Real-world size of the subject?** Decide before the first cube.
4. **Solo or shared file?** Shared work needs naming conventions, collections and linked assets.
5. **Render engine?** Cycles and EEVEE differ in which material and light setups are viable.

## Core rules

1. **Model at real-world scale.** 1 Blender unit = 1 metre. Bevel widths, physics, DOF, light
   falloff and engine import all assume it.
2. **Keep object scale at 1, 1, 1** unless you deliberately need otherwise. Non-uniform scale breaks
   bevels, normals, UV projection and exports.
3. **Object and mesh are different things.** Transform lives on the object; vertices live in the mesh
   data-block, which several objects can share.
4. **Non-destructive first.** Prefer modifiers, geometry nodes and shape keys over baked-in edits
   until the shape is final.
5. **Name things as you create them.** `chair_seat`, not `Cube.023`.
6. **Collections are the project's structure**, not a scratch pad: use them for exports, visibility
   and instancing.
7. **Save versioned files**, not one file overwritten forever.

## Workflow

**Step 0 - decide the target and the real-world size**, and record them in the file or a README.

**Step 1 - scene setup**: unit system, clipping, render engine, colour management. See
   `references/scene-and-units.md`.

**Step 2 - block with primitives at correct dimensions**, reading the N-panel instead of eyeballing.

**Step 3 - structure the file**: collections per logical group, empties as controls, linked
   duplicates for repeated parts. See `references/objects-and-datablocks.md`.

**Step 4 - build with a live modifier stack** in a deliberate order. See
   `references/modifiers-and-nondestructive.md`.

**Step 5 - apply only at the end**, keeping a pre-apply copy or an earlier file version.

**Step 6 - hygiene before handoff**: purge orphans, pack or relink textures, apply transforms where
   required, name everything. See `references/file-hygiene-and-versions.md`.

## References

| File | Read it for |
| --- | --- |
| `references/scene-and-units.md` | Unit system, real-size reference table, why scale matters per system, clipping distances, transform hygiene, origins and pivots, scale symptom table |
| `references/objects-and-datablocks.md` | Objects vs mesh data, shared data-blocks and linked duplicates, collections and collection instances, empties, parenting vs constraints, naming conventions |
| `references/modifiers-and-nondestructive.md` | Stack order rules, which modifiers stay live, mirror/array/bevel/subdivision practice, shape keys, when applying is unavoidable |
| `references/file-hygiene-and-versions.md` | Folder layout, external vs packed textures, link vs append, asset libraries, orphan purge, autosave and recovery, version numbering, Blender release landscape and LTS choice |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-hard-surface-modeling/SKILL.md` | Actually building the shape |
| `../blender-topology-and-retopology/SKILL.md` | Topology decisions, cleanup, shading errors |
| `../blender-geometry-nodes/SKILL.md` | Procedural setups instead of manual modelling |
| `../blender-lighting-and-rendering/SKILL.md` | Colour management, engine choice, output settings |
| `../blender-to-engine-export/SKILL.md` | Scale, orientation and export settings for engines |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Bevel width differs between identical-looking objects | Object scale is not 1, 1, 1 | Apply scale |
| Physics or particles move at absurd speed | Scene not at real-world scale | Model at 1 unit = 1 m, rescale and apply |
| Object arrives in engine 100x too small or rotated | Unapplied transforms plus axis convention | Apply transforms, set export axes |
| Editing one object changes another | Shared mesh data-block (linked duplicate) | Make object data single-user |
| Geometry disappears when zooming | Clip start/end wrong for scene scale | Adjust viewport and camera clipping |
| File is huge and slow | Packed high-res textures, no purge, duplicated data | Purge orphans, unpack textures, use links |
| Cannot go back after a change | Destructive edit with no version | Version files, keep pre-apply copies |
| Modifier result looks wrong | Wrong stack order | Generate before deform; bevel before subdivision |

## Answering style

- State the Blender version your answer assumes and note renamed settings.
- Give real-world dimensions in metres when describing blocking.
- Prefer a non-destructive route and say explicitly when applying is the only option.
- When a problem smells like scale or transforms, check those before anything else.
