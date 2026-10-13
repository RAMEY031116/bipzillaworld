# BIPZILLAWORLD 🎨

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
