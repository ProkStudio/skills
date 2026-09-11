# Timeline: 1.20 - 1.21.11

This era is where "game drops" replaced one big yearly update, so the useful unit is the
drop, not the major version.

## 1.20 - Trails & Tales (June 2023)

- **Cherry**: cherry log, wood, stripped variants, planks and the full plank set, cherry
  leaves, cherry sapling, pink petals. The only pink wood in the game.
- **Bamboo**: block of bamboo, stripped block of bamboo, bamboo planks, bamboo mosaic
  (stairs and slab only for mosaic), plus the full plank set and bamboo raft.
- **Chiseled bookshelf** - six slots, each individually filled, readable by a comparator.
  It uses `facing` plus per-slot occupancy states, so place it by hand rather than by
  command.
- **Hanging signs** for every wood, including the chained and wall-mounted forms.
- **Decorated pots** and the sherd system; suspicious sand and suspicious gravel.
- Calibrated sculk sensor, piglin head, torchflower, pitcher plant.

### 1.20.2

- Data pack format 18. Packs gained `supported_formats` (a declared range) and **overlay
  directories**, which is the correct way to ship one pack for several versions.
- Function macros.

### 1.20.5 - Armored Paws (April 2024)

- **Item NBT was replaced by the data component system** in commands and data packs.
  Entity NBT was not affected. Any `give`, `item` or loot-table snippet older than this
  needs rewriting.
- Armadillo, wolf armour, wolf variants.

## 1.21 - Tricky Trials (June 2024)

The biggest palette addition since 1.17.

- **Tuff family**: tuff stairs, slab and wall, polished tuff and its set, tuff bricks and
  their set, chiseled tuff. Tuff went from one block to a full masonry family.
- **Copper expansion**: chiseled copper, copper grate, copper door, copper trapdoor and
  copper bulb - each with four oxidation stages and waxed twins, which is roughly 32 new
  blocks. The bulb is a light that toggles and holds its state on a redstone pulse.
- **Crafter** - the first vanilla auto-crafting block, comparator-readable.
- Trial spawner, vault, heavy core, trial chambers structure, ominous bottle, mace.
- Breeze and bogged mobs; wind charges, which interact with blocks and can trigger
  pressure plates and buttons.

### 1.21.2 / 1.21.3 - Bundles of Bravery (October 2024)

- Bundles in all 16 colours.

### 1.21.4 - The Garden Awakens (December 2024)

- **Pale oak**: log, wood, stripped variants, planks and the full plank set, pale oak
  leaves, pale hanging moss, plus the pale garden biome. The whitest wood available.
- **Creaking and creaking heart** - the creaking heart is immovable by pistons.
- **Resin**: resin clump, block of resin, resin bricks with stairs, slab and wall, chiseled
  resin bricks. A strong orange masonry family.
- Eyeblossom.

### 1.21.5 - Spring to Life (March 2025)

Small blocks that carry a lot of ground-level detail:

- Leaf litter, wildflowers, bush, firefly bush, short dry grass, tall dry grass, cactus
  flower, fallen trees in world generation.
- Pig, cow and chicken variants.

### 1.21.6 - Chase the Skies (June 2025)

- Happy ghast, ghastling, harness items, **dried ghast block**, locator bar.

### 1.21.7 and 1.21.8 (June and July 2025)

- Maintenance releases. No builder-relevant additions.

### 1.21.9 - The Copper Age (September 2025)

- **Copper chest** - a second chest family, and **shelf**, a flat display and storage block
  that a comparator can read.
- **Copper golem** plus copper golem statues in several poses and oxidation stages.
- Copper chains, copper lanterns, mannequins.
- Check the wiki for the complete copper list before quoting it; this drop added a lot of
  near-duplicate variants.

### 1.21.10 (October 2025)

- Pure hotfix release for 1.21.9: piston and cobweb item clipping, wind charge collisions,
  chunk loading during teleports. Data pack format 88.0, resource pack 69.0, minimum
  Java 21.

### 1.21.11 - Mounts of Mayhem (December 2025)

The last release of the `1.x` line. Bedrock counterpart 1.21.130.

- Nautilus and zombie nautilus, nautilus armour, camel husk, parched, zombie horses spawn
  naturally, netherite horse armour, spear weapons.
- **Rendering work that matters for showcasing builds**: mipmaps now apply to all blocks
  including rails, vines and foliage; graphics presets; texture filtering and anisotropic
  filtering options; a see-through-leaves toggle with a real performance gain; underwater
  fog blended between biomes; nether fog no longer tied to render distance; sunrise and
  sunset colours affected by rain and thunder.
- Resource pack formats 70.0-75.0: item textures were split out of the block atlas into a
  separate items atlas, so resource packs from earlier versions need reorganising.

## Mechanics state at the end of 1.21.11

- Height `-64` to `320`; spawn-proofing target light 1.
- Copper is a full palette family with doors, grates, bulbs, chests, lanterns and chains.
- Wool and concrete still have **no** stairs or slabs - that arrives in 26.3.
- Minimum Java runtime is 21. From 26.1 it becomes 25.
