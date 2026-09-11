---
name: vfx-and-lighting-2d
description: Design 2D effects, lighting and game feel so actions land and scenes have mood. Use whenever the user is drawing or coding effects for a 2D game - hits, explosions, muzzle flashes, dust, smoke, fire, magic, trails, sparks, water splashes, weather - or asks about 2D lighting, light sources, shadows, glow, bloom, day-night colour, or fog. Also use when the game is described as feeling weak, dry, unresponsive, mushy or lacking punch, or when the user asks what "juice" to add. Covers effect anatomy with anticipation, impact and dissipation frames, frame budgets per effect class, additive and emissive colour handling in a limited palette, smears and trails, screen shake amplitude and decay, hit-stop, flashes, freeze frames and time scaling, layered light and shadow in 2D, contact shadows, normal-map versus hand-painted lighting, emissive tiles, weather and ambience, and a feedback checklist that maps each player action to a visual, an audio and a haptic response. Always asks which action needs feedback and whether the project is pixel-strict before proposing effects.
version: 1.0.0
---

# VFX and lighting in 2D

Effects and light are what turn correct mechanics into a game that feels good. A hit with no flash,
no shake and no particles is a number changing on screen. The same hit with three frames of freeze,
a white flash and a dust burst feels like a hit.

## When to use

- Drawing or planning effects: impacts, explosions, fire, smoke, magic, trails, splashes, sparks.
- Adding lighting to a 2D scene, or debugging lighting that looks flat or muddy.
- The game is described as weak, dry, unresponsive, floaty or "missing something".
- Deciding what feedback each player action should produce.
- Weather, ambience, day-night cycles, mood shifts between areas.

The drawing craft for effect frames is in `../pixel-art-fundamentals/SKILL.md`; the frame timing
language is in `../sprite-animation/references/timing-and-spacing.md`.

## Ask first

1. **Which action needs feedback?** Feedback is designed per action, not per game.
2. **Pixel-strict or free?** Glow, blur, transparency and bloom break a strict pixel-art contract;
   hand-dithered alternatives exist but cost frames.
3. **Engine capabilities** - real 2D lights and shaders, or only sprites and blend modes?
4. **Palette rules** - is the project on a fixed palette? Additive effects need reserved bright
   colours.
5. **Density** - how often does this effect play? An effect that fires 10 times a second must be
   quieter than a boss explosion.

## Core rules

1. **Every effect has three beats**: anticipation (1-2 frames), impact (1-3 frames, biggest and
   brightest), dissipation (3-6 frames, fading and expanding). Most amateur effects only have the
   middle beat.
2. **Effects start big and bright, then thin out.** Never fade uniformly; shrink, break up, and
   lose saturation as they die.
3. **Freeze before you shake.** Hit-stop of 2-5 frames does more for impact than any particle.
4. **Shake decays fast.** 100-200 ms total, high amplitude on the first frames, near zero by the
   end. Long shakes are nausea, not power.
5. **Light is composition.** The brightest point in the frame is where the player looks - spend it
   on gameplay, not decoration.
6. **Reserve palette slots for light.** Emissive and additive colours must be brighter and more
   saturated than anything in the environment, or nothing glows.
7. **One effect per event.** Stacking five particle systems on one hit reads as visual noise and
   hides the gameplay.

## Workflow

**Step 0 - list the events.** Every player-visible event gets a row: jump, land, dash, hit, get hit,
   pick up, level up, die, unlock. See `references/juice-and-feedback.md`.

**Step 1 - rank them.** Rare and important events get expensive effects; frequent ones get cheap
   and quiet ones.

**Step 2 - block the anatomy.** For each effect, decide frame count, shape language and colour
   ramp before drawing. See `references/effect-anatomy.md`.

**Step 3 - add non-art channels.** Hit-stop, shake, flash, time scale, sound. These are usually
   cheaper and stronger than more frames.

**Step 4 - light the scene.** Decide light sources, direction, ambient colour, and which objects are
   emissive. See `references/light-and-shadow.md`.

**Step 5 - tune in play, at speed.** Effects that look great in isolation are often far too loud
   during real combat. Cut 30% of everything on the second pass.

## References

| File | Read it for |
| --- | --- |
| `references/effect-anatomy.md` | Frame budgets per effect class, shape language, impact/dissipation construction, colour ramps for fire, smoke, magic and water, trails and smears, additive blending inside a limited palette |
| `references/light-and-shadow.md` | Light direction and ambient colour, hand-painted vs engine lights, contact and cast shadows, emissive tiles, glow and bloom without breaking pixel art, day-night and area mood, fog and volumetrics |
| `references/juice-and-feedback.md` | Action-to-feedback table, hit-stop and shake values, flashes and time scaling, camera work, feedback density budgets, and an audit checklist |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../sprite-animation/SKILL.md` | Frame timing, smears, attack windows and hit reactions |
| `../color-and-palettes/SKILL.md` | Reserving bright slots, keeping effects readable against terrain |
| `../pixel-art-fundamentals/SKILL.md` | Drawing the individual effect frames, dithered gradients and transparency |
| `../tilesets-and-environments/SKILL.md` | Emissive tiles, animated water, weather layers, parallax fog |
| `../game-ui-and-hud/SKILL.md` | Damage numbers, screen vignettes, low-health effects, UI juice |
| `../game-art-pipeline/SKILL.md` | Blend modes, shaders, overdraw and particle budgets, export of effect sheets |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Hits feel weak" | No freeze, no flash, no reaction | 3 frames hit-stop + 2 frame white flash + small knockback |
| "Explosion looks like a sticker" | Effect fades uniformly, no shape change | Expand and break up the shape; lose saturation as it dies |
| Effects hide the gameplay | Too many, too opaque, centred on the character | Fewer particles, offset from the character, shorter lifetimes |
| Screen shake makes people ill | Too long, too low frequency, no decay | Under 200 ms, fast decay, cap amplitude |
| Nothing glows | Emissive colours are the same brightness as the environment | Reserve the two brightest palette slots exclusively for light |
| Lighting looks muddy | Shadows are darker greys of the same hue | Shift shadows toward a cool hue, reduce saturation drop |
| Pixel art looks blurry after adding glow | Post-process bloom at a non-integer scale | Apply glow before upscaling, or dither the glow by hand |
| Every effect looks the same | One shape language reused | Give each damage type its own silhouette and ramp |

## Answering style

- Give numbers: frame counts, durations in ms, shake amplitude in pixels, flash length in frames.
- Always propose the cheap version first: hit-stop and a flash before new art.
- Name the three beats explicitly when describing an effect.
- If the project is pixel-strict, state which techniques are off the table and give the dithered
  alternative.
