"""BIPZILLAWORLD — Streamlit-powered Three.js virtual art museum."""
import base64
import json
import mimetypes
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="BIPZILLAWORLD · Infinite Art Museum", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>header[data-testid="stHeader"],footer,#MainMenu{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stAppViewContainer"]{background:#08070a}
iframe{display:block}</style>""",unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def museum_page():
    data_file = ROOT / "artworks.json"
    works = json.loads(data_file.read_text(encoding="utf-8")) if data_file.exists() else []
    for work in works:
        path = (ROOT / work["image"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            continue
        mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
        work["image"] = "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    return page.replace("/*ART_DATA*/[]", json.dumps(works))

components.html(museum_page(), height=920, scrolling=False)
