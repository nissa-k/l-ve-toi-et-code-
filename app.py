# app.py
# Streamlit wrapper qui affiche ta landing page (index.html + style.css) dans Streamlit.

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lève-toi et Code",
    layout="wide",
)

ROOT = Path(__file__).parent
HTML_PATH = ROOT / "index.html"
CSS_PATH = ROOT / "style.css"

def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")

html = load_text(HTML_PATH)
css = load_text(CSS_PATH)

if not html:
    st.error("index.html introuvable. Mets index.html à la racine du projet (au même niveau que app.py).")
    st.stop()

# Injecte le CSS dans le HTML (pour que ton style.css s'applique dans Streamlit)
# 1) Ajoute une balise <style> dans <head> si possible
# 2) Sinon, on préfixe le HTML avec <style>...</style>
style_tag = f"<style>\n{css}\n</style>" if css else ""

if "<head" in html.lower():
    # Insertion juste avant </head>
    lower = html.lower()
    idx = lower.rfind("</head>")
    if idx != -1:
        html = html[:idx] + style_tag + html[idx:]
    else:
        html = style_tag + html
else:
    html = style_tag + html

# (Optionnel) Nettoyage léger : évite le scroll-behavior (pas utile en iframe)
# Tu peux supprimer ces 2 lignes si tu veux
html = html.replace("scroll-behavior: smooth;", "")

# Affiche la page dans Streamlit
# height assez grand pour éviter une iframe trop petite
components.html(html, height=1400, scrolling=True)
