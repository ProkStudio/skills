---
name: minecraft-block-palettes
description: Verified Minecraft Java block reference for builders - which blocks actually exist, which have stairs, slabs, walls or fences, which are version-gated (1.20 cherry and bamboo, 1.21 tuff and copper families, 1.21.4 pale oak and resin, 1.21.5 plants, 1.21.9 copper chests and shelves), which are creative-only or uncraftable, plus colour and value groups, texture noise levels and ready-made tier palettes. Use whenever a build answer needs a block list, when picking or fixing a palette, when the user asks what blocks fit together or what to use for white, black, red, green or pastel surfaces, when a block variant must be confirmed before proposing it, or when a build must stay inside one game version. Prevents invented blocks, missing variants and version mistakes.
version: 1.0.0
---

# Minecraft Block Palettes

This skill is the **fact-checking layer** under every other Minecraft skill. Design advice
fails when it names a block that does not exist, a stair variant that was never added, or a
1.21.9 block in a 1.20 world.

**Target:** Java Edition. Version gates are stated explicitly, newest supported drop 1.21.9
("The Copper Age").

**Companions:** `../minecraft-architecture/references/palette-and-texture.md` owns the *theory*
(tiers, value hierarchy, blending). This skill owns the *inventory* (what exists, in what
variants, since when) and ready-made palettes.

## Non-negotiables

1. **Never invent a block.** If you cannot find it in `references/block-families.md`, do not
   name it. There is no marble, no slate roof tile, no plaster block, no wooden wall.
2. **Check the variant before promising it.** Stairs, slabs, walls, fences and doors exist only
   for specific families - see the variant matrix. Smooth stone has a slab but **no stairs**;
   terracotta, concrete and wool have **no** stairs, slabs or walls at all.
3. **State the version gate** the first time a gated block appears in an answer: "tuff bricks
   (1.21+)", "pale oak planks (1.21.4+)", "shelf (1.21.9+)".
4. **Ask or assume explicitly.** If the user's version is unknown and the design leans on gated
   blocks, say which blocks need which version and give a fallback.
5. **Respect obtainability.** Light blocks, barriers, budding amethyst, command blocks and
   spawners are creative/command-only. Flag them in survival contexts and offer alternatives.
6. **Use English block ids in brackets** when the chat language is not English, so the user can
   find the block in the creative inventory or in a command.

## How to use it

| Task | Read |
| --- | --- |
| "Does this block have stairs/slab/wall?" | `references/block-families.md` |
| "What is available in my version?" | `references/version-gates.md` |
| "I need a white / dark / red / green surface" | `references/colour-and-value.md` |
| "Give me a palette for X" | `references/palette-recipes.md` |
| "Is this safe in survival / does it move / does it glow?" | `references/special-blocks.md` |

## Workflow when answering a build question

1. Pick the palette **intent** first: mood, value split (light/mid/dark), style, biome light.
2. Pull a tier set from `references/palette-recipes.md`, or build one:
   base ~60%, secondary ~30%, accent ~10%, plus trim and glass/light.
3. **Verify every block** against `references/block-families.md`, including the exact variant
   you plan to use (stairs for the cornice, wall for the railing, fence for the pergola).
4. **Verify the version** against `references/version-gates.md`; annotate gated blocks.
5. Check the value spread: the three tiers must differ in brightness, not only in hue.
6. Check texture noise: mixing three noisy blocks turns to mush; mixing three flat blocks looks
   like a texture demo. Aim for one noisy, one medium, one flat per surface at most.
7. Deliver the palette as a table with tier, blocks, and where each goes.

## Quick sanity table (the mistakes that happen most)

| Claim | Truth |
| --- | --- |
| "smooth stone stairs" | Do not exist. Smooth stone has a slab only |
| "cut sandstone stairs" | Do not exist. Cut sandstone has a slab only |
| "terracotta / concrete / wool stairs or slabs" | Do not exist for any colour |
| "polished granite/diorite/andesite wall" | Do not exist. Walls exist for the **unpolished** blocks |
| "wooden wall" | Does not exist. Wood has fences, not walls |
| "quartz bricks stairs" | Do not exist. Stairs exist for quartz block and smooth quartz |
| "chiseled stone brick stairs" | Do not exist. Chiseled variants are single blocks |
| "marble / slate / plaster / limestone" | Not Minecraft blocks. Use calcite, deepslate, white terracotta, smooth sandstone |
| "copper roof tiles" | Use cut copper stairs/slabs in an oxidation stage |
| "tuff bricks" in a 1.20 world | 1.21+ only. Fallback: deepslate bricks or stone bricks |
| "pale oak" in a 1.21 world | 1.21.4+ only. Fallback: birch with white terracotta |
| "shelf" / "copper chest" in 1.21.4 | 1.21.9+ only. Fallback: item frames on trapdoors, barrels |

## Delivery format

Give palettes as a table, never as prose:

| Tier | Share | Blocks | Where |
| --- | --- | --- | --- |
| Base | 60% | deepslate bricks, cracked deepslate bricks, polished deepslate | walls |
| Secondary | 30% | dark oak log, stripped dark oak | frame, beams |
| Accent | 10% | oxidized cut copper stairs (1.17+) | roof |
| Trim | lines | polished deepslate slab, cobbled deepslate wall | sills, cornice, railing |
| Light | points | soul lantern, candle | fixtures |

Add a **fallback row** whenever a gated block is used, and 2-3 swap levers ("swap copper for
deepslate tiles for a colder read").

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| User says "that block does not exist" | Guessed from real-world materials | Verify in `references/block-families.md` before naming |
| "I cannot craft those stairs" | Variant does not exist for that family | Variant matrix in `references/block-families.md` |
| "I do not have that block in my version" | Version gate ignored | `references/version-gates.md`, annotate and give fallbacks |
| Palette looks muddy | Three noisy textures, no value contrast | `references/colour-and-value.md` - noise levels and value ladders |
| Palette looks sterile | Three flat textures, no weathering | Add one noisy block and damaged variants at the base |
| Build is unbuildable in survival | Creative-only blocks proposed | `references/special-blocks.md` |
| Colours fight each other | Two saturated families at 30%+ | Keep saturation to the 10% accent tier |

## References

| File | Contents |
| --- | --- |
| `references/block-families.md` | Every building family and the variant matrix (stairs/slab/wall/fence/door) |
| `references/version-gates.md` | What arrived in 1.20, 1.21, 1.21.4, 1.21.5, 1.21.6, 1.21.9, with fallbacks |
| `references/colour-and-value.md` | Value ladders, hue groups, texture noise levels, biome light |
| `references/palette-recipes.md` | 18 ready tier palettes by style and mood |
| `references/special-blocks.md` | Creative-only, gravity, piston, waterlogging, light, entity-cost blocks |
