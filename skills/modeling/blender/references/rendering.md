# Rendering and export

## Contents
1. Choosing an engine (Cycles vs Eevee)
2. Samples, denoising, resolution
3. Cameras
4. Output formats (stills & animation)
5. Transparent background & compositing basics
6. Exporting to glTF / FBX / OBJ / STL / USD

---

## 1. Engine: Cycles vs Eevee

- **Cycles** — physically-based path tracer. Best for realism: true reflections,
  refraction/glass, soft shadows, caustics, accurate GI. Slower. Set
  `scene.render.engine = "CYCLES"`. Use GPU if available:
  ```python
  scene.cycles.device = "GPU"
  prefs = bpy.context.preferences.addons["cycles"].preferences
  prefs.compute_device_type = "OPTIX"   # or "CUDA", "HIP", "METAL", "ONEAPI"
  prefs.get_devices()
  for d in prefs.devices: d.use = True
  ```
- **Eevee** — real-time rasteriser. Fast, great for stylised looks, previews, and
  animation on a budget. The engine id changed: **4.2+ is `BLENDER_EEVEE_NEXT`**;
  older is `BLENDER_EEVEE`. Set with a fallback:
  ```python
  for eng in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
      try: scene.render.engine = eng; break
      except TypeError: continue
  ```
  Eevee approximates glass/GI; for hero glass/caustics use Cycles.

Rule of thumb: **Cycles** when the user says photoreal/product/realistic;
**Eevee** for speed, previews, motion graphics, toon/flat styles.

---

## 2. Samples, denoising, resolution

```python
# Cycles
scene.cycles.samples = 128          # 32-64 preview, 128-512 final
scene.cycles.use_denoising = True   # OptiX/OpenImageDenoise cleans low samples
scene.cycles.use_adaptive_sampling = True

# Eevee-Next
scene.eevee.taa_render_samples = 64

# Resolution (both)
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
```
Denoising lets you use far fewer samples — always enable it for quick, clean
results.

---

## 3. Cameras

```python
cam_data = bpy.data.cameras.new("Camera")
cam_data.lens = 50               # mm; 35 wide, 50 natural, 85 portrait/compressed
cam = bpy.data.objects.new("Camera", cam_data)
bpy.context.collection.objects.link(cam)
cam.location = (7, -7, 5)
scene.camera = cam               # MUST set the active camera or render is empty
```
Aim it reliably with a `TRACK_TO` constraint at an empty (see boilerplate). Depth
of field: `cam_data.dof.use_dof = True`, set `focus_object` and `aperture_fstop`
(lower = shallower). Orthographic: `cam_data.type = "ORTHO"`,
`cam_data.ortho_scale`.

---

## 4. Output formats

Still:
```python
scene.render.image_settings.file_format = "PNG"   # or "OPEN_EXR" (HDR), "JPEG"
scene.render.image_settings.color_depth = "16"    # PNG/EXR
scene.render.filepath = "/tmp/render.png"
bpy.ops.render.render(write_still=True)
```
Animation → prefer a PNG sequence (resumable), or FFMPEG for a video file. See
animation.md §8.

---

## 5. Transparent background & compositing

```python
scene.render.film_transparent = True        # alpha where no object
scene.render.image_settings.color_mode = "RGBA"
```
For post effects (glow, color grade) enable the compositor:
`scene.use_nodes = True` and build in `scene.node_tree` (Render Layers → effects →
Composite). A Bloom/Glare node adds glow to bright emissive areas.

---

## 6. Exporting

Blender ships exporters; call them with a filepath. Prefer **glTF** for
web/real-time/interchange (materials + animation survive well), **STL** for 3D
printing (geometry only — run the manifold check in geometry.md first), **FBX**
for game engines, **OBJ** for simple static geometry, **USD** for pipelines.

```python
# glTF (recommended default for a 3D asset):
bpy.ops.export_scene.gltf(filepath="/tmp/asset.glb", export_format="GLB")

# STL for printing (4.x may use the newer io_scene name; try both):
try:
    bpy.ops.wm.stl_export(filepath="/tmp/asset.stl")      # 4.x+ core exporter
except AttributeError:
    bpy.ops.export_mesh.stl(filepath="/tmp/asset.stl")    # legacy add-on op

# FBX / OBJ:
bpy.ops.export_scene.fbx(filepath="/tmp/asset.fbx")
bpy.ops.wm.obj_export(filepath="/tmp/asset.obj")          # 4.x core; legacy: export_scene.obj
```
Before export: apply transforms (`object.transform_apply`) so scale/rotation bake
in, apply modifiers if the target format won't carry them, and pack or copy
textures. For glTF with animation, ensure actions exist and the frame range is set.
