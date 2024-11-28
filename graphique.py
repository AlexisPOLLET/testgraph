
import pandas as pd
import streamlit as st
import folium
import plotly.express as px

from streamlit_folium import folium_static


# Titre de l'application
st.title("Analyse des Séismes en France")

# Étape 1 : Téléchargement du fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV contenant les données des séismes", type=["csv"])

if uploaded_file:
    # Étape 2 : Lecture du fichier CSV
    try:
        data = pd.read_csv(uploaded_file)
        st.success("Fichier chargé avec succès !")

        # Aperçu des données
        st.subheader("Aperçu des données :")
        st.write(data.head())
        
        # Statistiques descriptives
        st.subheader("Statistiques descriptives des données :")
        st.write(data.describe())
        
        # Étape 3 : Filtrer les données pour la France
        st.subheader("Statistiques des séismes en France")
        data_france = data  # Utilisez un filtre si nécessaire pour votre dataset

data_france['date'] = pd.to_datetime(data_france['date'], infer_datetime_format=True, errors='coerce')
data_france['year'] = data_france['date'].dt.year

# Étape 4 : Frise chronologique des séismes
            st.subheader("Frise chronologique des séismes")
            data_france['date'] = pd.to_datetime(data_france['date'], infer_datetime_format=True, errors='coerce')
            data_france['year'] = data_france['date'].dt.year
            seismes_par_annee = data_france.groupby('year').size().reset_index(name='nombre_seismes')

            # Créer et afficher la frise chronologique avec Plotly
            fig = px.bar(
                seismes_par_annee, 
                x='year', 
                y='nombre_seismes', 
                title='Nombre de Séismes par Année en France',
                labels={'year': 'Année', 'nombre_seismes': 'Nombre de Séismes'},
                template='plotly_dark'
            )
            st.plotly_chart(fig)
