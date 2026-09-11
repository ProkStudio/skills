# Storage, sorters and shop mechanics

The goal is a storage room that looks like part of the build - a cellar, a warehouse, a shop
back room - with the machinery under the floor or behind the wall.

## Hopper rules that decide every design

- A hopper moves items **down**, or sideways into the container it faces.
- A hopper pulls items from a container directly above it, and picks up items lying on top.
- Transfer rate: 1 item every 4 game ticks (2.5 items/second) per hopper.
- A hopper is **locked** while it receives a redstone signal - the basis of every filter.
- Hoppers only insert an item into a slot that is empty or already holds the same item type.
  This is the whole trick behind item sorters.
- Chests, barrels, hoppers and shelves cannot be moved by pistons - never route a piston through
  a storage wall.

## The standard item sorter

One module per item type, tileable side by side:

1. An item line of hoppers runs along the top, feeding each module.
2. Each module has a **filter hopper** pointing down into an output hopper, which points into the
   chest or barrel below.
3. The filter hopper is preloaded so that only the target item can enter it:
   - slot 1: **41 of the target item**
   - slots 2-5: one **uniquely named or unstackable** filler item each (so nothing else fits)
4. A comparator reads the filter hopper. At rest the signal is low; when one more matching item
   arrives, the signal rises one step and, through a redstone torch, **unlocks** the output
   hopper so the surplus drops into the chest.
5. Items that match nothing travel to the end of the line and into an overflow chest.

Why 41: the count is chosen so the comparator sits just below the threshold at rest and crosses
it when a single extra item arrives. If a design in a tutorial uses a different number, keep the
tutorial's number - the principle matters, not the constant.

**Overflow protection** is mandatory: end the item line in a large overflow chest, or a
lava/cactus disposal for genuinely worthless drops. A sorter with nowhere to overflow backs up
and jams the whole line.

Limitations to state up front: items with durability, names, enchantments or potion data do not
sort cleanly. Use an unstackable filter (an input hopper that only unlocks on an unstackable
item) to split tools and armour off first.

## Hiding a storage system in a build

| Approach | How |
| --- | --- |
| Cellar warehouse | Sorter machinery in a 2-block void under a wooden cellar floor; the chests read as crates against the walls |
| Shop back room | Counter with trapped chests in front, hopper lines through the wall into the sorter behind |
| Library archive | Chest wall dressed with barrels, bookshelves and chiseled bookshelves (1.20+), hopper line in the ceiling void |
| Dwarven vault | Copper chests (1.21.9+) and barrels in stone niches, hoppers behind the niche wall |
| Farm silo | Hoppers under a harvest floor into barrels dressed as grain bins |

Presentation rules:

- Face chests and barrels so their fronts align; alternate barrels and chests to break the grid.
- Frame the storage wall with pilasters or timber posts every 3-5 blocks so it reads as joinery
  rather than a chest dump.
- Label with signs, hanging signs (1.20+), item frames, or shelves (1.21.9+) - shelves display
  items without an entity, so prefer them when the version allows.
- Leave a 2-block-wide walkway in front; storage rooms with no circulation always look wrong.

## Shop and display mechanics

- **Trapped chest tell:** a trapped chest in a shop counter can light a lamp in the back room
  when a customer opens it.
- **Vending machine:** a dispenser fed by a hopper, triggered by a button, with a trapped chest
  or an item frame showing the price. Keep the mechanism behind the counter.
- **Item display:** item frames (entity cost) or shelves (1.21.9+, comparator-readable and
  entity-free). Glow item frames read better in dim shops.
- **Auto-restock display:** hopper feeding a dropper into a display chest; only worth it in a
  server shop.
- **Museum vitrine:** armor stand or mannequin (1.21.9+) behind glass, with a lamp recessed
  under the plinth and a button to light it.

## Automatic doors and conveniences for storage rooms

- Pressure plate at the cellar stair bottom lighting the whole room (lever override at the top).
- Hopper minecart under the floor as a moving collection line for large rooms - hide the rail in
  a service trench with trapdoor covers.
- Furnace array (blast furnaces and smokers in a bank) fed by hoppers from a fuel barrel; dress
  the bank as a kitchen range or a smelter.

## Sizing guidance

| Storage need | Build |
| --- | --- |
| One player, early survival | 8-16 barrels/chests, no sorter, a labelled wall |
| One player, established | 20-40 chests, 10-20 sorter modules, cellar void |
| Shared base / server | Double-chest bank with 30+ modules, overflow chest, separate unstackable filter |
| Shop | 4-8 display chests front, sorter and bulk storage behind |

A sorter module costs roughly 3 hoppers, 1 comparator, 1 redstone torch, 1 chest and the filter
items. Give the user the total for the module count they need, and remind them that 41 of every
sorted item must be found before the system works.
