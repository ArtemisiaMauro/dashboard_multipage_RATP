import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import subprocess, sys
import re

st.write("En résumé, l'analyse du trafic 2021 met en évidence que la majorité des usagers se concentre sur quelques lignes et stations clés, notamment le RER A et les lignes 1 et 4 du métro, ainsi que dans des arrondissements et villes centrales comme Paris et certaines communes des Hauts-de-Seine. La présence de grandes gares semble être un facteur déterminant dans la fréquentation élevée de certaines stations. Globalement, le réseau RATP a connu une hausse significative du trafic par rapport à l'année précédente, soulignant l'importance de ces axes pour la mobilité quotidienne.")