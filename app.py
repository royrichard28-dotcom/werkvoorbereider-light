import streamlit as st

st.set_page_config(
    page_title="Werkvoorbereider Light",
    page_icon="🛠️",
    layout="wide"
)

# -----------------------------
# STYLING / BANNERS
# -----------------------------
st.markdown("""
<style>
.main-banner {
    background: linear-gradient(90deg, #111111, #2b2b2b);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    color: white;
}

.main-title {
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 5px;
}

.main-subtitle {
    font-size: 18px;
    color: #d6d6d6;
}

.gold-line {
    height: 5px;
    background: linear-gradient(90deg, #c9a227, #f2d16b);
    border-radius: 10px;
    margin-bottom: 25px;
}

.info-card {
    background-color: #f5f5f5;
    padding: 18px;
    border-radius: 14px;
    border-left: 6px solid #c9a227;
    margin-bottom: 25px;
}

.section-banner {
    background-color: #eeeeee;
    padding: 14px 18px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 20px;
}

.footer {
    background-color: #111111;
    color: #d6d6d6;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# LOGO + HEADER
# -----------------------------
st.image("rl_lew_logo.png", width=260)

st.markdown("""
<div class="main-banner">
    <div class="main-title">🛠️ Werkvoorbereider Light</div>
    <div class="main-subtitle">
        Snel en eenvoudig een basis werkvoorbereiding maken voor inspectie, onderhoud, reparatie en montage.
    </div>
</div>
<div class="gold-line"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <b>Light versie</b><br>
    Deze versie is bedoeld om snel een eenvoudige werkvoorbereiding te maken. 
    Voor uitgebreide functies zoals PDF-export, opslag, klantbeheer en AI-ondersteuning kan een Pro-versie worden aangeschaft.
</div>
""", unsafe_allow_html=True)


# -----------------------------
# INVOERGEGEVENS
# -----------------------------
st.markdown('<div class="section-banner">📌 Algemene gegevens</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    klant = st.text_input("Klantnaam")
    locatie = st.text_input("Locatie")
    datum = st.date_input("Datum")

with col2:
    beroep = st.selectbox(
        "Soort werk",
        [
            "Inspectie",
            "Onderhoud",
            "Reparatie",
            "Montage",
            "Keuring",
            "Storing",
            "Anders"
        ]
    )

    eigen_beroep = st.text_input("Anders, namelijk")
    prioriteit = st.selectbox("Prioriteit", ["Normaal", "Hoog", "Spoed"])


# -----------------------------
# WERKZAAMHEDEN
# -----------------------------
st.markdown('<div class="section-banner">📝 Werkzaamheden</div>', unsafe_allow_html=True)

werkzaamheden = st.text_area(
    "Omschrijf werkzaamheden",
    height=140,
    placeholder="Bijvoorbeeld: inspecteren van hijsmiddelen, uitvoeren van onderhoud, storing zoeken, onderdelen controleren..."
)


# -----------------------------
# GEREEDSCHAP
# -----------------------------
st.markdown('<div class="section-banner">🧰 Benodigd gereedschap</div>', unsafe_allow_html=True)

gereedschap = st.multiselect(
    "Selecteer benodigd gereedschap",
    [
        "Handgereedschap",
        "Meetgereedschap",
        "Momentsleutel",
        "Accuboormachine",
        "Ladder",
        "PBM",
        "Hijsmiddelen",
        "Markeermateriaal",
        "Laptop/tablet",
        "Reinigingsmateriaal",
        "Onderdelen",
        "Anders"
    ]
)

extra_gereedschap = st.text_input("Extra gereedschap / materialen")


# -----------------------------
# VEILIGHEID
# -----------------------------
st.markdown('<div class="section-banner">⚠️ Veiligheid en aandachtspunten</div>', unsafe_allow_html=True)

veiligheid = st.multiselect(
    "Selecteer veiligheidspunten",
    [
        "PBM verplicht",
        "Werkplek afzetten",
        "Spanning uitschakelen",
        "Hoogtewerk",
        "Hijsgebied vrijhouden",
        "LMRA uitvoeren",
        "Overleg met klant",
        "Machine/installatie buiten bedrijf stellen",
        "Controle op struikelgevaar",
        "Werkvergunning controleren"
    ]
)

extra_veiligheid = st.text_area(
    "Extra veiligheidsopmerkingen",
    height=100,
    placeholder="Bijvoorbeeld: toegang melden bij receptie, sleutel ophalen, overleg met contactpersoon..."
)


# -----------------------------
# RESULTAAT
# -----------------------------
st.markdown('<div class="section-banner">📋 Werkvoorbereiding genereren</div>', unsafe_allow_html=True)

if st.button("Maak werkvoorbereiding"):
    soort_werk = eigen_beroep if eigen_beroep else beroep

    st.success("Werkvoorbereiding is aangemaakt.")

    st.markdown("""
    <div style="
    background-color:#ffffff;
    padding:22px;
    border-radius:16px;
    border:1px solid #dddddd;
    margin-top:20px;">
    """, unsafe_allow_html=True)

    st.subheader("📋 Werkvoorbereiding")

    st.write(f"**Klant:** {klant}")
    st.write(f"**Locatie:** {locatie}")
    st.write(f"**Datum:** {datum}")
    st.write(f"**Soort werk:** {soort_werk}")
    st.write(f"**Prioriteit:** {prioriteit}")

    st.markdown("### 📝 Werkzaamheden")
    if werkzaamheden:
        st.write(werkzaamheden)
    else:
        st.write("Geen werkzaamheden ingevuld.")

    st.markdown("### 🧰 Benodigd gereedschap")
    if gereedschap:
        st.write(", ".join(gereedschap))
    else:
        st.write("Geen gereedschap geselecteerd.")

    if extra_gereedschap:
        st.write(f"**Extra:** {extra_gereedschap}")

    st.markdown("### ⚠️ Veiligheid / aandachtspunten")
    if veiligheid:
        st.write(", ".join(veiligheid))
    else:
        st.write("Geen veiligheidspunten geselecteerd.")

    if extra_veiligheid:
        st.write(f"**Extra opmerkingen:** {extra_veiligheid}")

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
    R. Lew | Technische Werkvoorbereiding Tool | Light versie
</div>
""", unsafe_allow_html=True)
