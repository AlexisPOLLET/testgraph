import pandas as pd
import streamlit as st
import plotly.express as px

# Titre de l'application
st.title("Analyse des Séismes en France entre 1990 et 2023")

# Étape 1.1 : Téléchargement du fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV contenant les données des séismes", type=["csv"])

if uploaded_file:
    # Étape 1.2 : Lecture du fichier CSV
    try:
        data = pd.read_csv(uploaded_file)
        st.success("Fichier chargé avec succès !")

        # Aperçu des données
        st.subheader("Aperçu des données :")
        st.write(data.head())
        
        show_stat = st.checkbox("Afficher les statistiques descriptives des séismes en France")
            
        if show_stat:
            # Statistiques descriptives
            st.subheader("Statistiques descriptives des données :")
            st.write(data.describe())
            
            # Étape 1.3 : Filtrer les données pour la France
            st.subheader("Statistiques des séismes en France")
            
        # Vérifiez que les colonnes nécessaires existent
        if 'date' in data.columns and 'latitude' in data.columns and 'longitude' in data.columns:
            # Conversion des dates
            data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True, errors='coerce')
            data['year'] = data['date'].dt.year

            # Compter le nombre de séismes par année
            seismes_par_annee = data.groupby('year').size().reset_index(name='nombre_seismes')

            show_graph = st.checkbox("Afficher le graphique des séismes en France par année depuis 1990")
            
            if show_graph:
                # Étape 1.4 : Diagramme en barres avec Plotly
                st.subheader("Frise chronologique des séismes")
                fig = px.bar(
                    seismes_par_annee,
                    x='year',
                    y='nombre_seismes',
                    title='Nombre de Séismes par Année en France',
                    labels={'year': 'Année', 'nombre_seismes': 'Nombre de Séismes'},
                    template='plotly_dark'
                )
                st.plotly_chart(fig)


        #  Etape 2. : Vérification des colonnes nécessaires
        if 'latitude' in data.columns and 'longitude' in data.columns and 'significance' in data.columns:
            # Étape 2.1 : Filtrer les séismes par niveau de significance
            st.subheader("Analyse des Séismes par Niveau de Significance")

            low_significance = data[data['significance'] < 50]
            medium_significance = data[(data['significance'] >= 50) & (data['significance'] < 150)]
            high_significance = data[data['significance'] >= 150]

            st.write(f"Nombre de séismes de faible significance : {len(low_significance)}")
            st.write(f"Nombre de séismes de moyenne significance : {len(medium_significance)}")
            st.write(f"Nombre de séismes de forte significance : {len(high_significance)}")

            show_map = st.checkbox("Afficher la carte descriptives des séismes en France avec leur significance: ")
            
            if show_map:
                # Étape 2.2 : Créer une carte interactive avec Plotly
                st.subheader("Carte Interactive des Séismes")
                fig_map = px.scatter_mapbox(
                    data,
                    lat="latitude",
                    lon="longitude",
                    color="significance",  # Couleur selon la significance
                    size="significance",  # Taille des points selon la significance
                    hover_name="significance",
                    title="Carte des Séismes en France",
                    zoom=5,
                    mapbox_style="carto-positron"
                )
                st.plotly_chart(fig_map)

        show_corr = st.checkbox("Afficher la correlation entre la magnitude et la significance")

        if schow_corr:
            data_france[['significance', 'magnitude', 'depth']].corr()

        else:
            st.error("Le fichier doit contenir les colonnes 'date', 'latitude' et 'longitude'.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")

