


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
