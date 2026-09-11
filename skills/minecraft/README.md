# Minecraft skills

Original skills for Minecraft work (not vendored from an upstream repo, so they are
intentionally absent from `catalog.json` / the root README tables, which are generated
from vendored sources).

## Layout

```
skills/minecraft/
  building/            # design & construction skills
    minecraft-architecture/
      SKILL.md
      references/      # deep-dive principles, read on demand
      styles/          # one file per architectural style (19)
    minecraft-block-palettes/
      SKILL.md
      references/
    minecraft-interiors/
      SKILL.md
      references/
    minecraft-organic-shapes/
      SKILL.md
      references/
    minecraft-settlements/
      SKILL.md
      references/
  terraforming/        # the land the build sits in
    minecraft-terraforming/
      SKILL.md
      references/
  redstone/            # mechanisms that serve architecture
    minecraft-redstone-for-builders/
      SKILL.md
      references/
  versions/            # what exists in which version, and how to move a build
    minecraft-version-history/
      SKILL.md
      references/
```

## Building skills

| Skill | Use it for |
| --- | --- |
| `building/minecraft-architecture` | A single building: massing, silhouette, facade depth, roofs, palette, terrain integration, variation, per-style guides (19 styles) |
| `building/minecraft-block-palettes` | The blocks themselves: block families and which variants exist, version gates, colour and value theory, 18 ready palettes, special block behaviour |
| `building/minecraft-interiors` | Everything inside the walls: room program, ceiling heights, floor/wall/ceiling tiers, furniture recipes, lighting and light levels, interiors by build type |
| `building/minecraft-organic-shapes` | Curves and geometry: circles, cylinders, towers, domes, spheres, arches, vaults, bridges, winding roads and rivers, trees, rocks, cliffs, statues (includes computed layer tables) |
| `building/minecraft-settlements` | More than one building: centre-first layout, road hierarchy, districts and zoning ratios, plot subdivision, building mix, ageing and signs of life |

### Styles available

`medieval-fantasy`, `japanese`, `modern-minimal`, `nordic-rustic`, `steampunk-industrial`,
`gothic`, `classical-antiquity`, `egyptian`, `mesoamerican`, `dwarven-underground`,
`sci-fi-futuristic`, `cottagecore`, `mediterranean`, `moorish-islamic`, `chinese-imperial`,
`art-deco`, `brutalist`, `western-frontier`, `elven-natural`.

## Other categories

| Skill | Use it for |
| --- | --- |
| `terraforming/minecraft-terraforming` | The site: mountains, cliffs, valleys, erosion and scree, rivers, lakes, coasts, biome blending, planting, WorldEdit/FAWE brush workflow |
| `redstone/minecraft-redstone-for-builders` | Mechanisms inside a build: hidden and piston doors, switched and automatic lighting, elevators, drawbridges, gates, portcullises, item sorters and hidden storage |
| `versions/minecraft-version-history` | What changed in each version from 1.13 to 1.21.11 and the 2026 drops (26.1, 26.2, 26.3), block substitutions for older targets, pack formats, Java runtime requirements, world and schematic migration |

They are designed to compose: terraforming shapes the land, architecture builds the shell,
block palettes choose the materials, organic shapes handles anything curved, interiors
furnish it, redstone makes it move, settlements plans the town that contains them, and
version history keeps all of it inside the block set the player actually has. Each skill
cross-references the others where the handover happens.

Add further Minecraft skills as sibling folders (`commands/`, `tooling/`, ...).
Each skill folder must contain a `SKILL.md` whose frontmatter `name` matches the folder
name. Validate with:

```bash
python scripts/validate_skills.py
```
