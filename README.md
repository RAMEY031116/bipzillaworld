# BIPZILLAWORLD — Orbital Art Museum 🌌

**Active experience (October 2026): a walkable 3D space-art station.** The former Nepal/Himalayan museum is **archived creative history**, not the current scene.

### Interactive 360° orbital museum and original artworks — October 2026

**Current implementation:** A real Three.js inward-facing panoramic sphere now surrounds the visitor. Unlike the former fixed CSS photo, the environment reveals different directions as the camera turns left, right, or behind; the 3D architecture, Nepal flags, exhibit globe, flooring and artwork stands remain actual walkable geometry. The sphere follows camera position (as a distant environment should), while the foreground moves with perspective. Vertical look is clamped to avoid camera roll or upside-down views. Touchscreen movement arrows and drag-to-look controls have been added. The user can switch to the procedural outer-space mode with the 360° panorama button.

**Installed imagery:** `assets/orbital-360-panorama.b64` is now actually committed to GitHub (a WebP image stored as base64 text to accommodate GitHub's text-file connector). Streamlit reads and embeds it directly; standalone hosting loads it with `fetch()`. The 4096×2048 texture was assembled from **four different cinematic AI-generated space-museum views**, not one stationary photograph; mobile scales it to 2048×1024 to save GPU memory. This is a stitched visual approximation, **not a genuine 360° photographed environment**, so some directional seams and perspective distortions may be visible, especially at the poles. No photogrammetry or true depth data exists in the photo.

**Original artist images installed:** `art/originals.json` now contains **all nineteen original user-supplied artwork images**, optimized as WebP data URIs. The Streamlit app and standalone viewer use these in preference to temporary placeholder images. The original source files were supplied by the user earlier in this conversation and remain preserved in the earlier original-art upload pack. The museum's private admin dashboard is preserved.

**Performance:** shadows disabled in the scene manifest; mobile panorama downsampled; static architectural instancing and FAST/BALANCED/DETAIL remain. This has passed source-level syntax checks only, **not a deployed browser render, FPS benchmark, or headset test**.

### Mobile-first museum, interactive art focus and visual polish — October 2026

The museum has a responsive, touch-friendly UI: larger directional buttons, compact quality and panorama controls, clearer navigation tabs, improved modal layouts on small screens, and touch drag-to-look using pointer coordinates rather than unreliable `movementX/movementY` on phones. VR headset setup has been deferred; desktop fullscreen remains available.

Artwork interaction now raycasts **at the actual tap/click position**, rather than only the centre reticle. Selecting a visible artwork within range smoothly pans and moves the camera toward it (where the gallery walkway permits), then opens a larger image inspection panel. The panel has **Previous / Next**, an artwork counter, Escape-to-close, and keyboard arrow navigation. The original image is displayed without cropping, with a fallback where supplied. Gallery frames have added brass depth, warm upper trim and individually rendered title/number labels. A redundant second layer of frame geometry was removed for performance. The clean single-Earth sky no longer restores floating asteroids when changing graphics quality.

**QA:** JavaScript syntax verified and gallery/admin assets preserved. Visual browser testing, touch-device testing, and frame-rate measurements remain pending. Existing NASA texture downloads can fail in restricted networks; the procedural Earth texture remains a fallback.

### Walkable architectural realism — October 2026

The next upgrade adds genuine textured Three.js architecture to the panoramic museum, rather than trying to simulate the whole station with more pictures. A tiled, metallic floor overlay has panel joints and brass inlays; the two side observatories now have three-dimensional bulkheads, observation-window framing, illuminated metalwork and external sightlines; four interactive-area control consoles sit near the main gallery windows. The additional panels share geometry and materials, so the existing instancing pass can batch many of them. The 360-degree image is retained as the distant exterior only.

Walking now uses one normalized movement vector (fixes doubled sideways speed), supports sliding against station boundaries and clamps vertical view. The original artwork galleries, Nepal flags, quality selector, mobile touch controls and panoramic/3D toggle remain intact.

**QA:** JavaScript syntax checked after each commit. The scene has not been tested visually or benchmarked in a live WebGL browser. This is an incremental architectural improvement, not yet a complete photogrammetric or production-grade photorealistic environment.

### Parallax / panorama realism update

The viewer now blends the 360-degree panoramic horizon with additional **genuine 3D geometry outside the station**: two multi-ring docking structures, solar-panel spacecraft docks, a slowly orbiting satellite and hundreds of perspective-correct star points. These elements change their relative positions when the visitor moves, rather than being baked into the panorama. The panoramic texture is also wrapped with crossfaded left/right seam columns and darkened poles, which reduces abrupt stitch lines and the worst stretching overhead. Mobile uses a 2048×1024 panorama and a smaller star layer; desktop uses 4096×2048.

**Important realism limitation:** the underlying panorama is still an image, and the camera cannot reveal true depth in the structures baked into that image. A fully photorealistic, parallax-correct 360-degree station requires custom textured 3D architecture (or multiple depth-mapped scenes), a matching HDR environment, and actual browser/device QA. These changes improve the hybrid effect but do not pretend to turn photographs into complete 3D geometry.

### Cinematic image + live 3D hybrid (October 2026)

The user requested that the website resemble the generated cinematic space-station reference rather than a simple mobile-game-like dome. **A new hybrid mode is implemented in `index.html` and `app.py`:** the panoramic cinematic image is used as a lightweight, fixed distant backdrop while the museum architecture, 19 artwork frames, Nepal flags, floor and walk controls remain real Three.js objects. A small look-based parallax offset gives the image a subtle response when the camera rotates. This is deliberately a **2D image background + genuine 3D foreground**, not a fully navigable 3D model of everything in the photograph.

**The image is already committed:** `assets/orbital-cinematic.b64` contains the 1600-pixel-wide optimized WebP encoded as text for compatibility with the GitHub connector. No manual upload is required. Streamlit's `app.py` automatically embeds it into the sandboxed iframe; standalone `index.html` fetches the encoded file and decodes it into a browser image. On successful load, photo mode activates automatically and hides the procedural Earth, Sun, stars and asteroids, avoiding doubled planets and reducing GPU work. The **✦ PHOTO SCENERY** button switches between the cinematic image and procedural 3D outer-space view. If the asset cannot be loaded, the original 3D backdrop remains.

The supplied photo is an AI-generated cinematic concept reference, **not a NASA photograph or a true 360-degree skybox**. It will not have correct 3D parallax when walking. A truly photorealistic fully navigable station would require dedicated textured 3D assets, HDR environment lighting and visual/performance testing.

### Earth-window composition + Nepal in space — October 2026

The default visitor spawn is now **inside the main observation hall**, looking directly through the panoramic window toward a **larger, repositioned Earth**. The large dome is now almost invisible glass rather than the earlier opaque blue layer, and the scene retains the sculpted curved window arches, marble and bronze interiors. A central viewing telescope and lounge seating help the hall feel inhabited.

Two **double-pennant Nepal flags** are displayed inside the orbital station, with a bilingual **NEPAL · ORBITAL ART MUSEUM / नेपाल · पृथ्वी अवलोकन ग्यालरी** plaque. This preserves the Nepalese identity without replacing the requested space-station architecture with temples. The flag is generated as a local canvas texture so it requires no additional network download.

**Performance preserved:** the architectural instancing, FAST/BALANCED/DETAIL switch, automatic resolution reduction, mobile star budget and shadow-lighting reductions from the prior optimization pass remain active. No live browser screenshot or frame-rate benchmark has been performed, so visual similarity to the concept image is a target, not a verified claim.

### Cinematic observatory rebuild + original artist collection — October 2026

The active 3D world now has a **marble-finished observation hall** with physically based environment reflections, bronze-and-gunmetal architecture, panoramic window framing, curved ceiling ribs, an elevated balcony, glass rails, warm exhibition spotlights, indoor greenery, and a miniature Earth globe sculpture. The external Earth is larger in the main forward view. This is actual walkable Three.js geometry, **not a flat generated picture**. The generated concept image is a visual target rather than an in-world texture.

**Nineteen original artwork slots:** `artworks.json` now lists the nineteen earlier uploaded works as `art/01.jpg` through `art/19.jpg`; the 3D scene has nineteen framed displays and keeps the artwork click-to-inspect interaction. `app.py` selects an original JPG when present and otherwise temporarily falls back to the existing SVG. The image files are **not yet present in the remote GitHub repository**. A separate upload pack, `BIPZILLAWORLD-original-19-artworks-upload-pack.zip`, was prepared in the chat with all nineteen JPGs. Extract it and upload `01.jpg` through `19.jpg` to the repo's `art/` folder to activate them on Streamlit. The user-supplied image files are not silently substituted by unrelated generated art.

**Limitations:** This pass improves materials, architectural depth and gallery layout but is still a procedural Three.js build, not a scanned photorealistic environment. Browser rendering and FPS remain unverified. On low-power devices, physically based reflections and extra geometry may reduce performance.

### Earth and Sun realism pass — October 2026

The forward observation view now frames **Earth and the Sun**. Earth uses NASA/GSFC's [Blue Marble 2048×1024 satellite-composite texture](https://svs.gsfc.nasa.gov/2915/) when the image host permits cross-origin loading, with an official Three.js Earth texture fallback and the existing procedural planet as the last fallback. The Earth has a separate moving cloud layer, night-side city-light texture (optional, from the Three.js example assets), and an atmosphere glow. The Sun uses an animated procedural plasma shader and corona. Earth was brought closer to make it more prominent from the museum arrival point.

**Honest visual status:** Earth's image is real satellite-derived data when the texture loads, but this is still a real-time 3D simulation rather than a photographic scene. The Sun is a stylized shader, not a live telescope image. No live-browser screenshot or FPS test has been performed. Credit: NASA/Goddard Space Flight Center Scientific Visualization Studio; Blue Marble data courtesy of Reto Stöckli (NASA/GSFC).

### What's in the space museum

- **5,100 depth-positioned stars**, with GPU-drawn soft point sprites, different star temperatures and gentle animated scintillation.
- Two diffuse **nebula clouds** and a luminous distant sun.
- A **3D blue planet** with seeded surface textures for ocean, land, polar ice, a separate animated cloud sphere and a shader-based atmospheric limb glow.
- A **3D ringed moon** with crater-like rocky texture and fourteen thin translucent rings.
- A **225-piece instanced asteroid field**, an animated scientific probe with solar arrays, and the station's rotating central holographic sculpture.
- Illuminated observation wings, artwork boards and three teleport destinations. Walking is limited to station walkways.
- **Immersive View** button: hides HUD and requests browser fullscreen (if permitted).
- **Experimental headset WebXR**: a VR entry button is offered *only if* the browser reports immersive-vr support and the host allows it. **Streamlit's embedded iframe may block headset permissions**, and VR controller navigation is not yet implemented. Do not describe headset support as universally available.

### Running it

The existing Streamlit deployment still uses `app.py` and preserves the private `?admin=1` artist dashboard and `artworks.json`.

The `index.html` viewer also supports **standalone HTTPS hosting**, loading `artworks.json` and `scene-assets.json` from the same directory when Streamlit has not injected them. This is useful for trying WebXR outside the Streamlit iframe. GitHub Pages is a possible host **if enabled in repository settings**, but no GitHub Pages deployment has been configured or verified by this change.

**Verification:** JavaScript syntax was checked after edits. Browser rendering, actual headset support, performance and visual quality have not been tested on the user's deployment. Planet/star textures are original procedural approximations, **not NASA imagery or photogrammetric scans**.

---

## Previous Nepal/Himalayan development (archived)


> **Creative direction and build specification:** [Hidden Himalayan Museum production blueprint](HIDDEN_HIMALAYAN_MUSEUM_BLUEPRINT.md) — the six-zone layout, required real 3D assets, lighting, atmosphere, performance targets, and acceptance criteria. The blueprint does not mean all models have been implemented yet.


## Kathmandu environment enhancement — October 2026

This version focuses on a small, scenic simulation rather than an enormous open world.

- **Actual Himalayas photograph:** the scene attempts to load Bijay Chaurasia's Annapurna panorama from Wikimedia Commons. If blocked, geometric distant terrain remains as a fallback. Photo © Bijay Chaurasia / Wikimedia Commons, licensed CC BY-SA 4.0, attribution appears in the UI.
- **Authentic photographic materials:** at runtime it requests 1K CC0 Poly Haven materials (red brick, red brick pavers, rock ground, dark planks and clay roof tiles), with normal maps where available. Existing browser-generated textures remain as fallback if CDN access is blocked. The live API/material source is credited in the UI as requested by Poly Haven.
- **Vegetation:** replaced conical trees with organic, irregular canopies, angled branches and bark trunks rendered through batched instancing to keep draw calls manageable.
- **Temple props:** added guardian-lion-inspired stone sculptures and bronze bell-like ornaments. These are stylistic approximations, *not historical scans*.
- **Performance:** distant mountains are scenic imagery rather than a fully explorable high-poly world. Most foliage does not cast individual dynamic shadows.

The **temples/buildings are still procedural**, not photogrammetry or scanned GLB geometry. To reach true semi-realism up close, import properly modelled pagoda/stupa/townhouse assets via `scene-assets.json`. The artist publishing dashboard is preserved, and artwork placeholders remain replaceable.

**Dependencies:** The 3D viewer loads Three.js from jsDelivr, optional material maps from Poly Haven, and the panorama from Wikimedia; these remote assets require an internet connection. If remote texture loads fail, the scene uses lightweight local procedural textures; if WebGL fails, an artwork-gallery fallback is shown.


## Scenic realism update — real Himalayan photography and temple details

This pass makes a meaningful visual improvement without turning BIPZILLAWORLD into a large open-world game:

- The default distant backdrop is a **real Annapurna panoramic photograph**, loaded over HTTPS from Wikimedia Commons. The source may fail on restricted networks; in that case, the previous generated mountain scenery remains as fallback.
- The former conical trees are replaced by instanced trunks, angled branches, and irregular shaded foliage clumps. This reduces repeated draw calls while producing more organic silhouettes.
- Two stone guardian sculptures and bronze temple ornaments now sit near the main courtyard.
- Soft directional sunlight and roof shadows remain enabled, and the private Streamlit artist upload dashboard is unchanged.

**Photograph credit:** [Bijay Chaurasia, *Annapurna Massif panorama*, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Annapurna_Massif-IMG_5221-Pano.jpg), licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Used as scenic backdrop without altering the source file. The visible in-world footer repeats this credit.

**Scope:** A good photograph as a distant backdrop is not a substitute for a photogrammetry-quality temple, statue or tree model. The foreground remains an optimized procedural interpretation until actual high-quality `.glb` assets are supplied. Performance and visual fidelity should be verified on the deployed site.


## Asset-ready semi-realistic Nepal scene (October 2026)

The WebGL scene now supports replacing the procedural temple models with actual **glTF binary (`.glb`) 3D assets**. It includes optional soft directional sun shadows and photographic Himalayan backdrop support.

### Add a detailed temple model
1. Obtain or make a low-to-medium-poly, properly licensed Nepali pagoda model in GLB format (ideally 5–25 MB with baked or PBR textures).
2. Upload it to `assets/models/` in the repository.
3. Open `scene-assets.json` and change `models[0].file` from `""` to `"assets/models/temple.glb"`.
4. Adjust `position`, `rotationY` and `scale` if necessary. The main temple is currently centred at world coordinates `[0, 0, -27]`.
5. Commit: Streamlit redeploys, the model loads from the public GitHub raw URL, and the procedural pagoda gets hidden **only if loading succeeds**.

Additional slots: `west-pagoda`, `east-pagoda`, `stupa`, and `buildings`. The last slot overlays the existing buildings by default; to replace them fully, models need matching fallback grouping.

### Use real Himalayan imagery
Upload a licensed mountain panorama to `assets/scenery/himalayas.webp`, then set `panorama.file` in `scene-assets.json` to `"assets/scenery/himalayas.webp"`. This displays the photograph on a distant scenic plane and hides the procedurally generated mountain meshes once the image loads.

For the best effect, use a properly cropped wide panorama (e.g. 4096×1024), with mountains in the lower portion and transparent or matching sky. A plain rectangular photo does not blend perfectly without transparency/masking.

### Performance and realism
- Sunlight uses one 1024-pixel shadow map, PCF soft shadows and no extra dynamic lights.
- The existing procedural geometry, low-resolution canvas material maps and temporary artwork still work as fallback.
- Use **GLB with embedded texture resources**, moderate mesh counts and compressed textures; very large models or 4K materials can cause Streamlit browser memory pressure.
- The current fallback is still stylised. **The appearance only becomes asset-driven after model and panorama files are supplied.**
- Streamlit private artist dashboard at `?admin=1` and the artwork catalogue remain unchanged.


## Kathmandu temple-square rebuild (current)

### Rendering pass — October 2026

The Kathmandu scene now uses UV-mapped procedural roof surfaces, thicker roof supports, instanced pagoda relief details, triangulated Himalayan ridge terrain with depth and snow/rock shading, and instanced paving pieces. This remains a stylised semi-realistic WebGL prototype: full realistic architecture would benefit from licensed/created GLB models and higher-quality PBR materials. The existing Streamlit artist dashboard and 12 temporary artworks are unchanged. JavaScript syntax was checked before committing; real-browser performance and visual fidelity are **not** yet verified.



The main museum scene has been rebuilt around a **compact 3D Kathmandu-inspired courtyard**, with:
- Three multi-tier pagoda temples made from sloping roof meshes, timber eaves and masonry bases
- Procedurally textured brick, roof shingles, wood and stone (generated locally in the browser; no large external texture downloads)
- Traditional-looking houses, a stupa with prayer flags, distant mountain terrain and a lakeside area
- Artwork on inspectable standing frames, using the existing `artworks.json` catalogue
- WASD / arrow-key movement, drag-to-look, click-to-inspect and location buttons
- A simple collision radius around main temples and stupa

**Honest quality note:** This is still a stylised procedural approximation of Nepalese architecture. It is more detailed than the original corridor scene, but true semi-realistic/photoreal quality would require professionally modelled GLB assets, detailed PBR textures, and in-browser performance testing. There is no guarantee of smooth frame rates on every device.

**Deployment:** Streamlit continues to render `index.html` through `app.py`. The private artist dashboard at `?admin=1` is preserved, and its GitHub token/password must be configured in Streamlit secrets before uploading art.

---


An ever-expanding immersive art museum — **colourful, expressive, contemporary**, built around BIPZILLA's work instead of a fantasy-game aesthetic.

## What is live in the code
- 3D exhibition with bright gallery walls, framed art, changing palettes and soft gallery lighting
- First-person movement: WASD / arrows to walk, drag mouse to look, scroll to zoom
- Walkable connecting galleries and staircases linking successive floors; every fourth gallery rises
- Procedural gallery extensions as visitors explore further, with old rooms unloaded
- Artwork inspector: click a frame (or press E) to view an artwork
- Artist-only upload dashboard: publish art to GitHub using your Streamlit secrets
- Non-3D fallback art gallery if WebGL / the Three.js CDN is unavailable

> **Prototype scope:** This is an expanding playable 3D foundation. It does not yet include sophisticated collision, interactive portals, a map, multi-user visits, or infinite *unique* art pieces. Rooms and existing artwork are reused as visitors travel deeper.

## Deploy to Streamlit Community Cloud
1. Visit https://share.streamlit.io and connect GitHub.
2. Choose `RAMEY031116/bipzillaworld`, branch `main`, main app file `app.py`.
3. Deploy. If already deployed, use **Reboot app** after updates.
4. Your public museum is at the app's Streamlit URL.

Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Add original artwork
The museum currently contains **12 original temporary Nepal-inspired SVG artworks** in `art/temp-01.svg` through `art/temp-12.svg`. These load immediately and are designed to be replaced with your real artworks later. Missing images still fall back to colourful illustrations.

To replace temporary art, upload your own JPG/PNG/WEBP image to the `art/` folder, then edit the corresponding `image` path and title in `artworks.json`. For example, change `"image": "art/temp-01.svg"` to `"image": "art/my-painting.jpg"`. The original temporary SVG can be kept or deleted. Alternatively, use the private artist studio to add new works without editing code. Only upload art you own or have permission to exhibit.

## Private artist dashboard — persistent uploads
The dashboard is available at `https://YOUR-APP.streamlit.app/?admin=1`. It is **not enabled until you configure both secrets**. In your Streamlit Community Cloud app, visit **Settings → Secrets** and add:

```toml
BIPZILLA_ADMIN_PASSWORD = "a-long-unique-private-password"
GITHUB_TOKEN = "YOUR_FINE_GRAINED_GITHUB_TOKEN"
```

Generate a fine-grained personal access token on GitHub, restricted to the **bipzillaworld** repository with **Contents: Read and write** permission. Do NOT commit the token or your password to the repository.

The artist studio provides an upload form for PNG, JPG, and WEBP images, allows a title, description, and collection, then saves each image to `art/` and appends an entry to `artworks.json`. GitHub is the persistent storage; Streamlit redeploys following commits. The uploaded images are public if your GitHub repository is public.

For a larger collection, replace embedded base64 artwork with dedicated image storage/CDN: Streamlit has memory and GitHub repository limits, and rendering hundreds of full-resolution images as data URLs will eventually slow down the experience.

## Controls
- WASD / arrows: move
- Drag: look around
- Scroll: zoom
- Click artwork or E: inspect
- Walk forward through adjoining galleries to reach the next floor staircase
- Explore button: quickly jump to the following room

## Design direction
Nepal-inspired open-air architecture with Kathmandu courtyard colours, Pokhara lakeside turquoise, Himalayan mountain silhouettes, warm brick tones, and a daytime gallery environment. Temporary artworks are original geometric illustrations, not photographs of real locations. Performance improvements include a reduced pixel ratio, fewer room meshes kept active, and removal of per-artwork point lights. The eventual goal is to create curated architectural variations based on each series, not procedurally repeat the same walls forever.
