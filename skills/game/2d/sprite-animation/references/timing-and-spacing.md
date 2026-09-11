# Timing, spacing and principles that matter

## Playback rate

Most 2D game animation is authored at 8-15 fps of *art* inside a 60 fps game. Common choices:

| Rate | Feel | Notes |
| --- | --- | --- |
| 6-8 fps | Choppy, retro, stylised | Cheap; works if poses are strong (early arcade, many indie games) |
| 10-12 fps | The standard for pixel art | One frame = 5 ticks at 60 fps; enough for readable motion |
| 15-20 fps | Smooth, more expensive | Detailed characters, fighting games |
| 24-30 fps | Very smooth, animation-heavy | Rotoscoped or vector 2D; rarely worth it in pixel art |

Prefer **per-frame durations** over a single clip rate. Almost every good animation has frames held
longer than others.

## Spacing is the message

Spacing - how far the subject moves between frames - communicates speed and weight:

- Even spacing = constant speed = machinery.
- Tight spacing at the ends, wide in the middle = ease in and out = organic motion.
- Wide spacing with a single in-between = fast, snappy action.
- A held frame before a fast move = anticipation; the eye reads the pause as tension.

In sprite animation you often cannot draw more in-betweens, so you "ease" by holding frames: show
the anticipation frame for 3 ticks, the action frame for 1.

## The principles that pay off at low resolution

| Principle | How it looks in a sprite |
| --- | --- |
| Anticipation | 1-3 frames moving *against* the coming action: crouch before a jump, pull back before a punch |
| Squash and stretch | Landing squashes 1-2 px shorter and wider; a leap stretches taller and narrower - volume constant |
| Follow-through | Cape, hair, weapon arrive 1-2 frames after the body stops |
| Overlapping action | Body parts start and stop at different frames; nothing moves in perfect unison |
| Arcs | Hands, feet and weapons travel curves, not straight lines |
| Slow in / slow out | Hold frames at the extremes, skip frames through the middle |
| Exaggeration | At 32 px, a subtle motion is invisible; push poses past realism |
| Solid drawing | Keep volume and proportion consistent frame to frame - easy to lose when redrawing pixels |
| Staging / silhouette | Every key pose must read as a black shape |
| Secondary action | One small extra motion (a blink, a tail flick) makes an idle feel alive |

Straight-ahead versus pose-to-pose: use pose-to-pose for anything gameplay-critical (you control
the key readable moments) and straight-ahead for chaotic effects like fire or smoke.

## Smears and multiple exposure

When a limb or weapon crosses a large distance in one frame, the eye expects a blur. Options:

- **Smear**: stretch the shape along its path for one frame - a long tapered streak.
- **Multiple exposure**: draw the limb two or three times in the same frame at different positions.
- **Motion trail**: draw only the path (an arc of bright pixels) and omit the limb entirely.

One frame is enough. Two consecutive smears read as slow motion. Smears are also a budget trick:
they let you skip in-betweens without the motion reading as a jump.

## Loops

- A loop needs an even number of contact beats for symmetrical motion (walks: 4, 6 or 8 frames).
- Check a loop by playing it at 3x speed; drift and pops become obvious.
- For idles, avoid a perfectly symmetric loop - a 4-frame breathe with one longer hold reads as
  alive, a 2-frame flip reads as a blinking light.
- Do not loop a motion that has a natural end (attack, land). Give it an explicit last frame.

## Common timing defects

| Defect | Cause | Fix |
| --- | --- | --- |
| Metronome feel | Every frame the same duration | Vary durations; hold extremes |
| Motion "pops" at loop point | First and last frames nearly identical | Delete one, or redraw the last frame as a true in-between |
| Too slow to read | Long uniform clip on a fast action | Cut frames, keep the extremes, shorten durations |
| Motion blur mush | Smears on several consecutive frames | One smear frame maximum |
| Nothing has weight | No held frames, no squash, symmetric rise and fall | Fall faster than you rise; hold the landing |
| Secondary motion fights the body | Hair and cloth animated in sync with the torso | Offset by 1-2 frames |
