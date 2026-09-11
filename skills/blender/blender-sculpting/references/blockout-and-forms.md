# Blockout and form hierarchy

## Where to start

| Starting point | When |
| --- | --- |
| UV sphere or cube + Voxel Remesh | Heads, creatures, free-form organic shapes |
| Simple box-modelled base mesh | When you know the proportions and want control |
| Primitives joined per body part | Characters and creatures with clear masses |
| Skin modifier on an armature-like edge skeleton | Fast gesture blockouts of limbed creatures |
| Metaballs converted to mesh | Blobby organic starting volumes |
| Existing base-mesh library | Production speed; a human base saves hours |

Whatever the start, keep it **low resolution**: 5-20k triangles is plenty to judge proportion, and
low resolution forces you to look at shape rather than detail.

## Gesture and proportion

1. Set real-world scale first - a human 1.7-1.85 m tall. Sculpting at the wrong scale breaks brush
   radius intuition and later physics and DOF.
2. Establish **gesture**: the line of action through the pose. A technically correct but gestureless
   figure looks dead.
3. Block major masses as separate simple volumes: cranium, jaw, ribcage, pelvis, limb segments.
4. Check proportions against reference with orthographic front/side views, but judge the final look
   in perspective from the intended camera.
5. Common proportion anchors for a realistic human: 7.5-8 heads tall, elbow at navel level, wrist at
   crotch level, knee midway between hip and floor, shoulder width about 2 head widths.

## Form hierarchy for organics

| Level | Content | Brush scale |
| --- | --- | --- |
| Primary | Overall masses and silhouette | Radius 30-60% of the form |
| Secondary | Muscle groups, skull planes, major folds, fat pads | 10-25% |
| Tertiary | Wrinkles, pores, scales, stitching, damage | under 5% |

Discipline rules:

- Do not advance a level until the previous one reads from a distance and in silhouette.
- If a sculpt looks wrong at tertiary stage, the error is almost always at primary or secondary.
- Squint or blur your view (or zoom out far) to test whether the big shapes read.

## Planes and edges

Organic forms are not soft everywhere. Every convincing sculpt has:

- **Planes**: flat or near-flat facets (the sides of the nose, the front of the shin, the forehead
  planes). Build them with Flatten, Scrape and Multiplane Scrape.
- **Transitions**: where two planes meet, sharp on bone, soft over fat and muscle.
- **Rhythm**: alternating convex and concave curves along a limb; two identical curves in a row look
  mechanical.

Soft everywhere = muddy. Hard everywhere = plastic. Contrast between hard bone landmarks and soft
tissue is what reads as organic.

## Anatomy checkpoints

For human and humanoid work, verify these before detailing:

- **Skull**: cranium mass vs face mass; brow ridge, temple depression, zygomatic arch, jaw angle.
- **Facial thirds**: hairline to brow, brow to nose base, nose base to chin - roughly equal.
- **Eyes**: eyeball is a sphere set in a socket; lids wrap over it with thickness.
- **Nose**: bone at the top, cartilage below; the tip is not a sphere.
- **Ears**: top aligns roughly with the brow, bottom with the nose base.
- **Torso**: ribcage and pelvis as two solid masses; the waist is soft tissue between them.
- **Limbs**: bony landmarks at elbow, wrist, knee, ankle; muscle bellies offset, never symmetric
  around the bone.
- **Hands and feet**: built from a mass plus digits; finger joints step down in size.

For creatures, apply the same logic with borrowed anatomy: pick real animals for skull, limb and
muscle logic instead of inventing.

## Stylisation

- Stylisation means deliberate exaggeration, not omission: pick what to push (eye size, jaw, hands)
  and simplify the rest.
- Keep shape language consistent - rounded shapes throughout, or angular throughout.
- Stylised work usually needs **cleaner** surfaces than realism: every lump is visible because there
  is no texture noise to hide it.
- Simplify anatomy into clear, big shapes that still obey the underlying structure.

## Symmetry

- X-symmetry on by default for the blockout and most of the sculpt.
- Use Mesh > Symmetrize (or the sculpt Symmetrize under Remesh) to force one side onto the other
  after asymmetric slips.
- Break symmetry deliberately at the end: pose, asymmetric detail, tilted features. A perfectly
  symmetric face looks uncanny.
- Symmetry uses the object origin. If it mirrors in the wrong place, the origin or an unapplied
  transform is the cause.

## Blockout review checklist

1. Real-world scale set.
2. Gesture present and readable in silhouette.
3. Masses blocked as simple volumes, low resolution.
4. Proportions checked against reference in perspective.
5. Planes established before any smoothing pass.
6. Anatomy checkpoints verified.
7. A saved version exists before increasing resolution.
