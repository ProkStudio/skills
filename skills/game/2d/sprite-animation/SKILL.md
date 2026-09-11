---
name: sprite-animation
description: Animate 2D sprites so motion reads, feels responsive and fits a frame budget. Use whenever the user is animating a character, enemy, prop, pickup, projectile or effect in 2D, asks how many frames an idle, walk, run, jump, attack, hit or death needs, asks why their animation looks stiff, floaty, robotic, slow or "like it slides", wants a walk cycle broken down pose by pose, or needs spritesheet, pivot, tag and frame-timing conventions for an engine. Covers timing and spacing as the primary tool, the animation principles that actually matter at low resolution, anticipation and follow-through, squash and stretch with volume preservation, smear and multiple-exposure frames, pose-by-pose breakdowns of the standard cycles with frame counts, attack anatomy with hit windows, hit-stop and cancel windows, loop construction, and spritesheet layout, pivots and naming. Always asks for frame budget, target feel and whether the animation is gameplay-critical before drawing frames.
version: 1.0.0
---

# Sprite animation

A still sprite shows a character; animation shows what kind of character it is. In games,
animation also carries information the player must read in a fraction of a second: that an attack
is coming, that a hit landed, that the character is about to stop.

## When to use

- Animating anything in 2D: characters, enemies, props, pickups, doors, projectiles, UI motion.
- The user asks for frame counts or timings.
- The animation is described as stiff, floaty, robotic, laggy, sliding, or "missing weight".
- The game feels unresponsive and the cause may be animation, not code.
- Building a spritesheet and needing layout, pivot or naming conventions.

Drawing craft is in `../pixel-art-fundamentals/SKILL.md`; impact effects and screen feedback are in
`../vfx-and-lighting-2d/SKILL.md`.

## Ask first

1. **Frame budget** - how many frames per animation can they actually draw and maintain across the
   whole cast? A 6-frame budget changes every later choice.
2. **Feel** - snappy arcade, weighty souls-like, cartoon bouncy, realistic?
3. **Gameplay-critical or decorative?** If the player must react to it, readability and telegraph
   windows outrank beauty.
4. **Playback rate and engine** - fixed 12 fps art on a 60 fps game, or per-frame durations in ms?
5. **Sprite size and view** - 32 px side view and 64 px eight-direction top-down are different jobs.

## Core rules

1. **Timing and spacing beat frame count.** Four frames with varied timing read better than twelve
   frames at a uniform rate. Uniform timing is the single most common defect.
2. **Every action needs three beats**: anticipation, action, recovery. Cut any of them and the
   motion reads as a teleport.
3. **Squash and stretch preserve volume.** Squash wider when you flatten, narrow when you stretch,
   or the character reads as growing and shrinking.
4. **Key poses first, in-betweens last.** Draw the two or three extremes; judge the loop from those
   alone before adding a single in-between.
5. **Responsiveness is not frame count.** Gameplay should react on frame 1; the animation can catch
   up. Never gate input on a long anticipation unless the delay is the mechanic.
6. **One pivot, every frame.** Misaligned pivots read as jitter nobody can diagnose.

## Workflow

**Step 0 - budget and list.** Write the full animation list for the character with frame counts
   before drawing (idle 4, walk 8, run 8, jump 3, land 2, attack 5...). See
   `references/core-cycles.md` for defaults.

**Step 1 - key poses.** Draw the extremes only: contact and passing for a walk, wind-up and strike
   for an attack. Flip between them to test.

**Step 2 - timing.** Assign a duration per frame, not one rate for the whole clip. Slow into
   anticipation, fast through the action, medium on recovery. See `references/timing-and-spacing.md`.

**Step 3 - in-betweens.** Add only where the eye needs them: arcs, overlaps, contact moments.

**Step 4 - secondary motion.** Hair, cloth, weapon, ears, tail - one or two frames behind the body.

**Step 5 - test in motion, in game.** At true size, on real backgrounds, at the real speed, with
   the real input. Most animation problems are only visible in play.

**Step 6 - export.** Layout, pivots, tags, per-frame durations. See
   `references/spritesheets-and-export.md`.

## References

| File | Read it for |
| --- | --- |
| `references/timing-and-spacing.md` | Playback rates, per-frame durations, easing with frame repeats, the principles that matter at low resolution, smears and multiple exposure, arcs, overlap, common timing defects |
| `references/core-cycles.md` | Pose-by-pose breakdowns and frame counts for idle, walk, run, jump, land, turn, climb, swim, death, plus top-down and eight-direction notes |
| `references/impact-and-combat.md` | Attack anatomy with wind-up/active/recovery windows, telegraphs, hit-stop, hit reactions, cancel windows, projectile and enemy tells |
| `references/spritesheets-and-export.md` | Sheet layout, pivots and anchors, naming and tagging, per-frame durations, padding and bleed, engine import notes, root motion vs code movement |

## Companion skills

| Skill | Hand off when |
| --- | --- |
| `../pixel-art-fundamentals/SKILL.md` | Frame drawing craft, keeping detail consistent across frames |
| `../color-and-palettes/SKILL.md` | Flash colours, status tints, keeping palettes stable across frames |
| `../vfx-and-lighting-2d/SKILL.md` | Impact effects, trails, screen shake, dust, hit flashes |
| `../game-ui-and-hud/SKILL.md` | UI motion, juice on menus and bars |
| `../game-art-pipeline/SKILL.md` | Atlas packing, dither crawl, filtering, engine import settings |

## Failure modes

| Symptom | Real cause | Fix |
| --- | --- | --- |
| "Looks robotic" | Uniform frame durations | Vary timing: hold the anticipation, rush the action |
| "Feels floaty" | No weight cues: no squash on landing, symmetric up/down timing | Fast fall, hard land frame, 1-2 frame squash, dust puff |
| "Character slides" | Foot contact moves while the body translates | Lock the contact foot to the ground per frame; match cycle length to move speed |
| "Feels unresponsive" | Input waits for the animation | React on frame 1, play anticipation concurrently or shorten it |
| "Jitters" | Pivot drift between frames, or odd-pixel bouncing | Fix the pivot; keep vertical bob to even pixel steps |
| "Attack comes out of nowhere" | No telegraph | Add 2-3 frames of readable wind-up with a distinct silhouette |
| "Hits feel weak" | No hit-stop, no reaction, no effect | 2-4 frames of freeze, white flash, knockback, impact sprite |
| "Looks like it flickers" | Dither or detail changing phase between frames | Lock dither and texture to the form, not the frame |

## Answering style

- Always give frame counts and per-frame durations: "5 frames: 100 ms, 60 ms, 40 ms, 80 ms, 120 ms".
- Describe poses, not adjectives: "contact pose: front heel down, rear toe up, torso at its lowest".
- Separate art fixes from code fixes; "floaty" is often gravity and jump curves, not frames.
- Offer the cheapest version first: which two frames get 80% of the effect.
