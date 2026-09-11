# Version differences and footguns

Blender's Python API changes across major versions. Current releases as of mid-2026
are **5.2 LTS** and **4.5 LTS**; 5.0 (Nov 2025) and 4.0 (Nov 2023) were the big
breaking points. Rather than memorising every change, **detect the version and
discover names at runtime.**

## Discover the API at runtime — do this instead of guessing

```python
import bpy
print("version:", bpy.app.version, bpy.app.version_string)

# Socket names on a node (e.g. Principled BSDF) vary by version:
mat = bpy.data.materials.new("t"); mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
print([s.name for s in bsdf.inputs])

# Available render engines:
print([e.bl_idname for e in
       bpy.types.RenderEngine.__subclasses__()])   # or try/except setting engine

# Any datablock collection or operator:
print([x for x in dir(bpy.data) if not x.startswith("_")])
print([x for x in dir(bpy.ops.mesh) if not x.startswith("_")])
```
When a script must be portable, wrap version-sensitive calls in `try/except` or
branch on `bpy.app.version`.

## Known breaking changes to guard against

**Principled BSDF sockets (4.0+)**
- `Specular` → `Specular IOR Level`.
- Emission is `Emission Color` + `Emission Strength` (single `Emission` in ≤3.6).
- Subsurface reworked (weight + radius/scale). Access by name; print if unsure.

**Auto-smooth removed (4.1+)**
- `mesh.use_auto_smooth` and `auto_smooth_angle` were removed. Use the **"Smooth
  by Angle"** modifier or the shade-smooth-by-angle operator instead:
  ```python
  with bpy.context.temp_override(active_object=obj, object=obj,
                                 selected_objects=[obj]):
      try:
          bpy.ops.object.shade_auto_smooth(angle=0.523599)   # 30° (4.1+)
      except AttributeError:
          for p in obj.data.polygons: p.use_smooth = True
  ```

**Eevee renamed (4.2+)**
- Engine id `BLENDER_EEVEE` → `BLENDER_EEVEE_NEXT`. Try both (rendering.md §1).

**Grease Pencil rewritten (4.3+)**
- "Grease Pencil v3": new datablock type and API. Old `bpy.data.grease_pencil`
  / GPencil code won't match. Discover the collection name at runtime.

**Color management (4.0+)**
- Default view transform is **AgX** (was Filmic). Renders look different; set
  explicitly (`Standard` for flat graphics, `AgX` for photoreal).

**Blender 5.0 (Nov 2025)**
- Bumped bundled **Python version** and dropped some long-deprecated APIs; some
  operator/enum defaults changed. If a 4.x snippet errors on 5.x, print the
  current names/enums at runtime and adjust. Nodes and defaults are the usual
  culprits — verify node input/output names.

## Context & reference footguns (all versions)

- **`context is incorrect`** — an operator ran headless without the needed
  context. Use `bpy.context.temp_override(...)` or, better, the data API.
- **`StructRNA of type ... has been removed`** — you held a Python reference to a
  datablock that got reallocated (often after an operator or `to_mesh`). Re-fetch
  from `bpy.data` by name; don't cache across operators.
- **`frame_current = n` doesn't update evaluated geometry** — use
  `scene.frame_set(n)` so the dependency graph re-evaluates before you read verts.
- **Reading evaluated (modified) geometry** — the base mesh ignores modifiers. To
  read the final result:
  ```python
  dg = bpy.context.evaluated_depsgraph_get()
  eval_obj = obj.evaluated_get(dg)
  eval_mesh = eval_obj.to_mesh()      # remember eval_obj.to_mesh_clear() after
  ```
- **Units/scale** — light watts and physical materials assume roughly meter-scale
  objects. A 0.01-unit model under a 5 W lamp renders black; a 1000-unit model
  needs huge light power. Model near real-world scale.
- **Selection/active object** — many operators act on `context.active_object` /
  selection. Headless these are often `None`; always pass them in the override.
- **Saving the file** — to keep a `.blend`: `bpy.ops.wm.save_as_mainfile(
  filepath="/tmp/scene.blend")`. Pack textures first (`bpy.ops.file.pack_all()`)
  for portability.

## Sanity checklist before declaring success

- [ ] Version detected; version-sensitive calls guarded.
- [ ] Scene cleaned of the default cube/camera/light.
- [ ] Every object linked to a collection.
- [ ] Coincident verts merged; normals recalculated outward.
- [ ] Materials use correct color spaces; textures packed (no pink).
- [ ] At least one light OR world lighting; power scaled to model size.
- [ ] Active camera set and aimed at the subject.
- [ ] View transform chosen deliberately (AgX vs Standard).
- [ ] Frame range set (for animation).
- [ ] Rendered a preview and **looked at it**; scene report printed.
