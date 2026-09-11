# Connecting blocks - panes, bars, fences, walls, chains

Why glass panes and fences end up as lone posts, and how to prevent it. Four different
causes, three of which are placement bugs and one of which is design.

## Contents

- Cause 1 - explicit blockstates in commands
- Cause 2 - no block update after bulk placement
- Cause 3 - neighbours that never connect
- Cause 4 - the opening is 1 block wide
- Wall post vs low profile
- Placement checklist

## Cause 1 - explicit blockstates in commands

`glass_pane`, `iron_bars`, all `*_wall` and all `*_fence` blocks store their connections as
blockstates (`north`, `south`, `east`, `west`, `up`). Writing them explicitly locks the block
in that shape forever.

```
# WRONG - every pane stays a lone post
/fill ~ ~ ~ ~10 ~ ~ glass_pane[north=false,south=false,east=false,west=false]

# RIGHT - let the game compute connections
/fill ~ ~ ~ ~10 ~ ~ glass_pane
```

Rule: **never** include connection states for panes, bars, walls or fences. Do specify state
for things that need it - `facing`/`half`/`shape` on stairs, `type` on slabs, `axis` on logs
and chains, `rotation` on signs.

Historically `/fill` and `/setblock` themselves failed to update these blocks (MC-129367);
that was fixed around 1.16, so on 1.21 plain commands connect correctly.

## Cause 2 - no block update after bulk placement

WorldEdit in fast mode, `//paste`, schematics, Litematica printing, structure blocks and
`/clone` can place blocks without triggering neighbour updates. The blocks are correct in the
world but render as disconnected, or keep stale connection states.

Fixes, cheapest first:

1. **F3 + A** - reload chunks client-side. Fixes purely visual desync instantly.
2. Break and replace one block in the run - the update propagates along it.
3. Re-place the same block over itself with a normal (non-fast) placement or a `//replace`
   of the block with itself.
4. Disable fast mode / enable block updates in the editor before mass-placing connecting
   blocks.
5. Leave and rejoin the world if states, not just visuals, look wrong.

Always run F3+A after a bulk placement and *then* judge the result.

## Cause 3 - neighbours that never connect

These blocks only connect sideways to specific neighbours. This is intended behaviour, and it
is the most common real cause of "single" panes and fences.

| Block | Connects to | Does not connect to |
| --- | --- | --- |
| Glass pane | other glass panes, full solid blocks (including glass blocks, logs, planks, stone), walls | fences, iron bars, slabs, stairs' open sides, trapdoors, leaves, most non-full blocks |
| Iron bars | other iron bars, full solid blocks, walls | glass panes, fences, slabs, leaves |
| Walls | other walls, full solid blocks, glass panes, iron bars | fences |
| Fences | fences of the same family (all wooden fences together, nether brick fence separately), fence gates, full solid blocks | walls, panes, iron bars |

Practical consequences:

- **Frame pane windows with full blocks.** If the jambs are stairs, slabs or trapdoors, the
  panes stay as posts. Put a log, plank or brick jamb beside the glass.
- **End fence railings on a full-block post** (log, block, pillar), not on a wall block.
- Do not mix fences and walls in one railing run - pick one language per railing.
- Panes and bars are different blocks; a pane window with an iron-bar grille needs a full
  block between them.
- A pane next to leaves, a bottom slab or a stair's open face will always show its post face -
  either change the neighbour to a full block or embrace it as a baluster.

## Cause 4 - the opening is 1 block wide

A single pane in a 1x1 hole has nothing to connect to and *must* render as a post. That is
not a bug. Options:

- Make the opening 2+ wide so panes connect into a sheet.
- Use a full glass block (or tinted glass) for a solid 1x1 window.
- Use a trapdoor, iron bars or a wall block if a post-like look is fine.
- Accept and repeat it deliberately as a slit-window motif (good for castles).

## Wall post vs low profile

Wall blocks render a tall centre post when `up=true`, which happens when something sits above
them or when their connections do not form a straight line. To control it:

- Want the low, flat run? Keep the wall in a straight line with nothing above it.
- Want a post (for balustrades, gate piers, lamp bases)? Put a block, slab, lantern, torch or
  another wall above it, or break the straight line.
- A wall run that alternates post/low without reason looks accidental - make it rhythmic.

## Placement checklist

- [ ] No connection blockstates in any command.
- [ ] F3+A after bulk placement, then re-inspect.
- [ ] Pane and bar jambs are full blocks.
- [ ] Fences terminate on full blocks; no fence-to-wall junctions.
- [ ] No unintentional 1-wide pane openings.
- [ ] Wall posts appear where intended and nowhere else.
- [ ] Chains, lanterns and item frames checked after chunk reload too (they are also prone to
      stale rendering after pasting).
