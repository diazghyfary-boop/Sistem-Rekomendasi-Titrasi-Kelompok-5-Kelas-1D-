import streamlit as st
import base64
from pathlib import Path

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Sistem Rekomendasi Indikator Titrasi yang Dilengkapi dengan Perhitungan Standardisasi Larutan",
    page_icon="⚛️",
    layout="centered",
)

# ─────────────────────────────────────────────
# FOTO LATAR BELAKANG (LABORATORIUM)
# ─────────────────────────────────────────────
ASSET_DIR = Path(__file__).parent / "assets"
BG_IMAGE_PATH = ASSET_DIR / "lab_background.jpg"

@st.cache_data
def _muat_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

_BG_B64 = _muat_base64(BG_IMAGE_PATH) if BG_IMAGE_PATH.exists() else ""

# Gambar cadangan dari URL GitHub jika file lokal tidak ada
URL_BG_GITHUB = "https://raw.githubusercontent.com/diazghyfary-boop/proyekdiaz137/6095178605cf20666f82dd24e2ef5ab90b4c2495/Screenshot_20260617_213235_Gallery.jpg"

TEMA_WARNA = {
    "default":              "50,140,193",
    "standarisasi":         "0,137,123",
    "asam_basa":            "229,57,53",
    "redoks_kmno4":         "142,36,170",
    "redoks_iodo":          "0,137,123",
    "kompleksometri":       "63,81,181",
    "argentometri_mohr":    "249,168,37",
    "argentometri_volhard": "229,57,53",
    "argentometri_fajans":  "67,160,71",
}

def set_background(tema: str = "default", opacity: float = 0.42):
    accent = TEMA_WARNA.get(tema, TEMA_WARNA["default"])
    
    # Memilih sumber gambar latar belakang (Prioritas: Lokal Base64 -> URL Github)
    if _BG_B64:
        bg_source = f'url("data:image/jpeg;base64,{_BG_B64}")'
    else:
        bg_source = f'url("{URL_BG_GITHUB}")'

    style_bg = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(135deg, rgba(7,18,32,0.66) 0%, rgba({accent},{opacity}) 100%),
                {bg_source};
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            transition: background 0.7s ease-in-out;
        }}
        [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, rgba(11,60,93,0.95), rgba(50,140,193,0.95)) !important;
        }}
        [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] h3 {{
            color: #ffffff !important;
        }}
        </style>
    """
    st.markdown(style_bg, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CUSTOM CSS UNTUK ELEMEN UI (MAIN BODY)
# ─────────────────────────────────────────────
page_styles = """
<style>
.main .block-container h1, .main .block-container h2, .main .block-container h3, 
.main .block-container h4, .main .block-container h5, .main .block-container h6,
.main .block-container p, .main .block-container label, .main .block-container .stMarkdown {
    color: #111111 !important;
    font-weight: bold !important;
}
div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span, div[data-baseweb="select"] div {
    color: white !important;
    font-weight: bold !important;
}
div[data-baseweb="popover"] ul, div[role="listbox"], [data-baseweb="menu"], [data-baseweb="menu"] ul {
    background: linear-gradient(135deg, #0b3c5d 0%, #1d5f8a 100%) !important;
    background-color: #0b3c5d !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[role="option"], div[role="option"] span, div[role="option"] div,
li[role="option"], li[role="option"] span {
    color: white !important;
    background-color: transparent !important;
    font-weight: bold !important;
}
div[role="option"]:hover, li[role="option"]:hover {
    background-color: #328cc1 !important;
}
div[data-baseweb="input"] {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="input"] input {
    background-color: transparent !important;
