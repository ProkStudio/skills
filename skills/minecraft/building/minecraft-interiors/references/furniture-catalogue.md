# Furniture catalogue

Notation: `block A + block B` means combine; `(facing X)` means the block state matters.
Every prop below is 2-5 blocks - single-block "furniture" is what makes interiors look fake.
Version-gated blocks are marked.

## Seating

- **Chair:** stairs (facing the table) + wall sign on each side as armrests; hanging sign
  behind as a tall back (1.20+).
- **Stool:** fence post + carpet on top, or a single mud brick wall block + trapdoor lid.
- **Bench:** 2-4 stairs in a row + signs at both ends; or slab on two fence posts.
- **Sofa:** 3 stairs + wall signs as arms, carpet in front as a rug, trapdoor "cushion" trick:
  place trapdoors on the sides of the stairs.
- **Armchair:** stairs + 2 signs + a banner behind for a high back.
- **Booth (tavern):** two benches facing each other with a table between, separated by a
  plank+trapdoor partition.
- **Sittable:** boats and minecarts on rails actually seat the player - use for cinema rows,
  boats in baths, carts in mines (entity cost applies).

## Tables and desks

- **Small table:** fence post + carpet, or fence post + pressure plate.
- **Round table:** 4 fence posts + 4 trapdoors around a central block + carpet.
- **Dining table:** stripped logs in a row with trapdoors along both sides, or a row of
  blocks with slabs on top for an overhanging top.
- **Long hall table:** 2x6 blocks with stair ends, white carpet runner, item frames as plates,
  candles down the middle.
- **Desk:** barrel + block + trapdoor top; add a lectern for the "open book", an item frame
  with a map, a quill look with an armor stand holding a feather (1.19+ for pose control).
- **Workbench cluster:** crafting table + smithing table + fletching table + cartography
  table in a row, unified by a slab top overhang and a tool wall above.

## Storage

- **Cupboard:** barrel + trapdoor "door" on the front; two barrels stacked with a shared
  trapdoor pair reads as a wardrobe.
- **Kitchen counter:** run of barrels/smokers/blast furnaces with trapdoors over the fronts and
  a slab or full-block worktop; cauldron or hopper as the sink.
- **Dresser:** 2 blocks + 2 trapdoors + item frame handles; flower pot and candle on top.
- **Shelves:** the shelf block holds three displayed items (Copper Age drop, version-gated);
  otherwise slabs on trapdoor brackets, or chiseled bookshelves (1.20+) for filled/empty mixes.
- **Crates:** barrels with the top facing out, stacked irregularly, some with trapdoor lids,
  item frames showing contents.
- **Storage hall:** rows of barrels/chests with item frames as labels above and hoppers
  feeding a sorter behind a false wall; keep access unblocked.
- **Copper chest** (Copper Age drop) oxidizes - a free aging effect in old cellars.

## Beds and bedrooms

- **Bed dressing:** bed + hanging sign or stair footboard + banner headboard + carpet runner.
- **Four-poster:** 4 fence posts at the bed corners, trapdoors or slabs as the canopy frame,
  wool/banner curtains on 2-3 sides.
- **Bunk bed:** lower bed + slab ceiling + upper bed on the slabs, ladder at one end.
- **Nightstand:** decorated pot (1.20) or barrel + candle/lantern + flower pot.
- **Wardrobe:** 2x2 of planks with iron trapdoor or dark oak trapdoor doors + item frames with
  armor pieces inside; armor stand beside it as a dressing mannequin.

## Kitchen and bathroom

- **Stove:** blast furnace or smoker inset in the counter; hopper above as a hood, campfire in
  a stone recess for open fire, chain + lantern over it.
- **Sink:** cauldron (empty or with water) or hopper sunk into a slab counter; item frame with
  a blue item, or a lever/button, as the tap.
- **Fridge:** iron block/copper block column + iron trapdoor front + item frame handle;
  barrel behind it if you want it functional.
- **Pantry:** barrels + item frames with food, chiseled bookshelf jars look, decorated pots,
  hanging melon/hay for texture.
- **Bathtub:** 2x1 quartz/white concrete frame with a cauldron or water source; soul sand
  under water gives bubbles; boat inside to sit in it.
- **Shower:** water source above a trapdoor grate, or a cauldron + chain + trapdoor head.
- **Toilet:** cauldron + trapdoor lid + button flush.
- **Mirror:** item frame with a map, glass pane with a light source behind, or smooth quartz
  framed with trapdoors.

## Fireplaces and focal points

- **Hearth:** 3-5 wide recess in the wall, stone/bricks surround, campfire or fire on
  netherrack inside, chimney breast above with a slab mantel, andirons from iron bars.
- **Mantel dressing:** candles, flower pots, item frames, a painting above, sword on the wall
  (item frame), logs stacked beside it in a barrel.
- **Forge (smithy):** blast furnace + anvil + lava behind iron bars, tool wall in item frames,
  water cauldron for quenching, soot texture with basalt/blackstone gradient.
- **Bar (tavern):** counter run with trapdoor front panels, barrels behind, bottles from
  potions in item frames, chiseled bookshelf as the bottle rack, chains and lanterns above.
- **Altar (temple):** raised 2-3 step plinth, enchanting table or lodestone as the object,
  candles in odd numbers, banners flanking, light from above.

## Plants, textiles, clutter

- **Plants:** flower pots (on blocks, on slabs, hanging on trapdoor brackets), decorated pots
  (1.20), big dripleaf as a broad-leaf plant, azalea/flowering azalea, hanging vines and glow
  berries (light 14), moss carpet for overgrowth.
- **Rugs:** carpets in 2-3 colours, bordered by a darker carpet ring; wool under a slab edge
  for a thicker look.
- **Curtains and drapes:** banners (the pattern system lets you match the palette), wool
  columns with trapdoor rods.
- **Clutter:** item frames with tools/food/potions, glow item frames for emphasis, books on
  lecterns, candles in groups of 1/3/4, armor stands with items, cauldron with water, hay and
  crates, anvils, decorated pots, amethyst clusters, sea pickles, copper grate vents (1.21).

## Entity budget

Item frames, glow item frames, armor stands, paintings (block-like but still entities in
Java), boats and minecarts are entities. On servers keep decorative entities to a few dozen
per room and prefer block-based detail; in single-player showcase builds spend freely.

## Rules of thumb

- Props in groups of 3 with mixed heights (tall / mid / low).
- Every prop needs support: no floating slabs, no chairs without a table, no lamp without a
  surface or bracket.
- Rotate: chairs face the table, beds face the room, counters face the walkway.
- Do not reuse the same prop cluster in two rooms of the same build.
- Use the accent tier of the palette for fabric and small props - that is where colour belongs.
