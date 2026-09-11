# LODs, collision and sockets

## LODs

Levels of detail swap in simpler meshes at distance. A workable default chain:

| Level | Triangle ratio | Typical switch trigger |
| --- | --- | --- |
| LOD0 | 100% | Close-up, hero view |
| LOD1 | 50-60% | Mid distance |
| LOD2 | 25-30% | Far |
| LOD3 | 10-15% | Very far / crowd |
| Billboard or impostor | A textured plane | Extreme distance, vegetation |

Guidance:

- LOD0 should already be budget-conscious; LODs do not fix an over-dense hero mesh.
- Preserve the **silhouette** at every level; interior detail can go first.
- Keep UVs consistent so all levels share the same textures.
- Keep material slots identical across levels, or engines will complain.
- Watch for popping: if a level change is visible, the ratio step is too aggressive or the switch
  distance is too near.
- Small props often need only LOD0 and LOD1; vegetation and architecture benefit most.

## Generating LODs in Blender

| Method | Behaviour | Use |
| --- | --- | --- |
| Decimate > Collapse | Merges edges by ratio; fast, gives triangles | General-purpose LOD generation |
| Decimate > Un-Subdivide | Reverses subdivision by iterations; keeps quads | Cleanly subdivided meshes |
| Decimate > Planar | Merges faces within an angle limit | Hard-surface and architectural meshes with large flat areas |
| Manual retopology | Full control | Hero assets, deforming meshes |
| Weld / Merge by Distance | Removes micro detail | Cleanup before decimation |
| Quad Remesh (Quadriflow) | Even quads at a target count | Organic LODs that must still deform |

Practical procedure:

1. Duplicate LOD0, apply a Decimate modifier, set the ratio, apply it.
2. Fix the worst damage by hand: broken silhouettes, collapsed openings, pinched UV areas.
3. Recalculate normals; re-mark sharp edges if the decimation destroyed them.
4. Check that UVs survived; heavy decimation distorts them.
5. For deforming meshes, verify skin weights transferred correctly (Data Transfer from LOD0).

## LOD naming conventions

| Engine | Convention |
| --- | --- |
| Unreal (FBX with LOD group) | `SM_Asset_LOD0`, `SM_Asset_LOD1`, ... inside an FBX, or an LOD group; Unreal also supports importing LODs separately |
| Unity | Separate meshes named `Asset_LOD0`, `Asset_LOD1`, assembled into an LOD Group component |
| Godot | Godot 4 generates mesh LODs automatically on import for many meshes; explicit LODs are usually unnecessary |

Check the engine version's importer documentation - LOD import rules change more often than most
export settings.

## Collision meshes

Collision should almost never be the render mesh:

| Collision type | Cost | Use |
| --- | --- | --- |
| Box / sphere / capsule primitive | Cheapest | Crates, barrels, characters, most props |
| Convex hull | Cheap | Rocks, irregular but solid shapes |
| Multiple primitives / hulls | Moderate | Complex props built from simple volumes |
| Convex decomposition | Moderate | Automatically generated multi-hull approximations |
| Triangle mesh (concave) | Expensive | Static level geometry only, never dynamic bodies |

Authoring rules:

- Keep collision simple: dozens of triangles, not thousands.
- Collision volumes must be **closed and convex** (per hull), with normals facing out.
- Slightly undersize or simplify collision so the player never catches on invisible detail; keep it
  slightly larger only where blocking matters.
- Do not include collision meshes in the render material list; they carry no material.

Naming (Unreal FBX conventions, widely borrowed elsewhere):

| Prefix | Meaning |
| --- | --- |
| `UBX_` | Box collision |
| `USP_` | Sphere collision |
| `UCP_` | Capsule collision |
| `UCX_` | Convex collision |

Unity and Godot use their own components and do not require these prefixes, but following one
convention across the library keeps things predictable.

## Sockets and attachment points

- Sockets mark where things attach: weapon grips, effect emitters, mounting points, doors' hinges.
- In Blender, use **empties** named by convention (`socket_weapon_r`, `fx_muzzle`) parented to the
  object or bone.
- Unreal's FBX pipeline recognises empties named with a socket prefix for static meshes; Unity and
  Godot import them as child transforms you can reference.
- Keep socket orientation meaningful: define which local axis points "out" and apply it consistently.
- For skinned characters, sockets are usually extra bones instead of empties.

## Pivots and modular kits

| Rule | Why |
| --- | --- |
| Origin on the grid | Pieces snap without manual nudging |
| Consistent module sizes (e.g. 1 m, 2 m, 4 m) | Kit pieces interchange |
| Seams at module boundaries | No visible cracks; use trim sheets to hide joins |
| Consistent forward axis | Rotation by 90 degrees always works |
| Matching wall thickness and floor heights | Pieces combine without gaps |
| Shared trim sheet or atlas | Fewer materials, consistent look |

Modular kits live or die by discipline: one piece with a 3 cm offset breaks every layout built from
it.

## Extras checklist

1. LOD chain present where distance matters, with silhouettes preserved.
2. LOD material slots identical to LOD0.
3. Collision simple, convex and closed, named by convention.
4. Sockets placed, named and oriented consistently.
5. Origins on the grid for modular pieces.
6. Nothing non-render (collision, sockets, helpers) hidden in the render mesh's material list.
7. Triangle counts recorded per LOD for the budget sheet.
