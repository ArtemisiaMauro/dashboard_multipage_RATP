import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import re

df = pd.read_excel("trafic_2021.xlsx")
df_clean = df[df['Arrondissement'].notna()]
df['Correspondance_1'] = df['Correspondance_1'].astype(str)

st.subheader("Les 10 stations les plus fréquentées")
# --- Nettoyage et conversion en numérique ---
df['Trafic'] = pd.to_numeric(df['Trafic'], errors='coerce').fillna(0)

# Top 10 des stations
df_top_stations = df.groupby(['Station', 'Réseau'], as_index=False)['Trafic'].sum()
df_top_stations = df_top_stations.sort_values('Trafic', ascending=False).head(10)
df_top_stations = df_top_stations.sort_values('Trafic', ascending=True)  # Trier croissant

# Altair bar chart avec couleur par réseau
import altair as alt

chart = alt.Chart(df_top_stations).mark_bar().encode(
    x=alt.X('Trafic:Q', title='Trafic'),
    y=alt.Y('Station:N', sort=None, title='Station'),
    color=alt.Color(
        'Réseau:N',
        title='Réseau',
        scale=alt.Scale(
            domain=['Métro', 'RER'],
            range=['#1f77b4', "#6ea2c7"]
        )
    ),
    tooltip=['Station', 'Réseau', 'Trafic']
).properties(height=400)

st.altair_chart(chart, use_container_width=True)

st.write("Comme vu précédemment, les quartiers les plus fréquentés étaient parfois ceux comportant une ou plusieurs gares. Ce dernier graphique nous montre qu'effectivement la présence de ces gares doit être l'un des facteurs les plus importants quant au nombre d'usagers répertoriés.")

st.write("Parmi les 10 stations qui comptaient le plus d'usagers en 2021, 7 d'entres elles sont des stations desservant de grandes gares parisiennes. À côté de ces gares nous retrouvons aussi de grandes stations connues pour leur fréquentation comme Châtelet Les Halles ou Nanterre Préfecture.")
