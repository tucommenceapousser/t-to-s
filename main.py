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
Trhacknon est un hacktiviste, hacker et développeur web engagé, axé sur la lutte contre les injustices sociales et politiques. Voici un aperçu détaillé de ses compétences, expériences et engagements :

1. **Développement Web Sécurisé**
   - Expertise dans la conception et la mise en œuvre de sites web sécurisés.
   - Connaissance approfondie des meilleures pratiques en matière de sécurité web, y compris la prévention des vulnérabilités telles que XSS, CSRF et SQL Injection.

2. **Hacking Éthique**
   - Réalisation de tests d'intrusion pour identifier et corriger les failles de sécurité dans les systèmes.
   - Expérience dans l'audit de sécurité et la sensibilisation des organisations aux menaces de cybersécurité.

3. **Activisme Numérique**
   - Soutien actif aux causes sociales et politiques, avec un accent particulier sur la justice sociale, la cause palestinienne et ukrainienne.
   - Participation à des campagnes numériques pour promouvoir des causes anticapitalistes et anti-oppression.

4. **Projets Notables**
   - Développement de plusieurs outils et applications pour le soutien des causes sociales.
   - Collaboration avec des groupes de défense des droits de l'homme et des organisations non gouvernementales.

5. **Valeurs et Objectifs**
   - Engagement envers la transparence, la justice sociale, et la lutte contre l'oppression sous toutes ses formes.
   - Utilisation des compétences en développement web et hacking éthique pour promouvoir la sécurité et la justice.

- **Motivations Personnelles** : Trhacknon est profondément motivé par le désir de défendre les droits humains et de lutter contre les injustices politiques. Il croit fermement dans l'utilisation des compétences techniques pour faire progresser des causes importantes.

- **Méthodes de Travail** : Il adopte une approche rigoureuse dans le développement web sécurisé, en mettant en œuvre des pratiques de codage sécurisées et en effectuant des audits réguliers. En hacking éthique, il utilise des outils de pointe pour identifier et corriger les vulnérabilités des systèmes.

- **Exemples Concrets** :
   - Développement d'une plateforme sécurisée pour des groupes de défense des droits humains.
   - Participation à des projets de sensibilisation numérique pour les causes palestinienne et ukrainienne.
   - Collaboration avec des ONG pour la création de solutions technologiques visant à soutenir des initiatives anticapitalistes.

- **Valeurs Personnelles** : Trhacknon se distingue par son intégrité, son engagement envers la transparence et sa détermination à utiliser ses compétences pour un impact positif sur la société.
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


# st.title("Présentation de Trhacknon")

st.markdown('<div class="title">Présentation de Trhacknon</div>', unsafe_allow_html=True)

st.markdown("""
    <script>
        document.title = "Présentation de Trhacknon";
    </script>
""", unsafe_allow_html=True)
st.image("https://d.top4top.io/p_314462a0r0.png", caption="Trhacknon")

# Define custom CSS for styling
st.markdown("""
    <style>
            .title {
                margin-bottom: 30px;
                color: #00ff00; /* Couleur du texte */
                font-family: 'Roboto', sans-serif;
                font-size: 36px; /* Taille de la police */
                font-weight: bold; /* Gras */
                text-align: center; /* Alignement du texte */
                background-color: #000000; /* Couleur de fond */
                padding: 20px; /* Espacement autour du texte */
                border-radius: 10px; /* Bords arrondis */
            }
            .caption {
                font-size: 18px; /* Taille de la police de la légende */
                color: #ffffff; /* Couleur de la légende */
                text-align: center; /* Alignement de la légende */
            }

    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

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
        footer[class*="st-emotion-cache"] {
            display: none;
        }
        /* Custom Footer Style */
        .custom-footer {
            background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
            color: #fff;
            text-align: center;
            padding: 30px 20px;
            position: relative;
            box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.7);
            margin-top: 50px;
        }

        .custom-footer .footer-content h2 {
            font-family: 'Courier New', Courier, monospace;
            font-size: 2.5rem;
            color: #00ff99;
            text-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99;
            margin: 0 0 10px;
            animation: neon 1.5s ease-in-out infinite alternate;
        }

        .custom-footer .footer-content p {
            font-size: 1rem;
            color: #ccc;
            margin: 0 0 20px;
            font-style: italic;
        }

        .custom-footer .social-icons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .custom-footer .social-icon {
            display: inline-block;
            width: 40px;
            height: 40px;
            line-height: 40px;
            background-color: #00ff99;
            color: #1a1a1a;
            font-size: 1.5rem;
            border-radius: 50%;
            transition: all 0.3s ease;
            text-align: center;
            text-decoration: none;
            box-shadow: 0 0 10px #00ff99;
        }

        .custom-footer .social-icon:hover {
            background-color: #fff;
            color: #00ff99;
            box-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99;
        }

        @keyframes neon {
            from {
                text-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99;
            }
            to {
                text-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99;
            }
        }
    </style>
""", unsafe_allow_html=True)


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
st.markdown('<div class="content">Pour me contacter ou pour discuter de projets, envoyez un e-mail à: <a href="mailto:trhacknon@example.com" style="color:#00ffff;">trhacknon@example.com</a></div><footer class="custom-footer"><div class="footer-content"><h2>TRHACKNON</h2><p>Hacking the Future, One Code at a Time</p><div class="social-icons"><a href="https://www.facebook.com/bbatf021211612" class="social-icon facebook" target="https://www.facebook.com/bbatf021211612">F</a><a href="https://t.me/trhacknon" class="social-icon telegram" target="https://t.me/trhacknon">T</a><a href="https://github.com/tucommenceapousser" class="social-icon github" target="https://github.com/tucommenceapousser">G</a></div></div></footer>', unsafe_allow_html=True)