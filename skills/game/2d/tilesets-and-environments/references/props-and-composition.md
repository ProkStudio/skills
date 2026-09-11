# Props, decals and level composition

## A prop library that scales

Build the library in three size classes and reuse aggressively:

| Class | Size | Count to aim for | Role |
| --- | --- | --- | --- |
| Small | under half a tile | 15-25 | Texture and noise-breaking: pebbles, cracks, tufts, bolts, bones |
| Medium | 1-2 tiles | 10-15 | Readable objects: crates, bushes, barrels, signs, lamps, rubble |
| Large | 3+ tiles | 4-8 | Landmarks and set dressing: dead trees, statues, machines, ruins |

Twenty small props placed well beat two hundred drawn and dumped. Rotate and mirror where the art
allows (be careful with light direction - mirroring moves the highlight to the wrong side).

## Density rules

- Decoration density should vary across a level: quiet stretches, then a dense pocket. Uniform
  density reads as wallpaper and hides landmarks.
- Cluster props in odd-numbered groups (1, 3, 5) with varied spacing; evenly spaced pairs look placed.
- Keep the gameplay lane clear. In a platformer, the band where the player jumps and lands should be
  the least decorated part of the screen.
- Anchor props to something: a wall, a floor line, a corner. Props floating in the middle of a flat
  surface look accidental.

## Leading the eye and navigation

- **Landmarks**: one large, unique silhouette per area gives players a mental map. Reuse it as the
  area's identity in UI and dialogue.
- **Light and colour as signposts**: the eye goes to the brightest, most saturated, highest-contrast
  spot. Put it where you want the player to go, not on decoration.
- **Repetition then break**: three identical arches and then a broken one - the break reads as
  "something happened here".
- **Framing**: use foreground shapes to funnel attention toward the next objective.
- **Dead ends should look like dead ends** from a distance: lower contrast, no light, no path lines.

## Biome recolours instead of new tilesets

One tileset plus palettes is usually the right answer for multiple biomes:

1. Draw the tileset with a strict palette, in ramp order.
2. Author each biome as a palette remap, plus 3-5 biome-specific props and one animated tile.
3. Change a few silhouettes (grass overhang to snow drift to ash crust) to avoid the "same level,
   different hue" feeling.

See `../../color-and-palettes/references/palette-library.md` for swap mechanics.

## Composition checklist for a screen

1. Squint: is there one clear focal point, and is it gameplay-relevant?
2. Desaturate: can you still read platforms, hazards and interactables?
3. Is the highest contrast in the frame on something the player must see?
4. Is there depth: at least one background layer and one foreground element?
5. Is the decoration clustered rather than evenly spread?
6. Can a new player tell, from one still frame, where to go next?
7. Does anything decorative sit exactly where the player's eyes must be during a hard jump?

## Cheap wins, in order

1. Add a foreground layer.
2. Mute background saturation by a third.
3. Add overhang decoration on all top edges of terrain.
4. Add one landmark silhouette per area.
5. Add a contact shadow under every prop and character
   (`../../pixel-art-fundamentals/references/shading-and-form.md`).
6. Add one animated element per screen - water, a flag, a lamp flicker.
