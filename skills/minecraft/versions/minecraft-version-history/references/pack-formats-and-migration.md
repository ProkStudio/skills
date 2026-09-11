# Pack formats, runtimes and migration

## Data pack formats (verified anchors)

| `pack_format` | Java versions | Notable change |
| --- | --- | --- |
| 4 | 1.13 - 1.14.4 | Data packs introduced |
| 5 | 1.15 - 1.16.1 | Predicates |
| 6 | 1.16.2 - 1.16.5 | Experimental custom world generation |
| 7 | 1.17 - 1.17.1 | `/replaceitem` replaced by `/item`; loot tables need `type` fields |
| 8 | 1.18 - 1.18.1 | Loot table `type` field required; scoreboard name limits removed |
| 9 | 1.18.2 | `/locate` takes a configured structure, so grouped structures need a tag (`/locate #village`) |
| 10 | 1.19 - 1.19.3 | - |
| 12 | 1.19.4 | - |
| 15 | 1.20 - 1.20.1 | - |
| 18 | 1.20.2 | `supported_formats` range and overlay directories added; function macros |
| 88.0 | 1.21.10 | Format numbering moved to `major.minor` |
| 106.1 | 26.2 | - |

Between 1.20.2 and 1.21.x the number changes almost every release, and from 1.21.9 onward it
is a decimal. **Do not memorise or guess it** - look up the exact value for the target
version on the wiki's Pack format page, and prefer declaring a range:

- `supported_formats` (1.20.2+) declares the range a pack supports.
- **Overlay directories** (1.20.2+) let one pack ship different files per format range. This
  is the correct answer to "how do I support 1.20 through 26.3 with one pack".
- Resource packs have their own separate numbering. Two breaking ones: formats 70.0-75.0
  (1.21.11) split item textures out of the block atlas, and format 88.0 (26.2) renamed
  `quartz_pillar.png` and `purpur_pillar.png` with a `_side` suffix.

## Java runtime requirements

| Versions | Minimum Java |
| --- | --- |
| 1.18 - 1.20.4 | Java 17 |
| 1.20.5 - 1.21.11 | Java 21 |
| 26.1 and later | **Java 25** |

A server or launcher profile that ran 1.21.x will fail to start 26.x until the runtime is
upgraded. This is the single most common 2026 migration failure, and the error message is
usually an unhelpful class version exception.

## Moving a world forward

1. **Back up the save folder** before opening it in a newer version. There is no undo.
2. Opening a world in a newer version converts it permanently. Old chunks keep their
   terrain, so a pre-1.18 world upgraded to 1.18+ gets a visible seam where new chunks
   generate against old ones. Options: accept the wall, hide it behind terraforming, or
   reset unexplored chunks with a chunk tool before upgrading.
3. 1.18 extends existing worlds to `-64` - `320`: the space above the old ceiling becomes
   air, and the space below the old floor depends on the migration path.
4. Re-test redstone after any upgrade. Piston, observer and hopper timing edge cases have
   changed several times, and 1.21.10 specifically fixed piston interactions with cobwebs
   and powder snow.

## Moving a world backward

**Do not.** Worlds are not designed to downgrade, and every converter has caveats - for
example Amulet does not reliably downgrade renamed or aliased block IDs. Move the *build*
instead:

1. Export the build as a schematic (WorldEdit or Litematica) from the newer world.
2. Import it into the older world.
3. Run a substitution pass for every block that does not exist in the target, using
   `block-substitutions.md`, typically as a series of WorldEdit `//replace` commands.
4. Re-check height: anything built below `y=0` cannot exist in a pre-1.18 target.

## Tools

| Tool | Use | Notes |
| --- | --- | --- |
| **Chunker** (chunker.app, open source, Hive Games) | Java to Bedrock and back, plus upgrading and downgrading between supported formats | The most practical converter for whole worlds; check its supported-format list for the pair you need |
| **Amulet** (amuletmc.com) | World editing and conversion, Java 1.12+ and Bedrock 1.7+ | Can copy and paste between worlds of different versions and editions; downgrades can leave invalid aliased block IDs |
| **Litematica** (Fabric mod) | Schematic export, import and holographic placement | Best route for moving a single build between versions |
| **WorldEdit / FAWE** | `//copy`, `//schem save`, `//replace` passes | The substitution pass after a cross-version import |
| **MCA Selector** | Deleting or trimming chunks before an upgrade | Use to remove unexplored chunks so new terrain generates cleanly |

## Cross-edition differences to check before porting

- **Quasi-connectivity** exists in Java only. Any piston, dispenser or dropper circuit that
  relies on it breaks on Bedrock.
- **Block entities** (chests, furnaces, hoppers and similar) can be pushed by pistons on
  Bedrock but not on Java, so Bedrock piston doors can use blocks a Java build cannot.
- Bedrock has its own version numbers for the same drop - see `timeline-2026.md`.
- Redstone tick behaviour and update order differ in edge cases; always rebuild and test
  rather than assuming a circuit ports cleanly.
