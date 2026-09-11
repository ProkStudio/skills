---
name: blender
description: >-
  Generate, edit, and render 3D and 2D scenes in Blender by writing Python (bpy)
  scripts that run headless. Use this skill WHENEVER the task involves Blender or
  a .blend file, or asks to create/model/join 3D objects, 2D shapes, curves, or
  text; build or assign materials and textures; UV unwrap; set up lighting or an
  HDRI environment; rig, keyframe, or animate; or render stills and animations —
  even if the user does not say the word "Blender" but clearly wants a 3D model,
  a rendered image, a procedural scene, or a 3D asset exported as glTF/FBX/OBJ/STL.
  Trigger this to get clean, watertight, correctly-joined geometry with proper
  normals, PBR materials, good lighting, and working animation instead of fragile
  bpy.ops-based code that breaks headless.
---

# Blender scripting (bpy)

Blender is driven from Python through the `bpy` module. The reliable way to produce
3D/2D assets, materials, lighting, and animation from a prompt is to **write a
`.py` script and run Blender headless**, then **render a preview to verify the
result before declaring success**. This skill encodes the non-obvious rules that
separate scripts that actually work from ones that silently produce garbage
(duplicate vertices, flipped normals, black renders, context errors).

## The one rule that matters most: prefer data-API over operators

`bpy.ops.*` operators (e.g. `bpy.ops.mesh.primitive_cube_add`) depend on **context**
— the active object, the current mode, the area under the mouse. Headless, that
context is often wrong or missing, so operators throw `RuntimeError: context is
incorrect` or quietly act on the wrong object. **Default to the low-level data API
and `bmesh` instead.** Operators are a last resort, and when you must use one,
wrap it in a context override.

```python
# FRAGILE — depends on context, may fail or hit the wrong object headless:
bpy.ops.mesh.primitive_cube_add(size=2)

# ROBUST — explicit data creation, no context needed:
import bpy
mesh = bpy.data.meshes.new("Cube")
obj  = bpy.data.objects.new("Cube", mesh)
bpy.context.collection.objects.link(obj)
# ...then fill `mesh` with bmesh (see references/geometry.md)
```

When an operator is genuinely the best tool (booleans applied via modifier are
usually better, but e.g. some unwraps), override context explicitly:

```python
# Blender 4.x / 5.x context override:
with bpy.context.temp_override(active_object=obj, selected_objects=[obj],
                               object=obj):
    bpy.ops.object.shade_smooth()
```

## Standard workflow

1. **Detect the version first.** APIs shift between major versions (4.0 renamed
   Principled BSDF sockets; 4.3 replaced Grease Pencil; 5.0 changed defaults).
   Start every script with a version check and branch where it matters. If unsure
   what a socket/attribute is called in the running version, read
   `references/gotchas.md`, and when still unsure, print the available names at
   runtime (see below) instead of guessing.

   ```python
   import bpy
   print("Blender", bpy.app.version_string)   # e.g. (5, 2, 0)
   ```

2. **Start from a clean, deterministic scene.** Blender's default file ships a
   cube, a camera, and a light that will pollute your scene. Use the boilerplate
   in `scripts/boilerplate.py` (it wipes orphan data too) and always run Blender
   with `--factory-startup` so user preferences/add-ons can't change behaviour.

3. **Build geometry** with `bmesh` for meshes, `bpy.data.curves` for 2D/curves.
   Follow `references/geometry.md`. Crucially: **join correctly** — merge
   coincident vertices, recalculate normals outward, and decide deliberately
   between *join* (one object), *boolean* (fused watertight solid), and *parent*
   (grouped but separate). Wrong choice here is the #1 cause of "it looks broken".

4. **Materials & UVs** per `references/materials.md`: node-based Principled BSDF,
   proper UV unwrap before image textures, correct color space (sRGB for base
   color, Non-Color for roughness/normal/metallic maps).

5. **Lighting & world** per `references/lighting.md`: a three-point rig or an HDRI,
   physically-scaled light power, and the right view transform (AgX/Filmic) so
   renders aren't blown out or flat.

6. **Animation** per `references/animation.md`: keyframes via `keyframe_insert`,
   F-curve interpolation, drivers, constraints, and armatures — set the scene
   frame range explicitly.

7. **Render to verify** per `references/rendering.md`, then **look at the output.**
   A script that runs without error can still produce a black frame (no light),
   an empty frame (camera pointing away, object not linked), or a pink frame
   (missing texture). Rendering a low-sample preview and inspecting it is part of
   the job, not optional polish.

## How to run

```bash
# Headless, reproducible, render a still:
blender --background --factory-startup --python scene.py

# Pass args to the script after `--` (everything after -- is sys.argv):
blender -b -P scene.py -- --out /tmp/render.png --frames 1
```

Inside the script, read args after `--`:

```python
import sys
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
```

If Blender isn't installed in the environment, say so and offer to (a) write the
script for the user to run locally, or (b) install Blender if the sandbox allows
it (`apt-get`/download of the portable build). Never fabricate a render you
didn't produce.

## Verifying without a GUI

- Render one frame at low samples to a PNG and **open/inspect the image**.
- Print a scene report: object count, each object's vertex count, bounding box,
  material names, light count, camera location. A silent script that reports
  "0 lights" explains a black render before you even open the image.
- For meshes destined for export or 3D print, assert **manifold + consistent
  normals** (see `references/geometry.md`).
- Check the console for `RuntimeError`/`ReferenceError` — a freed datablock
  (`ReferenceError: StructRNA ... has been removed`) means you kept a Python
  reference across an operator that reallocated it; re-fetch from `bpy.data`.

## Common failure modes (symptom → cause)

| Symptom | Likely cause |
|---|---|
| Black render | No light, or light power far too low, or world set to pure black |
| Empty/transparent render | Object not linked to a collection, or camera aimed away, or object behind camera |
| Pink / magenta surfaces | Image texture path missing or not packed |
| Faceted where it should be smooth | Forgot `shade_smooth` / normals not recalculated |
| Object looks "inside out" | Normals flipped inward — recalc outside |
| Seams/cracks after joining | Coincident vertices not merged (remove doubles) |
| Boolean gives holes/artefacts | Non-manifold input, or overlapping coplanar faces |
| `context is incorrect` | Used an operator headless without a context override |
| `StructRNA has been removed` | Held a stale reference after data was reallocated |
| Washed-out/overexposed render | Wrong view transform or exposure; light power too high |

## Reference files

Read the one(s) relevant to the task — don't load all of them by default:

- `references/geometry.md` — creating meshes with bmesh; **joining objects
  correctly** (join vs boolean vs parent), merging vertices, recalculating
  normals, manifold checks, modifiers, procedural generation, instancing.
- `references/materials.md` — node materials, Principled BSDF, PBR texture maps,
  color spaces, UV unwrapping, procedural textures, applying different materials
  to different faces.
- `references/lighting.md` — light types & power units, three-point lighting,
  HDRI world lighting, view transform / color management, emissive materials.
- `references/animation.md` — keyframes, F-curve interpolation & easing, drivers,
  constraints, armatures/rigging, shape keys, following a path, frame range.
- `references/rendering.md` — Cycles vs Eevee, samples/denoise, resolution,
  output formats, rendering stills vs animation, cameras, exporting glTF/FBX/etc.
- `references/objects_2d.md` — 2D work: bezier/NURBS curves, filled shapes, text
  objects, the Grease Pencil (v3), logos/SVG, and 2D-in-3D compositions.
- `references/gotchas.md` — version-specific API differences (4.0/4.3/5.0), how to
  discover correct socket/attribute names at runtime, and other footguns.

- `scripts/boilerplate.py` — copy this as the top of a new script: clean scene,
  purge orphans, helper to add a camera that frames the scene, and a robust
  render function. Start here for almost every task.
