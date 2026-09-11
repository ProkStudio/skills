# Geometry: creating and correctly joining objects

This is the file that makes assets look *right* instead of broken. The three most
common defects — visible seams, flipped/inside-out surfaces, and failed booleans —
all come from skipping the steps below.

## Contents
1. Creating meshes with bmesh
2. Joining objects: the three correct methods (join / boolean / parent)
3. Merging coincident vertices (the "remove doubles" step)
4. Normals: recalculate outward, smooth vs flat shading
5. Manifold / watertight checks
6. Modifiers (apply order matters)
7. Procedural generation & instancing

---

## 1. Creating meshes with bmesh

`bmesh` is the robust, context-free way to build and edit geometry. Build in a
bmesh, write to a mesh datablock, then link an object.

```python
import bpy, bmesh

bm = bmesh.new()
bmesh.ops.create_cube(bm, size=2.0)            # or create_uvsphere, create_cone...
mesh = bpy.data.meshes.new("MyMesh")
bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new("MyObj", mesh)
bpy.context.collection.objects.link(obj)
```

Build arbitrary geometry from raw verts/faces without operators:

```python
verts = [(0,0,0), (1,0,0), (1,1,0), (0,1,0)]
faces = [(0,1,2,3)]
mesh = bpy.data.meshes.new("Quad")
mesh.from_pydata(verts, [], faces)
mesh.update()
mesh.validate()          # ALWAYS validate hand-built meshes; catches bad indices
```

Useful `bmesh.ops`: `create_cube`, `create_uvsphere`, `create_icosphere`,
`create_cone`, `create_grid`, `extrude_face_region`, `inset_region`, `bevel`,
`subdivide_edges`, `spin` (lathe), `bridge_loops`, `solidify`.

---

## 2. Joining objects — pick the RIGHT method

"Join these two objects" has three completely different correct answers. Choosing
wrong is the number-one reason a result "looks connected but is broken."

### (a) `join` — merge into ONE object, geometry kept as-is
Use when parts belong to a single object but you do **not** need the surfaces
fused (e.g. a body + separate buttons). Geometry is combined into one mesh but
overlapping/touching vertices are **not** welded — so if the parts touch and you
want a seamless surface, you must also merge by distance (section 3).

```python
# Data-API join is finicky; the operator with an override is reliable here:
target = bpy.data.objects["A"]
sources = [bpy.data.objects["B"], bpy.data.objects["C"]]
with bpy.context.temp_override(active_object=target,
                               selected_editable_objects=[target, *sources],
                               object=target, selected_objects=[target, *sources]):
    bpy.ops.object.join()
# `target` now contains all geometry; sources are gone. Then merge_by_distance.
```

Pure-data alternative (no operator) — append geometry with bmesh:

```python
bm = bmesh.new()
for src in [target, *sources]:
    bm.from_mesh(src.data)            # note: ignores per-object transforms
bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
bm.to_mesh(target.data)
bm.free()
```
If sources have different transforms, bake each object's `matrix_world` into a
temp mesh copy before `from_mesh`, or transform the bmesh verts accordingly.

### (b) Boolean — fuse into a watertight SOLID (union / difference / intersect)
Use when you need a single continuous manifold surface: welding two shapes into
one solid, cutting a hole, keeping the overlap. This is what "properly connected"
usually means for a printable/renderable solid. Prefer the **modifier**, not the
operator:

```python
mod = objA.modifiers.new("Bool", type="BOOLEAN")
mod.operation = "UNION"          # or "DIFFERENCE", "INTERSECT"
mod.object = objB
mod.solver = "EXACT"             # EXACT handles coplanar/tricky cases; FLOAT is fast
# Apply it (bake the result into objA's mesh):
with bpy.context.temp_override(active_object=objA, object=objA,
                               selected_objects=[objA]):
    bpy.ops.object.modifier_apply(modifier=mod.name)
bpy.data.objects.remove(objB, do_unlink=True)   # hide/remove the cutter
```
Boolean requirements — booleans fail or leave holes when violated:
- Both inputs should be **manifold** (closed, no holes). See section 5.
- Normals must be **consistent** (all outward). See section 4.
- Avoid perfectly **coplanar overlapping faces** with the FLOAT solver; use EXACT,
  or nudge one object by an epsilon.
- After a union you'll usually still want `remove_doubles` + normal recalc.

### (c) Parent — group but keep SEPARATE objects
Use when parts move together but stay distinct objects (a car body + wheels that
spin, a lamp + its shade). No geometry is merged; transforms are hierarchical.

```python
child.parent = parent
child.matrix_parent_inverse = parent.matrix_world.inverted()  # keep world pos
```
For rigid mechanical links use an empty as the parent, or a constraint
(`CHILD_OF`, `COPY_TRANSFORMS`) — see animation.md.

### Decision guide
- Seamless single solid, will be 3D-printed or booleaned again → **boolean union**.
- One editable object, parts may or may not touch → **join** (+ merge if touching).
- Parts articulate or you want per-part materials/transforms → **parent**.

---

## 3. Merge coincident vertices ("remove doubles")

Whenever two pieces of geometry meet at the same location — after a join, a
mirror, an array wrap-around, or duplicated verts from `from_pydata` — weld them,
or you get invisible cracks, shading seams, and non-manifold edges.

```python
bm = bmesh.new()
bm.from_mesh(obj.data)
bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)   # tune dist to scale
bm.to_mesh(obj.data)
bm.free()
obj.data.update()
```
Pick `dist` relative to model scale: too large welds distinct detail, too small
misses near-coincident verts. `1e-4` suits meter-scale models.

---

## 4. Normals: outward, and smooth vs flat

Rendering, booleans, and 3D printing all assume face normals point **outward**.
Imported or hand-built meshes are often inconsistent.

```python
bm = bmesh.new()
bm.from_mesh(obj.data)
bm.normal_update()
bmesh.ops.recalc_face_normals(bm, faces=bm.faces)   # make consistent (outward)
bm.to_mesh(obj.data)
bm.free()
```
Flip all normals (if the recalc chose inward for a closed inverted mesh):
`bmesh.ops.reverse_faces(bm, faces=bm.faces)`.

Smooth vs flat shading is per-face and independent of normal *direction*:

```python
for poly in obj.data.polygons:
    poly.use_smooth = True          # smooth shading
# Optional: auto-smooth by angle. In 4.1+ this is a "Smooth by Angle" modifier /
# geometry-nodes op, NOT mesh.use_auto_smooth (removed). See gotchas.md.
```
For hard-surface models, smooth-shade then add a bevel/weighted-normals pass, or
mark sharp edges. For organic models, smooth-shade everything.

---

## 5. Manifold / watertight checks

A watertight mesh has every edge shared by exactly two faces, no stray verts, and
consistent normals. Check before boolean/export:

```python
bm = bmesh.new(); bm.from_mesh(obj.data)
non_manifold = [e for e in bm.edges if not e.is_manifold]
loose_verts  = [v for v in bm.verts if not v.link_edges]
print("non-manifold edges:", len(non_manifold), "loose verts:", len(loose_verts))
bm.free()
```
Fixes: `remove_doubles` (welds gaps), `bmesh.ops.holes_fill`,
`bmesh.ops.delete` loose geometry, `recalc_face_normals`.

---

## 6. Modifiers

Modifiers are non-destructive until applied; **order matters** (top-to-bottom).
Common ones and typical order: Mirror → Array → Solidify → Bevel → Subdivision →
Boolean → Triangulate (for export). Add via `obj.modifiers.new(name, type)`, set
properties, then apply with a context override (see boolean example). Apply order
= list order; reorder with `bpy.ops.object.modifier_move_to_index` under override
if needed. Subdivision surface for smooth organic; set `levels` (viewport) and
`render_levels` separately.

---

## 7. Procedural generation & instancing

- **Parametric loops**: build repeated geometry in a bmesh with math, or duplicate
  a base mesh and offset transforms. For thousands of copies, use **instancing**,
  not real copies, to stay memory-light:

```python
# Linked duplicates share mesh data (cheap):
inst = bpy.data.objects.new("Inst", base.data)   # SAME mesh datablock
inst.location = (x, y, z)
bpy.context.collection.objects.link(inst)
```
- **Collection instancing** and **Geometry Nodes** scale to huge counts; reach for
  Geometry Nodes when the user wants scatter/parametric/procedural systems (a
  node group added as a `NODES` modifier). Geometry Nodes changed across 4.x/5.x —
  verify node names at runtime.
- **Randomness**: seed Python's `random` for reproducibility.
