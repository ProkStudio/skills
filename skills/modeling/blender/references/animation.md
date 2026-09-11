# Animation

Animation in Blender = keyframes on properties, stored as F-curves, plus higher
level tools (drivers, constraints, armatures, shape keys, paths). Always **set the
frame range explicitly** — the default 1–250 will silently truncate or pad.

## Contents
1. Keyframes and the frame range
2. F-curve interpolation & easing
3. Drivers (property linked to another)
4. Constraints (follow, track, copy)
5. Armatures / rigging basics
6. Shape keys (morphs)
7. Follow path / along a curve
8. Rendering an animation

---

## 1. Keyframes and frame range

```python
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 120           # 5 s at 24 fps
scene.render.fps = 24

obj = bpy.data.objects["Cube"]

# Keyframe location at two frames:
obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=1)
obj.location = (0, 0, 3)
obj.keyframe_insert(data_path="location", frame=48)
```
Keyframe-able `data_path`s include `"location"`, `"rotation_euler"`, `"scale"`,
`'["custom_prop"]'`, material/node values (via the datablock's `keyframe_insert`),
and shape-key `value`. Insert a single channel with `index=` (0=x,1=y,2=z).

Set the current frame before reading evaluated state:
`scene.frame_set(f)` (updates the dependency graph; plain `frame_current = f`
does not fully evaluate).

---

## 2. F-curve interpolation & easing

Newly inserted keys default to Bezier (smooth). Control the feel by editing
F-curves after inserting:

```python
action = obj.animation_data.action
for fc in action.fcurves:
    for kp in fc.keyframe_points:
        kp.interpolation = "BEZIER"     # CONSTANT (steps), LINEAR, BEZIER
        kp.easing = "AUTO"              # EASE_IN, EASE_OUT, EASE_IN_OUT
        # For springy motion: kp.interpolation = "BACK" or "ELASTIC" or "BOUNCE"
    fc.update()
```
- **LINEAR** — mechanical, constant speed.
- **BEZIER + ease in/out** — natural start/stop; the default good choice.
- **CONSTANT** — stop-motion / hold poses.
- **BOUNCE / ELASTIC / BACK** — stylised overshoot.
Add cycles (loops) with an F-Curve modifier: `fc.modifiers.new("CYCLES")`.

---

## 3. Drivers

Link one property to another with an expression (procedural animation without
keys): e.g. a wheel's rotation driven by forward position.

```python
fcurve = wheel.driver_add("rotation_euler", 0)   # X rotation
drv = fcurve.driver
drv.type = "SCRIPTED"
var = drv.variables.new()
var.name = "x"
var.type = "TRANSFORMS"
tgt = var.targets[0]
tgt.id = car
tgt.transform_type = "LOC_Y"
tgt.transform_space = "WORLD_SPACE"
drv.expression = "-x / 0.35"     # radius 0.35 m -> radians rolled
```

---

## 4. Constraints

Constraints animate relationships without baking transforms:
- `TRACK_TO` / `DAMPED_TRACK` — always face a target (cameras, eyes, lights).
- `FOLLOW_PATH` — move an object along a curve (section 7).
- `COPY_LOCATION` / `COPY_ROTATION` / `COPY_TRANSFORMS` — mirror another object.
- `CHILD_OF` — parent-like, animatable influence (mechanical linkages, pick-up).
- `LIMIT_*` — clamp motion.

```python
con = cam.constraints.new("TRACK_TO")
con.target = subject
con.track_axis = "TRACK_NEGATIVE_Z"
con.up_axis = "UP_Y"
```

---

## 5. Armatures / rigging basics

For characters or anything that deforms. Build the armature, then keyframe pose
bones. Bone editing needs Edit mode (use a context override).

```python
arm_data = bpy.data.armatures.new("Arm")
arm = bpy.data.objects.new("Arm", arm_data)
bpy.context.collection.objects.link(arm)

with bpy.context.temp_override(active_object=arm, object=arm,
                               selected_objects=[arm]):
    bpy.ops.object.mode_set(mode="EDIT")
    eb = arm_data.edit_bones.new("Bone")
    eb.head = (0, 0, 0)
    eb.tail = (0, 0, 1)
    child = arm_data.edit_bones.new("Bone.001")
    child.head = (0, 0, 1); child.tail = (0, 0, 2)
    child.parent = eb; child.use_connect = True
    bpy.ops.object.mode_set(mode="OBJECT")

# Bind a mesh with automatic weights:
with bpy.context.temp_override(active_object=arm, object=arm,
                               selected_objects=[mesh_obj, arm]):
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")

# Animate a pose bone:
scene.frame_set(1)
pbone = arm.pose.bones["Bone"]
pbone.rotation_mode = "XYZ"
pbone.rotation_euler = (0, 0, 0)
pbone.keyframe_insert("rotation_euler", frame=1)
pbone.rotation_euler = (0.5, 0, 0)
pbone.keyframe_insert("rotation_euler", frame=30)
```
Add an IK constraint on a pose bone for limbs (`pbone.constraints.new("IK")`).

---

## 6. Shape keys (morphs)

Blend between mesh shapes (facial expressions, morph targets):

```python
obj.shape_key_add(name="Basis")
key = obj.shape_key_add(name="Smile")
# move key.data[i].co for the deformed shape, then animate key.value 0->1
key.value = 0.0; key.keyframe_insert('value', frame=1)
key.value = 1.0; key.keyframe_insert('value', frame=20)
```

---

## 7. Follow path / along a curve

```python
con = obj.constraints.new("FOLLOW_PATH")
con.target = curve_obj
con.use_curve_follow = True         # orient along the path
# Animate the curve's evaluation time, or set path_duration + use_path:
curve_obj.data.use_path = True
curve_obj.data.path_duration = 120
curve_obj.data.eval_time = 0;   curve_obj.data.keyframe_insert('eval_time', frame=1)
curve_obj.data.eval_time = 120; curve_obj.data.keyframe_insert('eval_time', frame=120)
```

---

## 8. Rendering an animation

Set an output **directory + file pattern** and use `animation=True`. Prefer
rendering an image sequence (resumable, crash-safe) over a single video file, then
optionally encode.

```python
scene.render.filepath = "/tmp/frames/frame_"   # -> frame_0001.png ...
scene.render.image_settings.file_format = "PNG"
bpy.ops.render.render(animation=True)
# For direct video: file_format = "FFMPEG"; scene.render.ffmpeg.format="MPEG4";
# scene.render.ffmpeg.codec="H264".
```
See rendering.md for engine/samples. Keep samples modest for animation to control
render time; enable denoising.
