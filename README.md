# BIPZILLAWORLD 🎨

## Kathmandu temple-square rebuild (current)

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
