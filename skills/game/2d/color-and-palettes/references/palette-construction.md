# Building a palette

## Start from a light story, not from swatches

Write one sentence: "Overcast coastal morning, cool white key, warm sand bounce." That sentence
determines your highlight hue, shadow hue, and how saturated the world can be. Palettes built
swatch-by-swatch look like a swatch collection.

## The build order

1. **Neutral spine (4-6 colours).** From the darkest shadow to the lightest light, tinted by the
   light story - never pure greys. Everything else hangs off this.
2. **Two or three material ramps (4-5 each).** The families that dominate the game: skin, stone,
   foliage, metal, wood, cloth.
3. **One or two accents (2-3 each).** High saturation, reserved for characters, pickups, hazards,
   and UI emphasis. Accents must not appear in backgrounds.
4. **Sky / atmosphere colours (2-4).** Usually light, low saturation, cool.

That is a coherent 24-32 colour palette. Most 2D games need fewer colours than the artist thinks
and more *value separation* than they think.

## Interlocking ramps

Share endpoints between ramps so the palette stays small and the world feels lit by one light:

- The darkest step of every ramp can be the same colour, or two shared darks.
- The lightest step of several ramps can be one shared near-white tinted by the key light.
- A midtone in the stone ramp can double as the shadow of the skin ramp.

Rule of thumb: with interlocking, 5 material ramps cost about 16-18 unique colours instead of 25.

## Palette size budgets

| Count | Character | Good for |
| --- | --- | --- |
| 4 | Extreme constraint, all value | Game Boy homage, jam games, strong graphic identity |
| 8 | One ramp plus accents | Stylised minimal, very fast to author |
| 16 | Two or three ramps plus accents | The classic sweet spot; PICO-8, DB16 |
| 32 | Several material families, comfortable | Most indie pixel games; DB32, Endesga 32 |
| 64 | Rich, needs discipline to stay coherent | Detailed backgrounds, illustration-heavy work |
| Unlimited | Requires self-imposed rules or it drifts | Non-pixel 2D, painted art |

A smaller palette forces value discipline and makes everything look intentional. If a project looks
incoherent, halving the palette usually helps more than adding colours.

## Per-asset colour limits

Even with a 32-colour project palette, cap colours *per sprite*: 4-6 for a 32 px character, 8-10
for a 64 px one. This is what keeps individual sprites crisp and the set consistent, and it mirrors
old hardware limits that produced the look people associate with pixel art.

## Extending a palette without breaking it

- Add by extending an existing ramp (a new midtone), not by inserting a new hue family.
- New hue families must borrow their darkest and lightest steps from the existing spine.
- Before adding a colour, check whether an existing colour at a different value would do.
- Keep a "reserved" list: colours used only by VFX or UI, never by world art.

## Documenting it

- Store the palette in the repo as both a strip PNG (1 px per colour, in ramp order) and a hex list.
- Group hexes by ramp in the text file, with the material name - future-you will not remember which
  brown was for wood and which for leather.
- Aseprite, Photoshop and Godot can all import a palette from a strip PNG, so one file serves
  everyone.
- When a palette changes mid-project, change it by remapping indices, not by hand-editing sprites.
  See `../../game-art-pipeline/SKILL.md`.

## Sanity checks

- Convert the palette strip to greyscale: are there clear steps, or three colours at the same value?
- Is there exactly one region of maximum saturation?
- Can you name the role of every colour? Unnamed colours are usually accidents.
- Do backgrounds and characters draw from different value bands?
