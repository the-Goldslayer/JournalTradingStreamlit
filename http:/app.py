# Permet de naviguer entre les trades
    trade_list = df.index.tolist()
    selected_trade_index = st.selectbox("Sélectionnez le Trade à visualiser :", trade_list)

    if selected_trade_index is not None:
        trade_data = df.loc[selected_trade_index]
        st.subheader(f"Trade du {trade_data['Date'].strftime('%d-%m-%Y')} ({trade_data['Tag_Strategie']})")
        st.info(f"Résultat : {trade_data['Resultat']} | P&L : ${trade_data['P&L_Brut']:.2f} | R : **{trade_data['R_Multiple']:.2f}**")

        col_img_1, col_img_2 = st.columns(2)

        # NOTE : Les liens Google Drive doivent être publics ou vous devez utiliser
        # une méthode d'authentification plus complexe pour Streamlit Cloud.

        with col_img_1:
            st.markdown(f"**Avant (Lien Drive)** : {trade_data['Screenshot_Avant_Lien']}")
            # Streamlit peut afficher une image directement si le lien est un lien direct vers l'image.
            # Pour Google Drive, il faut un lien direct (pas l'URL de partage classique).
            try:
                st.image(trade_data['Screenshot_Avant_Lien'], caption="Screenshot Avant", use_column_width=True)
            except Exception:
                st.warning("Impossible d'afficher l'image. Assurez-vous que le lien Google Drive est un lien direct (embed ou public).")

        with col_img_2:
            st.markdown(f"**Après (Lien Drive)** : {trade_data['Screenshot_Apres_Lien']}")
            try:
                st.image(trade_data['Screenshot_Apres_Lien'], caption="Screenshot Après", use_column_width=True)
            except Exception:
                st.warning("Impossible d'afficher l'image. Assurez-vous que le lien Google Drive est un lien direct (embed ou public).")

        st.markdown("---")
        st.subheader("Notes & Émotions")
        st.write(f"**Émotions :** {trade_data['Emotions']}")
        st.write(f"**Notes :** {trade_data['Notes']}")
