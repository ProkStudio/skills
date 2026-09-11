# 2D objects: curves, text, Grease Pencil

"2D" in Blender means a few different things — pick the right primitive:
- **Curves** (bezier/NURBS) — outlines, paths, logos; can be filled or given depth.
- **Text objects** — real editable text, convertible to mesh/curve.
- **Grease Pencil** — hand-drawn 2D strokes in 3D space; 2D animation.
- **Planes with an image/alpha** — the simplest "2D sprite" in a 3D scene.

## Contents
1. Bezier / NURBS curves
2. Filled shapes & giving curves depth
3. Text objects
4. Grease Pencil (v3)
5. Image planes / sprites
6. SVG / logo import

---

## 1. Bezier & NURBS curves

Build curves from control points via the data API (no operators):

```python
import bpy
curve = bpy.data.curves.new("Path", type="CURVE")
curve.dimensions = "3D"                 # or "2D" for a flat, fillable shape
spline = curve.splines.new("BEZIER")    # or "NURBS", "POLY"
spline.bezier_points.add(2)             # starts with 1; add 2 -> 3 total
coords = [(0,0,0), (1,2,0), (3,0,0)]
for bp, co in zip(spline.bezier_points, coords):
    bp.co = co
    bp.handle_left_type = bp.handle_right_type = "AUTO"
obj = bpy.data.objects.new("Path", curve)
bpy.context.collection.objects.link(obj)
```
`POLY` splines are simplest (straight segments); `BEZIER` gives smooth handles;
`NURBS` gives smooth without per-point handles. Close a loop with
`spline.use_cyclic_u = True`.

---

## 2. Filled shapes & giving curves depth

A **2D** curve (`curve.dimensions = "2D"`) with a closed spline renders as a
**filled flat shape** — ideal for logos and flat graphics. Give any curve
thickness/volume without converting to mesh:

```python
curve.bevel_depth = 0.05        # round tube thickness along the curve
curve.bevel_resolution = 4
curve.extrude = 0.1             # flat extrusion (gives a 2D shape depth in Z)
curve.fill_mode = "BOTH"        # cap the ends
# Or use a second curve as a custom bevel profile: curve.bevel_object = profile_obj
```
Convert to mesh when you need mesh editing/booleans:
```python
with bpy.context.temp_override(active_object=obj, object=obj,
                               selected_objects=[obj]):
    bpy.ops.object.convert(target="MESH")
```

---

## 3. Text objects

```python
txt = bpy.data.curves.new("Text", type="FONT")
txt.body = "Hello"
txt.align_x = "CENTER"
txt.align_y = "CENTER"
txt.extrude = 0.1               # 3D depth (0 = flat)
txt.bevel_depth = 0.01          # rounded edges
# txt.font = bpy.data.fonts.load("/path/font.ttf")   # custom font
obj = bpy.data.objects.new("Text", txt)
bpy.context.collection.objects.link(obj)
```
Text is a curve under the hood — convert to mesh/curve as in §2 for booleans or
per-letter effects.

---

## 4. Grease Pencil (v3)

Grease Pencil was **rewritten in Blender 4.3** ("Grease Pencil v3"); the data API
and type id changed from earlier versions. **Verify the API at runtime** for the
running version (print `dir(bpy.data)` for the grease-pencil collection name and
check `bpy.app.version`). Use Grease Pencil for 2D/traditional animation, hand
drawn looks, and annotations in 3D. If the goal is just flat vector graphics,
filled 2D curves (§2) are usually simpler and version-stable.

Because the v3 API differs by version, the robust approach in a script is:
1. Print the available grease-pencil datablock names/types for this version.
2. Create the object and a layer/frame, then add strokes with point coordinates.
If a task leans heavily on Grease Pencil, fetch the Python API docs for the exact
running version rather than relying on any single code snippet.

---

## 5. Image planes / sprites

The lightest way to put a 2D image into a 3D scene: a plane with an image texture
and alpha.

```python
# a 1x1 plane via bmesh, then an emission/alpha material:
import bmesh
me = bpy.data.meshes.new("Plane"); bm = bmesh.new()
bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=1.0)
bm.to_mesh(me); bm.free()
plane = bpy.data.objects.new("Sprite", me)
bpy.context.collection.objects.link(plane)

mat = bpy.data.materials.new("Sprite"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage")
tex.image = bpy.data.images.load("/path/sprite.png")
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
nt.links.new(tex.outputs["Alpha"], bsdf.inputs["Alpha"])
mat.blend_method = "BLEND"          # respect alpha (name may vary by version)
plane.data.materials.append(mat)
```
For a flat, unshaded look (stickers/UI), drive Emission Color from the texture and
set the view transform to Standard (lighting.md §4).

---

## 6. SVG / logo import

Blender imports SVG as filled 2D curves (great for logos):

```python
bpy.ops.import_curve.svg(filepath="/path/logo.svg")   # add-on op; enable if needed
# Imported curves land in a new collection; they're tiny (SVG units) —
# select and scale up, then extrude/bevel (§2) for a 3D logo.
```
If the importer isn't enabled, enable the add-on or rebuild the shapes as curves
from the path data.
