# Materials, textures, and UVs

Materials in Blender are **node graphs**. The workhorse is the Principled BSDF
(one node covering metal/dielectric/glass/emission). Get color spaces and UVs
right or textures render wrong even when the graph is correct.

## Contents
1. A basic node material
2. Principled BSDF inputs (and the 4.0 rename)
3. Image-texture PBR (base color, roughness, normal, metallic)
4. Color spaces — the silent killer
5. UV unwrapping
6. Multiple materials on one mesh (per-face)
7. Procedural textures & emission

---

## 1. Basic node material

```python
mat = bpy.data.materials.new("MyMat")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links
bsdf = nodes.get("Principled BSDF")     # created by default with use_nodes
bsdf.inputs["Base Color"].default_value = (0.8, 0.1, 0.1, 1.0)  # RGBA, linear
bsdf.inputs["Roughness"].default_value = 0.4
bsdf.inputs["Metallic"].default_value = 0.0
obj.data.materials.append(mat)          # assign to object
```

Colors set in code are **linear**, not sRGB. To match a hex/sRGB swatch, convert:

```python
def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
# hex #CC1919 -> (0.8,0.1,0.1) sRGB -> linear per channel
```

---

## 2. Principled BSDF inputs (mind the version)

Blender **4.0 renamed and restructured** several sockets. Access by name and, if a
name is missing, print the socket names rather than guessing:

```python
print([s.name for s in bsdf.inputs])    # discover exact names for THIS version
```
Notable changes to watch for (verify at runtime):
- `Specular` → `Specular IOR Level` (4.0+).
- Subsurface reworked: `Subsurface` weight + `Subsurface Radius`/`Subsurface Scale`.
- Emission split into `Emission Color` + `Emission Strength` (4.0+); older files
  used a single `Emission`.
- Transmission is a 0–1 weight; for glass also lower roughness and set IOR ~1.45.

Common looks:
- **Plastic**: metallic 0, roughness 0.3–0.5, some specular.
- **Metal**: metallic 1, roughness controls polish (0.1 shiny → 0.6 brushed).
- **Glass**: transmission 1, roughness 0, IOR 1.45, use Cycles for realism.
- **Emissive**: set Emission Color + Emission Strength > 1 (see lighting.md).

---

## 3. Image-texture PBR

Wire texture nodes into the BSDF. Set **interpolation** and, critically, the
**color space** per map (section 4).

```python
def image_node(mat, filepath, non_color=False):
    tex = mat.node_tree.nodes.new("ShaderNodeTexImage")
    img = bpy.data.images.load(filepath, check_existing=True)
    tex.image = img
    if non_color:
        img.colorspace_settings.name = "Non-Color"
    return tex

nt, links = mat.node_tree, mat.node_tree.links
base = image_node(mat, "/path/base_color.png")                 # sRGB
rough = image_node(mat, "/path/roughness.png", non_color=True) # Non-Color
norm  = image_node(mat, "/path/normal.png",    non_color=True) # Non-Color

links.new(base.outputs["Color"],  bsdf.inputs["Base Color"])
links.new(rough.outputs["Color"], bsdf.inputs["Roughness"])

# Normal map needs a Normal Map node between the texture and the BSDF:
nmap = nt.nodes.new("ShaderNodeNormalMap")
links.new(norm.outputs["Color"], nmap.inputs["Color"])
links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])
```
**Pack external images** so the .blend/render is portable:
`bpy.ops.file.pack_all()` (or `img.pack()` per image). A missing path renders pink.

---

## 4. Color spaces — the silent killer

- **Base color / albedo / emission color** → `sRGB` (the default).
- **Roughness, metallic, normal, displacement, AO, masks** → `Non-Color`.

If a roughness/normal map is left on sRGB, the surface looks subtly (or badly)
wrong with no error. This is the most common "my textures look off" bug.

---

## 5. UV unwrapping

Image textures need UVs. Primitives from `bmesh.ops.create_*` and `from_pydata`
often have none or poor ones. Unwrapping is one place an operator (with override)
is the practical tool:

```python
# Ensure the object is in Edit mode with all faces selected, via override:
with bpy.context.temp_override(active_object=obj, object=obj,
                               selected_objects=[obj]):
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.smart_project(angle_limit=1.15, island_margin=0.02)  # good default
    # or bpy.ops.uv.unwrap(method="ANGLE_BASED") if seams are marked
    bpy.ops.object.mode_set(mode="OBJECT")
```
For boxes/planes, `bpy.ops.uv.cube_project` or a simple generated UV is enough.
For tiling/repeat, add a Mapping + Texture Coordinate node and scale the UVs.

---

## 6. Multiple materials on one mesh (per-face)

Append several materials; each polygon has a `material_index` into the object's
material slots.

```python
obj.data.materials.append(mat_red)     # slot 0
obj.data.materials.append(mat_blue)    # slot 1
for poly in obj.data.polygons:
    poly.material_index = 1 if poly.center.z > 0 else 0
obj.data.update()
```

---

## 7. Procedural textures & emission

Procedural (no image files) via nodes: `ShaderNodeTexNoise`, `TexVoronoi`,
`TexWave`, `TexGradient`, combined with `ShaderNodeMapRange`, `ColorRamp`
(`ShaderNodeValToRGB`), and `ShaderNodeBump` for surface relief. Example bump from
noise:

```python
noise = nt.nodes.new("ShaderNodeTexNoise")
bump  = nt.nodes.new("ShaderNodeBump")
links.new(noise.outputs["Fac"], bump.inputs["Height"])
links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
```
For glowing surfaces set `Emission Color` + `Emission Strength` on the Principled
BSDF (a full node is unnecessary in 4.0+). Emissive materials also **light the
scene** in Cycles and Eevee-Next — handy for screens, neon, lava.
