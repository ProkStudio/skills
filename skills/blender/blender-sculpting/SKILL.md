---
name: blender-sculpting
description: Sculpt organic and stylised forms in Blender and hand the result off cleanly. Use whenever the user wants to sculpt a character creature head or organic prop, asks which brushes to use for what, how to block out forms before detailing, when to use Dyntopo versus Multiresolution versus Voxel Remesh, how to add skin pores wrinkles cloth folds or other fine detail, why the sculpt looks muddy soft or noisy, why Dyntopo is slow or destroys detail, how masking Face Sets symmetry and the Mesh Filter work, how to sculpt with layers non-destructively, or how to get a sculpt into a usable low-poly with baked maps. Covers the blocking to refining to detailing progression, primary secondary and tertiary form discipline, brush selection per task with their real behaviour, the three geometry strategies and when each breaks, brush assets in recent Blender versions, masking and auto-masking, Face Sets, trim and remesh cleanup, performance limits, and the sculpt to retopology to bake handoff.
version: 1.0.0
---

# Sculpting

Sculpting is drawing in 3D: large shapes first, always, and resolution only where you have earned it.
Most bad sculpts are not badly detailed - they are detailed too early on forms that were never right.

## When to use

- Sculpting characters, creatures, heads, anatomy, organic props, stylised forms.
- Adding wrinkles, folds, pores, scales, damage, or any fine surface detail.
- Choosing between Dyntopo, Multiresolution and Voxel Remesh.
- Diagnosing a muddy, lumpy, soft or noisy sculpt.
- Preparing a sculpt for retopology, baking, printing or rendering.

Scale and file hygiene come from `../blender-fundamentals/SKILL.md`. Rebuilding a clean mesh over the
sculpt is `../blender-topology-and-retopology/SKILL.md`.

## Ask first

1. **What is the end product?** Render, game asset, 3D print, or a base for retopology. This decides
   the geometry strategy and how far to detail.
2. **Realistic or stylised?** Stylised forms need cleaner, larger shapes and less noise; realism
   needs reference and anatomy discipline.
3. **Do you have reference?** Anatomy from memory produces generic mush.
4. **What machine?** Sculpting is RAM and CPU bound; a 20-million-triangle plan needs hardware to
   match.
5. **Will it deform later?** If yes, plan for retopology rather than shipping the sculpt.

## Core rules

1. **Primary, secondary, tertiary - in that order.** Big masses, then major forms, then fine detail.
   Never sculpt a pore before the skull is right.
2. **Resolution follows form.** Only subdivide or remesh when the current density stops you from
   expressing the shape you already see.
3. **Silhouette first.** Check the outline from front, side and three-quarter constantly; rotate
   often.
4. **Use symmetry until the pose breaks it**, then work asymmetrically on purpose.
5. **Smooth is a tool, not a rescue.** Over-smoothing is the main cause of soft, muddy sculpts.
6. **Keep the low-detail version.** Save versions before every remesh or big topology change.
7. **Detail is not the same as noise.** Detail follows anatomy and direction; noise is random.

## Workflow

**Step 0 - reference board**: anatomy references, scale figure, real dimensions.

**Step 1 - blockout** from primitives or a simple base mesh; proportion and gesture only. See
   `references/blockout-and-forms.md`.

**Step 2 - primary forms**: the big masses, with a low-resolution mesh and big brushes. Voxel remesh
   whenever density limits you.

**Step 3 - secondary forms**: muscle groups, major folds, planes of the face; still low enough
   resolution to move things.

**Step 4 - choose the geometry strategy** for detailing: Multires if the base is clean, Dyntopo for
   free-form growth, Voxel for repeated reshaping. See `references/geometry-strategies.md`.

**Step 5 - refine**: crease, pinch, flatten, scrape - define planes and edges rather than adding
   noise. See `references/brush-kit.md`.

**Step 6 - tertiary detail**: pores, wrinkles, scales, stitches - layered, directional, varied. See
   `references/detail-and-handoff.md`.

**Step 7 - handoff**: retopologise, unwrap, bake normal/displacement, or prepare for print.

## References

| File | Read it for |
| --- | --- |
| `references/blockout-and-forms.md` | Base-mesh options, gesture and proportion, form hierarchy for organics, anatomy checkpoints, silhouette checking, stylisation decisions |
| `references/geometry-strategies.md` | Dyntopo vs Multires vs Voxel Remesh in detail, their real limitations, performance limits, remesh and trim cleanup, when to switch strategies |
| `references/brush-kit.md` | Which brush does what, recommended strengths, brush assets in recent versions, masking and auto-masking, Face Sets, Mesh and Cloth filters, symmetry options |
| `references/detail-and-handoff.md` | Detail passes and layering, direction and variation, skin/cloth/hard-surface detail recipes, retopology and bake handoff, displacement vs normal maps, print preparation |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../blender-topology-and-retopology/SKILL.md` | Building the low-poly over the sculpt |
| `../blender-uv-and-baking/SKILL.md` | Unwrapping and baking sculpt detail to maps |
| `../blender-materials-and-texturing/SKILL.md` | Skin, cloth and surface shading |
| `../blender-rigging-and-animation/SKILL.md` | Posing and deforming the retopologised mesh |
| `../blender-lighting-and-rendering/SKILL.md` | Presenting the sculpt |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| Sculpt looks soft and muddy | Over-smoothing, detail before form | Rebuild planes with Flatten/Scrape, work larger |
| Detail looks like random noise | No direction, uniform density | Follow anatomy, vary scale, layer passes |
| Blender becomes unusably slow | Dyntopo with too fine a detail size, or 20M+ triangles | Raise detail size, remesh coarser, hide parts, use Multires levels |
| Dyntopo destroyed fine detail | Detail size too coarse when a stroke touched that area | Sculpt detail after topology is stable; use Multires instead |
| Voxel remesh erased UVs and groups | Voxel Remesh discards object data layers | Remesh before UVs; keep the original |
| Multires refuses to subdivide sensibly | Base mesh has bad topology, N-gons or triangles | Fix the base first; Multires wants a clean quad base |
| Lumpy surface with visible bumps | Brush strength too high, alpha tiling, no smoothing pass | Lower strength, use Smooth sparingly, Mesh Filter > Smooth |
| Symmetry not working | Object not at origin, unapplied transforms, or sculpt already asymmetric | Apply transforms, reset origin, use Symmetrize |
| Retopology impossible | Sculpt has intersecting and non-manifold geometry | Voxel Remesh to a clean manifold first |

## Answering style

- Always ask what the sculpt is for before recommending a geometry strategy.
- Name the form level (primary/secondary/tertiary) that the user's problem actually lives at.
- Give brush names with strengths and intent, not just a list.
- Mention performance limits honestly: some plans need hardware, not technique.
