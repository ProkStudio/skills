---
name: minecraft-organic-shapes
description: Build curved and organic geometry in Minecraft Java 1.21+ - circles, ellipses, cylinders, towers, spheres, domes, onion domes, cones, arches, vaults, tunnels, curved bridges, aqueducts, spiral stairs, winding roads, rivers, lakes, custom trees, rocks, cliffs and statues. Use whenever the user asks for something round, curved, smooth, sloped, "not blocky" or organic, or when a build needs a dome, rotunda, tower cap, arcade, arch, bridge span, terraced hillside or natural landform. Contains verified block-by-block layer tables for circles up to diameter 33, domes and spheres, semicircular arch rises, diagonal line slopes, plus slab and stair smoothing rules, the no-straight-line-over-7 rule for organics, and command/WorldEdit workflows.
version: 1.0.0
---

# Minecraft Organic Shapes

Curves in a cube world are approximations. Good ones come from a deliberate layer table and
consistent smoothing - not from placing blocks "roughly round" and hoping.

**Target:** Java Edition 1.21+. Every table here is computed for vanilla full blocks; slabs
and stairs are used only for smoothing on top of a correct block layer.

**Companion skills:** `../minecraft-architecture/SKILL.md` for massing, palette and roofs;
`../minecraft-interiors/SKILL.md` for what goes inside the dome or rotunda.

## Non-negotiables

1. **Pick the exact diameter/span before placing blocks** and take the layer widths from the
   reference tables. Freehand circles are always lumpy on the second quadrant.
2. **Odd vs even is a design decision.** Odd diameters have a 1x1 centre (a centre axis,
   a keystone, a symmetrical door); even diameters have a 2x2 centre and no true axis.
3. **Build one quarter, then mirror it.** Mirror along both axes; for odd diameters mirror
   along the centre row/column itself, not next to it.
4. **Smoothing comes last.** Get the full-block silhouette right, then add stairs/slabs.
   Never use stairs to fix a wrong layer table.
5. **Organics never run straight for more than ~7 blocks.** Paths, rivers, cliffs, tree
   trunks and shorelines all break their line before block 8.
6. **No gravity blocks** (sand, gravel, concrete powder, anvils) in unsupported curved shells
   while building; place them last or support them.
7. **State the shape spec** in the answer: diameter, height, layer sequence, smoothing rule.
   The user must be able to place it without guessing.

## Step 0 - Ask 1-3 questions

- **What shape, how big** - "dome over an 11-wide room, or a 31-wide cathedral dome?"
- **Placement method** - hand-placed, `/fill` + `/setblock`, or WorldEdit (changes the whole
  delivery format).
- **Precision vs feel** - geometric perfection (dome, rotunda, bridge) or natural irregularity
  (rocks, trees, rivers, cliffs)? These use opposite rule sets.

## Step 1 - Classify the shape

| Family | Examples | Rule set |
| --- | --- | --- |
| Revolved geometry | Cylinder, tower, rotunda, dome, cone, sphere, silo | `references/circles-and-cylinders.md`, `references/domes-and-spheres.md` |
| Extruded curve | Arch, vault, tunnel, bridge, aqueduct, arcade | `references/arches-and-bridges.md` |
| Path in plan | Road, river, shoreline, wall following terrain, terraces | `references/curves-paths-and-rivers.md` |
| Freeform organic | Tree, rock, cliff, root, statue, creature, blob | `references/natural-forms.md` |

Geometric families get exact tables. Organic families get rules of irregularity. Mixing them
up is the most common failure: a "natural" rock built from a perfect sphere, or a dome built
with random noise.

## Step 2 - Lay the control geometry

1. Mark the centre (or the axis for extrusions) with a temporary column of a bright block.
2. Mark the radius/span extremes with 4 (or 8) temporary markers.
3. Build **one quarter** of the shape, or the profile rib for extrusions.
4. Mirror, then delete the markers.

For domes and spheres, build the ribs first (4 or 8 great-circle ribs), then fill between
them layer by layer. The ribs catch errors before you place 2000 blocks.

## Step 3 - Smoothing

- **Stairs** for 1-block steps on a 45-degree run; **slabs** for half-step transitions and
  flatter runs; **full blocks** where two curves meet so panes and walls stay connected.
- Outer shell of a dome: stairs facing outward on every step where the layer diameter drops
  by 2; slabs where it drops by 1 over two layers.
- Never mix stair smoothing and slab smoothing in the same run - pick one per surface.
- Inside a vault, upside-down stairs (`half=top`) give a clean soffit.
- On natural forms, smooth with the same blocks as the mass, not with a new material.

## Step 4 - Structure and detail

Curved shells need visible structure or they read as plastic:

- Domes: ribs, a drum with windows, a cornice at the springline, an oculus or a lantern on top.
- Towers: a base flare, a string course every 4-6 blocks, machicolations or a cornice under
  the cap.
- Arches: voussoirs (alternate two blocks around the arch), a keystone in the accent block,
  an extrados band 1 block out.
- Bridges: piers, spandrel walls, a parapet, drainage/weep holes, wear at the deck edges.

## Step 5 - QA before delivering

- [ ] Layer widths match the table; all four quadrants identical (mirrored, not re-placed).
- [ ] Odd/even centre matches the intended axis, door or keystone position.
- [ ] Silhouette checked from 3 angles plus straight above.
- [ ] Dome keeps its maximum diameter for the first 10-15% of its height (no pancake).
- [ ] Smoothing is consistent; no stair/slab mix on one surface; no floating smoothing blocks.
- [ ] Organic forms: no straight run longer than 7; clusters in 3 sizes; no single lonely prop.
- [ ] Panes/bars/fences/walls framed by full blocks; no explicit connection blockstates written.
- [ ] After bulk placement, chunks reloaded (F3+A) so connections update.
- [ ] Gravity blocks supported.

## Delivery format

- **Hand-placed:** the layer table as a list ("y+0 to y+3: d=21 ring; y+4: d=19 ..."), the
  quarter-arc description, the marker workflow, then smoothing and detail passes.
- **Commands:** `/fill` per ring segment or per layer; give the exact coordinates relative to a
  stated centre, and the stair `facing=`/`half=` states. For spheres/cylinders prefer WorldEdit.
- **WorldEdit:** `//cyl`, `//hcyl`, `//sphere`, `//hsphere`, `//pyramid`, `//curve` (with
  `//sel convex`), `//cone` via generate; `//g` for formula shapes such as a torus or an
  ellipsoid: `//g stone (x^2+z^2)^0.5 ...`. Always say what selection the command needs and
  warn that bulk edits skip block updates.

End with 2-3 variation levers ("drop to d=17 and add a drum", "switch the semicircular arch
for a pointed one to gain 3 blocks of height").

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "My circle has flat sides" | Wrong layer table or freehand placement | Use the table in `references/circles-and-cylinders.md`; mirror a quarter |
| "Dome looks like a pancake" | Layers shrink linearly from the start | Keep max diameter for the first 10-15% of height (`references/domes-and-spheres.md`) |
| "Dome looks like a cone" | Constant -2 per layer | Use the computed layer sequence; steps get bigger near the crown |
| "Arch looks pointy/squashed" | Rise not matched to span | Use the arch rise table; a semicircular arch rises span/2 |
| "Bridge looks flat and thin" | No spandrel, no pier rhythm, deck 1 thick | Piers every 1-1.5x span, deck 2-3 thick with a parapet |
| "Path looks like a snake made of diagonals" | Uniform 1:1 stepping | Mixed run lengths, curve radius 5-9, never >7 straight |
| "Rock/tree looks like a sphere/lollipop" | Geometric rules applied to organics | `references/natural-forms.md` - 3-size clusters, asymmetry, taper |
| "Statue looks deformed from the ground" | No silhouette pass, wrong scale | Build the outline first, scale 15+ blocks, check from eye level |

## References

| File | Read it when |
| --- | --- |
| `references/circles-and-cylinders.md` | Any circle, ring, tower, rotunda, cone, ellipse |
| `references/domes-and-spheres.md` | Domes, spheres, onion/lantern caps, planetariums |
| `references/arches-and-bridges.md` | Arches, arcades, vaults, tunnels, bridges, aqueducts |
| `references/curves-paths-and-rivers.md` | Roads, paths, rivers, shorelines, terraces, walls on terrain |
| `references/natural-forms.md` | Trees, rocks, cliffs, caves, statues, creatures |
