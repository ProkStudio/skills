# Effect anatomy

## The three beats

| Beat | Frames | What changes | Purpose |
| --- | --- | --- | --- |
| Anticipation | 0-2 | Small, tight, often just a bright dot or a gather | Tells the player something is about to happen |
| Impact | 1-3 | Largest, brightest, most saturated; may be a full flash | The event itself |
| Dissipation | 3-8 | Expands, breaks into pieces, loses saturation and value | Sells scale and energy loss |

Common mistakes: no anticipation (the effect appears from nowhere), and uniform fade-out (reads as a
sticker turning transparent rather than energy dispersing).

## Frame budgets by class

| Effect | Frames | Duration at 12-15 fps | Notes |
| --- | --- | --- | --- |
| Small hit spark | 3-4 | ~250 ms | Fires constantly - keep it cheap and quiet |
| Sword slash / trail | 3-5 | ~300 ms | Arc shape; one smear frame does most of the work |
| Muzzle flash | 2-3 | ~150 ms | Bright, tiny, offset to the barrel |
| Dust puff (land, step) | 4-5 | ~350 ms | Expands outward and upward, then thins |
| Explosion (small) | 6-8 | ~500 ms | Flash frame first, then fireball, then smoke |
| Explosion (boss) | 10-16 | ~1 s | Multiple staggered bursts beat one big one |
| Magic cast | 6-10 | ~600 ms | Gather (anticipation) is the readable part |
| Water splash | 5-7 | ~450 ms | Droplets separate and fall with gravity |
| Smoke plume | 8-12 looping | - | Slow, low contrast, drifts and dissipates |
| Pickup sparkle | 3-4 | ~250 ms | Star or cross shape, single bright colour |

## Shape language

Give each damage or element type a distinct silhouette so players can identify it instantly:

| Type | Shape | Motion |
| --- | --- | --- |
| Physical / blunt | Radial burst, chunky shards | Fast out, abrupt stop |
| Slash | Thin crescent arc | Follows the weapon arc, one smear |
| Fire | Tongues with flickering tips, rising | Rises, curls, breaks into embers |
| Ice | Angular crystals, straight edges | Snaps out, then shatters |
| Lightning | Jagged branching lines, 1 px wide | Instant, 2-3 frames, strobes |
| Poison | Round blobs, bubbling | Slow, drifting up, lingering |
| Holy / energy | Concentric rings, vertical beams | Smooth, symmetric, slow fade |
| Dark | Tendrils, smoky wisps, inward pull | Sucks inward before bursting |

## Colour ramps for effects

Effects need their own ramps, hotter and brighter than the environment ramps:

- **Fire**: white -> pale yellow -> orange -> deep red -> dark smoke. The white core is only present
  on the first 1-2 frames.
- **Smoke**: light warm grey -> mid grey -> transparent/dark. Saturation near zero.
- **Water**: white foam -> light cyan -> mid blue -> dark blue outline.
- **Electric**: white core -> pale cyan -> saturated blue-violet.
- **Magic**: pick a hue nobody else uses in the game so it reads as "not natural".

Rules:

- Hot core, cool edge. A flat single-colour effect never reads as energy.
- Brightness drops before size does; an effect that stays white while shrinking looks like a bug.
- Desaturate as the effect dies, do not just darken.

## Additive blending in a limited palette

With a fixed palette you cannot rely on additive blending. Options:

1. Reserve the two brightest slots exclusively for light and effects and never use them in
   environments (`../../color-and-palettes/references/palette-construction.md`).
2. Hand-draw the "additive" result: draw the overlap area in the correct lighter palette colour.
3. Use dithered transparency: a checkerboard of the effect colour over the background reads as ~50%
   opacity while staying on-palette
   (`../../pixel-art-fundamentals/references/dither-and-texture.md`).

If the project allows shaders, additive blending on top of a palette-quantised render pass is the
usual compromise: render the scene, quantise, then add glow.

## Trails and smears

- **Weapon trail**: an arc that follows the blade path, brightest at the leading edge, 3 frames.
- **Motion trail for a dash**: 2-4 fading copies of the sprite silhouette, each one value darker.
- **Projectile trail**: a short tapering tail, 2-4 px, plus 1-2 sparks left behind per frame.
- **Afterimages** read as speed; stack no more than 4 or the character becomes unreadable.

## Particles vs hand-drawn frames

| Approach | Best for | Watch out |
| --- | --- | --- |
| Hand-drawn frame sequences | Signature effects, stylised pixel art, anything that must read at 16-32 px | Expensive; each variation costs frames |
| Engine particles | Dust, smoke, sparks, weather, continuous emitters | Sub-pixel positions break the pixel grid - snap positions and use point filtering |
| Hybrid | Hand-drawn core + particle debris | Keep them on the same palette |

For pixel-strict projects, force particle sizes to multiples of the pixel scale and snap their
positions, or the effect will visibly "float" above the pixel grid.

## Sanity checks

1. Does the effect have all three beats?
2. Does it change shape as it dies, not just opacity?
3. Is it offset from the character so it does not hide them?
4. Is it readable against the busiest background in the game?
5. At 10 simultaneous copies, is the screen still legible?
6. Is the brightest pixel in the frame where the gameplay is?
