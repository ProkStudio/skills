# Animation craft

## Principles that change a shot

| Principle | What it means in practice |
| --- | --- |
| Timing | How many frames an action takes; the difference between heavy and light |
| Spacing | How motion is distributed between keys; where the ease lives |
| Anticipation | A small opposite motion before the main action |
| Follow-through and overlap | Parts arrive late and settle after the main mass stops |
| Arcs | Nearly all natural motion follows curves, not straight lines |
| Squash and stretch | Volume-preserving deformation that sells weight and impact |
| Exaggeration | Push the pose past reality so it reads |
| Contrast | Fast against slow, still against moving; uniform motion is invisible |
| Silhouette / staging | The pose must read as a black shape |
| Secondary action | Supporting motion that adds character without stealing focus |
| Successive breaking of joints | A whip-like sequence through a chain (hips, chest, shoulder, elbow, wrist) |
| Moving holds | Never a completely frozen frame; drift slowly instead |

## Blocking to spline

1. **Plan**: thumbnails, reference video, or acting it out. Decide the key storytelling poses.
2. **Blocking**: set the key poses with **Constant** interpolation (stepped). Judge only poses and
   timing. No polish.
3. **Breakdowns**: add the in-between poses that define the path of action - still stepped.
4. **Spline**: switch to Bezier, then fix the mess the interpolation created. Expect this to feel
   worse before it feels better.
5. **Polish**: arcs, overlap, follow-through, contact fixes, finger and facial detail.
6. **Review in real time**: play at the correct frame rate, and check silhouettes and flipbook-style
   pose readability.

Useful habits: key all channels on the same frames during blocking (easier to retime), use the
Breakdowner tool (Shift+E-style pose breakdown) to place in-betweens, and keep a rest/reference
action for comparison.

## Walk and run cycles

A walk cycle at 24 fps is commonly 24 frames (one step per 12 frames); a run is 12-16 frames total.

Key poses per step:

| Pose | Content |
| --- | --- |
| Contact | Heel strike, legs at maximum spread, arms at opposite extremes |
| Down (recoil) | Body at its lowest, weight absorbed, knee bent |
| Passing | Free leg passes the support leg, body at mid height, hips rotated |
| Up | Body at its highest, support leg nearly straight, push-off |

Also true of most cycles:

- Hips lead: rotation (tilt and twist) plus a two-per-step vertical bob.
- Shoulders counter-rotate against the hips.
- Arms swing opposite to the legs, with a late wrist.
- Head stays relatively level; it is the last thing to bounce.
- For a run, add an airborne phase and a deeper contact compression.
- Cycle mechanics: copy the first frame to the last, then use a Cycles F-Modifier or NLA repeat.

For game cycles, keep the character in place and let the engine move it, unless the engine uses root
motion (see `game-rigs-and-export.md`).

## Graph editor discipline

| Concept | Guidance |
| --- | --- |
| Interpolation | Bezier for organic motion, Linear for mechanical/constant, Constant for stepped blocking and snappy holds |
| Handle types | Auto Clamped avoids overshoot, Aligned gives smooth control, Free for asymmetric ease, Vector for linear-in/out |
| Easing | Ease Out of a pose and Ease In to the next; equal spacing reads as robotic |
| Overshoot | Let a curve pass the target and settle back for weight - deliberate, not accidental |
| Normalize | Turn on to compare channels with different scales |
| Clean Keyframes | Removes redundant keys after baking or heavy editing |
| F-Modifiers | Cycles for loops, Noise for handheld or organic jitter, Generator for procedural motion |
| Channel groups | Keep bones grouped; hide what you are not working on |

Curve reading shortcuts: a straight diagonal is constant speed; a flat section is a hold; an S-curve
is ease in and out; a spike is a snap. Floaty animation almost always shows as long, gentle S-curves
everywhere.

## Rotation modes and gimbal

- Quaternions for bones that rotate freely - no gimbal lock, but curves are hard to read.
- Euler (XYZ) for controls where you want readable single-axis curves; watch for gimbal lock when two
  axes align.
- Avoid mixing: choose per bone and keep it consistent through a shot.
- If an Euler channel flips 360 degrees, fix it with Discontinuity (Euler) Filter in the graph editor
  channel menu.

## Actions and the NLA

- Each animation is an **action**. Name them clearly (`run_fwd`, `idle_breathe`, `attack_01`).
- Push actions into the NLA editor as strips to layer, blend, repeat and offset them.
- NLA blending: Replace, Combine, Add; use Combine for additive layers like breathing or a lean.
- Use strip extrapolation and repeat for cycles; use the strip's Action Clip settings for offsets.
- Enable Fake User on actions you want kept in the file even when unassigned, or they will be purged.
- Recent Blender versions (4.4 onward) support slotted actions, where one action holds animation for
  multiple data-blocks; check the version before relying on that structure in a pipeline.

## Frame rates

| Rate | Use |
| --- | --- |
| 24 fps | Film, cinematic, most character animation reference |
| 25 / 30 fps | Broadcast, some game cinematics |
| 30 / 60 fps | Games, real-time playback |
| 12 fps (on twos at 24) | Stylised, hand-drawn feel |

Set the frame rate before animating. Changing it later rescales nothing automatically, and retiming
an animated shot is real work.

## Polish pass checklist

1. Silhouette reads on every key pose.
2. Arcs smooth: track a hand or head through the shot and look for kinks.
3. Timing has contrast: fast and slow sections, not uniform.
4. Anticipation before big actions; follow-through after them.
5. Overlap: chains break successively, extremities arrive late.
6. No dead holds - moving holds instead.
7. Contacts locked: feet do not slide, hands do not float off surfaces.
8. Facial and finger detail last, not first.
9. Played back in real time at the final frame rate.
