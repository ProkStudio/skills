# Juice: mapping actions to feedback

"Juice" is not decoration. Every player action should produce an immediate, unmistakable response in
at least two channels (visual, audio, haptic, camera).

## Action-to-feedback table

| Action | Visual | Camera / time | Audio | Cheap version |
| --- | --- | --- | --- | --- |
| Jump | 2-frame squash, small dust puff | - | Short whoosh | Dust puff only |
| Land | 2-frame squash, dust ring | 1-2 px shake for hard landings | Thud, pitch by fall height | Squash frame |
| Dash | 3 afterimages, speed lines | Slight FOV/zoom or 2 px shake | Whoosh | Afterimages |
| Attack swing | Weapon trail arc, 1 smear frame | - | Swing sound | Trail arc |
| Hit landed | White flash 2-3 frames on target, spark burst, knockback | 2-5 frames hit-stop, 2-4 px shake | Impact layered with material sound | Hit-stop + flash |
| Critical hit | Bigger burst, different colour, damage number | 4-6 frames hit-stop, brief time slow | Distinct higher-pitch hit | Colour change + longer stop |
| Player takes damage | Red vignette pulse, character flash, knockback | 3-6 px shake, 2-4 frames stop | Low thud + pain cue | Vignette + flash |
| Enemy death | Death animation or burst, debris | Small shake, brief slow on the last enemy | Layered death sound | Burst + debris |
| Pickup | Sparkle, pop-scale, item arcs to HUD | - | Bright ping | Pop-scale |
| Level up / unlock | Radial burst, colour wash, UI flourish | Short slow-motion | Fanfare | Radial burst |
| Door / switch | Movement plus a light change | - | Mechanical clunk | Light change |
| Death | Full-screen flash, slow motion, fade | Time scale down to ~0.2, hold | Distinct stinger | Flash + slow fade |

## Hit-stop

- 2-3 frames for light hits, 4-6 for heavy, 6-10 for finishers (at 60 fps, roughly 30-100 ms).
- Freeze both attacker and target; keep particles and UI running so the screen does not look hung.
- Buffer player input during hit-stop, or the game feels like it drops inputs.
- Hit-stop is the highest-impact, lowest-cost feel improvement in a 2D action game.

## Screen shake

- Duration 80-200 ms. Anything longer is noise.
- Amplitude 1-3 px for small events, 4-8 px for explosions, at native resolution. Scale with the
  pixel scale, not with the window size.
- Use a fast decay curve (exponential), random direction per frame, and cap the maximum offset.
- Prefer trauma-based shake: events add "trauma", trauma decays, shake = trauma squared. Multiple
  events then blend instead of stacking.
- Always give players an option to reduce or disable shake
  (`../../game-ui-and-hud/references/accessibility.md`).

## Flashes and time

- **Target flash**: replace the sprite's palette with a single bright colour for 2-3 frames. Cheap
  shader or a pre-rendered white silhouette frame.
- **Screen flash**: a full-screen fill at low alpha for 1-2 frames. Use very sparingly; it is
  fatiguing and a photosensitivity risk.
- **Time scale**: drop to 0.3-0.5 for 150-400 ms on major events (boss death, last enemy, perfect
  dodge). Never during normal combat flow.
- **Freeze frames** for finishing blows: hold 100-200 ms, then resume with extra shake.

## Camera work

- Small look-ahead in the movement direction, smoothed, makes movement feel responsive.
- Punch-in zoom of 2-5% on big impacts, then ease back. With pixel art, prefer shake to zoom, since
  non-integer zoom breaks the grid.
- Keep the camera snapped to whole pixels every frame.

## Density budget

Juice is a currency; spend it on rare, important events:

| Frequency | Allowed intensity |
| --- | --- |
| Several times per second (steps, basic hits) | Tiny: 1-2 px shake at most, small particles, short sounds |
| Every few seconds (kills, pickups) | Medium: hit-stop, flash, particle burst |
| Once per minute (boss phase, level up) | Large: time scale, screen effects, fanfare |
| Once per session (boss kill, ending) | Everything |

If every event is loud, none of them read. When a scene feels chaotic, cut the frequent effects
first, not the rare ones.

## Audit checklist

1. Does every player input produce a visible change within 1-2 frames?
2. Does every landed hit have freeze, flash, particle and sound?
3. Is there any state where the player cannot tell whether an action registered?
4. Are frequent effects quieter than rare ones?
5. Is the screen still readable during the busiest fight in the game?
6. Can shake, flashes and time-scale effects be reduced in options?
7. Remove every effect for one playtest: which removals hurt most? Those are the ones worth polishing.
