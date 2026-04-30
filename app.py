import streamlit as st

st.set_page_config(
    page_title="Werkvoorbereider Light",
    page_icon="🛠️",
    layout="wide"
)

# LOGO (PAS EXTENSIE AAN!)
st.image("rl_lew_logo.png", width=250)

st.title("🛠️ Werkvoorbereider Light")
st.write("Eenvoudige tool om snel een basis werkvoorbereiding te maken.")

st.markdown("---")

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

werkzaamheden = st.text_area("Omschrijf werkzaamheden")

gereedschap = st.multiselect(
    "Benodigd gereedschap",
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
        "Anders"
    ]
)

extra_gereedschap = st.text_input("Extra gereedschap")

veiligheid = st.multiselect(
    "Veiligheid / aandachtspunten",
    [
        "PBM verplicht",
        "Werkplek afzetten",
        "Spanning uitschakelen",
        "Hoogtewerk",
        "Hijsgebied vrijhouden",
        "LMRA uitvoeren",
        "Overleg met klant"
    ]
)

st.markdown("---")

if st.button("Maak werkvoorbereiding"):
    soort_werk = eigen_beroep if eigen_beroep else beroep

    st.subheader("📋 Werkvoorbereiding")

    st.write(f"**Klant:** {klant}")
    st.write(f"**Locatie:** {locatie}")
    st.write(f"**Datum:** {datum}")
    st.write(f"**Soort werk:** {soort_werk}")
    st.write(f"**Prioriteit:** {prioriteit}")

    st.markdown("### Werkzaamheden")
    st.write(werkzaamheden)

    st.markdown("### Benodigd gereedschap")
    if gereedschap:
        st.write(", ".join(gereedschap))
    if extra_gereedschap:
        st.write(f"Extra: {extra_gereedschap}")

    st.markdown("### Veiligheid / aandachtspunten")
    if veiligheid:
        st.write(", ".join(veiligheid))

    st.success("Werkvoorbereiding is aangemaakt.")