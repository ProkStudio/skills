# Colour management

## Why it matters

Blender renders in scene-linear space, then a **view transform** maps that to your display. Judging
materials or colour without knowing which transform is active is guesswork - the same render can look
flat, punchy or clipped depending on it.

Settings live in Render Properties > Color Management: View Transform, Look, Exposure, Gamma,
Sequencer/Display device.

## View transforms

| Transform | Behaviour | Use |
| --- | --- | --- |
| **AgX** | Default since Blender 4.0. Handles about 16.5 stops of dynamic range, rolls off highlights gracefully and desaturates them toward white | General rendering; anything with bright lights |
| **Filmic** | The old default; deprecated and superseded by AgX | Only for matching older projects |
| **Standard** | Straight sRGB, no tone mapping; clips hard above 1.0 | Texture and UI work, flat colour output, matching source colours exactly |
| **Filmic Log** | Log encoding of the scene | Intermediate for grading pipelines |
| **Raw** | No transform at all | Data passes, non-colour output |
| **False Color** | Maps luminance to a colour heat map | Exposure diagnosis; read it against its legend |
| **Khronos PBR Neutral** | Tone mapper that preserves albedo colour accuracy under bright light | Product visualisation, e-commerce, material accuracy |

Practical guidance:

- Keep **AgX** for lit renders. Its highlight desaturation is physically motivated (real cameras and
  eyes do the same), so fighting it with saturation nodes usually looks worse.
- Switch to **Standard** when you need the exact colour you authored - texture bakes, flat graphics,
  UI elements, colour references.
- Use **False Color** to find blown highlights and under-exposed areas before critiquing a look.
- Use **Khronos PBR Neutral** when the client needs the product's real colour to survive the render.

## Recovering vibrancy under AgX

AgX intentionally desaturates bright values. If the render looks washed out:

1. Check exposure first - most "AgX looks flat" cases are simply over-exposed.
2. Adjust **before** the transform: exposure, gamma, and contrast in the compositor operate on
   scene-linear data, which is where those adjustments belong.
3. Use the Look presets (various contrast options) rather than pushing saturation after the transform.
4. Reduce the intensity of the brightest lights instead of raising saturation - highlights desaturate
   because they are bright.
5. For a graded workflow, render to EXR and grade elsewhere; the EXR keeps the full scene-linear data.

## Which formats bake the view transform

| Format | View transform baked in? |
| --- | --- |
| PNG, JPEG, BMP, TIFF | Yes - what you see is what is saved |
| OpenEXR, Radiance HDR, DPX | No - scene-linear/log data is written, the transform is not applied |

Consequences:

- An EXR opened in a viewer with no colour management looks flat and dark. That is correct: it holds
  raw data.
- Never deliver an EXR as a final image to a non-technical client without a graded LDR version.
- For compositing and grading, EXR is the right choice precisely because the look is not baked.
- For data maps and baked textures, use PNG/TIFF with the image set to Non-Color and the view
  transform set to Standard/Raw so nothing is applied.

## Texture colour spaces

| Texture | Colour space |
| --- | --- |
| Base colour / albedo / diffuse | sRGB |
| Normal, roughness, metallic, AO, height, masks, ID | Non-Color |
| HDRI / environment | Linear Rec.709 or the file's own (EXR/HDR handled automatically) |
| Emission colour | sRGB |
| Photographic reference used as colour | sRGB |

Getting this wrong is the most common texture bug: a normal map read as sRGB gives subtly wrong
shading, and an albedo read as Non-Color looks washed out and pale.

## Exposure and light values

- Work with physically plausible light strengths (in watts for point/area lights, or W/m2 for the
  world) and use Exposure to set the overall level, rather than dialling arbitrary light values.
- Film-style workflow: set the key light for correct exposure on the subject, then balance fill and
  rim as ratios, then adjust Exposure once for the whole image.
- Check with False Color: the subject's midtones should sit in the middle of the legend, with only
  intended highlights in the top band.

## Displays and delivery

- Calibrate the monitor if colour accuracy matters; otherwise colour decisions are unrepeatable.
- For video delivery, confirm the target space (Rec.709 for HD, Rec.2020/HDR pipelines differ) and
  render EXR sequences for grading rather than baked LDR frames.
- For web and thumbnails, sRGB PNG or high-quality JPEG with the view transform baked is correct.
- Keep the same view transform across a project; comparing shots rendered with different transforms
  is meaningless.

## Colour-management checklist

1. View transform known and consistent across the project.
2. Exposure set before judging saturation or contrast.
3. False Color used at least once per lighting setup.
4. All data textures set to Non-Color; all colour textures sRGB.
5. Deliverables chosen with the bake-in behaviour in mind (EXR for grading, PNG/JPEG for final).
6. Standard/Raw used when authoring or baking textures.
7. Grading done pre-transform in the compositor, or downstream from EXR.
