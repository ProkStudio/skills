# Texel density, packing and texture sets

## The formula

```
texel density (px/m) = texture resolution (px) / real-world size (m)
```

Worked examples:

| Texture | Real size covered | Density |
| --- | --- | --- |
| 1024 px | 4 m | 256 px/m (2.56 px/cm) |
| 2048 px | 4 m | 512 px/m |
| 2048 px | 2 m | 1024 px/m |
| 4096 px | 2 m | 2048 px/m |
| 512 px | 1 m | 512 px/m |

To find the needed resolution for a target density: `resolution = density x size`. A 3 m wall at
512 px/m needs 1536 px, so you round up to 2048 and either accept more density or reuse the slack.

## Picking a standard

Density is a project decision, not a per-asset one. Pick a number and make every asset obey it.
Common working ranges:

| Content | Rough density |
| --- | --- |
| Distant background, terrain | 64-128 px/m |
| Large architecture, floors, walls | 256-512 px/m |
| Standard props the player walks past | 512-1024 px/m |
| Interactive or hero props | 1024-2048 px/m |
| First-person hands and weapons | 2048+ px/m |

Characters are usually specified as a texture budget rather than a density: 2048 px per texture set
is a long-standing norm for AAA game characters, with 4096 increasingly common for hero characters
and cinematics. Environment assets are usually specified by density.

Rules:

1. **Consistency beats absolute value.** A scene at a uniform 400 px/m looks better than one mixing
   200 and 1200.
2. **Pixel size, not texture size, is what the player sees.** A 4K texture on a 20 m building is
   lower density than a 1K texture on a 1 m crate.
3. **Raise density only where the camera goes.** Hero areas, gameplay-critical surfaces, close-ups.
4. **Check density per object** after scaling anything. Scaling a model without re-checking is the
   classic source of drift.
5. **Document the standard** in the project readme, including the padding rule.

Tools: the bundled Texel Density Checker-type add-ons report and set density directly; without one,
compare a known-size checker texture across objects.

## Packing

- **UV > Pack Islands** with margin. Enable rotation for better fill unless direction matters.
- Margin is expressed as a fraction of the UV space; translate it into pixels for the target
  resolution before choosing.
- Padding guidance by resolution (edge padding, i.e. space between islands, split across both):

| Resolution | Padding between islands |
| --- | --- |
| 512 px | 4-8 px |
| 1024 px | 8-12 px |
| 2048 px | 12-16 px |
| 4096 px | 16-32 px |

- Padding must survive mipmapping: each mip halves the resolution, so 16 px at 4K becomes 1 px at the
  fifth mip. Block compression (BC/DXT) works in 4x4 blocks, another reason not to hug island edges.
- Straight-edged islands pack better than ragged ones; rectangular islands waste the least space.
- Scale islands by importance, not uniformly - the face of a character deserves more space than the
  soles of its boots.
- Aim for 75-90% UV space utilisation; chasing 99% costs more time than it saves texture memory.

## Atlases, trim sheets and tiling

| Approach | How it works | Best for |
| --- | --- | --- |
| Unique unwrap | Every surface has its own texture space | Hero props, characters, baked detail |
| Atlas | Many objects share one texture | Sets of small props, modular kits, mobile |
| Trim sheet | A strip of reusable materials and mouldings; UVs snap onto strips | Architecture, sci-fi corridors, modular kits |
| Tiling material | UVs scaled to repeat a seamless texture | Floors, walls, terrain, large surfaces |
| Decals / mesh decals | Detail projected on top | Signs, wear, panel lines, damage |

Trim sheets and tiling are how large environments stay inside memory budgets: unique 512 px/m
texturing of a whole building is unaffordable, while a trim sheet gives high density everywhere.

For tiling UVs:

- Keep the UV scale a clean multiple so texture repeats align with geometry.
- Straighten islands so the pattern runs true.
- UV coordinates outside 0-1 are fine and normal for tiling.

## UDIM

- UDIM spreads one UV layout across multiple tiles, each with its own texture file, numbered 1001,
  1002, ... (tile = 1001 + u + 10 x v).
- Blender supports UDIM tiled images natively; the UV editor can show and manage tiles.
- Use it for: film-quality characters and creatures, large props needing many 4K maps, anything
  textured in Mari or Substance with multiple tiles.
- Avoid it for real-time work - most engines handle UDIM poorly or not at all; use multiple texture
  sets or atlases instead.

## Multiple texture sets

- Split by material logic (skin / clothing / armour / props) rather than arbitrarily; each set becomes
  a material and a draw call.
- More sets = more draw calls and more memory overhead; fewer sets = less flexibility and lower
  density.
- Typical real-time character: 2-4 sets. Typical prop: 1 set.
- Keep one set per material slot so export and engine assignment stay predictable.

## Overlapping and mirrored UVs

| Technique | Gain | Cost |
| --- | --- | --- |
| Mirrored halves sharing UVs | Doubles density | Symmetric detail, normal-map handedness issues, no unique dirt |
| Repeated parts stacked (bolts, wheels) | Big savings | Identical wear on every copy |
| Fully unique | Full artistic freedom | Highest memory cost |

When stacking or mirroring:

- Offset the duplicate islands by exactly one UV tile so bakers and lightmappers can tell them apart.
- Keep the lightmap UV channel non-overlapping regardless of what the main channel does.
- Beware mirrored normal maps: mirrored tangent space can flip detail; test with a directional bake.

## Density and packing checklist

1. Project density standard written down.
2. Asset real-world size verified.
3. Average Islands Scale run, then density set to the standard.
4. Padding chosen for the target resolution and mip plan.
5. Utilisation 75-90%, rotation allowed unless direction matters.
6. Island scale weighted by visual importance.
7. Overlaps and mirrors intentional and offset by a tile.
8. Lightmap channel non-overlapping if the engine bakes light.
