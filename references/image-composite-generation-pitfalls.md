# Image composite/generation prompt pitfalls

Session lesson: when a user starts from an image-composite prompt, then asks to generate a similar new image instead of compositing, switch the contract explicitly.

## 1. One-block output

For a single image edit/generation prompt, output one paste-ready code block. Do not split main prompt, stronger prompt, Korean note, and negative prompt into separate blocks unless the user asks for multiple variants. Fold constraints/negative-like exclusions into the same block.

## 2. Composite vs similar generation

If the user says "합성 말고 비슷하게 생성" or similar:

- Start with: `Generate an original image, not a composite.`
- Treat the model/reference photo as **styling inspiration**, not identity lock.
- Avoid exact cloning language such as `preserve her face` unless the user still wants same-person identity.
- Keep the reference model's observable style traits: hair shape, outfit category, silhouette, expression, shoes, posture energy.

## 3. Pose/composition anchoring

When the target composition is a reference image with a distinctive pose, describe the pose mechanically, not only with mood words.

Useful anchors:

- subject position in frame: `near the upper third`, `centered vertical tower`, `full vertical frame`, `white negative space`
- body support: `hips anchored`, `perched sideways`, `seated high on the top mass`, `never flat on the floor`
- limb geometry: `one knee bent close`, `the other leg angled downward`, `long leg lines`
- torso/head: `torso twisted back toward camera`, `shoulders slightly turned`, `chin level`, `calm gaze`
- camera: `slightly low camera makes the tower feel tall`
- contact realism: `correct scale`, `contact shadows`, `grounding`, `not floating`

## 4. Replacing a persistent object class

If the model keeps leaving unwanted objects behind, demote the reference image to composition-only and make the replacement class total:

- `Use the reference only for pose/composition/lighting/mood.`
- `Do not preserve the [object] objects.`
- `Replace the entire [object] structure with [new material/object].`
- `Every visible structural part is [new material/object].`
- Put object remnants in the same constraints tail: `no chairs, no chair legs/backs/seats, no hidden chair silhouettes`.

## 5. Clothing vs prop collision

When the person's outfit uses the same material as the prop, distinguish them explicitly:

`Her worn jeans stay clothing; the denim pile is a separate sculptural prop.`
