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
```

Add further Minecraft skills as sibling folders (`redstone/`, `terraforming/`, ...).
Each skill folder must contain a `SKILL.md` whose frontmatter `name` matches the folder
name. Validate with:

```bash
python scripts/validate_skills.py
```
