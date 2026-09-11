# Canvas, resolution and pixel density

Everything downstream - proportions, detail budget, animation cost - is decided here. Choose
sprite height, tile size and base resolution as one decision.

## Pick the sprite height first

| Height | Detail you actually get | Typical use |
| --- | --- | --- |
| 8-12 px | Silhouette and 2 values | Minions, tiny strategy units, minimap pips |
| 16 px | Silhouette, 3 values, one accent (eye, weapon) | Classic top-down RPG, item icons |
| 24-32 px | Face suggestion, clothing shapes, 4 values | The workhorse size: platformers, action RPGs |
| 48-64 px | Readable facial features, material contrast, 5-6 values | Detailed platformer hero, fighting game chibi |
| 96-128 px | Anatomy, folds, specular detail | Bosses, portraits, key art |
| 200+ px | Illustration rules apply, pixel discipline gets expensive | Cutscene portraits, promo art |

Doubling the height multiplies the pixels - and the animation work - by four. A 64 px hero with 8
frames of walk costs about as much as a 32 px hero with 32 frames.

## Proportions at small sizes

Head counts: 2-3 heads for chibi, 4-5 for stylised, 6-7 for realistic. Below 48 px you cannot draw
7-head proportions - the head becomes 6 px and the face disappears. Pick the head count that fits
the height:

- 16 px tall: 1 head = 6-7 px, roughly 2.5 heads. Chibi, no facial detail beyond eyes.
- 32 px tall: 1 head = 8-10 px, 3-4 heads. Eyes plus a hint of mouth.
- 64 px tall: 1 head = 10-12 px, 5-6 heads. Proper facial features.

## Base resolutions that scale cleanly

Pick a base resolution whose integer multiples land on common displays. For 16:9:

| Base | x to 1280x720 | x to 1920x1080 | x to 3840x2160 |
| --- | --- | --- | --- |
| 320x180 | 4 | 6 | 12 |
| 384x216 | - | 5 | 10 |
| 480x270 | - | 4 | 8 |
| 640x360 | 2 | 3 | 6 |

320x180 is very tight - a 32 px character occupies a sixth of the screen height. 480x270 and
640x360 are the comfortable modern choices. Avoid bases that need fractional scaling (for example
256x144 at 1080p is 7.5x): you get uneven pixels or a blur.

## Historic hardware, for reference and for style

| System | Screen | Colour constraint worth copying |
| --- | --- | --- |
| Game Boy | 160x144 | 4 shades of one hue, whole screen |
| NES | 256x240 (about 224 visible) | Sprite = 3 colours + transparent, per 8x8 or 8x16 tile; 8 sprites per scanline |
| SNES | 256x224 | Many colours, but backgrounds still built from 8x8 tiles in 16-colour sets |
| Game Boy Advance | 240x160 | 15-bit colour, small screen - chunky readable shapes |
| PICO-8 | 128x128 | Fixed 16-colour palette, 8x8 sprites |

You do not have to obey these. Adopting one on purpose ("NES-style: 4 colours per sprite") gives a
project instant visual coherence; adopting one by accident just limits you.

## One pixel density, everywhere

The single most common thing that makes a project look homemade is mixed pixel sizes.

- Decide that 1 art pixel = N screen pixels, and hold it for sprites, tiles, UI, fonts and effects.
- Never scale an asset by a non-integer factor to make it fit; redraw it.
- Never mix a 16 px-grid tileset with characters drawn on an effectively 8 px grid (double-size pixels).
- Rotation breaks the grid. Rotate only in 90 degree steps, or draw the rotated frames by hand, or
  accept that rotation is a non-pixel-art effect and use it deliberately (spinning coins, projectiles).
- Scaling a pixel sprite up and down for "perspective" has the same problem. Draw two or three
  discrete sizes instead.
- UI is part of the project. A crisp 1x bitmap font next to 3x-scaled sprites looks like two games.

## Tile sizes

| Tile | Character height in tiles | Notes |
| --- | --- | --- |
| 8 px | 2-3 | Dense retro look, cheap to author, hard to detail |
| 16 px | 1.5-2 | Default for 2D; good detail-to-cost ratio |
| 32 px | 1-1.5 | Modern "HD pixel" look, four times the authoring cost of 16 |
| 48-64 px | 1 | Detailed backgrounds, fewer unique tiles, more hand placement |

Keep collision on the tile grid even when art overhangs it. Overhang (grass blades, roof edges) is
what stops a tile map from looking like graph paper - see `../../tilesets-and-environments/SKILL.md`.

## Canvas hygiene

- Work zoomed in but keep a 100% preview window open at all times. Judge at 100%, edit at 600%.
- Leave 1 px of empty margin around a sprite for outlines and AA; crop later during export.
- Keep the pivot in the same place in every frame of a set (feet centre for characters, visual
  centre for projectiles). Misaligned pivots read as a jitter that no one can find.
- Power-of-two canvas sizes are not required for sprites; they matter only for some atlas setups.
- Name and size files consistently from the start - see `../../game-art-pipeline/SKILL.md`.

## When pixel art is the wrong tool

Pixel art is expensive per frame and hostile to free transforms. Prefer higher-resolution 2D art if
the project needs smooth rotation and scaling, dozens of animation frames per character,
resolution-independent UI, or if nobody on the team enjoys placing pixels. A "pixel art" game with
bilinear-filtered, rotated, arbitrarily scaled sprites gets the costs of both approaches and the
benefits of neither.
