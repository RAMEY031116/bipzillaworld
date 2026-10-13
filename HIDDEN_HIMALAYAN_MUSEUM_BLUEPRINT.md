# BIPZILLAWORLD — Hidden Himalayan Museum
## Production blueprint · v1 · 13 October 2026

**Vision:** A compact, cinematic, semi-realistic Nepal-inspired art sanctuary built *into* a Himalayan ridge. An art museum discovered through exploration, not a blocky game level. The architecture and landscape must feel physically grounded; the magic comes from composition, light, clouds, reflection and revelation rather than random supernatural objects.

**Non-negotiables**
1. The first 20 seconds look beautiful **before** the visitor moves.
2. Close-up architecture uses curated licensed/original **real glTF meshes** and authored PBR textures, not boxes standing in for detailed façades.
3. Distant snow mountains remain *scenic*; don't spend performance budget on walkable far mountains.
4. The terrain must be three-dimensional and terraced: no huge flat grassy rectangle.
5. Keep existing `app.py` Streamlit dashboard, `artworks.json`, and the ability to replace the 12 temporary illustrations.
6. Respect Nepalese architecture and Buddhist/Hindu cultural references: do not present the invented world as an exact reconstruction of a real temple or a functioning sacred site. Avoid treating worship objects as artwork pedestals.

## 1. Spatial design (metres, indicative; adapt to real model dimensions)

Use world axis +Y up; gallery visitor begins at Z=+35 looking toward -Z. Overall explorable footprint ~105m × 125m; scenic mountain canvas extends much farther.

```text
                              NORTH  /  HIMALAYAS
             ______________________________________________
             |      6. CLOUD OVERLOOK · Z -76             |
             |         single hero artwork & bench         |
             |        ^ cliffside stair / viewing path     |
             |                                              |
             | 5. REFLECTION GARDEN -- 4. SACRED TERRACE   |
             | Z -48, X -30       Z -42, X +27             |
             |      \                           /          |
             |       \    3. TEMPLE INTERIOR   /           |
             |        \   Z -26, X 0          /            |
             |        2. MAIN COURTYARD       |            |
             |           Z -5, X 0           |             |
             |       [art cloister]   [art cloister]         |
             |                   |                          |
             |        1. ARRIVAL GATE Z +30               |
             |______________________________________________|
                                  SOUTH
```

Visitor path: gate → courtyard → indoor collection → terrace → reflection garden → overlook. A short side connection garden→courtyard forms a loop. Paths 2–3.5m wide; avoid dead ends that trap first-person visitors. Secondary spaces can be decorative only.

### Zone 1 — Arrival gate
- Camera begins outside a carved-look wooden/brick gateway, with the main pagoda framed by its opening and the mountains beyond.
- Build 4–6 broad worn stone steps, a plastered brick wall with a genuine timber lattice panel mesh, iron/bronze fittings, overhead fabric and a single welcoming label.
- First piece of art, optional, in a *gallery niche* on the right; no art displayed on a religious shrine.
- Mood: late-afternoon side-light and a quiet hint of cloud beyond roofs.

### Zone 2 — Main courtyard: hero environment
- Footprint roughly 42×40m. Highly detailed pagoda slightly offset from centre; brick-paved plaza, irregular paving edges, stepped stone plinth and drainage grooves.
- Main pagoda: **one high-quality GLB**, detailed timber struts/jalis, multilayer roof geometry, individual under-eave beams, finely worked door, believable stone/brick material variation. Avoid using axis-aligned cube geometry as the main building.
- Three to four surrounding houses, each *different* facade and height; small roofs, shuttered windows and balconies.
- Art: 4 framed works in sheltered colonnades, 2 works in separate accessible wall bays, with warm diffuse spot-like baked illumination.
- Props: **two respectful guardian-lion-inspired stone sculptures**, bell, carved lamps, steps, plants in cracks. Avoid repeated identical props.
- Palette: deep sienna brick, weathered limestone, dark walnut wood, oxidised bronze, muted gold.

### Zone 3 — Interior collection
- Small gallery (~15×18m) connected to courtyard with an actual open doorway; avoid doorway blocked by collider.
- Warm diffuse interior; carved beams and lattice windows, rough plaster walls, 4–6 artworks, one feature wall.
- Baked pools of warm illumination, minimal realtime lights. Art is displayed as a museum exhibition, never on altar structures.
- In first release, a separate small GLB gallery can load when the visitor approaches; if missing, use a deliberately polished pavilion fallback, *not* an infinite corridor.

### Zone 4 — Sacred terrace
- Raised 4–6m above courtyard, approached by walkable ramp/stair with valid camera height handling.
- Fluted stone parapet, carved timber pergola, three art panels, breeze-facing mountain view.
- This is the cinematic midpoint: the world opens and distant scenery becomes fully visible.

### Zone 5 — Reflection garden
- White/gold stupa offset from the walking path; shallow dark-stone reflecting pool nearby, not blocking circulation.
- Flags span between physically grounded poles. A few native-looking shrubs, irregular rocks and two well-shaped trees.
- 1–2 works in a separate sheltered display area. Maintain visual quietness.
- Use physically believable reflections selectively. On low setting use reflection probe/cubemap or art-directed gradient rather than a full planar reflection pass.

### Zone 6 — Himalayan overlook
- A stone balcony built into rock with safety parapet and a single oversized framed hero work (replaceable via catalog).
- Snow peaks above layers of blue-green mountain ridges. Below, atmospheric cloud; the near foreground cliff must be a terrain mesh with rock textures, NOT floating slabs.
- Final composition: artwork on left, stone seating in midground, mountain peaks on the right.

## 2. Environment asset list & acquisition rules

**P0 (must-have to remove the blockout look)**
| Asset | Format | Target | Notes |
|---|---|---:|---|
| Main Nepali-style pagoda | GLB | 8–20 MB | Proper roof/struts/door geometry, PBR embedded |
| Temple gate + entrance | GLB | 3–8 MB | Deep recesses and carved timber detail |
| Traditional townhouse set (3 variants) | GLB | 4–12 MB combined | Different silhouettes |
| Terraced hillside/cliff | GLB | 5–12 MB | Real relief/UV, walk mesh separate |
| Courtyard slabs/edge kit | GLB | 2–6 MB | Stone/brick transitions |
| Trees 2 types, bushes 2 types | GLB | 3–10 MB combined | Good organic foliage, alpha-tested material |
| Guardian sculpture pair | GLB | 1–5 MB | Licensed/sculpted asset, appropriate cultural care |
| Himalayan panorama | WEBP/PNG | 1–5 MB | Wide scene; proper sky transition, source license |
| PBR materials | KTX2/WebP | ~1K each | Brick, stone, wood, tile, rock, soil |
| Colonnade gallery stands | GLB | 1–4 MB | Art frames remain clickable |

**P1:** stupa, terraced staircase, flag ropes with cloth normals, lanterns, rock scatter, detailed parapets, water basin, benches.

**Asset licensing:** only own/original, CC0, CC BY or otherwise correctly licensed assets. Keep an `assets/ATTRIBUTION.md` with author, URL, license and attribution instructions. For religious and heritage structures use references respectfully; do not label custom models as authentic scans.

**Important:** The current repository has **no real GLB model configured** in `scene-assets.json`; photo/material upgrades alone cannot replace blocky temple meshes. Prioritise sourcing or commissioning the temple, gate and houses rather than another procedural-shape pass.

## 3. Materials (physically plausible)

- Brick: albedo with imperfect joints, roughness ~0.82–0.95, 1K normals; different dirt masks on steps and courtyard.
- Stone: varied low-gloss warm-grey limestone/river stone, roughness ~0.88; occasional lichen/edge dirt.
- Timber: dark weathered grain plus carved mesh detail, roughness ~0.7–0.85, no overgloss.
- Tile roofs: real tile/granular dark clay normal maps, roughness ~0.88.
- Bronze: muted aged copper-bronze metallic ~0.6–0.85, roughness ~0.55; do not use shiny yellow plastic.
- Stupa plaster: slightly imperfect ivory, roughness ~0.9.
- Vegetation: instanced organic mesh models with shape variation and wind only if performant.
- Terrain: baked rock/grass texture blends with actual height variation (not a single flat ground plane).

## 4. Camera, atmosphere, lighting

- Late-afternoon sun from camera-left, colour temperature warm but neutral enough to display art accurately.
- Hemisphere/skylight cool fill; shadowed crevices remain readable. 1 directional sunlight with cascaded shadows only if performance justifies it; otherwise one 1024–2048 shadow map focused on hero courtyard.
- Distance haze, not dense scene-wide milky fog; distant snowy ridges cool/desaturated.
- Art displays use subtle emissive-baked glow, never hundreds of realtime spotlights.
- Aerial cloud layer at overlook optional; always disable in reduced-quality mode.
- Tone mapping ACES or neutral; exposure calibrated against actual temple textures, not overblown bloom.
- Avoid fake particle sparkles, portal effects, and neon magic. Mystery comes from sightlines and scale.

## 5. Interactions & access

- Primary: WASD/arrows move, drag to look, click/E to inspect framed art, Esc closes; keyboard and touch support.
- Add optional simple guided path/teleport menu, plus a clear 'Reset to gate' control.
- Collision mesh for temple/rail/landscape; height adaptation on stairs/ramp with gravity-free stable walking.
- No jumping/quests/enemies. People can explore at their own pace.
- Keep gallery interaction logic tied to the JSON catalog, including placeholder images and the private publishing dashboard.
- If 3D fails: list/grid of artworks loads without blank screen. If one GLB fails: show fallback for that asset only.

## 6. Engineering / repository plan

Keep:
`app.py`, `artworks.json`, `art/`, `README.md`, Streamlit admin `?admin=1`.

New structure:
```text
assets/
  models/
    pagoda-hero.glb
    gate.glb
    terrace-cliffs.glb
    houses-01.glb
    houses-02.glb
    houses-03.glb
    guardian-lions.glb
    stupa.glb
    trees.glb
    gallery-interior.glb
  textures/
  scenery/
    himalayas.webp
  ATTRIBUTION.md
src/
  scene.js
  navigation.js
  gallery.js
  lighting.js
  quality.js
  assets.js
scene-assets.json
index.html
app.py
artworks.json
```

**Streamlit caveat:** the app injects inline HTML into a Streamlit iframe and resolves assets to public raw GitHub URLs. External GLB models, textures and panorama must load from origins that allow browser CORS. Prefer self-contained GLBs or a single controlled public asset origin. Do not assume relative file paths in the iframe will work.

**Scene manifest:** increment `scene-assets.json` to version 2 when real models are added. Keep slot IDs and `replaces` stable to avoid regressions. Only hide placeholder models after real asset load success.

## 7. Performance budgets (targets, verify in browser)
- Desktop scene: 40–60 FPS on common integrated GPUs, with quality presets; mobile 25–40 FPS target in low preset.
- First view: aim for interactive shell within 3 s on a typical good connection; heavy GLBs stream afterward and should never block Enter.
- Initial scene draw calls ideally < 250; triangles ideally < 500k visible in high preset. Treat as engineering targets, not guarantees.
- 1K materials default; hero textures 2K only if needed. Instanced foliage/props and strict frustum culling.
- Use compressed textures (KTX2) or WebP; glTF meshopt/Draco if deployment compatibility is tested.
- High: sunlight shadows, more plants, reflection details; Low: fewer trees, no water reflection, reduced pixel ratio/texture detail.
- Cache loaded GLBs; avoid repeated downloads when swapping between zones.
- Check 1280×720 desktop, 1920×1080 desktop, and representative mobile viewport for load/drag/walk/inspect flow.

## 8. Definition of done (no fake finish claims)

**Visual:** Opening screenshot has convincing Nepal-inspired gate/pagoda silhouette, readable texture detail, true depth with rock terraces and mountains, natural foliage, authored light and shadow. Aesthetically consistent foreground and background.

**Usability:** Enter works. Walk and look work. Stairs do not trap the camera. Click artwork works. Missing art/GLB/texture yields graceful fallback. Private admin still uploads art.

**Technical:** No JavaScript syntax error, no uncaught console errors on a tested browser, no broken CORS assets, no excessive GPU memory usage. One real-browser walkthrough and load-speed check documented.

**Licensing:** Each asset attribution recorded; religious structures accurately labelled as artistic interpretations.

## 9. Production order — don't build everything at once

1. **Vertical slice**: hero gate, one real main pagoda, textured stone courtyard, meaningful cliff edge, Himalayan backdrop, 2 good trees, shadows, 2 artwork panels. This must look beautiful.
2. **Composition and material polish**: adjust real model scale, light, baked details, player height and mountain blending. Freeze look once approved.
3. Add interior gallery and protected artwork alcoves with admin integration.
4. Add terrace, reflection garden, stupa and hidden overlooking path.
5. Add ambient detail, accessibility, quality presets and browser performance validation.

### Acceptance gate for phase 1
Do NOT expand zone count until an actual in-browser screenshot of the arrival/courtyard reads as 'cinematic semi-real Nepal' rather than 'blockout'. That is the single highest-priority milestone.

### Status on 13 October 2026
This document is a **production plan**, not proof the final visual standard is already implemented. The existing GitHub scene has panoramic photo and procedural PBR fallbacks and supports GLB loading, but is not yet fitted with high-quality temple/terrain/vegetation GLB assets.
