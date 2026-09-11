# Critique checklist

Run these in order. Each test isolates one class of defect, and the early tests catch the
expensive problems.

## The tests

1. **Silhouette test.** Fill the sprite with one solid colour. Is it still identifiable? Does it
   have a distinctive contour rather than a blob? Fix here first - shading cannot rescue a shape.
2. **Value test.** Desaturate. Do figure and background separate? Is there a clear lightest and
   darkest area, or is everything mid-grey?
3. **Squint / 50% test.** Squint, or scale to 50%. Big shapes should survive; detail should blur
   into tone. If the sprite falls apart, detail is doing work that shapes should do.
4. **1:1 test.** Look at it at the exact size players will see. Not 400%.
5. **Motion / context test.** Put it in the engine, on the real backgrounds, moving. AA halos,
   dither crawl and value collisions only appear here.
6. **Flip test.** Mirror horizontally. Asymmetric mistakes become obvious.
7. **Palette audit.** Count unique colours. Semi-transparent leftovers from a soft brush,
   near-duplicate colours and off-palette pixels all show up here.
8. **Set test.** Put the asset next to three others from the project. Same pixel density? Same
   outline rule? Same light direction? Same saturation range?

## Symptom to fix

| What you see | Name | Fix |
| --- | --- | --- |
| Dark rim, light middle, no direction | Pillow shading | Pick a light direction, shade planes not edges |
| Thick parallel stripe along a diagonal | Banding | Band compression, vary run lengths, or remove a value |
| Scattered single pixels, "dirty" look | Noise / orphan pixels | Merge into clusters of 2+, delete the rest |
| Irregular steps in a curve | Jaggies | Rebuild with a monotone step pattern, then AA |
| A 1 px bump next to a long run | Doubles | Merge the stray pixel into its neighbour |
| Everything mid-tone, no punch | Muddy values | Cut to 3 values, push extremes apart |
| Soft ghost edge over some backgrounds | AA halo | Remove outer AA or move it inside the outline |
| Some pixels twice the size of others | Mixed density | Redraw at the project grid; never non-integer scale |
| Sprite floats | No contact shadow | Add a dark contact shadow or ground ellipse |
| Reads as texture close up, grey far away | Over-dithering | Replace dither with a real colour step |
| Busy but unreadable | No detail hierarchy | 60/30/10 budget; strip 20% of detail pixels |
| Characters vanish against the level | Value collision | Reserve a value range for characters, mute backgrounds |
| Two assets look like two different games | Convention drift | One outline style, one light direction, one palette |

## Giving feedback on someone else's sprite

- Lead with what already works, specifically: "the silhouette reads instantly, the helmet shape is distinctive".
- Name the defect using the table above. A name is teachable; "it looks off" is not.
- Give one concrete fix with pixel counts: "drop the outline to a dark brown on the lit side",
  "cut the mid-tone so you have three values".
- One priority per round. If the silhouette is wrong, do not discuss dithering.
- Separate "this breaks a rule" from "this is not my taste", and say which you are doing.
