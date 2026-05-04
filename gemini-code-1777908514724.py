import streamlit as st
import pandas as pd

# Konfiguration
st.set_page_config(page_title="Supply Chain Game", layout="centered")

# Daten-Speicher (Simuliert für die Session)
if 'history' not in st.session_state:
    st.session_state.history = {f"Team {i}": [] for i in range(1, 13)}

st.title("🚲 Bikes & More - Manager Interface")

# Lehrer-Bereich (mit Passwort geschützt oder einfach diskret einklappbar)
with st.sidebar.expander("👨‍🏫 Lehrer-Konsole"):
    runde = st.number_input("Aktuelle Runde", 1, 10, step=1)
    nachfrage = st.number_input("Nachfrage bekanntgeben", value=20)
    if st.button("Spiel zurücksetzen"):
        st.session_state.history = {f"Team {i}": [] for i in range(1, 13)}
        st.rerun()

# Team-Bereich
team = st.selectbox("Wähle dein Team:", [f"Team {i}" for i in range(1, 13)])
st.info(f"Phase: Runde {runde}")

bestellung = st.number_input(f"Bestellmenge für Runde {runde}:", min_value=0, step=1)

if st.button("Bestellung abschicken"):
    # Speichere die Bestellung für das gewählte Team
    st.session_state.history[team].append({"Runde": runde, "Bestellung": bestellung})
    st.success(f"Bestellung für Team {team} gesichert!")
    st.balloons()

# Historie anzeigen
st.subheader("Eure bisherigen Entscheidungen")
df_team = pd.DataFrame(st.session_state.history[team])
st.table(df_team)