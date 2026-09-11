# Pixel-perfect rendering

## Base resolution

Author the game at one low native resolution and upscale. Choose a base whose integer multiples hit
your targets:

| Base | x3 | x4 | x5 | x6 | Notes |
| --- | --- | --- | --- | --- | --- |
| 320 x 180 | 960 x 540 | 1280 x 720 | 1600 x 900 | 1920 x 1080 | 16:9; x12 gives 3840 x 2160 (4K). Very chunky pixels |
| 384 x 216 | 1152 x 648 | 1536 x 864 | 1920 x 1080 | - | x10 gives 4K. Good middle ground |
| 480 x 270 | 1440 x 810 | 1920 x 1080 | - | - | x8 gives 4K. Room for detail and UI text |
| 640 x 360 | 1920 x 1080 | 2560 x 1440 | - | - | x6 gives 4K. Nearly "HD-pixel" look |

Historical references for scale intuition: Game Boy 160 x 144 with 4 shades; NES 256 x 240 (about
224 visible), 3 colours plus transparency per sprite tile and 8 sprites per scanline; SNES 256 x 224;
GBA 240 x 160; PICO-8 128 x 128 with 8 x 8 sprites.

Pick based on how much UI text you need: at 320 x 180 a 7 px font occupies a big share of the screen.

## Integer versus fractional scaling

- **Integer scaling** (x2, x3, x4...) maps every source pixel to an identical square block. This is
  the only way every pixel stays the same size.
- **Fractional scaling** (for example x2.5) must decide what to do with half pixels: with point
  filtering some source pixels become 2 blocks wide and others 3 (visible unevenness); with bilinear
  filtering everything softens.

Since monitors are rarely an exact integer multiple of your base resolution, pick a policy:

| Policy | How it looks | Cost |
| --- | --- | --- |
| Integer scale + letterbox/pillarbox | Perfect pixels, black bars | Lost screen area |
| Integer scale + expand the viewport | Perfect pixels, more world visible on wider screens | Level design must tolerate a variable visible area |
| Fractional scale to fill | No bars, uneven or soft pixels | Breaks pixel purity |
| Integer scale for the game, free scale for UI | Crisp world, flexible UI | Two rendering paths; UI must not be pixel-strict |

Most pixel-art games ship with integer scaling plus a small overscan or expanded viewport, and offer
a "stretch to fill" option for players who prefer it.

## Snapping

Three places need whole-pixel discipline:

1. **Camera position** - round to whole pixels in the render step, after all smoothing. A smoothed
   camera that is not rounded makes the entire screen shimmer.
2. **Sprite positions** - round at draw time, not in the physics or logic, so movement stays smooth
   internally while rendering stays crisp.
3. **Pivots and sprite sizes** - whole pixels; a 0.5 px pivot guarantees jitter.

Round rather than truncate, and do it consistently; mixing the two produces 1 px jumps between
related objects.

## Sub-pixel motion

A slow-moving object at whole-pixel positions moves in visible steps. Options:

- Accept the stepping (classic, and honest to the style).
- Keep sub-pixel logic and render snapped: the object advances one pixel when it accumulates one.
- Render at a higher internal resolution and accept non-pixel-perfect art (a project-level choice).

Never mix: snapped characters over smoothly-scrolling backgrounds is the "my game feels wrong"
symptom nobody can name.

## Rotation, scaling and zoom at runtime

- **Rotation** resamples the grid; pixel art rotated at arbitrary angles wobbles. Draw 4, 8 or 16
  discrete angles instead. Exception: intentionally smooth-rotating non-pixel elements, such as
  particles, if the style allows.
- **Runtime scaling** must be integer-only; scale the whole viewport rather than individual sprites.
- **Camera zoom** must move in integer steps, or be off. Smooth zoom is incompatible with a fixed
  pixel grid.
- **Flipping** is free geometrically, but it moves baked highlights to the wrong side. Either accept
  it or draw both facings.

## Diagnosing the classic defects

| What you see | Almost always |
| --- | --- |
| Everything soft | Bilinear filtering enabled |
| Some pixels bigger than others | Fractional scale with point filtering |
| Edges crawl while the camera moves | Camera not snapped to pixels |
| Single sprite jitters, rest is fine | Half-pixel pivot or unsnapped sprite position |
| Thin bright/dark lines between tiles | Atlas bleeding, or mipmaps on |
| Detail disappears at distance | Mipmaps enabled |
| Sprite outline breaks up when rotating | Runtime rotation |
| Text soft while sprites are crisp | UI canvas scaling differently from the game viewport |

## Verification scene

Keep a test scene in the project containing:

- A 1 px checkerboard covering the screen (shows filtering and scaling errors instantly).
- A sprite with 1 px details and a diagonal line (shows resampling).
- A tiled surface (shows bleeding).
- UI text at the smallest used size (shows font scaling).
- A slow-moving object and a fast-moving camera (shows snapping errors).

Run it at every supported resolution and window mode after any rendering change.
