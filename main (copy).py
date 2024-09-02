import streamlit as st
import openai
import os
from dotenv import load_dotenv
import html

# Charger les variables d'environnement
load_dotenv()

# Récupérer les clés API depuis les variables d'environnement
API_KEYS = [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY1"),
    os.getenv("OPENAI_API_KEY2"),
    os.getenv("OPENAI_API_KEY3")
]

# Fonction pour obtenir la clé API disponible
def get_available_api_key():
    for key in API_KEYS:
        if key:
            return key
    raise ValueError("Aucune clé API OpenAI valide trouvée.")

# Configurer OpenAI avec la clé API disponible
def configure_openai():
    openai.api_key = get_available_api_key()

# Contexte sur Trhacknon
CONTEXT = """
Trhacknon est un hacktiviste, hacker et développeur web passionné par la lutte contre les injustices sociales et politiques. Il soutient activement la cause palestinienne et ukrainienne et utilise ses compétences pour promouvoir des causes anticapitalistes. Voici quelques-unes de ses compétences et engagements :
- Développement web sécurisé
- Hacking éthique pour protéger les données et systèmes
- Activisme numérique pour soutenir des causes sociales et politiques
"""

# Fonction pour appeler l'API OpenAI avec le modèle de chat
def query_openai(prompt):
    configure_openai()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": CONTEXT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erreur lors de l'appel à l'API OpenAI: {e}"

# Fonction pour échapper les entrées HTML
def escape_html(text):
    return html.escape(text)

# Define custom CSS for styling
st.markdown("""
    <style>
        .title {
            color: #00ff00; /* Neon green */
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            background-color: #000000; /* Black background */
            padding: 20px;
            border-radius: 10px;
        }
        .section-header {
            color: #ff00ff; /* Neon pink */
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
        .content {
            color: #00ffff; /* Cyan */
            font-size: 18px;
            background-color: #222222; /* Dark gray background */
            padding: 15px;
            border-radius: 8px;
        }
        .button {
            background-color: #ff00ff; /* Neon pink */
            color: #ffffff; /* White text */
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #ff99ff; /* Light pink on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Set the title
st.markdown('<div class="title">Présentation de Trhacknon</div>', unsafe_allow_html=True)

# Introduction
st.markdown('<div class="section-header">Introduction</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Bonjour, je suis Trhacknon, un hacktiviste, hacker et développeur web passionné par la lutte contre les injustices sociales et politiques. Mon objectif est d’utiliser mes compétences pour soutenir des causes qui me tiennent à cœur.</div>', unsafe_allow_html=True)

# Query section
st.markdown('<div class="section-header">Interrogez l\'IA</div>', unsafe_allow_html=True)
user_query = st.text_input('Posez une question sur les compétences de Trhacknon:', '')

if st.button('Obtenir Réponse'):
    if user_query:
        # Échapper les entrées pour éviter XSS
        safe_query = escape_html(user_query)
        result = query_openai(f"Décrivez les compétences de Trhacknon en réponse à : {safe_query}")
        if result:
            st.markdown(f'<div class="content">{result}</div>', unsafe_allow_html=True)
        else:
            st.error("Erreur lors de la récupération de la réponse.")
    else:
        st.error("Veuillez entrer une question.")

# Add more content with styling
st.markdown('<div class="section-header">Soutien aux Causes</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Mon engagement pour les causes palestinienne et ukrainienne passe par la sensibilisation, le soutien à des initiatives locales et internationales, et la participation à des actions qui visent à lutter contre l’oppression et les injustices.</div>', unsafe_allow_html=True)
st.markdown('<div class="content"><ul><li><a href="https://www.palestinecampaign.org/" style="color:#00ffff;">Palestine Campaign</a></li><li><a href="https://www.ukraine.ua/" style="color:#00ffff;">Ukraine.ua</a></li><li><a href="https://antifa.com/" style="color:#00ffff;">Antifa</a></li></ul></div>', unsafe_allow_html=True)

# Contact Information
st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Pour me contacter ou pour discuter de projets, envoyez un e-mail à: <a href="mailto:trhacknon@example.com" style="color:#00ffff;">trhacknon@example.com</a></div>', unsafe_allow_html=True)