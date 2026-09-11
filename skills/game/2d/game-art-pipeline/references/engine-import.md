# Engine import and rendering settings

Setting names move between engine versions; treat these as the concepts to look for, and confirm the
exact labels in the version you use.

## Godot

**Project-wide display settings**

- Set the base viewport width/height to your authoring resolution (for example 480 x 270), and the
  window size to a multiple of it.
- **Stretch mode**:
  - `disabled` - no scaling; the game renders at window resolution.
  - `canvas_items` - the viewport is scaled up; vector/UI elements stay smooth, 2D art scales.
  - `viewport` - renders at the low base resolution into a viewport and upscales the whole image;
    this is the classic pixel-art choice.
- **Stretch aspect**: `keep` for letterboxing, `expand` to show more world on wider screens.
- **Scale mode**: set to `integer` to force whole-number scale factors (with black bars); this is the
  pixel-perfect option.
- Exclusive fullscreen is generally recommended over borderless for pixel-perfect output, since the
  compositor does not resample the image.

**Textures**

- Default texture filter: `Nearest` (project setting `rendering/textures/canvas_textures/default_texture_filter`),
  or per-texture in the import dock.
- Turn off mipmaps and any "fix alpha border" style option that modifies edge pixels for strict art.
- Use `snap_2d_transforms_to_pixel` and `snap_2d_vertices_to_pixel` for pixel snapping, plus a
  camera that rounds its position.

**Tilemaps**

- Terrain sets support side-only matching and corner-and-side matching, matching the 16-tile and
  47-tile schemes (`../../tilesets-and-environments/references/grids-and-autotiling.md`).
- Prefer a single tileset texture with padding; enable the texture region margin/separation values
  that match how the sheet was exported.

## Unity

**Sprite import settings (per texture)**

- Filter Mode: `Point (no filter)`
- Compression: `None` (or lossless), Max Size large enough not to downscale
- Generate Mip Maps: off
- Pixels Per Unit: one consistent value project-wide (commonly equal to the sprite's pixel size, for
  example 16)
- Mesh Type: `Full Rect` for sprites used in UI or 9-slice
- Sprite Mode: `Multiple` with a grid slice for sheets; set pivots explicitly

**Pixel-perfect rendering**

- Either use the Pixel Perfect Camera component (2D URP / 2D Pixel Perfect package) with a reference
  resolution and "Upscale Render Texture" / integer-scaling options, or render the scene to a
  fixed-size render texture at the base resolution and blit it to the screen with point filtering at
  an integer scale. The render-texture approach is the most predictable and also gives you a place to
  apply post-processing before upscaling.
- UI: a Canvas with `Canvas Scaler` in `Scale With Screen Size` mode fights integer scaling; for
  pixel-strict UI, place UI inside the same low-resolution render target, or restrict the scale
  factor to integers.
- Keep sprite positions snapped in a late update or in the render path, and snap the camera too.

**Atlases**

- Sprite Atlas with Padding 2-4 and "Tight Packing" off for tiles; enable Read/Write only if needed.
- Ensure the atlas inherits Point filtering and no compression.

## GameMaker and generic engines

- GameMaker: set the camera and viewport sizes explicitly, use `Interpolate colours between pixels`
  off, and disable texture page bleeding by leaving the default padding in place. Application surface
  scaling is where most blurriness comes from.
- Love2D / SDL / custom: set nearest-neighbour filtering globally, render to a canvas/render target
  at the base resolution, then draw that target scaled by an integer factor.
- Web (canvas/WebGL): set `image-rendering: pixelated` in CSS and disable image smoothing on the 2D
  context; also make sure the canvas backing size is an integer multiple of the base resolution.

## Fonts

- Bitmap/pixel fonts: use at their native size or integer multiples only; disable any font smoothing,
  hinting or subpixel positioning.
- Vector fonts in a low-resolution viewport look cramped; either render UI at full resolution or
  choose a pixel font designed for the size.
- Test text at every supported UI scale; font rendering is the first thing to break when scaling
  changes (`../../game-ui-and-hud/references/typography-and-icons.md`).

## Shaders commonly needed in 2D

| Shader | Purpose | Notes |
| --- | --- | --- |
| Palette swap | Recolour sprites by index | Requires stable palette order and indexed art |
| Flash / hit white | Damage feedback | Replace all non-transparent pixels with one colour |
| Outline | Readability against busy scenes | Expand alpha by 1 px; snap to the pixel grid |
| Dissolve | Death and spawn effects | Use a dither pattern texture to stay on-style |
| Screen palette quantise | Unify post-processed output | Apply before upscaling |

Apply all post-processing at the base resolution, then upscale. Post-processing after upscaling
destroys the pixel grid (`references/pixel-perfect-rendering.md`).

## Settings audit

1. Viewport/base resolution documented and matching the art.
2. Integer scaling enabled, or an explicit decision recorded not to use it.
3. Point filtering, no mipmaps, no lossy compression on all 2D textures.
4. Camera and sprite positions snapped in the render step.
5. Atlas padding/extrusion configured for tiles.
6. UI scaling policy chosen and consistent with the game viewport.
7. Fullscreen mode tested, not just windowed.
