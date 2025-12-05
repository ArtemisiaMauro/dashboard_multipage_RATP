import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import re

df = pd.read_excel("trafic_2021.xlsx")
df_clean = df[df['Arrondissement'].notna()]
df['Correspondance_1'] = df['Correspondance_1'].astype(str)

st.subheader("Trafic par ligne ou arrondissement")
# --- Sélecteur utilisateur ---
choix = st.selectbox("Afficher le trafic par :", ["Ligne", "Arrondissement"])

if choix == "Ligne":
    # Agréger par la colonne 'Ligne'
    df_group = df.groupby('Ligne', as_index=False)['Trafic'].sum()
    x_col = 'Ligne'
else:
    # Agréger par arrondissement
    df_group = df.groupby('Arrondissement', as_index=False)['Trafic'].sum()
    x_col = 'Arrondissement'

# --- Tri croissant ---
df_group = df_group.sort_values('Trafic', ascending=True)

# --- Affichage du graphique ---
st.bar_chart(data=df_group, x=x_col, y='Trafic', color='#1f77b4')
st.write("Les 3 lignes les plus fréquentées sont le RER A et les métros 4 et 1. Le RER A combine à lui seul environ 15,3%, soit près d'un tiers du trafic total annuel")

st.write("Les arrondissements les plus fréquentés sont quant à eux le 12ème, 10ème, 8ème et 1er : d'importantes gares comme la Gare du Nord ou la Gare saint Lazare se trouve dans certains de ces arrondissements.")
