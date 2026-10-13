# Phase 1 — Hero Courtyard Asset Queue

**Status:** Preparation underway. The 3D scene currently uses procedural placeholders for the arrival gate, pagodas and cliff. None should be represented as a finished realistic asset.

## Courtyard composition pass — 13 October 2026

**Committed to `index.html`:** sheltered museum cloisters along the east/west court edges, deeper display bays, column and arch rhythm, dark timber entrance lattice, carved bronze-like details, two flanking earthen embankments, a stronger stone courtyard boundary and broken-up paving. The landing page now says **Hidden Himalayan Museum**.

**Honest status:** These additions increase compositional depth but are **still procedural meshes**. They do not substitute for commissioned/licensed, detailed pagoda and gate GLBs. No browser visual or FPS check has been performed. The first live screenshot is the next required review.

**Known risks to test:** courtyard walkway and art panels must remain visible from the new spawn; gate and cloister columns should not clip camera; positioning near two embankments; source attribution links; imported shrine asset's remote accessibility.


## October 2026 active integration update

A **real low-poly photogrammetry Patan chaitya** (Semantic Creation / NepalVR360, via [Zenodo record 10293668](https://zenodo.org/records/10293668), CC BY) is now configured as an **optional external 3D asset** at the arrival-courtyard edge. The viewer normalizes its size to ~3.8 world metres. If Zenodo blocks CORS or changes its download path, loading will fail gracefully and the rest of the world remains usable. Confirm licensing and attribution against the original record before production promotion.

This does **not** replace the detailed pagoda, houses, natural vegetation or terrain GLBs still needed for final visual quality. A browser screenshot and measured FPS remain outstanding.


## Existing project integration
- `scene-assets.json`: Phase 1 model slots (`arrival-gate`, `terrain-cliff`, `main-pagoda`, `museum-pavilion`) and positions.
- `index.html`: named fallback meshes for arrival gate, hero pagoda and sculpted terrain; higher-quality GLBs automatically replace the matching fallback when successfully loaded.
- `app.py`: Streamlit serves the model manifest to the museum and preserves the private publishing dashboard.
- `artworks.json`: remains the authoritative source for artworks.

## Real asset candidates (not yet installed)
1. **A real Kathmandu Valley shrine (chaitya)**: [NepalVR360 / Semantic Creation, Sketchfab](https://sketchfab.com/3d-models/buddha-chaitya-shrine-photogrammetry-69d45b35d4c146dfad42d9bda6a7b5b8), CC BY attribution. A low-poly photogrammetry model from Nepal; suitable for a small shrine prop, **not** a replacement for the pagoda. [Zenodo record](https://zenodo.org/records/10293668) lists a ~1.1 MB GLB for a NepalVR360 shrine in Patan; confirm attribution and exact asset before downloading or integrating.
2. **Traditional Nepalese Pagoda Temple**: [Fab listing](https://www.fab.com/listings/3acddcfc-8ac9-4be7-aa36-bc975eaa64c5), advertises realistic Newari-inspired architecture and GLB. **Commercial/licence conditions must be checked and a legitimate asset obtained before use.** No assumption that it is free.
3. **Scanned rock / terrain**: [Poly Haven](https://polyhaven.com/) provides CC0 rock models and PBR stone materials. Choose only game-ready, decimated models and test performance. Source licenses are CC0, but document origins nonetheless.
4. **Vegetation**: CC0 or explicitly licensed game-ready broadleaf / Himalayan woodland tree GLBs with realistic alpha foliage and branches. **Not selected yet**.
5. **Mountain image**: keep the licensed Annapurna backdrop currently referenced in `scene-assets.json`; test browser retrieval/CORS and image alignment against near terrain.

## Assets needed before Phase 1 visual sign-off
- [ ] One visually accurate, well-textured Nepali pagoda GLB with detailed roof struts and carved windows.
- [ ] Matching gateway, balcony and adjacent façade models, or licensed custom derivatives.
- [ ] Tiled rocky terrace ground mesh with proper UV/PBR mapping and walkable collision.
- [ ] Two game-ready realistic tree variants, one understory shrub set, clustered naturally.
- [ ] Realistic statue / architectural sculpture with appropriate license and contextual use.
- [ ] A verified panorama and sky colour/light that match the foreground.
- [ ] One captured browser screenshot of initial arrival and one near the main pagoda.
- [ ] No broken asset loads; Enter and artwork modal continue to work.
- [ ] Streamlit ?admin=1 remains functional.

## Review order
**Gate framing → temple model → terrain transition → light/colour → vegetation → art placement → performance.**

Do not increase the map until the first screenshot has the quality of the real reference photographs rather than an obvious procedural blockout.

### Implementation caveats
The remote assets in the current application are fetched at runtime. Some content hosts may block cross-origin requests, and some GLBs include external textures not suitable for embedding into Streamlit. Prefer self-contained, legally obtained GLBs committed in `assets/models/`; log attribution in `assets/ATTRIBUTION.md`. Target a small scene and test actual browser FPS.
