"""
Blender headless boilerplate. Copy the helpers you need to the top of a script.

Run with:
    blender --background --factory-startup --python scene.py -- --out /tmp/out.png

Design goals:
- Deterministic: wipe the default cube/camera/light and purge orphan data.
- No context dependence: everything uses the data API, safe headless.
- Fail loud: a report function so a "working" script that renders black is caught.
"""

import bpy
import bmesh
import math
import sys
from mathutils import Vector


# ---------------------------------------------------------------------------
# Args after `--`
# ---------------------------------------------------------------------------
def get_args():
    argv = sys.argv
    return argv[argv.index("--") + 1:] if "--" in argv else []


# ---------------------------------------------------------------------------
# Clean scene: remove everything and purge orphaned datablocks
# ---------------------------------------------------------------------------
def clean_scene():
    # Remove all objects via the data API (no context/mode needed).
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    # Purge orphaned meshes, materials, images, etc. so re-runs stay clean.
    for coll in (bpy.data.meshes, bpy.data.curves, bpy.data.materials,
                 bpy.data.images, bpy.data.lights, bpy.data.cameras,
                 bpy.data.node_groups, bpy.data.armatures):
        for block in list(coll):
            if block.users == 0:
                coll.remove(block)
    print("Scene cleaned:", len(bpy.data.objects), "objects remain")


# ---------------------------------------------------------------------------
# Link helper: create an object from mesh data and link it to the scene
# ---------------------------------------------------------------------------
def new_object(name, data):
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    return obj


# ---------------------------------------------------------------------------
# Camera that frames all mesh objects in the scene
# ---------------------------------------------------------------------------
def scene_bounds():
    """World-space min/max corners over all mesh/curve objects."""
    mins = Vector((math.inf,) * 3)
    maxs = Vector((-math.inf,) * 3)
    found = False
    for obj in bpy.data.objects:
        if obj.type not in {"MESH", "CURVE", "FONT", "SURFACE"}:
            continue
        found = True
        for corner in obj.bound_box:
            world = obj.matrix_world @ Vector(corner)
            mins = Vector(map(min, mins, world))
            maxs = Vector(map(max, maxs, world))
    if not found:
        return Vector((-1, -1, -1)), Vector((1, 1, 1))
    return mins, maxs


def add_framing_camera(angle=(1.1, 0.0, 0.8), margin=1.4, lens=50.0):
    """Add a camera that looks at the scene center and frames its bounds.
    `angle` is a direction (radians-ish tilt); tweak for a nicer 3/4 view."""
    mins, maxs = scene_bounds()
    center = (mins + maxs) * 0.5
    radius = max((maxs - mins).length * 0.5, 0.5)

    cam_data = bpy.data.cameras.new("Camera")
    cam_data.lens = lens
    cam = new_object("Camera", cam_data)

    # Place the camera back along a 3/4 direction, distance scaled to fit.
    dist = radius * margin / math.tan(cam_data.angle * 0.5) * 0.5 + radius
    direction = Vector((math.cos(angle[2]) * math.cos(angle[0]),
                        math.sin(angle[2]) * math.cos(angle[0]),
                        math.sin(angle[0]))).normalized()
    cam.location = center + direction * dist * 1.5

    # Aim at center via a Track To constraint pointed at an empty.
    target = new_object("CamTarget", None)  # empty
    target.location = center
    con = cam.constraints.new("TRACK_TO")
    con.target = target
    con.track_axis = "TRACK_NEGATIVE_Z"
    con.up_axis = "UP_Y"

    bpy.context.scene.camera = cam
    return cam


# ---------------------------------------------------------------------------
# Quick three-point-ish default light so nothing renders black by accident
# ---------------------------------------------------------------------------
def add_basic_lighting(strength=3.0):
    world = bpy.context.scene.world or bpy.data.worlds.new("World")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    if bg:
        bg.inputs["Strength"].default_value = strength * 0.15  # soft ambient

    key = bpy.data.lights.new("Key", type="AREA")
    key.energy = 1000
    key.size = 5
    ko = new_object("Key", key)
    ko.location = (4, -4, 6)
    ko.rotation_euler = (math.radians(50), 0, math.radians(40))
    return ko


# ---------------------------------------------------------------------------
# Render report: catch black/empty renders before they surprise you
# ---------------------------------------------------------------------------
def report_scene():
    scene = bpy.context.scene
    print("--- SCENE REPORT ---")
    meshes = [o for o in bpy.data.objects if o.type == "MESH"]
    lights = [o for o in bpy.data.objects if o.type == "LIGHT"]
    print(f"objects: {len(bpy.data.objects)}  meshes: {len(meshes)}  "
          f"lights: {len(lights)}  camera: {scene.camera.name if scene.camera else 'NONE!'}")
    for o in meshes:
        print(f"  mesh {o.name!r}: {len(o.data.vertices)} verts, "
              f"{len(o.data.materials)} materials")
    if not lights and not (scene.world and scene.world.use_nodes):
        print("  WARNING: no lights and no world lighting -> render will be black")
    print("--------------------")


# ---------------------------------------------------------------------------
# Render a still. Uses Eevee for speed; switch to CYCLES for realism.
# ---------------------------------------------------------------------------
def render_still(path, engine="BLENDER_EEVEE_NEXT", samples=64,
                 res=(1280, 720), transparent=False):
    scene = bpy.context.scene
    # Engine id changed across versions; fall back gracefully.
    try:
        scene.render.engine = engine
    except TypeError:
        scene.render.engine = "CYCLES"
    scene.render.resolution_x, scene.render.resolution_y = res
    scene.render.film_transparent = transparent
    if scene.render.engine == "CYCLES":
        scene.cycles.samples = samples
        scene.cycles.use_denoising = True
    else:
        try:
            scene.eevee.taa_render_samples = samples
        except AttributeError:
            pass
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = path
    if scene.camera is None:
        add_framing_camera()
    report_scene()
    bpy.ops.render.render(write_still=True)
    print("Rendered ->", path)


if __name__ == "__main__":
    args = get_args()
    out = args[args.index("--out") + 1] if "--out" in args else "/tmp/render.png"
    clean_scene()
    # ---- build your scene here ----
    cube = bpy.data.meshes.new("Cube")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2.0)
    bm.to_mesh(cube)
    bm.free()
    obj = new_object("Cube", cube)
    # -------------------------------
    add_basic_lighting()
    add_framing_camera()
    render_still(out)
