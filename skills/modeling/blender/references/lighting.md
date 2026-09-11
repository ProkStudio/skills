# Lighting and color management

Good lighting is the difference between a flat, amateur render and a convincing
one. Two things break renders here: **wrong light power** (black or blown-out) and
**wrong view transform** (washed-out or crushed). Both are quick to get right.

## Contents
1. Light types and power units
2. Three-point lighting rig
3. HDRI / world environment lighting
4. Color management (view transform, exposure)
5. Emissive materials as lights

---

## 1. Light types and power units

Create lights via the data API:

```python
light_data = bpy.data.lights.new("Key", type="AREA")  # POINT, SUN, SPOT, AREA
light_data.energy = 1000        # power — units depend on type!
light_data.color = (1.0, 0.95, 0.9)
lo = bpy.data.objects.new("Key", light_data)
bpy.context.collection.objects.link(lo)
lo.location = (4, -4, 6)
```

Power units — the usual cause of "too dark"/"too bright":
- **POINT / SPOT / AREA**: `energy` is in **watts**. Small scenes need hundreds to
  thousands of watts. A 10 W area light barely registers; try 300–2000 W.
- **SUN**: `energy` is **irradiance in W/m²**, and is scale-independent. Realistic
  midday sun ≈ 3–5. A sun `energy` of 1000 will nuke the frame.
- **AREA**: bigger `size` = softer shadows (and more total light for the same
  wattage spreads out). Set `size` (and `size_y` for rectangles).
- **SPOT**: `spot_size` (cone angle, radians) and `spot_blend` (edge softness).

Point the light with `rotation_euler`, or add a `TRACK_TO` constraint aimed at an
empty/target so it always faces the subject.

---

## 2. Three-point lighting rig

A dependable default for products/characters: a bright **key** at ~45°, a softer
**fill** opposite to lift shadows, and a **rim/back** light to separate the
subject from the background.

```python
import math
def add_light(name, ltype, energy, loc, target, size=3.0, color=(1,1,1)):
    d = bpy.data.lights.new(name, type=ltype)
    d.energy = energy
    d.color = color
    if ltype == "AREA":
        d.size = size
    o = bpy.data.objects.new(name, d)
    bpy.context.collection.objects.link(o)
    o.location = loc
    con = o.constraints.new("TRACK_TO")
    con.target = target
    con.track_axis = "TRACK_NEGATIVE_Z"
    con.up_axis = "UP_Y"
    return o

# target = an empty at the subject center
target = bpy.data.objects.new("LightTarget", None)
bpy.context.collection.objects.link(target)
target.location = (0, 0, 1)

add_light("Key",  "AREA", 1500, ( 4, -4, 5), target, size=4, color=(1,0.96,0.9))
add_light("Fill", "AREA",  400, (-5, -2, 3), target, size=6, color=(0.9,0.95,1))
add_light("Rim",  "AREA",  900, ( 0,  5, 4), target, size=2)
```
Warm key + cool fill reads naturally. Larger area lights = softer, more flattering
shadows.

---

## 3. HDRI / world environment lighting

An HDRI lights the whole scene realistically and gives reflections a believable
environment — often better than manual lights for products.

```python
world = bpy.context.scene.world or bpy.data.worlds.new("World")
bpy.context.scene.world = world
world.use_nodes = True
nt = world.node_tree
bg = nt.nodes["Background"]

env = nt.nodes.new("ShaderNodeTexEnvironment")
env.image = bpy.data.images.load("/path/studio.hdr")   # .hdr / .exr
nt.links.new(env.outputs["Color"], bg.inputs["Color"])
bg.inputs["Strength"].default_value = 1.0              # overall brightness
```
No HDRI file? A plain colored world still provides ambient light:
`bg.inputs["Color"].default_value = (0.05, 0.05, 0.06, 1)` and a small strength.
Pure black world + no lights = black render. To hide the HDRI from the *camera*
background while keeping its lighting, set `scene.render.film_transparent = True`
or use a Light Path node to mix a solid color for camera rays.

---

## 4. Color management (view transform)

The **view transform** maps rendered light to display. Getting it wrong makes even
well-lit scenes look bad.

```python
scene = bpy.context.scene
scene.view_settings.view_transform = "AgX"   # 4.0+ default; filmic, natural highlights
# "Filmic" (older), "Standard" (flat/no tone-mapping — good for flat 2D/graphics)
scene.view_settings.look = "AgX - Medium High Contrast"   # optional
scene.view_settings.exposure = 0.0          # +/- stops to brighten/darken
scene.view_settings.gamma = 1.0
```
Guidance:
- **AgX** (default in 4.0+) — best for photoreal scenes; rolls off highlights so
  bright lights don't clip to ugly white.
- **Standard** — no tone mapping; use for flat-color 2D art, UI mockups, logos,
  toon looks, or when you need exact colors.
- If a scene is uniformly too dark/bright, adjust light power first, then
  `exposure` as a global trim.

---

## 5. Emissive materials as lights

Any surface with emission contributes light in Cycles and Eevee-Next. Use for
screens, neon, glowing objects, or as soft "panel" lights.

```python
bsdf.inputs["Emission Color"].default_value = (0.2, 0.6, 1.0, 1.0)
bsdf.inputs["Emission Strength"].default_value = 20.0   # >1 to actually emit light
```
A large emissive plane makes an excellent soft key light and shows up in
reflections, which dedicated lamps do not.
