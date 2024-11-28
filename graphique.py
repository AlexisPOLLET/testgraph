import pandas as pd
import streamlit as st
import plotly.express as px

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
        
        # Vérifiez que les colonnes nécessaires existent
        if 'date' in data.columns and 'latitude' in data.columns and 'longitude' in data.columns:
            # Conversion des dates
            data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True, errors='coerce')
            data['year'] = data['date'].dt.year

            # Compter le nombre de séismes par année
            seismes_par_annee = data.groupby('year').size().reset_index(name='nombre_seismes')
                
            # Étape 4 : Diagramme en barres avec Plotly
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
            
            bot = st.checkbox("Afficher le graphique de la colonne alcohol: ")
            if bot:
              st.line_chart(fig)
                
        else:
            st.error("Le fichier doit contenir les colonnes 'date', 'latitude' et 'longitude'.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")

