# Core cycles, pose by pose

Frame counts below are practical defaults for pixel art at 10-12 fps. Halve them for a tight
budget; the poses marked *key* are the ones you cannot cut.

## Idle (2-6 frames)

- 2 frames: a 1 px vertical bob. Cheap, reads as "alive" at a distance.
- 4 frames: breathe in (chest up, shoulders up 1 px), hold, breathe out, hold. Add a 1-frame blink
  every few loops.
- 6+ frames: add secondary motion - hair sway, cape settle, weapon shift.
- Hold one frame noticeably longer than the others, or the idle pulses like a light.

## Walk (4, 6 or 8 frames)

Key poses, in order:

1. **Contact** *key* - legs at their widest, front heel down, rear toe up. Body at mid height.
2. **Down / recoil** - weight lands, body at its lowest, support knee bent.
3. **Passing** *key* - legs cross, free leg lifted, body rising, weight over the support foot.
4. **Up** - body at its highest, support leg straight, push-off beginning.

Then mirror for the other leg. A 4-frame walk uses contact and passing for each side; an 8-frame
walk uses all four per side.

Rules:

- The body bobs 1-2 px: lowest at down, highest at up. Without the bob a walk reads as a slide.
- Arms swing opposite the legs, one frame behind.
- The contact foot must not move relative to the ground while it is planted. If it does, the
  character skates - match the animation's stride length to the movement speed in code.
- Head stays relatively stable; torso does the work.

## Run (6-8 frames)

- Deeper body lean forward, bigger vertical travel (2-4 px), knees higher, arms bent.
- Include one airborne frame where both feet are off the ground - that single frame is what
  separates a run from a fast walk.
- Longer strides, fewer contact frames, wider spacing.

## Jump and fall (3-5 frames plus land)

1. **Anticipation** *key* - crouch, 1-2 frames, squashed.
2. **Take-off** - stretched tall, arms up, 1 frame.
3. **Rise** - neutral airborne pose.
4. **Apex** - hold 1 frame, limbs slightly gathered; this is the readable moment.
5. **Fall** - stretched downward, legs trailing.
6. **Land** *key* - 1-2 frames of squash plus a dust puff, then return to idle.

Fall faster than you rise (asymmetric gravity) - it reads as weight and makes platforming feel
better. Give the landing a real frame: a jump with no landing frame always feels floaty.

## Turn (1-3 frames)

A single transitional frame - body twisted, feet mid-pivot - removes the "instant mirror" snap that
makes 2D characters look like cardboard. Three frames if the character is large.

## Climb, swim, crouch-walk (4-6 frames)

- Climb: alternating reach with a 1 px body rise per grab; keep hands locked to rungs.
- Swim: long slow arcs, ease at the extremes, 6 frames minimum or it looks frantic.
- Crouch-walk: shorter stride, no vertical bob, head stable.

## Hit reaction (2-3 frames)

1. Sharp recoil pose away from the hit *key*, held 2-4 ticks (see hit-stop).
2. Mid-recovery.
3. Return to idle or stagger loop.

## Death (4-8 frames)

Pick a language and keep it: collapse (weight-driven, slow at the end), blow-apart (fast, VFX-heavy),
or fade/dissolve (2-3 frames plus a particle burst). Enemies that die identically feel cheap; a
2-frame difference per enemy family is enough variety.

## Top-down and eight-direction sets

- Four directions: draw down, up, side; mirror the side for the fourth. Down gets the most detail
  because players see it most.
- Eight directions: add the diagonals; they cost as much as the cardinals. Consider four directions
  plus a run-blend before committing.
- Keep the head position consistent between directions or characters appear to grow.
- Top-down walks need visible leg motion *and* a body bob; without the bob nothing reads.

## Budget table

| Character role | Sensible total |
| --- | --- |
| Basic enemy | idle 2, walk 4, attack 4, hit 2, death 4 = 16 frames |
| Player character | idle 4, walk 8, run 8, jump 4, land 2, attack 5-8, hit 2, death 6 = 40-45 |
| Boss | 60-120, mostly attacks and telegraphs |
| Prop / pickup | 2-4 (bob, glint) |

Budget per *cast*, not per character: twenty enemies at 16 frames is 320 frames of work.
