import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import re

st.caption("Artemisia MAURO")

st.header("Analyse du trafic du réseau de métro parisien (RATP)")

st.write("La Régie autonome des transports parisiens (RATP) assure l'exploitation d'une partie des transports en commun de Paris et de sa banlieue.")
st.write("Afin d'observer l'efficacité de ce réseau, nous allons analyser le trafic de certaines lignes de métro et de RER en 2021.")

st.subheader("Aperçu de la table")
st.caption("🔗 [Source : Trafic annuel entrant par station du réseau ferré 2021 (data.ratp)](https://data.ratp.fr/explore/dataset/trafic-annuel-entrant-par-station-du-reseau-ferre-2021/export/)")
df = pd.read_excel("trafic_2021.xlsx")

st.dataframe(df.head(10))
st.caption("(La variable Ligne est identique à la variable Correspondance_1, mais formatée de manière à pouvoir être exploitée correctement pour l'analyse de la page suivante.)")

df_clean = df[df['Arrondissement'].notna()]
df['Correspondance_1'] = df['Correspondance_1'].astype(str)


st.subheader("Chiffres clés de 2021")

# --- Nettoyage et conversion en numérique ---
df['Trafic'] = pd.to_numeric(df['Trafic'], errors='coerce')
nb_usagers = df['Trafic'].sum()

df['Correspondance_1'] = pd.to_numeric(df['Correspondance_1'], errors='coerce')
nb_lignes = df['Correspondance_1'].nunique()

# --- Valeur de l'année précédente ---
nb_usagers_annee_prec = 913_388_062

# --- Calcul de la différence ---
delta_usagers = nb_usagers - nb_usagers_annee_prec
delta_pourcentage = (delta_usagers / nb_usagers_annee_prec) * 100

# --- Affichage des metrics ---
col1, col2 = st.columns(2)

col1.metric(
    label="💼 Usagers",
    value=f"{nb_usagers:,.0f}",
    delta=f"{delta_usagers:+,.0f} ({delta_pourcentage:.1f}%)"
)

col2.metric(
    label="🚇 Lignes",
    value=f"{nb_lignes:,.0f}"
)

st.write("Parmi les 14 lignes analysées, la RATP a vu sa part d'usagers augmenter d'un peu plus de 33%, c'est-à-dire de près de 305 millions d'usagers.")
