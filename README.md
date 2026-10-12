# BIPZILLAWORLD

**An ever-expanding 3D virtual art museum**, built with Three.js and published through Streamlit.

## Features
- First-person movement with WASD / arrow keys
- Drag to look around, scroll to zoom
- Click framed artwork to inspect it
- Four themed collections and procedurally extending galleries
- Artwork library controlled by `artworks.json`
- Responsive interface; best on desktop

## Deploy with Streamlit Community Cloud
1. Visit https://share.streamlit.io and sign in with GitHub.
2. Choose repository `RAMEY031116/bipzillaworld`, branch `main`, entry file `app.py`.
3. Click **Deploy**.

The Three.js viewer loads from a CDN, so users need an internet connection.

## Add your artwork
The first published version uses stylized placeholders until your images are uploaded.

1. In this GitHub repository, choose **Add file → Upload files**.
2. Upload artwork JPEG files named `01.jpg`, `02.jpg`, through `19.jpg` inside the `art/` folder. You can also add more files under `art/`.
3. Edit `artworks.json` to give each file a title, description, and correct image path. Every entry looks like:
```json
{"image":"art/01.jpg","title":"Eyes","description":"Story behind the artwork"}
```
4. Commit your changes. Streamlit Community Cloud will automatically redeploy.

**Tip:** To create `art/` initially, click the `art` folder in this repository or upload files using an `art/filename.jpg` path; GitHub doesn't track empty folders.

Please only publish images that you own or have permission to display.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

This is an expanding-gallery prototype, not yet a seamless architecturally connected multi-level world. Floor navigation currently uses buttons.
