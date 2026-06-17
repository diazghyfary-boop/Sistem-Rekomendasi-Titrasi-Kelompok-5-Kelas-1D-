import streamlit as st

# =============================================
# 1. PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="Sistem Rekomendasi Titrasi",
    page_icon="⚛️",
    layout="centered",
)

# =============================================
# 2. GLOBAL INJECTED CSS (BACKGROUND & SIDEBAR)
# =============================================
page_bg_img = """<style>
/* Background Utama Aplikasi Tetap Gambar */
.stApp {
    background-image: url("https://raw.githubusercontent.com/diazghyfary-boop/proyekdiaz137/6095178605cf20666f82dd24e2ef5ab90b4c2495/Screenshot_20260617_213235_Gallery.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Mengubah Warna Sidebar Menjadi Putih Bersih */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1px solid #e0e0e0;
}

/* Memastikan Teks di Sidebar Berwarna Gelap & Jelas */
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] label, 
[data-testid="stSidebar"] .stRadio label {
    color: #1c2833 !important;
    font-weight: bold !important;
}

/* Memaksa semua teks di halaman utama berwarna hitam tebal */
h1, h2, h3, h4, h5, h6,
p, label, .stMarkdown, .stText, .stRadio label, .stSelectbox label {
    color: black !important;
    font-weight: bold !important;
}

/* Dropdown & Input Box Styling */
div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span, 
div[data-baseweb="select"] div {
    color: white !important;
    font-weight: bold !important;
}
div[data-baseweb="popover"] ul,
div[role="listbox"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul {
    background: linear-gradient(135deg, #0b3c5d 0%, #1d5f8a 100%) !important;
    background-color: #0b3c5d !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[role="option"], div[role="option"] span, div[role="option"] div, li[role="option"], li[role="option"] span {
    color: white !important;
    background-color: transparent !important;
    font-weight: bold !important;
    font-size: 14px !important;
}
div[role="option"]:hover, li[role="option"]:hover, div[data-baseweb="popover"] ul li:hover {
    background-color: #328cc1 !important;
    background: #328cc1 !important;
    color: white !important;
}
div[data-baseweb="input"] {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="input"] input {
    background-color: transparent !important;
    color: white !important; 
    font-weight: bold !important;
}
div[data-baseweb="input"] button {
    color: white !important;
    background-color: transparent !important;
}
.main .block-container {
    background: rgba(255,255,255,0.45);
    padding: 2rem;
    border-radius: 15px;
}
table, th, td {
    color: black !important;
    font-weight: bold !important;
}
.stInfo {
    color: black !important;
    font-weight: bold !important;
}
.custom-white-box {
    background-color: rgba(255, 255, 255, 0.9) !important;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# =============================================
# 3. INTERFACE & LAYOUT CSS
# =============================================
ui_css = """<style>
body { font-family: 'Segoe UI', sans-serif; }
.banner h1 {
    color: #0b3c5d !important; 
    font-weight: bold !important;
    font-size: 2em;
}
.banner p {
    color: #328cc1 !important; 
    font-weight: bold !important;
}
.banner {
    background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 50%, #80deea 100%);
    border-radius: 14px;
    padding: 28px 20px;
    text-align: center;
    margin-bottom: 28px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
.card {
    background: #ffffff !important;
    border-radius: 12px;
    padding: 18px 20px;
    margin: 10px 0;
    border-left: 6px solid #2196F3;
    box-shadow: 0 2px 8px rgba(0,0,0,.08);
}
.card.red    { border-color: #e53935; }
.card.green  { border-color: #43a047; }
.card.orange { border-color: #fb8c00; }
.card.purple { border-color: #8e24aa; }
.card.yellow { border-color: #f9a825; }
.card.teal   { border-color: #00897b; }
.card, .card h4, .card p, .card span, .card li {
    color: #000000 !important;
    font-weight: bold !important;
}
.card h4 { margin: 0 0 6px 0; font-size: 1.05em; }
.card p { margin: 2px 0; font-size: .93em; }
.badge {
    display: inline-block;
    background: #fff8e1;
    color: #000000 !important;
    border: 1px solid #ffe082;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: .8em;
    margin-top: 6px;
}
.warn {
    background: #fff3e0;
    border-left: 5px solid #FF9800;
    border-radius: 8px;
    padding: 14px 16px;
    margin: 10px 0;
    font-size: .92em;
    color: #5d4037 !important;
}
.warn b { color: #e65100 !important; }
.warn * { color: #5d4037 !important; }
.step-badge {
    display: inline-block;
    background: #e8eaf6;
    color: #3949ab !important;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: .82em;
    font-weight: 600;
    margin-bottom: 12px;
}
.done {
    background: linear-gradient(90deg,#e8f5e9,#f1f8e9);
    border: 1.5px solid #a5d6a7;
    border-radius: 10px;
    padding: 14px 18px;
    color: #2e7d32 !important;
    font-weight: 600;
    margin-top: 14px;
    text-align: center;
}
</style>"""

st.markdown(ui_css, unsafe_allow_html=True)

# =============================================
# 4. BANNER ATAS
# =============================================
st.markdown(
    """<div class="banner">
        <h1>👩🏻‍🔬 Sistem Rekomendasi Titrasi</h1>
        <p>Pilih jenis titrasi → Ikuti langkah → Dapatkan rekomendasi indikator</p>
        <p>Pilih jenis metode standarisasi → Masukkan nilainya → Dapatkan hasil perhitungannya</p>
    </div>""",
    unsafe_allow_html=True,
)

# =============================================
# 5. HELPER FUNCTIONS
# =============================================
def card(title, rows: list, color="", starred=False):
    extra = f' <span class="badge">⭐ Direkomendasikan</span>' if starred else ""
    body = "".join(f"<p>• {r}</p>" for r in rows)
    st.markdown(
        f'<div class="card {color}"><h4>{title}{extra}</h4>{body}</div>',
        unsafe_allow_html=True,
    )

def warn(msg):
    st.markdown(f'<div class="warn">⚠️ <b>Catatan:</b> {msg}</div>', unsafe_allow_html=True)

def done():
    st.markdown('<div class="done">✅ Selesai — gunakan indikator di atas sesuai ketersediaan laboratorium.</div>', unsafe_allow_html=True)

def step(n, label):
    st.markdown(f'<div class="step-badge">Langkah {n}</div>', unsafe_allow_html=True)
    st.markdown(f"**{label}**")

# =============================================
# 6. SIDEBAR NAVIGATION (MENU DI SAMPING KIRI)
# =============================================
with st.sidebar:
    st.markdown("## ⚛️ Sistem Rekomendasi Titrasi")
    st.markdown("### 📋 Menu Halaman")
    
    fitur = st.radio(
        label="Pilih Halaman:",
        options=[
            "🏠 Beranda",
            "🔴 Menentukan Indikator Titrasi",
            "🧪 Menghitung Standarisasi Larutan"
        ],
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown("🧪**Sistem Rekomendasi Titrasi**🧪")
    st.markdown("Dibuat oleh Kelompok 5")

# =============================================
# 7. KONTEN HALAMAN BERANDA
# =============================================
if fitur == "🏠 Beranda":
    st.markdown(
        """<div class="custom-white-box" style="text-align: center; padding: 30px;">
            <h2 style="color: #0b3c5d !important; margin-bottom: 5px;">👋 SELAMAT DATANG DI PROGRAM APLIKASI KAMI</h2>
            <p style="font-size: 1.2em; color: #328cc1 !important; margin-top: 0px; margin-bottom: 20px;">DARI</p>
            <h1 style="color: #e53935 !important; letter-spacing: 2px; margin-bottom: 5px;">⚜️ KELOMPOK 5 ⚜️</h1>
            <h3 style="color: #43a047 !important; margin-top: 0px; margin-bottom: 35px;">KELAS 1D</h3>
            <hr style="border: 1px solid #ddd; margin-bottom: 25px;">
            <h4 style="text-align: left; color: #0b3c5d !important; margin-bottom: 15px; border-bottom: 2px solid #0b3c5d; padding-bottom: 5px;">👥 NAMA-NAMA ANGGOTA:</h4>
            <ol style="text-align: left; font-size: 1.1em; line-height: 2; padding-left: 20px; color: black !important;">
                <li><b>DIAZ AQILIA GHYFARY</b> (2560610)</li>
                <li><b>Izamary Layla Muzdalifah</b> (2560647)</li>
                <li><b>Nicholas Kusuma Irwana P</b> (2560725)</li>
                <li><b>Nida Nafisah Herlistyo</b> (2560726)</li>
                <li><b>Ridha Putra Pratama</b> (2560754)</li>
            </ol>
        </div>""",
        unsafe_allow_html=True
    )

# =============================================
# 8. FITUR — STANDARISASI LARUTAN
# =============================================
elif fitur == "🧪 Menghitung Standarisasi Larutan":
    st.subheader("🧪 PERHITUNGAN STANDARISASI LARUTAN")
    metode = st.selectbox(
        "Pilih Metode Standarisasi",
        [
            "── PILIH ──",
            "Natrium Hidroksida (NaOH) dengan Asam Oksalat (H₂C₂O₄)",
            "Asam Klorida (HCl) dengan Boraks (Na₂B₄O₇.10H₂O)",
            "Kalium Permanganat (KMnO₄) dengan Asam Oksalat (H₂C₂O₄)",
            "Tiosulfat (Na₂S₂O₃) dengan Kalium Dikromat (K₂Cr₂O₇)",
            "EDTA (C₁₀H₁₆N₂O₈) dengan Kalium Karbonat (CaCO₃)",
        ]
    )

    if metode == "Natrium Hidroksida (NaOH) dengan Asam Oksalat (H₂C₂O₄)":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume NaOH (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 63.0  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Asam Oksalat (mg) / ((100mL / 25mL) × volume NaOH (mL) × BE Asam Oksalat)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas NaOH = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Asam Klorida (HCl) dengan Boraks (Na₂B₄O₇.10H₂O)":
        massa = st.number_input("Massa Boraks (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume HCl (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 190.7  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Boraks (mg) / ((100mL / 25mL) × volume HCl (mL) × BE Boraks)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas HCl = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Kalium Permanganat (KMnO₄) dengan Asam Oksalat (H₂C₂O₄)":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume KMnO₄ (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 63.0  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Asam Oksalat (mg) / ((100mL / 25mL) × volume KMnO₄ (mL) × BE Asam Oksalat)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas KMnO₄ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Tiosulfat (Na₂S₂O₃) dengan Kalium Dikromat (K₂Cr₂O₇)":
        massa = st.number_input("Massa K₂Cr₂O₇ (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume Na₂S₂O₃ (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 49.04  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa K₂Cr₂O₇ (mg) / ((100mL / 25mL) × volume Tiosulfat (mL) × BE K₂Cr₂O₇)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas Na₂S₂O₃ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "EDTA (C₁₀H₁₆N₂O₈) dengan Kalium Karbonat (CaCO₃)":
        massa = st.number_input("Massa CaCO₃ (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume EDTA (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BM = 100.09  
                M = massa / ((100 / 25) * volume * BM)
                st.write("**Rumus:**")
                st.code("M = massa CaCO₃ (mg) / ((100mL / 25mL) × volume EDTA (mL) × BM CaCO₃)") 
                st.write("**Perhitungan:**")
                st.write(f"M = {massa:.1f} mg / (4 × {volume:.2f} mL × {BM} mg/mmol)")
                st.success(f"Molaritas EDTA = {M:.4f} M")
            else:
                st.error("Volume tidak boleh 0.")

# =============================================
# 9. FITUR — MENENTUKAN INDIKATOR
# =============================================
elif fitur == "🔴 Menentukan Indikator Titrasi":
    st.subheader("🧪 PILIH JENIS TITRASI")
    JENIS = [
        "── PILIH ──",
        "🔴 JENIS TITRASI ASAM-BASA",
        "🟡 TITRASI REDOKS",
        "🟣 TITRASI KOMPLEKSOMETRI",
        "🟢 TITRASI ARGENTOMETRI",
    ]
    pilih_jenis = st.selectbox("Jenis Titrasi", JENIS, label_visibility="collapsed")
    st.divider()

    if pilih_jenis == "🔴 JENIS TITRASI ASAM-BASA":
        st.subheader("🔴 JENIS TITRASI ASAM-BASA")
        col1, col2 = st.columns(2)
        with col1:
            step(2, "JENIS TITRASI ASAM-BASA")
            titran = st.radio(
                "Titran",
                [
                    "Asam Kuat oleh Basa Kuat",
                    "Basa Lemah oleh Asam Kuat",
                    "Asam Lemah oleh Basa Kuat",
                    "Asam Lemah oleh Basa Lemah",
                ],
                label_visibility="collapsed",
            )
        with col2:
            st.divider()
            st.subheader("💡 Rekomendasi Indikator")
            if titran == "Asam Kuat oleh Basa Kuat":
                card("Bromtimol Biru", ["Rentang pH: 6.0 – 7.6", "Perubahan: Kuning → Biru"], "teal", True)
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0", "Perubahan: Tidak berwarna → Pink"], "red")
            elif titran == "Basa Lemah oleh Asam Kuat":
                card("Metil Jingga", ["Rentang pH: 3.1 – 4.4", "Perubahan: Kuning → Merah"], "orange", True)
                card("Metil Merah", ["Rentang pH: 4.2 – 6.2", "Perubahan: Kuning → Merah"], "red")
                warn("Fenolftalein tidak direkomendasikan karena perubahan warna terjadi di daerah basa.")
            elif titran == "Asam Lemah oleh Basa Kuat":
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0", "Perubahan: Tidak berwarna → Pink"], "red", True)
                warn("Jangan gunakan metil oranye atau metil merah.")
            else:  
                warn("Titrasi asam lemah – basa lemah tidak direkomendasikan secara analitik.")
        done()

    elif pilih_jenis == "🟡 TITRASI REDOKS":
        st.subheader("🟡 TITRASI REDOKS")
        step(2, "PILIH METODE TITRASI REDOKS")
        metode = st.radio(
            "Metode",
            ["Permanganometri", "Iodometri / Iodimetri"],
            horizontal=True,
            label_visibility="collapsed",
        )
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Permanganometri":
            card("KMnO₄ — Autoindicator", ["KMnO₄ bertindak sebagai indikator", "Titik akhir: larutan merah muda"], "purple", True)
            warn("Penggunaan blanko sangat dianjurkan untuk mengoreksi hasil titrasi.")
        else:  
            card("Larutan Kanji (Amilum)", ["Melibatkan iodin (I₂)", "Perubahan: Biru → Tidak berwarna"], "teal", True)
            warn("Tambahkan larutan kanji menjelang titik akhir titrasi (saat warna sudah kuning pucat).")
        done()

    elif pilih_jenis == "🟣 TITRASI KOMPLEKSOMETRI":
        st.subheader("🟣 TITRASI KOMPLEKSOMETRI (EDTA)")
        step(2, "Pilih Ion Logam yang Dititrasi")
        ION_DATA = {
            "Ca²⁺ / Mg²⁺": [("EBT", ["pH 10 — buffer amonia", "Perubahan: Merah anggur → Biru"], "teal", True)],
            "Zn²⁺": [("EBT", ["pH 10 — buffer amonia", "Perubahan: Merah anggur → Biru"], "teal", True)],
            "Cu²⁺": [("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True)],
            "Fe²⁺ / Fe³⁺": [
                ("Asam salisilat", ["pH 1–2", "Perubahan: Merah → Tidak berwarna"], "red", True),
                ("Tiron", ["pH 4–10", "Perubahan: Biru → Tidak berwarna"], "teal", False)
            ],
            "Pb²⁺": [("Xylenol Orange", ["pH 5–6", "Perubahan: Merah-ungu → Kuning"], "orange", True)],
            "Hg²⁺": [("Xylenol Orange", ["pH 2–3", "Perubahan: Merah → Kuning"], "orange", True)],
            "Al³⁺": [("Xylenol Orange + titrasi balik", ["pH 5", "Perubahan: Kuning → Merah-ungu"], "orange", True)],
            "Ni²⁺": [("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True)],
            "Co²⁺": [("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True)],
        }
        ion = st.selectbox("Ion Logam", ["── Pilih Ion Logam ──"] + list(ION_DATA.keys()), label_visibility="collapsed")
        if ion != "── Pilih Ion Logam ──":
            st.divider()
            st.subheader(f"💡 Rekomendasi Indikator untuk {ion}")
            for name, rows, color, starred in ION_DATA[ion]:
                card(name, rows, color, starred)
            done()

    elif pilih_jenis == "🟢 TITRASI ARGENTOMETRI":
        st.subheader("🟢 TITRASI ARGENTOMETRI")
        step(2, "PILIH METODE ARGENTOMETRI")
        metode = st.radio(
            "Metode",
            ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"],
            horizontal=True,
            label_visibility="collapsed",
        )
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Argentometri (Mohr)":
            card("Kalium Kromat — K₂CrO₄", ["Kondisi: pH 6.5 – 10,0", "Titik akhir: endapan merah bata"], "yellow", True)
        elif metode == "Argentometri (Volhard)":
            card("Besi(III) Amonium Sulfat", ["Kondisi: suasana asam", "Titik akhir: larutan berwarna merah"], "red", True)
        else:  
            card("Diklorofluoresein", ["Kondisi: pH 4 – 10", "Titik akhir: endapan merah muda"], "green", True)
            card("Fluoresein", ["Kondisi: pH 7 – 8,5", "Titik akhir: endapan merah muda"], "green")
        done()

    else:
        st.info("👆 Pilih jenis titrasi di atas untuk memulai.", icon="⚠️")
        st.markdown(
            """<div class="custom-white-box">
                <p>Panduan singkat:</p>
                <table style="width:100%; border-collapse: collapse;">
                    <thead>
                        <tr style="border-bottom: 2px solid black;">
                            <th style="padding: 8px;">Jenis</th>
                            <th style="padding: 8px;">Titran</th>
                            <th style="padding: 8px;">Contoh Analit</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td style="padding: 8px;">Asam-Basa</td><td style="padding: 8px;">NaOH / HCl</td><td style="padding: 8px;">CH₃COOH</td></tr>
                        <tr><td style="padding: 8px;">Redoks</td><td style="padding: 8px;">KMnO₄</td><td style="padding: 8px;">Fe²⁺</td></tr>
                        <tr><td style="padding: 8px;">Kompleksometri</td><td style="padding: 8px;">EDTA</td><td style="padding: 8px;">Ca²⁺, Mg²⁺</td></tr>
                        <tr><td style="padding: 8px;">Pengendapan</td><td style="padding: 8px;">AgNO₃</td><td style="padding: 8px;">Cl⁻</td></tr>
                    </tbody>
                </table>
            </div>""",
            unsafe_allow_html=True
        )

# =============================================
# 10. FOOTER
# =============================================
st.divider()
st.markdown(
    """<div class="custom-white-box" style="text-align:center; max-width: 400px; margin: 0 auto;">
        <span style='color: #000000 !important; font-weight: 900 !important; font-size: .9em;'>
            ⚛️ Sistem Rekomendasi Titrasi &nbsp;|&nbsp; Kelompok 5
        </span>
    </div>""",
    unsafe_allow_html=True,
  )
