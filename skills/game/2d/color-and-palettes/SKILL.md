---
name: color-and-palettes
description: Choose, build and debug colour for 2D games. Use whenever the user asks which colours to use, how to build a palette, how many colours to allow, why their art looks dull, muddy, washed out, oversaturated or "like a filter", how to shade with colour rather than just darkening, how to make characters pop against backgrounds, how to do day-night or faction palette swaps, or which existing palette (PICO-8, DawnBringer, Sweetie, Endesga, Nyx8, Lost Century) fits their project. Covers value ramps and hue shifting, temperature of light and shadow, building a palette from a key light plus ambient, interlocking and shared ramps, palette size budgets, figure-to-ground contrast, saturation zoning, UI text contrast targets, colour-blindness safety, never encoding information in hue alone, and palette swapping for variants. Always asks for the game's mood, palette budget and whether characters must read over busy backgrounds.
version: 1.0.0
---

# Colour and palettes

Most "bad colour" in 2D games is one of three things: shading by darkening only, no value
separation between characters and backgrounds, or a palette assembled one colour at a time with no
system. This skill fixes all three.

## When to use

- Picking or fixing the colours of a sprite, tileset, effect or UI.
- Building a project palette, or deciding whether to adopt an existing one.
- The art is described as dull, muddy, washed out, garish, flat, or "all the same colour".
- Characters get lost against levels.
- Day-night cycles, factions, elemental variants, damage states, rarity tiers.
- Accessibility questions about colour.

Drawing craft is in `../pixel-art-fundamentals/SKILL.md`; this skill assumes values are already
under control and deals with hue and saturation.

## Ask first

1. **Mood and reference** - one or two existing games, or three adjectives ("warm, dusty, hopeful").
2. **Budget** - free colour, a fixed count (16, 32, 64), or an existing named palette?
3. **Gameplay pressure** - must characters, pickups and hazards read instantly over busy
   backgrounds? Is any information (team, element, status) carried by colour?
4. **Lighting story** - one dominant light (sunset, moonlight, torch), or neutral daylight?

## Core rules

1. **Value does the work, hue does the mood.** Decide value structure first; colour is applied to a
   working value plan (`../pixel-art-fundamentals/references/shading-and-form.md`).
2. **Never shade by lowering brightness alone.** As a colour goes darker it should also shift hue
   and usually gain saturation in the midtones; as it goes lighter it shifts toward the light's hue
   and loses saturation at the very top. This is hue shifting, and it is the single biggest
   difference between amateur and professional palettes.
3. **Light and shadow are opposite temperatures.** Warm light means cool shadow, and vice versa.
   Pick one story and hold it across the project.
4. **Saturation is a budget.** If everything is saturated, nothing is. Keep backgrounds muted and
   reserve high saturation for characters, interactables and effects.
5. **Colour is never the only carrier of information.** Add shape, icon, value or motion, both for
   colour-blind players and for readability on bad screens.

## Workflow

**Step 0 - write the lighting story.** "Late afternoon sun, warm key from upper left, cool blue sky
   ambient." Everything else derives from this sentence.

**Step 1 - build the core ramps.** One ramp per material family (skin, metal, foliage, stone,
   cloth). 4-5 steps each, hue-shifted. See `references/ramps-and-hue-shifting.md`.

**Step 2 - interlock.** Share endpoints between ramps so the palette feels like one world and
   stays small. See `references/palette-construction.md`.

**Step 3 - zone the saturation and value.** Assign value/saturation bands to background, midground,
   characters and UI so they cannot collide. See `references/readability-and-contrast.md`.

**Step 4 - test.** Desaturate, squint, simulate deuteranopia, and look at the art on a phone in
   daylight. Fix collisions by moving *value*, not hue.

**Step 5 - freeze and document.** Export the palette as a strip PNG plus a hex list in the repo, so
   every asset uses the same colours. See `../game-art-pipeline/SKILL.md`.

## References

| File | Read it for |
| --- | --- |
| `references/ramps-and-hue-shifting.md` | How to build a 4-5 step ramp, how far to shift hue, temperature of light vs shadow, bounce light, saturation curve, gold vs silver, common ramp mistakes |
| `references/palette-construction.md` | Building a palette from a key light plus ambient, interlocking ramps, palette size budgets, neutral spine, accent colours, extending a palette without breaking it |
| `references/readability-and-contrast.md` | Figure-to-ground separation, value and saturation zoning, UI text contrast targets, hazard and pickup colour language, colour-blindness, testing procedure |
| `references/palette-library.md` | Named palettes worth using and what each is good for, hardware-style constraints, palette swapping for factions, day-night and status effects |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../pixel-art-fundamentals/SKILL.md` | Values, edges, shading craft, texture |
| `../tilesets-and-environments/SKILL.md` | Backgrounds that must stay behind characters, biome recolours |
| `../vfx-and-lighting-2d/SKILL.md` | Emissive colours, additive blending, glow, tinting by light sources |
| `../game-ui-and-hud/SKILL.md` | UI colour semantics, text contrast, state colours |
| `../game-art-pipeline/SKILL.md` | Storing palettes, palette-swap shaders, colour management on export |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Looks dull" | Shading by brightness only; shadows are grey | Hue-shift shadows toward the ambient colour, raise midtone saturation |
| "Looks muddy" | Too many desaturated midtones, narrow value range | Cut colours, widen value range, keep one clean accent |
| "Looks like a cheap filter" | Global overlay applied to finished art | Rebuild ramps under the new light instead of tinting on top |
| "Too loud" | Everything at max saturation | Mute background bands, keep saturation for characters and VFX |
| "Characters get lost" | Value collision, not hue collision | Reserve a value band for characters; darken or desaturate the level |
| "Palette feels random" | Colours picked one by one | Rebuild as 4-6 interlocking ramps from one light story |
| "Players can't tell red from green states" | Information carried by hue alone | Add icon, shape or value difference |

## Answering style

- Give concrete hex values or HSV moves ("shadow: rotate hue -25 degrees toward blue, drop value
  30%, raise saturation 10%"), not vague advice.
- Say which decision is objective (value separation, contrast for text) and which is taste (hue choice).
- When the user's palette is broken, diagnose in this order: value range, saturation zoning,
  hue shifting, colour count.
- Offer an existing named palette when the user has no strong direction - it is faster than
  designing one and easy to outgrow later.
