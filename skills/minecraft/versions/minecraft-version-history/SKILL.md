---
name: minecraft-version-history
description: Answer "what changed in which Minecraft version" and keep a build inside the block set that actually exists in the target version. Covers Java Edition from 1.13 to 1.21.11 and the year-based 2026 drops (26.1 Tiny Takeover, 26.2 Chaos Cubed, 26.3 Wilderness Bound), with per-version lists of builder-relevant blocks, variants and mechanics, the Bedrock version mapping, substitutions for older targets, pack format numbers, Java runtime requirements and world migration tools. Use when a build must run on a specific version or version range, when a palette may contain blocks that do not exist yet in the target, when downgrading or upgrading a world or schematic, or when a data pack, resource pack or server needs the right format numbers.
version: 1.0.0
---

# Minecraft version history

A per-version record of what changed, written for builders and project owners rather than
for changelog completeness. Use it to answer three questions: *does this block exist in my
version*, *what do I use instead if it does not*, and *what breaks if I move the project*.

## Non-negotiables

1. **Never name a block without knowing the floor version of the project.** If the user has
   not said which version they play, ask once, or state the gate inline: "deepslate bricks
   (1.17+)". A palette the player cannot place is worse than a boring palette.
2. **The floor version decides the palette, not the newest version.** For a range like
   1.19-26.2, everything structural must exist in 1.19. Newer blocks may only appear as
   optional swaps, clearly marked.
3. **Never claim a survival-obtainable block is available in creative-only form, or the
   reverse.** Gates and obtainability are different questions.
4. **World upgrades are one-way.** Back up the save folder before opening it in a newer
   version, and never promise a downgrade path for a world; only builds move backwards.
5. **This file set is a snapshot taken in September 2026.** For anything newer than
   26.3, or for an exact pack format number, check `minecraft.wiki` instead of trusting
   the tables here.

## Version numbering, in two schemes

Minecraft changed how it numbers releases in December 2025, so half the advice on the
internet describes a scheme the game no longer uses.

| Era | Scheme | Examples |
| --- | --- | --- |
| Until December 2025 | `1.<major>.<minor>` on Java, `1.<major>.<build>` on Bedrock | Java 1.21.9, Bedrock 1.21.130 |
| From 2026 | `<year>.<drop>.<hotfix>` on Java; Bedrock shares the year prefix with its own second number | Java 26.1, 26.1.2, 26.2; Bedrock 26.10, 26.30, 26.50 |

- The `1.x` line ended at **1.21.11**. There is no 1.22 and there never will be.
- Java ships three to four drops a year, roughly quarterly, with hotfixes hanging off each.
- Java and Bedrock share the drop *name* and release date but not the number. Always ask
  which edition before answering a version question - see `references/timeline-2026.md`
  for the 2026 mapping.
- Snapshots are now named by week (`26w05a`) or by drop (`26.3-snapshot-9`).

## How to use this skill

1. **Pin the target.** Edition (Java or Bedrock), floor version, and whether the project must
   also keep working on the newest release.
2. **Look up the floor.** Read the timeline file covering that version and note which
   families are missing. The most commonly missed gates are deepslate and copper (1.17),
   mud bricks (1.19), bamboo and cherry (1.20), the tuff and copper expansion (1.21),
   pale oak and resin (1.21.4), and wool and concrete stairs and slabs (26.3).
3. **Substitute, do not compromise the design.** `references/block-substitutions.md` gives a
   replacement for every family added since 1.13, so an old-version build can still have
   three value tiers and a proper accent.
4. **Check the mechanics, not just the blocks.** Height limits, spawn-proofing light level,
   waterlogging and piston behaviour all changed mid-history and will silently break a
   design that was copied from a newer tutorial.
5. **State the gates in the answer.** Write `sculk (1.19+)` the first time a gated block
   appears in a palette, then stop repeating it.

## The five hard walls

These are the version boundaries that break projects rather than just adding blocks.

| Wall | Version | What breaks |
| --- | --- | --- |
| The Flattening | 1.13 | Numeric block IDs and data values are gone; every command, data pack, schematic and tutorial older than 1.13 needs rewriting |
| Height and light | 1.18 | World is `-64` to `320` (top block `y=319`); the light engine changed and hostile mobs now need block light **0**, so pre-1.18 spawn-proofing at light 8 is wrong |
| Item components | 1.20.5 | Item NBT in commands and data packs was replaced by the data component system; entity NBT was not affected |
| Copper and tuff expansion | 1.21 | A large share of modern palettes (chiseled copper, copper grate and bulb, copper doors, the whole tuff brick family) simply does not exist before this |
| Year-based versions and Java 25 | 26.1 | Version numbers change shape, and 26.x refuses to start on the Java runtime that ran 1.21.x |

## Reference files

| File | Contents |
| --- | --- |
| `references/timeline-1-13-to-1-16.md` | 1.13 Update Aquatic through 1.16 Nether Update: the flattening, the 1.14 variant explosion, blackstone and the nether wood sets |
| `references/timeline-1-17-to-1-19.md` | 1.17 copper, deepslate and candles; 1.18 height and light rewrite; 1.19 mud, mangrove and sculk |
| `references/timeline-1-20-to-1-21.md` | 1.20 bamboo, cherry and hanging signs through the 1.21 drops, ending at 1.21.11 |
| `references/timeline-2026.md` | The numbering change, 26.1 Tiny Takeover, 26.2 Chaos Cubed, 26.3 Wilderness Bound, and the Bedrock mapping |
| `references/block-substitutions.md` | What to build with instead when the target version lacks a family |
| `references/pack-formats-and-migration.md` | Pack format numbers, Java runtime requirements, world and schematic migration, tooling |

## Companion skills

| Skill | Use for |
| --- | --- |
| `../../building/minecraft-block-palettes/SKILL.md` | Choosing the palette itself; its `references/version-gates.md` is the short form of these timelines |
| `../../building/minecraft-architecture/SKILL.md` | The build process the palette serves |
| `../../redstone/minecraft-redstone-for-builders/SKILL.md` | Mechanism behaviour, which is the most version-sensitive part of any build |

## Failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| "This block does not exist for me" | Palette written for the newest release | Ask for the version, then re-cut the palette at that floor using `references/block-substitutions.md` |
| Mobs spawn inside a lit build | Pre-1.18 advice applied to a 1.18+ world | Every enclosed surface needs block light 1 or a non-spawnable surface |
| Build cannot be placed at the planned depth | Design assumes `-64` in a pre-1.18 world | Floor is `y=0` before 1.18; re-datum the whole section |
| Redstone contraption behaves differently | Java-only quasi-connectivity, or a Bedrock port | Confirm the edition first; see the redstone skill |
| Data pack refuses to load | Wrong `pack_format` | Look the number up per version; use `supported_formats` and overlays for a range (1.20.2+) |
| World will not open after a downgrade attempt | Worlds only move forward | Restore the backup, then move the *build* with a schematic instead |

## Answering style

- Lead with the answer, then the version: "Copper grates, yes - but only from 1.21."
- When a user asks "what changed in X", give the builder-relevant items first (blocks,
  variants, mechanics), then one line on the rest (mobs, items, technical).
- When a drop is still in snapshot or pre-release, say so; block lists change before release.
