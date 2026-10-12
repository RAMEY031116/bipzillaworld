"""BIPZILLAWORLD — 3D museum and private publishing dashboard."""
from pathlib import Path
import base64
import hmac
import json
import mimetypes
import re
import requests
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
REPO = "RAMEY031116/bipzillaworld"
st.set_page_config(page_title="BIPZILLAWORLD · Open Art Universe", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
header[data-testid="stHeader"],footer,#MainMenu,[data-testid="stToolbar"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"]{background:#f7eee4}
iframe{display:block;border:0}
</style>""", unsafe_allow_html=True)

def settings(name):
    try:
        return str(st.secrets.get(name, ""))
    except Exception:
        return ""

@st.cache_data(show_spinner=False)
def museum():
    raw = json.loads((ROOT / "artworks.json").read_text(encoding="utf-8"))
    works = []
    for item in raw:
        w = dict(item)
        p = Path(str(w.get("image", "")))
        w["image"] = ""
        if p.parts and not p.is_absolute() and ".." not in p.parts:
            target = ROOT / p
            if target.is_file():
                mime = mimetypes.guess_type(target.name)[0] or "image/jpeg"
                w["image"] = "data:" + mime + ";base64," + base64.b64encode(target.read_bytes()).decode("ascii")
        works.append(w)
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    return html.replace("__ART_DATA__", json.dumps(works).replace("</", "<\\/"))

def gh_request(method, path, token, **kwargs):
    headers = {"Authorization": "Bearer " + token,
               "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.request(method, "https://api.github.com/repos/" + REPO + "/contents/" + path,
                                headers=headers, timeout=40, **kwargs)
    response.raise_for_status()
    return response.json()

def dashboard():
    st.title("BIPZILLAWORLD / ARTIST STUDIO")
    st.caption("Private artwork publishing · new artwork is stored in your GitHub repository and redeployed automatically.")
    password = settings("BIPZILLA_ADMIN_PASSWORD")
    token = settings("GITHUB_TOKEN")
    if not password or not token:
        st.warning("Dashboard setup required: add BIPZILLA_ADMIN_PASSWORD and GITHUB_TOKEN in your Streamlit app Secrets. Nothing is published until configured.")
        st.code('BIPZILLA_ADMIN_PASSWORD = "use-a-long-unique-password"\nGITHUB_TOKEN = "your-fine-grained-github-token"', language="toml")
        return
    entered = st.text_input("Studio password", type="password")
    if not hmac.compare_digest(entered, password):
        if entered:
            st.error("Incorrect password.")
        return
    st.success("Artist studio unlocked")
    st.info("Only upload artwork you own or are licensed to exhibit. Publishing commits images to your GitHub repository.")
    title = st.text_input("Artwork title", max_chars=120)
    description = st.text_area("Description / story", max_chars=1200)
    collection = st.selectbox("Collection", ["Figures & Faces", "Ink & Illustration", "Colour Experiments", "Sketchbook", "Other Worlds"])
    uploads = st.file_uploader("Choose artwork (PNG / JPG / WEBP)", type=["png","jpg","jpeg","webp"], accept_multiple_files=True)
    if st.button("PUBLISH TO MUSEUM", type="primary", disabled=not uploads):
        try:
            catalog_data = gh_request("GET", "artworks.json", token)
            catalog = json.loads(base64.b64decode(catalog_data["content"]).decode("utf-8"))
            for i, upload in enumerate(uploads):
                raw = upload.getvalue()
                if len(raw) > 8_000_000:
                    st.warning(upload.name + " is larger than 8 MB. Please compress and retry.")
                    continue
                ext = Path(upload.name).suffix.lower()
                if ext not in (".jpg", ".jpeg", ".png", ".webp"):
                    continue
                safe = re.sub(r"[^a-z0-9-]+", "-", Path(upload.name).stem.lower()).strip("-")[:45] or "work"
                import uuid
                path = "art/" + safe + "-" + uuid.uuid4().hex[:8] + ext
                gh_request("PUT", path, token, json={"message": "Publish BIPZILLAWORLD artwork " + path,
                    "content": base64.b64encode(raw).decode("ascii"), "branch": "main"})
                catalog.append({"image":path,"title":title.strip() or Path(upload.name).stem,
                                "description":description.strip(),"collection":collection})
                st.write("Uploaded:", upload.name)
            new_content = base64.b64encode(json.dumps(catalog, indent=2, ensure_ascii=False).encode()).decode()
            gh_request("PUT", "artworks.json", token, json={"message":"Update BIPZILLAWORLD artwork catalog",
                "content":new_content,"sha":catalog_data["sha"],"branch":"main"})
            museum.clear()
            st.success("Published! Streamlit Community Cloud will redeploy after GitHub updates.")
            st.balloons()
        except requests.HTTPError as exc:
            st.error("GitHub upload failed: " + str(exc))
        except Exception as exc:
            st.error("Could not publish: " + str(exc))
    st.divider()
    st.caption("Tip: open the public museum by removing ?admin=1 from the URL.")

if st.query_params.get("admin") == "1":
    dashboard()
else:
    components.html(museum(), height=900, scrolling=False)
