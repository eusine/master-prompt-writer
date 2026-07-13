# Pixel-bound composite preservation

Use this when the user provides or asks for strict background replacement where the original person/photo must remain fixed: “absolute frame”, “identity preservation”, “pixel-bound composite”, “background only”, “no reframing”, “same crop”, “don’t move the subject”, or similar.

## Core move

Start by redefining the task as a locked composite, not image generation:

```text
This is a pixel-bound background replacement composite. Treat the original photo as the locked base plate: final canvas size, crop, aspect ratio, subject position, and subject bounding box stay identical. Subject pixels are read-only; only the background plate may change.
```

Then add scene/location/style details. Do not lead with the destination location; if the location comes first, many image models optimize framing and rebuild the person to fit the scene.

## Reusable qualified keywords

| term | effect | prompt tokens |
|---|---|---|
| pixel-bound composite mode | 이미지 편집을 자유 생성이 아니라 잠긴 원본 사진 위의 배경 교체로 고정한다 | locked photographic plate, background-only generation, hard fail framing |
| immutable base layer | 피사체 픽셀을 읽기 전용으로 두어 리샘플·워핑·포즈 재구성을 차단한다 | read-only subject pixels, no resampling, no silhouette change |
| absolute canvas lock | 입력 폭·높이·비율·크롭·피사체 좌표를 최종 결과의 유일한 프레임으로 삼는다 | identical canvas bounds, subject coordinate lock, no virtual camera shift |
| recognition over beauty | 미화보다 동일인 인식을 우선해 얼굴 평균화·대칭 보정·피부 스무딩을 막는다 | same individual recognition, no face averaging, microtexture preservation |
| garment fidelity lock | 의상 패턴·질감·색상 계열을 유지해 배경 톤이나 글로벌 그레이드가 옷을 바꾸지 못하게 한다 | fabric pattern fixed, preserve hue chroma, no black crush |
| background plate replacement | 새 외부 배경이 캔버스를 채우되 원본 배경을 확장·재사용하지 않게 한다 | new external background, fills locked canvas, no original background reuse |
| background clipping allowance | 배경 오브제를 살리려고 카메라를 움직이지 않고, 잠긴 프레임 밖 요소는 잘리게 둔다 | background may be clipped, no reframing to preserve landmarks, model priority |
| bounded tone blend | 얼굴·의상은 원본 톤을 우선하고 배경/글로벌 그레이드는 제한 비율로만 섞는다 | face tone blend, max luminance shift, no hue drift |
| lighting hierarchy dial | 광원 우선순위를 정해 색번짐과 재조명을 제한한다 | source priority lighting, direct flash foreground, urban ambient background |
| composite contact proof | 발밑 그림자·바닥 질감 상호작용·그레인 통일·헤어 엣지로 붙여넣기 티를 줄인다 | realistic contact shadow, consistent grain, no halo edges |
| passive perspective match | 카메라 재추정/보정 없이 기존 사진 시점에 배경 깊이만 맞춘다 | match existing perspective, no camera correction, background depth alignment |
| environment cue pack | 장소를 로고·간판이 아니라 시간·재료·스케일·빛·필수 구조물로 정의한다 | location material cues, time-of-day palette, abstract signage lights |

## Location cue packs from session

- **Shibuya early-evening ambient flow** — dusk-blue sky, wide crosswalk geometry, signage as abstract light shapes, pedestrians as ghosted motion only, no distinct faces, accidental ambient fashion rather than cinematic lighting.
- **Paris bridge mixed flash/tungsten** — direct on-camera flash on the locked subject, warm Paris street lamps/Seine reflections in the background, aged stone textures, contact shadow matching flash direction.
- **Grand Palais muted stone daylight** — monumental pale limestone facade, fluted columns, sculptural groups, neutral-warm high-key muted film grade, subject secondary tone blend.
- **Haussmann balcony background plate** — high-angle Paris balcony perspective, beige limestone facades, black wrought-iron balconies, architecture lines aligned to existing camera; background plate only.
- **Mt. Fuji waterside minimalism** — cold overcast late-winter/early-spring atmosphere, calm water, distant hazy Fuji silhouette, side white architectural panel may be clipped; model/canvas integrity outranks landmark completeness.

## Compression rule

Do not copy long `SYSTEM OVERRIDE` headers or repeated absolute-ban JSON into final prompts. Compress to:

1. one operation declaration,
2. canvas/subject/identity/garment locks,
3. bounded tone/lighting integration,
4. background location cue pack,
5. short hard-fail clause.

## Compact clause template

```text
This is a pixel-bound background replacement composite, not free image generation. Preserve the original canvas, crop, aspect ratio, subject position, subject bounding box, pose, silhouette, face geometry, expression, hair edges, garment color/pattern/texture, and foot contact exactly. The original subject photo is the immutable base layer; subject pixels are read-only. Generate only a new external background plate that fills the locked canvas; background elements may be clipped by the frame. Keep face recognition and garment fidelity above beauty or composition improvement. Apply only bounded tone matching: preserve face hue/microtexture and garment hue/chroma, with subtle global grade only. Add realistic contact shadow, matching grain, clean edge integration, no halo or pasted-on separation. If any crop, recentering, subject shift, resize, pose change, face redraw, or garment reinterpretation occurs, the edit fails.
```

## Pitfalls

- If the destination place/landmark is described before the frame lock, the model may reframe or center the person to showcase the place.
- If a landmark/panel must be visible but the frame is locked, say the background may be clipped; never move the model to save the landmark.
- If tone unity is requested, protect face and garments separately. Global grading without limits can cause identity drift, skin smoothing, fabric color drift, black crush, or highlight washout.
- Crowds and signage in real streets should become motion/light grammar: ghosted silhouettes, abstract sign shapes, no readable logos, no distinct bystander faces.
