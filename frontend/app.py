import streamlit as st
import requests
from PIL import Image
import io

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Auto-Shop AI",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# URL du Backend
API_URL = "http://backend:8000/api/v1/products/process"

# --- GESTION DE LA MÉMOIRE (SESSION STATE) ---
# C'est ce qui empêche les données de disparaître quand on clique sur un bouton
if 'processed_results' not in st.session_state:
    st.session_state.processed_results = {}

# --- STYLE CSS CUSTOM ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%; border-radius: 5px; height: 3em;
        background-color: #FF4B4B; color: white;
    }
    /* Correction du texte invisible : On force le noir sur fond blanc */
    .description-box {
        background-color: white; 
        padding: 15px; 
        border-radius: 5px; 
        border: 1px solid #ddd;
        color: #000000 !important; /* Force le texte en noir */
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=80)
    st.title("Auto-Shop AI")
    st.markdown("---")
    
    st.header("📤 Importation")
    uploaded_files = st.file_uploader(
        "Déposez vos produits ici", 
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )
    
    # Bouton d'action
    process_btn = st.button("✨ Lancer l'Automatisation", type="primary", disabled=len(uploaded_files) == 0)
    
    # Bouton pour tout effacer
    if st.button("🗑️ Tout effacer"):
        st.session_state.processed_results = {}
        st.rerun()

    st.markdown("---")
    st.info("💡 **Conseils pour de meilleurs résultats :**\n\n"
            "✅ Objet bien éclairé\n"
            "✅ Objet entier dans l'image\n"
            "✅ Évitez les objets transparents (verres)\n"
            "✅ Contraste fort avec le fond")

# --- LOGIQUE DE TRAITEMENT (S'exécute au clic) ---
if process_btn and uploaded_files:
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, uploaded_file in enumerate(uploaded_files):
        # On utilise le nom du fichier comme clé unique pour éviter les doublons
        if uploaded_file.name not in st.session_state.processed_results:
            
            status_text.text(f"Traitement IA en cours : {uploaded_file.name}...")
            
            try:
                # Préparation
                image = Image.open(uploaded_file)
                uploaded_file.seek(0)
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                
                # Appel API
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    # ON SAUVEGARDE DANS LA MÉMOIRE DE SESSION
                    st.session_state.processed_results[uploaded_file.name] = {
                        "original_image": image,
                        "data": data,
                        "status": "success"
                    }
                else:
                    st.session_state.processed_results[uploaded_file.name] = {
                        "status": "error",
                        "message": response.text
                    }
            except Exception as e:
                st.session_state.processed_results[uploaded_file.name] = {
                    "status": "error",
                    "message": str(e)
                }
        
        progress_bar.progress((i + 1) / len(uploaded_files))
    
    status_text.success("🎉 Traitement terminé !")

# --- AFFICHAGE DES RÉSULTATS (Depuis la mémoire) ---
st.title("🏭 L'Usine à Contenu E-commerce")

if not st.session_state.processed_results:
    st.markdown("### 👋 Bienvenue ! Commencez par uploader des images à gauche.")

else:
    # On boucle sur les résultats stockés en mémoire
    # reverse() pour afficher les plus récents en haut
    for filename, result in list(st.session_state.processed_results.items())[::-1]:
        
        with st.expander(f"📦 Résultat : {filename}", expanded=True):
            
            if result["status"] == "success":
                data = result["data"]
                
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    st.caption("Originale")
                    st.image(result["original_image"], use_container_width=True)
                
                with col2:
                    st.caption("Détourée")
                    st.image(data["processed_image_url"], use_container_width=True)
                    
                    # Le téléchargement ne fera plus disparaître les images !
                    response_img = requests.get(data["processed_image_url"])
                    st.download_button(
                        label="⬇️ Télécharger PNG",
                        data=response_img.content,
                        file_name=f"clean_{filename}.png",
                        mime="image/png",
                        key=f"dl_{filename}" # Clé unique importante
                    )

                with col3:
                    st.caption("Description SEO Générée")
                    description = data.get("description", "Pas de description générée.")
                    # Utilisation de la classe CSS corrigée
                    st.markdown(f"<div class='description-box'>{description}</div>", unsafe_allow_html=True)
            
            else:
                st.error(f"Erreur sur {filename} : {result['message']}")