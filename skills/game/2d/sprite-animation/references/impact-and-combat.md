# Attacks, impact and game feel

## Attack anatomy

Every attack has three windows, and the animation must make them legible:

| Window | Frames (typical) | Player reads it as | Art job |
| --- | --- | --- | --- |
| Wind-up / anticipation | 2-4 | "Something is coming" | Distinct silhouette, pulled back, often a colour or VFX tell |
| Active / strike | 1-2 | "It is happening now" | Biggest pose change, smear or trail, maximum extension |
| Recovery | 2-4 | "I can punish now" | Overshoot then settle; slower than the strike |

Gameplay rules of thumb: the strike frames should be the *fewest* frames and the wind-up the most
readable. Fast weak attacks get 2-frame wind-ups; slow heavy attacks get 4-6 and a clearer tell.

## Telegraphs

For anything the player must dodge:

- Silhouette change first - a new shape reads faster than a colour.
- Hold the wind-up frame. A telegraph that plays for 3 ticks is not a telegraph.
- Add one non-animation channel: a flash, a glow, a sound, a ground marker.
- Keep each enemy's tells distinct from each other, not just from its own idle.

## Hit-stop (freeze frames)

On impact, freeze both attacker and target for 2-5 frames (roughly 30-80 ms). This is the cheapest,
most effective "juice" in 2D combat: it sells mass, gives the eye time to register the hit, and
makes the same animation feel twice as strong.

Combine with:

- **Hit flash** - swap the target's palette to solid white (or the damage colour) for 2-3 frames.
- **Knockback** - a few pixels of displacement, eased out.
- **Impact sprite** - a 3-5 frame burst at the contact point, not centred on the enemy.
- **Screen shake** - small amplitude, fast decay. See `../../vfx-and-lighting-2d/SKILL.md`.

Hit-stop is code, not art, but the animation must be authored with a frame that is worth freezing.

## Cancel windows and responsiveness

- Gameplay reacts on frame 1 of input; art can lag behind.
- Allow the recovery window to be cancelled into movement or the next attack, or combat feels like
  wading. Long uncancellable recoveries are a deliberate design choice (heavy games), not a default.
- Never require the player to watch a full anticipation before the game accepts input unless the
  delay itself is the mechanic.
- Buffer input during hit-stop so combos feel tight.

## Projectiles

- Spawn frame: a muzzle flash or launch puff at the origin, 2-3 frames.
- Travel: 2-4 looping frames, plus a trail. Keep the silhouette readable against busy backgrounds -
  reserve a bright value for projectiles (`../../color-and-palettes/references/readability-and-contrast.md`).
- Impact: a separate 3-6 frame burst that does not loop, aligned to the surface hit.
- Rotating a pixel projectile breaks the grid; draw 4-8 discrete angles instead.

## Enemy and boss patterns

- Every attack gets a matching "recover" pose so the player can learn the rhythm.
- Vary timings between attacks in a moveset, not within a single attack's repetitions - players
  learn fixed timings and feel cheated by random ones.
- Boss phase changes deserve a dedicated 6-12 frame transition; it is the cheapest way to make a
  fight feel structured.

## Feel checklist

1. Does input produce a visible change within 1-2 frames?
2. Is there a distinct silhouette for wind-up, strike and recovery?
3. Is there hit-stop, a flash, and one particle burst on every landed hit?
4. Does the landing of a jump have its own frame and its own dust?
5. Can you tell what happened from a single screenshot of the strike frame?
6. Does anything freeze the player longer than about 400 ms without a design reason?
