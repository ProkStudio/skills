# Objects, data-blocks and scene structure

## The data model

Blender separates containers from data:

```
Scene
  Collection
    Object            <- transform, modifiers, constraints, parent
      Mesh data       <- vertices, edges, faces, UV maps, attributes, material slots
        Material      <- shared shader
        Image         <- shared texture
```

Consequences worth internalising:

- Two objects can share one mesh data-block. Editing the mesh in edit mode changes **both**. That is
  a linked duplicate (Alt+D), not a copy (Shift+D).
- Data-blocks are reference counted. Unused ones are dropped when the file is saved and reloaded,
  unless a fake user is set (the shield icon).
- Materials, node groups, images, actions, worlds and scenes are all data-blocks with the same
  sharing and fake-user rules.

## Duplicates

| Operation | Shortcut | Result |
| --- | --- | --- |
| Duplicate Objects | Shift+D | New object, new copy of mesh data |
| Duplicate Linked | Alt+D | New object, **shared** mesh data |
| Collection instance | Add > Collection Instance | Empty that draws a whole collection |
| Object > Relations > Make Single User | - | Breaks a shared data-block into an independent copy |

Use linked duplicates for repeated identical parts (bolts, window frames, fence posts): editing one
updates all, and the file stays small. Use collection instances for repeated assemblies (a whole
window, a tree, a modular wall section).

## Collections

- Collections nest, and an object can live in several at once.
- Use them for: logical grouping, export selection, visibility toggling, instancing, render layers,
  and to control what a modifier or physics system sees.
- Exclude (checkbox) removes a collection from the view layer entirely; hide (eye) is temporary
  viewport only; disable in renders (camera icon) affects output. Know which one you toggled -
  "my object vanished from renders" is almost always one of these.
- A practical layout for a prop file:

```
high_poly/       sculpt or subdivision source
low_poly/        game-ready or render-ready mesh
bakers/          cages, floaters, helper geometry
refs/            reference images, blockout, scale figure
render/          camera, lights, backdrop
```

## Empties, parenting and constraints

- **Empties** have no geometry. Use them as pivots, controls, instancing anchors, targets for
  constraints, and parents for groups of objects.
- **Parenting** (Ctrl+P) builds a transform hierarchy; children inherit the parent's transform. Keep
  Transform preserves the current world position.
- **Constraints** are better than parenting when you need one axis, a copy of rotation only, a
  target-tracking relationship, or a limit. They are also non-destructive and animatable.
- For engine export, hierarchies matter: most engines import the parent/child structure, and empties
  become transform nodes.

## Naming conventions

Pick one and apply it everywhere:

```
<asset>_<part>[_variant][_lod]
chair_seat, chair_leg_a, chair_leg_b
wall_modular_2m_lod0
prop_barrel_low, prop_barrel_high
```

Rules:

- Lowercase, underscores, no spaces or non-ASCII.
- Object name and its mesh data name should match; Blender does not keep them in sync automatically.
- Prefix helper objects clearly: `x_cage_`, `x_floater_`, `x_ref_`, so they are easy to filter and
  exclude from export.
- Material names describe the material, not the object: `mat_steel_painted`, not `mat_chair`.
- For engine work, the exported object name usually becomes the mesh name in the engine, so the
  convention must satisfy the engine's naming rules too.

## Library linking between files

| Operation | Behaviour | Use for |
| --- | --- | --- |
| Append | Copies data into the current file | One-off reuse, editing freely |
| Link | References data from another file, read-only | Shared assets across scenes, team pipelines |
| Library Override | Linked data with local, editable overrides | Posing a linked character, per-shot tweaks |

Linked files must keep their paths stable - use relative paths (`//../assets/`) and never move a
linked file without relinking. Structure shared assets so each is a separate .blend with one
top-level collection named after the asset.

## Structure checklist

1. Every object named; mesh data names match.
2. Collections reflect logical groups and export sets.
3. Repeated parts are linked duplicates or collection instances, not copies.
4. Helper geometry prefixed and in its own collection.
5. Origins placed meaningfully for each object.
6. Hierarchies intentional; constraints used where they beat parenting.
