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
    minecraft-interiors/
      SKILL.md
      references/
    minecraft-organic-shapes/
      SKILL.md
      references/
    minecraft-settlements/
      SKILL.md
      references/
```

## Building skills

| Skill | Use it for |
| --- | --- |
| `building/minecraft-architecture` | A single building: massing, silhouette, facade depth, roofs, palette, terrain integration, variation, per-style guides |
| `building/minecraft-interiors` | Everything inside the walls: room program, ceiling heights, floor/wall/ceiling tiers, furniture recipes, lighting and light levels, interiors by build type |
| `building/minecraft-organic-shapes` | Curves and geometry: circles, cylinders, towers, domes, spheres, arches, vaults, bridges, winding roads and rivers, trees, rocks, cliffs, statues (includes computed layer tables) |
| `building/minecraft-settlements` | More than one building: centre-first layout, road hierarchy, districts and zoning ratios, plot subdivision, building mix, ageing and signs of life |

They are designed to compose: architecture builds the shell, interiors furnish it, organic
shapes handles anything curved, settlements plans the town that contains them. Each skill
cross-references the others where the handover happens.

Add further Minecraft skills as sibling folders (`redstone/`, `terraforming/`, ...).
Each skill folder must contain a `SKILL.md` whose frontmatter `name` matches the folder
name. Validate with:

```bash
python scripts/validate_skills.py
```
