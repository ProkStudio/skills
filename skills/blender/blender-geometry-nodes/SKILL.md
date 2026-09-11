---
name: blender-geometry-nodes
description: Build procedural geometry in Blender with Geometry Nodes and keep it fast and debuggable. Use whenever the user asks how to scatter objects trees rocks or grass, how to instance geometry on points, how to build a procedural generator for fences pipes cables buildings or arrays, how fields work and why a socket will not connect, what attributes and domains are, how to store or read named attributes, how to deform geometry procedurally with noise or textures, how to use curves to mesh, how to use repeat or simulation zones, how to make node tools for edit mode, why a node setup is slow or crashes, or how to inspect what a node tree is actually producing. Covers the field and data-flow model, attribute domains and interpolation, instancing versus realized geometry, scattering with density masks and collision avoidance, sampling and proximity nodes, curve workflows, zones for loops and simulation, node groups and exposed controls, node tools, performance limits, and a viewer plus spreadsheet debugging routine.
version: 1.0.0
---

# Geometry Nodes

Geometry Nodes is a data pipeline: geometry flows through it, and **fields** describe per-element
values evaluated where they are used. Almost every confusing error comes from mixing up those two
ideas, or from the wrong attribute domain.

## When to use

- Scattering: forests, rocks, grass, debris, crowds, city blocks.
- Generators: fences, pipes, stairs, railings, cables, modular buildings, arrays.
- Procedural deformation: noise displacement, bending along curves, growth animation.
- Anything that must stay editable or be re-rolled with different parameters.
- Node tools that act like custom modelling operators in edit mode.

Use plain modelling when the asset is a one-off and will never change; procedural setups cost time up
front and pay off on variation, iteration and scale.

## Ask first

1. **One asset or a family?** Procedural pays off on families and on things that change.
2. **Does it need to be real geometry downstream?** Exporters, booleans and some modifiers need
   realized geometry; instances stay cheap but are not editable.
3. **How many elements?** A thousand instances and ten million are different engineering problems.
4. **Will it be exported to an engine?** Engines want baked meshes, not node trees.
5. **Who will use the setup?** If another person drives it, the node group needs clean exposed inputs
   and sane defaults.

## Core rules

1. **Fields are recipes, not values.** A diamond socket accepts a field; a round socket wants a
   single value. If a connection is refused, one side needs a context to evaluate in.
2. **Every attribute lives on a domain** (point, edge, face, face corner, curve, instance). Most bugs
   are domain mismatches; interpolation between domains is implicit and lossy.
3. **Instance, do not realize.** Realize Instances multiplies memory; keep geometry instanced until
   something truly requires real data.
4. **Name attributes deliberately** and document them; anonymous attributes are fine inside a tree but
   named ones cross boundaries.
5. **Randomness needs an ID.** Use the ID or a stable index as the seed source or the randomisation
   will pop when topology changes.
6. **Expose a small set of controls** on the node group; a generator with forty inputs is unusable.
7. **Debug with the Viewer node and the Spreadsheet**, not by staring at the tree.
8. **Procedural does not mean free.** Measure, and simplify the heaviest branch.

## Workflow

**Step 0 - state the goal as inputs and outputs**: what geometry comes in, what should come out, what
   parameters should the user control.

**Step 1 - build the smallest working version** on a simple input, with hardcoded values.

**Step 2 - check the data** with the Viewer node and the Spreadsheet at each step. See
   `references/patterns-and-debugging.md`.

**Step 3 - replace constants with fields**: textures, attributes, random values, masks. See
   `references/fields-and-domains.md`.

**Step 4 - instance rather than build** wherever possible. See
   `references/instancing-and-scattering.md`.

**Step 5 - add control**: expose inputs, set ranges and defaults, group and label.

**Step 6 - measure performance** and cut the heaviest operations.

**Step 7 - decide the handoff**: keep procedural, apply to a mesh, or bake for export.

## References

| File | Read it for |
| --- | --- |
| `references/fields-and-domains.md` | The field model, socket shapes, domains and interpolation, capture and store, named vs anonymous attributes, selection inputs, common field errors |
| `references/instancing-and-scattering.md` | Instance on Points, Collection and Object Info, scattering with Distribute Points on Faces, density masks, Poisson disk, random rotation and scale, collision avoidance, realize costs, camera culling |
| `references/generators-and-curves.md` | Curve to Mesh workflows, profiles and resampling, extrusion, repeat and simulation zones, modular generators, boolean use, node tools for edit mode, reusable node groups |
| `references/patterns-and-debugging.md` | Viewer and Spreadsheet routine, recipe patterns for common asks, performance limits and optimisation order, error message decoder, handoff and baking |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-fundamentals/SKILL.md` | Modifier stack order, scale and units |
| `../blender-materials-and-texturing/SKILL.md` | Shading the generated geometry, attributes in shaders |
| `../blender-lighting-and-rendering/SKILL.md` | Rendering heavy instanced scenes |
| `../blender-to-engine-export/SKILL.md` | Baking procedural results for an engine |
| `../blender-hard-surface-modeling/SKILL.md` | When plain modelling is simply faster |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Socket will not connect | Field connected where a single value is required | Capture the field, or use it inside a node that evaluates fields |
| Attribute values look wrong or averaged | Domain mismatch with implicit interpolation | Store on the intended domain; check the Spreadsheet domain tabs |
| Randomisation pops when geometry changes | Seed based on index, which changes | Use the ID attribute or a stable custom ID |
| Scattered objects float or sink | Instance origin not at the base, or no alignment | Fix object origins; align rotation to the normal |
| Blender freezes or runs out of memory | Realize Instances on a huge scatter, or boolean on dense meshes | Keep instances; reduce counts; avoid heavy booleans |
| Nothing appears | Output not connected, geometry consumed by a node, or selection empty | Follow the Viewer down the chain |
| Exported mesh is empty | Instances never realized for the exporter | Realize or apply before export |
| Material lost on generated geometry | Material not set inside the tree | Use Set Material, or Realize and assign |
| UVs missing after generation | UVs are a face-corner attribute that generators must create | Store a UV attribute explicitly, or unwrap after applying |
| Setup is unusable by others | Too many raw inputs, no defaults, no labels | Group, label, expose a minimal control set |

## Answering style

- Name the exact nodes in order, as a chain, not as prose.
- State which domain each attribute lives on.
- Say when plain modelling would be faster than a node tree.
- Give the debugging step (Viewer plus Spreadsheet) before theorising about a bug.
