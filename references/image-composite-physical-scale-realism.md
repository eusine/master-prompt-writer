# Image Composite Physical Scale Realism

Use when an image edit/composite asks for a large prop, tower, pile, installation, furniture replacement, or object mass that must feel physically plausible around a person.

## Trigger signals
- User says the result is too unrealistic, weightless, skinny, toy-like, or not matched to the model’s proportions.
- The prompt replaces an object with many repeated items: clothing piles, boxes, books, chairs, bags, flowers, products.
- A person sits/stands/climbs on the generated object.

## Prompt moves
1. **Scale lock against the body** — give approximate real-world dimensions relative to the model. Example: `2.4–2.8 m tall, 1.8–2.2 m wide heavy base, tapering upward so it can support her`.
2. **Quantity density** — prevent “a few oversized objects” by naming count impression: `hundreds to over a thousand real pairs/items compressed into a dense installation`.
3. **Load-bearing geometry** — broad base, tapering top, center of mass under the person, no impossible skinny columns.
4. **Gravity and compression** — lower layers flattened by weight, middle layers bulge/sag, top layers tightly packed with visible dents where the person sits/stands.
5. **Contact proof** — contact shadows, pressure dents, fabric/object deformation, grounding, small gaps, realistic pile geometry.
6. **Support realism** — allow hidden internal support if needed, but keep visible surfaces aligned with the requested material: `Hidden support may be implied, but every visible surface is denim`.

## Compact clause template
```text
Make the <object> realistic and model-scale: <height> tall, <base width> wide heavy base, tapering upward so it can support her. It must read as hundreds to over a thousand real <items> compressed into a dense installation, not a few oversized props. Lower layers are flattened by weight; middle layers bulge and sag; top layers are tightly packed with visible dents where she sits. Show gravity, contact pressure, shadows, compression, gaps, realistic pile geometry. Hidden support may be implied, but every visible surface is <material>.
```

## Pitfall
Do not rely on “realistic” alone. For load-bearing props, realism must be translated into scale, base width, density, compression, contact shadows, and support logic.