# Colour, value and texture noise

Value (brightness) carries a build; hue only flavours it. Pick the light/mid/dark split first.

## Value ladders

### Greys, light to dark

white concrete -> snow block -> quartz block -> diorite -> polished diorite -> white terracotta
-> smooth stone -> stone -> light gray concrete -> andesite -> polished andesite -> cobblestone
-> tuff (1.21) -> gray concrete -> cobbled deepslate -> deepslate -> polished deepslate ->
deepslate bricks -> deepslate tiles -> blackstone -> polished basalt -> black concrete ->
obsidian

### Warm browns and tans, light to dark

smooth sandstone -> sandstone -> birch planks -> oak planks -> packed mud -> mud bricks ->
stripped spruce -> brown terracotta -> granite -> bricks -> spruce planks -> dark oak planks ->
soul soil -> dark oak log

### Warm whites vs cool whites

- Warm: calcite, bone block, smooth quartz, white terracotta, birch planks, sandstone
- Cool: white concrete, snow block, quartz block, diorite, white glazed terracotta

Mixing warm and cool whites in one surface is the most common reason a "white build" looks
dirty. Pick one temperature.

## Hue groups

| Hue | Blocks | Use |
| --- | --- | --- |
| Red | bricks, red nether bricks, red terracotta, granite, crimson planks, copper (unoxidized), resin bricks (1.21.4) | Warm accents, roofs, industrial |
| Orange / tan | acacia, orange terracotta, sandstone, packed mud, honeycomb block, resin bricks | Desert, autumn, warm masonry |
| Yellow | bamboo planks, birch, yellow terracotta, ochre froglight, hay | Highlights, thatch |
| Green | moss block, green terracotta, prismarine, warped planks, verdant froglight, oxidized copper | Nature, patina, temples |
| Blue | lapis, blue terracotta, blue concrete, prismarine bricks, dark prismarine, warped (teal) | Water, magic, cool accents |
| Purple | purpur, amethyst, purple terracotta, cherry log, crimson | End, arcane, fantasy |
| Pink / pastel | cherry planks, pink terracotta, calcite + quartz, pink petals (1.20), pale oak (1.21.4) | Cottagecore, spring, fairy |
| Black | deepslate tiles, blackstone, polished basalt, black concrete, obsidian, sculk | Roofs, contrast, void themes |

Keep saturated blocks (concrete, glazed terracotta, red nether bricks, prismarine) under 10% of
the surface. Terracotta is the safe middle ground: muted, 16 hues, matches stone.

## Texture noise levels

| Noise | Blocks | Behaviour |
| --- | --- | --- |
| High | cobblestone, gravel, granite, andesite, tuff, deepslate, calcite, blackstone, mossy variants | Reads busy; great at ground level and in ruins, mush at distance |
| Medium | stone bricks, deepslate bricks/tiles, bricks, mud bricks, resin bricks, sandstone, planks | The workhorse tier |
| Low / flat | concrete, smooth stone, smooth quartz, terracotta, bone block, smooth sandstone | Modern, clean, large surfaces |
| Patterned | glazed terracotta, chiseled variants, purpur pillar, bookshelves, quartz bricks, copper grate (1.21) | Accent only, 1-5% |

Rule: **at most one high-noise block per surface**, and never three flat blocks together in a
rustic style.

## Biome light changes everything

Grass colour and fog tint the whole build:

| Biome | Effect | Adjust |
| --- | --- | --- |
| Plains / forest | Neutral green | Anything works |
| Snowy | Blue-white bounce, high contrast | Warm woods and warm whites, avoid grey-on-grey |
| Desert / badlands | Yellow-orange glare | Cool greys and dark accents read well; avoid tan-on-tan |
| Swamp / jungle | Green-grey murk | Light bases, warm light sources, avoid green blocks |
| Cherry grove | Pink ambience | Calcite, pale oak, dark accents; avoid pink blocks |
| Nether | Red gloom | Cool blues, warm whites, soul lanterns; almost nothing reads dark |
| End | Purple-black void | Quartz, purpur, end stone, light sources at 3x normal density |
| Deep dark / underground | No skylight | Value hierarchy must come from light placement, not block choice |

## Testing a palette

1. Place a 5x5x5 test cube of each tier next to each other before committing.
2. Look from 40+ blocks away - if the tiers merge, the values are too close.
3. Look at night and in rain.
4. Imagine it in grayscale: three distinguishable steps or redo it.
5. Count materials per wall - more than 3-4 is almost always too many.
