# Readability, contrast and accessibility

Gameplay readability beats beauty. A gorgeous scene where the player cannot find their own
character is a broken scene.

## Figure to ground

The separation that works is **value**, then **saturation**, then **hue** - in that order of
reliability. Two colours of the same value will merge no matter how different their hues are,
especially in motion, at small sizes, and for colour-blind players.

Practical zoning for a side-scroller or top-down game:

| Layer | Value band | Saturation | Notes |
| --- | --- | --- | --- |
| Far background | Light or very dark, low contrast internally | Low | Should read as atmosphere, not objects |
| Midground / level geometry | Mid band, moderate internal contrast | Low-medium | This is where most of the screen lives |
| Interactive objects | Steps away from the midground band | Medium-high | Doors, chests, ladders, switches |
| Characters and enemies | Reserved band at one end of the range | High | Never share the midground's exact values |
| VFX and projectiles | Brightest values in the game | Highest | Reserve near-white and a saturated accent for these |

If a character still gets lost, do not recolour the character first. Mute the background: drop its
saturation by a third and pull its values toward the middle.

## Silhouette and edge tricks

- A 1 px rim in a contrasting value around characters keeps them readable over any background
  (subtle in art, common in fighting games and bullet hells).
- A darker "vignette" band behind gameplay space separates playfield from decoration.
- Depth-of-field by value compression: distant layers use a narrower value range, closer layers a
  wider one. See `../../tilesets-and-environments/references/depth-and-parallax.md`.

## UI and text contrast

- Aim for a contrast ratio of at least 4.5:1 between body text and its background, 3:1 for large
  text and for UI shapes that carry meaning. These are the WCAG thresholds; games are not legally
  bound by them but players' eyes are.
- Never put text directly on busy art. Use a panel, a scrim (semi-transparent dark layer), or an
  outline/shadow on the glyphs.
- Test UI on a phone screen in daylight and on a dim TV. These two cases kill most subtle palettes.
- Details in `../../game-ui-and-hud/references/typography-and-icons.md`.

## Colour language for gameplay

Pick conventions and hold them for the whole game:

| Meaning | Common convention | Caveat |
| --- | --- | --- |
| Health | Red or green bar | Red also often means danger; pick one meaning per hue |
| Damage / hazard | Red, orange, or a strong outline | Distinguish "hostile" from "hot" with shape |
| Interactive | One reserved accent colour plus an animated glint | Never use the accent for decoration |
| Team / faction | Hue swap on the same sprite | Add a shape badge for colour-blind play |
| Rarity tiers | Grey - white - green - blue - purple - orange | The genre convention; deviating costs comprehension |
| Status effects | Icon plus tint | Tint alone fails on busy sprites |

## Colour-blindness

About 8% of men and 0.5% of women have some form of colour vision deficiency; red-green types
(deuteranomaly, protanomaly) are by far the most common.

Rules:

- Never encode information in hue alone. Pair colour with icon, shape, value, pattern, or position.
- Avoid red-versus-green as the only distinction between two states. Red-versus-blue and
  light-versus-dark survive almost all deficiency types.
- Keep a value difference between any two colours that must be told apart - value survives every
  deficiency type.
- Simulate deuteranopia and protanopia on screenshots during development, not at the end. Many
  image editors and engine plugins do this; a greyscale check catches most of the same problems.
- If you offer colour-blind modes, change the *palette assignments*, not just a global filter.

## Testing procedure

1. Greyscale the screenshot. Can you still play it?
2. Squint or downscale to 25%. Do characters and hazards still pop?
3. Simulate deuteranopia. Any state pairs that merge?
4. View on a phone in bright light and on an uncalibrated TV.
5. Ask someone to point at "the thing that will kill you" in a still frame. If they hesitate, the
   colour plan failed, not the player.
