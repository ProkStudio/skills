# Formats and exporter settings

## Format comparison

| Format | Meshes | Skinning / animation | Materials | Notes |
| --- | --- | --- | --- | --- |
| **glTF 2.0** (.glb / .gltf) | Yes | Yes | PBR metal/rough, embedded or referenced textures | Conventions defined by the format; best default for Godot, web, and increasingly Unity/Unreal |
| **FBX** | Yes | Yes | Limited, importer-dependent | Industry standard in Unity/Unreal pipelines; many conventions left to the exporter |
| **OBJ** | Yes | No | MTL, basic | Simple static geometry exchange; no animation, no proper PBR |
| **USD / USDZ** | Yes | Yes | MaterialX/UsdPreviewSurface | Scene interchange and large pipelines; support varies by application |
| **Alembic** (.abc) | Yes (cached) | Baked point caches, no rig | No | Heavy cached deformation for VFX, not for game rigs |
| **STL / 3MF** | Yes | No | No / limited | 3D printing |
| **PLY** | Yes | No | Vertex colours | Scans and point clouds |

Default recommendation: **glTF** when the target supports it well, **FBX** when the pipeline demands
it, **OBJ** only for quick static exchange, **USD** for scene-level interchange, **Alembic** for
baked deformation caches.

## glTF export settings that matter

| Setting | Guidance |
| --- | --- |
| Format | `.glb` (single binary file) for engines; `.gltf` + separate files when textures must stay editable |
| Include | Selected Objects / Visible / Renderable - be explicit rather than exporting the whole scene |
| Transform +Y Up | On by default and correct for glTF; leave it on |
| Geometry: Apply Modifiers | On for final assets, off when shape keys must survive |
| UVs / Normals / Tangents | Export normals always; tangents when the engine wants them precomputed |
| Vertex Colors | Export only if used; stray colour attributes bloat files |
| Compression (Draco) | Useful for web delivery; check engine support before enabling |
| Materials | Export for previewing; most game pipelines rebuild materials in-engine |
| Images | Automatic/JPEG/None - `None` when textures ship separately |
| Animation | Enable for rigged assets; choose whether to export all actions or the active one; sampling rate matters |
| Skinning | On for characters; check the influence limit setting |
| Shape Keys / Morph targets | Enable when blend shapes are needed, with normals if the engine uses them |

## FBX export settings that matter

| Setting | Guidance |
| --- | --- |
| Include > Limit to Selected Objects | Almost always on |
| Object Types | Restrict to Mesh (and Armature for characters); exclude Empty/Camera/Light unless intended |
| Transform > Scale | Leave at 1.0 and control units with Apply Scalings |
| Apply Scalings | `FBX_SCALE_ALL` / `FBX_SCALE_UNITS` / `FBX_SCALE_CUSTOM` / `FBX_SCALE_NONE`; choose once per target and save a preset |
| Forward / Up | Set to the target engine's convention |
| Apply Unit | Controls whether the FBX file's unit metadata is used |
| Apply Transform (`bake_space_transform`) | Experimental; known to misbehave with armatures and animation. Avoid for rigged assets |
| Geometry > Smoothing | `Face`, `Edge`, `Normals Only` or `Off` - Unity/Unreal generally want Face or Edge; smoothing groups matter for some DCC targets |
| Export Subdivision Surface | Usually off; bake subdivision by applying it instead |
| Apply Modifiers (`use_mesh_modifiers`) | On for static meshes; note it prevents shape keys from exporting |
| Tangent Space | Export when the engine expects authored tangents; requires triangulated, UV-mapped meshes |
| Armature > Only Deform Bones | On - keeps control bones out of the export |
| Add Leaf Bones | Usually off for Unity/Unreal; it creates extra end bones |
| Primary/Secondary Bone Axis | Leave at defaults unless the target requires otherwise, then keep it consistent |
| Bake Animation | On for animated exports; set Simplify to 0 for exact keys, or higher to reduce file size |
| NLA Strips / All Actions | Choose deliberately; "All Actions" can produce unexpected extra clips |
| Force Start/End Keying | Useful for clean clip boundaries |

## Normals and smoothing

- Since Blender 4.1 there is no mesh Auto Smooth checkbox: use Object > **Shade Auto Smooth**, which
  adds a **Smooth by Angle** geometry-nodes modifier, or mark edges sharp manually.
- Mark sharp edges explicitly for hard-surface assets; combined with UV seams this is what makes
  baked normals and engine shading agree.
- Custom split normals give exact control. If an engine ignores them, the usual causes are the
  exporter's smoothing option or an importer setting overriding normals.
- Weighted Normal modifier (before triangulation) fixes shading on beveled hard-surface meshes.
- Recalculate normals outside (Shift+N) and check with the face-orientation overlay before export.

## Triangulation

- Engines triangulate on import. If you do not control it, their triangulation may differ from what
  you saw in Blender, changing shading subtly.
- Options: add a **Triangulate** modifier (Beauty for quads, Fixed for predictability) at the end of
  the stack, or enable the exporter's triangulate option.
- Keep the quad version as the source; export triangles.
- Triangulate **after** the Weighted Normal / bevel work, never before.

## Materials and textures

| Topic | Guidance |
| --- | --- |
| Material slots | One slot per intended engine material; order and names are preserved |
| Slot count | Each slot is a draw call in most engines; merge where possible |
| Material names | Use the project convention; engines often match by name on reimport |
| Textures | Export separately in most game pipelines; embed only for standalone .glb delivery |
| Paths | Use relative paths (File > External Data) so nothing breaks on another machine |
| Packed files | Unpack before exporting when the engine needs loose files |
| Channel packing | Pack AO/Roughness/Metallic into one image (ORM) where the engine expects it; document channel order |
| Colour spaces | Base colour sRGB; all data maps Non-Color |

## Scene-level exports

- For whole environments, prefer exporting modular pieces and assembling in-engine; a single giant
  FBX is hard to iterate on.
- If a layout must transfer, export empties as placeholders or use the engine's own scene format, and
  keep names stable.
- Collections can map to engine prefabs conceptually; keep one collection per logical asset.
- Instances: many exporters realize instances, which multiplies file size. Check before exporting a
  scattered scene, and consider exporting the source asset plus a transform list instead.

## Format decision shortcuts

| Situation | Format |
| --- | --- |
| Godot 4 asset | glTF (.glb) |
| Web viewer / three.js | glTF (.glb), Draco if size matters |
| Unity static prop | FBX or glTF, depending on project convention |
| Unity / Unreal skinned character | FBX (project standard) or glTF where supported |
| Unreal static mesh with LODs and collision | FBX with named LOD/collision meshes |
| Handing geometry to another DCC | FBX, USD, or OBJ for simple cases |
| Cached simulation or cloth | Alembic |
| 3D print | STL or 3MF at real scale |
