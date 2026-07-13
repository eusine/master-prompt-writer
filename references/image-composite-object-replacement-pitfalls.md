# Image composite object replacement pitfalls

Session learning: when a user wants a reference scene but wants one object class fully replaced, prompts that say only “replace the lower/base section” often leave remnants of the original object.

## Durable rule

For full object replacement, write the source reference as limited to composition/lighting/mood only, then explicitly forbid retaining the replaced object class anywhere.

Good pattern:

```text
Use image 2 only as the composition, lighting, white studio, and surreal editorial mood reference. Do not keep the chair objects from image 2. Replace the entire stacked plastic-chair structure with a sculptural tower/mound made only of denim jeans. No plastic chairs should remain anywhere: no chair legs, backs, seats, hidden silhouettes, or leftover colorful plastic furniture.
```

## Format preference captured

If the user asks not to split sections, output one copy-paste block that includes both main positive directions and negative constraints. Do not separate “main prompt” and “negative prompt” unless they ask for that format or the target UI requires separate fields.
