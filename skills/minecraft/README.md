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
      styles/          # one file per architectural style
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
```

## Building skills

| Skill | Use it for |
| --- | --- |
| `building/minecraft-architecture` | A single building: massing, silhouette, facade depth, roofs, palette, terrain integration, variation, per-style guides (11 styles) |
| `building/minecraft-block-palettes` | The blocks themselves: block families and which variants exist, version gates (1.20-1.21.9), colour and value theory, 18 ready palettes, special block behaviour |
| `building/minecraft-interiors` | Everything inside the walls: room program, ceiling heights, floor/wall/ceiling tiers, furniture recipes, lighting and light levels, interiors by build type |
| `building/minecraft-organic-shapes` | Curves and geometry: circles, cylinders, towers, domes, spheres, arches, vaults, bridges, winding roads and rivers, trees, rocks, cliffs, statues (includes computed layer tables) |
| `building/minecraft-settlements` | More than one building: centre-first layout, road hierarchy, districts and zoning ratios, plot subdivision, building mix, ageing and signs of life |

## Other categories

| Skill | Use it for |
| --- | --- |
| `terraforming/minecraft-terraforming` | The site: mountains, cliffs, valleys, erosion and scree, rivers, lakes, coasts, biome blending, planting, WorldEdit/FAWE brush workflow |
| `redstone/minecraft-redstone-for-builders` | Mechanisms inside a build: hidden and piston doors, switched and automatic lighting, elevators, drawbridges, gates, portcullises, item sorters and hidden storage |

They are designed to compose: terraforming shapes the land, architecture builds the shell,
block palettes choose the materials, organic shapes handles anything curved, interiors
furnish it, redstone makes it move, settlements plans the town that contains them. Each
skill cross-references the others where the handover happens.

Add further Minecraft skills as sibling folders (`commands/`, `tooling/`, ...).
Each skill folder must contain a `SKILL.md` whose frontmatter `name` matches the folder
name. Validate with:

```bash
python scripts/validate_skills.py
```
