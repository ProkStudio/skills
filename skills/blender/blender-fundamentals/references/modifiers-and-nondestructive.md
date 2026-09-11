# Modifiers and the non-destructive mindset

## The stack

Modifiers evaluate top to bottom. Order changes the result, and most "the modifier looks wrong"
reports are order problems.

A reliable default order:

```
1. Mirror            (build symmetry first)
2. Array / Screw     (generate repetition)
3. Boolean           (cut shapes)
4. Bevel             (round the edges that now exist)
5. Solidify          (give thickness)
6. Subdivision       (smooth - always after bevel)
7. Weighted Normal   (fix shading on hard-surface)
8. Armature / Lattice / Simple Deform  (deform last)
9. Triangulate       (export only, last of all)
```

Rules of thumb:

- **Generate before deform.** A bend applied before an array bends each copy differently than
  expected.
- **Bevel before subdivision**, never the reverse.
- **Triangulate last**, and ideally only in the export settings rather than the stack.
- Mirror before anything that would be duplicated asymmetrically.

## Modifiers worth keeping live as long as possible

| Modifier | Why keep it live |
| --- | --- |
| Mirror | Symmetry stays editable; clipping keeps the seam welded |
| Array | Count and offset remain parameters |
| Bevel | Width and segments are the main tuning dial of hard-surface work |
| Subdivision | Viewport/render levels let you work light and render heavy |
| Boolean | Cutters stay editable and re-positionable |
| Solidify | Thickness is a decision you will revisit |
| Weighted Normal | Pure shading fix, no geometry cost |
| Geometry Nodes | Fully procedural; see `../../blender-geometry-nodes/SKILL.md` |

## Key settings that solve common problems

- **Mirror**: enable Clipping to stop vertices crossing the seam; set Bisect/Flip when mirroring an
  already-full mesh.
- **Bevel**: Limit Method Angle for a global pass, Weight for per-edge control (edge bevel weight),
  Miter options to clean up intersections, Harden Normals with Auto Smooth for hard-surface shading.
- **Subdivision**: viewport level 1-2, render level 2-3. Use Optimal Display to see the cage.
- **Boolean**: use Exact solver for reliability; keep cutters in a hidden collection; both meshes
  should be manifold or artifacts appear.
- **Solidify**: Complex mode handles self-intersection better; Even Thickness helps on curved shapes.
- **Weighted Normal**: needs Keep Sharp and a mesh with face areas that make sense; it removes most
  bevel shading artifacts on hard-surface models.
- **Remesh** and **Decimate**: destructive in effect even as modifiers - they discard the original
  flow, so keep the source object.

## Shape keys, vertex groups and attributes

- **Shape keys** store alternative vertex positions non-destructively: blend shapes, corrective
  shapes, simple animation. They break if topology changes, so finish topology first.
- **Vertex groups** drive modifiers (bevel, solidify, mask, armature weights) and are the standard
  way to make a modifier affect only part of a mesh.
- **Attributes** (custom per-vertex/edge/face data) feed geometry nodes and shaders; prefer them to
  destructive geometry tricks.
- Modifier order matters for vertex groups too: a modifier that creates geometry may not carry the
  group to the new elements the way you expect.

## When applying is unavoidable

Apply when:

- Sculpting on the result (multires and dyntopo need real geometry).
- Retopologising or baking, where the high-poly must be final geometry.
- Exporting to a format or pipeline that cannot evaluate the stack (though most exporters can apply
  modifiers on export - prefer that).
- Performance in the viewport has collapsed and the shape is locked.

Before applying: save a new file version, or duplicate the object into a `wip/` collection with the
stack intact. "Ctrl+A then Ctrl+S then realise" is the classic mistake.

## Non-destructive alternatives to common destructive edits

| Instead of | Use |
| --- | --- |
| Deleting half and mirroring by hand | Mirror modifier |
| Duplicating a part 20 times | Array modifier or linked duplicates |
| Manually beveling every edge | Bevel modifier with edge weights |
| Sculpting a dent into final geometry | Displace with a texture, or geometry nodes |
| Rebuilding a mesh to change proportions | Lattice or Simple Deform |
| Hand-placing scatter objects | Geometry nodes distribution |
| Decimating to reduce polys | Proper retopology, or LOD generation at export |

## Stack review checklist

1. Order follows generate > cut > bevel > thickness > smooth > deform.
2. Nothing is applied that could still be a parameter.
3. Cutters and helpers are hidden but not deleted.
4. Viewport subdivision level is low enough to work comfortably.
5. Triangulation happens at export, not in the model.
6. A pre-apply version of the file exists.
