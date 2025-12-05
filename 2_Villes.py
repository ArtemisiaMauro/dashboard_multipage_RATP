import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import re

df = pd.read_excel("trafic_2021.xlsx")
df_clean = df[df['Arrondissement'].notna()]
df['Correspondance_1'] = df['Correspondance_1'].astype(str)

st.subheader("Les villes les plus fréquentées par le réseau d'usagers")

# --- Nettoyage et conversion en numérique ---
df['Trafic'] = pd.to_numeric(df['Trafic'], errors='coerce').fillna(0)

# Top 5 des villes
df_top_villes = df.groupby('Ville', as_index=False)['Trafic'].sum()
df_top_villes = df_top_villes.sort_values('Trafic', ascending=False).head(5)
df_top_villes = df_top_villes.sort_values('Trafic', ascending=True)  # Trier croissant

# Graphique Altair sans légende
chart = alt.Chart(df_top_villes).mark_bar(color='#1f77b4').encode(
    x=alt.X('Trafic:Q', title="Nombre d'usagers"),
    y=alt.Y('Ville:N', sort=None, title='Ville')  # respect ordre DataFrame
).properties(height=300)

st.altair_chart(chart, use_container_width=True)

st.write("La ville bien en tête du classement est la capitale, avec près de 870 millions d'usagers. Parmi les 4 autres villes du classement, 3 d'entre elles se situent dans le département des Hauts-de-Seine (92) : ces villes sont parmi les principales communes du département.")
