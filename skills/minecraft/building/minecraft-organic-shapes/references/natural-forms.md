# Trees, rocks, cliffs, statues

Organic forms follow rules of irregularity, not tables. Three principles cover almost
everything:

1. **Three sizes.** Any cluster (rocks, bushes, leaf clumps, boulders) has a dominant element,
   a medium one and small debris. Never two elements of equal size next to each other.
2. **Taper and asymmetry.** Nothing organic is symmetrical or of constant thickness; trunks,
   branches, cliffs and roots all taper and lean.
3. **Never a lonely object.** Vegetation and rocks appear in groups of 3+; a single tree or a
   single boulder in the open reads as placed by a player, unless that is the point (a
   landmark oak, a standing stone).

## Custom trees

Vanilla-generated trees are sticks with a tuft - build your own for anything showcased.

- **Trunk:** 2x2 for a 12-20 block tree, 3x3 or a 5-block irregular blob for an ancient tree,
  1x1 only for saplings and birches under 10 blocks. Taper: lose 1 block of section every
  6-10 blocks of height.
- **Flare and roots:** widen the base by 1-2 blocks for the bottom 2-3 layers, then send 4-8
  roots outward: logs stepping down 1 per 1-2 blocks, ending in coarse dirt or podzol, some
  roots over a rock.
- **Branches:** start above 1/3 of the height, 4-8 primary branches, each stepping 1 up per
  1-2 out (a 2:1 or 1:1 slope), thinning from 2x2 to 1x1, curving - never straight to the tip.
  Use the log axis states (`axis=x/y/z`) so the bark direction follows the branch.
- **Crown:** leaf clumps, not a leaf ball. Each primary branch gets its own clump of 5-9 blocks
  in an irregular blob; leave gaps so light comes through; hollow out the interior (the crown
  should be a shell 2-3 blocks thick).
- **Silhouette:** the crown outline needs bumps of 2-4 blocks; draw it against the sky before
  filling. Wider than tall for oaks, narrow and tall for conifers.
- **Mix:** 2-3 leaf types for one species (oak + azalea, spruce + mangrove), plus vines, glow
  berries, moss carpet under the canopy, and mushrooms on the north side.
- **Conifers:** central 1x1 or 2x2 trunk, branch whorls every 2-3 blocks getting shorter
  upward, leaves hugging the trunk, bare lower trunk.
- **Mangrove / swamp:** stilt roots from 2-3 blocks up, water below, hanging propagules, moss.
- **Giant/fantasy tree:** trunk 7-15 wide with buttress roots, branch as a building structure
  (walkable), stairs and platforms integrated; scale the crown to at least 2x the trunk height.

## Rocks and boulders

- Build from an irregular blob, not a sphere: 3 overlapping masses of different sizes, then
  carve bites out of the silhouette.
- Gradient of 3-4 blocks (stone + andesite + cobbled deepslate + tuff), patched irregularly,
  darker at the base and in crevices, lighter on the top faces.
- Skirt the base with gravel/coarse dirt/moss so the rock is planted, never sitting on a flat
  line of grass.
- Clusters: one dominant boulder, one medium, 2-4 small; align their long axes roughly the
  same way, as if they broke off the same outcrop.
- Smooth with stairs and slabs only where a face wants a flatter plane; keep the outline blocky
  and chaotic.

## Cliffs and mountains

- **Strata:** horizontal bands of 2-5 blocks of different stone, offset in plan. Strata are what
  separate a cliff from a wall of stone.
- **Profile:** alternate steep faces (near vertical) with ledges of 2-5 blocks; add at least one
  overhang per 20 blocks of cliff.
- **Scree:** a talus slope at the base - gravel and cobble, thinning upward, at roughly a 1:2
  slope, with the biggest blocks at the bottom.
- **Erosion:** vertical gullies every 10-20 blocks, water stains (darker blocks) below them,
  cracks and caves at the base.
- **Vegetation line:** grass and moss on the ledges, azalea and vines on the wet side, bare
  rock on the windward faces; nothing growing on a vertical face except vines.
- Never let a cliff top meet the flat ground in a single straight edge - roll it over with
  2-4 blocks of transition.

## Caves and overhangs

- Wide-narrow-wide rhythm along the passage; never a constant cross-section.
- Floor debris: pointed dripstone, gravel piles, fallen blocks, water pools.
- Support the ceiling visually with columns of dripstone or stone; light with glow lichen,
  amethyst, magma and hidden sources.

## Statues and creatures

- **Scale:** below 10 blocks a humanoid statue cannot read - aim for 15-25 for a monument,
  30-60 for a colossus. Heads are 1/6 to 1/7 of the height for realism, 1/4 for a stylised look.
- **Workflow:** silhouette -> skeleton -> volumes -> surface -> detail.
  1. Draw the outline in a single cheap block from the main viewing angle.
  2. Build a centreline skeleton (spine, limbs) with logs, keeping the pose readable.
  3. Wrap volumes: limbs as tapering 3x3 to 5x5 masses, torso as a barrel, no flat slabs.
  4. Surface with stairs and slabs for muscles, cloth folds and armour plates.
  5. Detail the face last and check it from the ground - eyes read best as recessed dark blocks.
- **Pose:** contrapposto (weight on one leg, shoulders counter-rotated) beats a T-pose; give
  the figure a 1-2 block lean so it is not a column.
- **Support:** cloaks, wings, weapons and rocks hide the fact that thin ankles cannot hold a
  colossus visually; put the statue on a plinth 2-4 blocks tall.
- **Symmetry check:** mirror the finished half with WorldEdit (`//copy`, `//flip`, `//paste`)
  rather than hand-building both sides, then break the symmetry deliberately (one arm raised,
  cloak to one side).
- **Creatures:** build the skeleton to the real animal proportions first; the most common error
  is a head 2x too small and legs 2x too thick.

## Gradients and blending

- Any material transition needs 3 steps: A -> A+B patches -> B. One block of mixing is not a
  gradient.
- Vignette: darker blocks in crevices and at the base of masses, lighter on exposed top faces -
  this fake ambient occlusion is what makes organic builds look sculpted.
- Foliage transitions: grass -> grass with moss -> moss carpet -> podzol/coarse dirt as you go
  under a canopy.
