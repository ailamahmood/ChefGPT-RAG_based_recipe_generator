# recipe_page.py
import streamlit as st
from query_engine import get_recipe_from_query

def show():
    st.set_page_config(page_title="RAG Recipe Generator", page_icon="🍲")

    page_bg_image = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    /* Apply font to everything */
    html, body, [data-testid="stAppViewContainer"] *, .stMarkdown, .stButton, .stTextInput {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Background image */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/free-photo/top-view-frame-with-delicious-breakfast-copy-space_23-2148329262.jpg?t=st=1747043149~exp=1747046749~hmac=33ab8a2e121648d0333fd21806f3cde0c0b305ebaeb9e82e230278884690af86&w=1380");
        background-size: cover;
        margin-top: -40px;
    }

    /* Remove Streamlit's header background */
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }

    /* Push main content left */
    .main > div {
        max-width: 100% !important;
        padding-left: 3rem !important;
        padding-right: 1rem !important;
        margin-left: 0 !important;
    }

    /* General text styling */
    h1, h2, h3, h4, h5, h6,
    p, div, span, label,
    .stTextInput label,
    .stMarkdown, .stAlert p {
        color: black !important;
        text-align: left !important;
    }

    /* Button styling */
    .stButton > button {
        background-color: #706d6b !important;
        color: white !important;
        border: none !important;
        padding: 1em 3em !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        transition: all 0.3s ease !important;
        margin: 30px auto 0 0 !important; /* Align left */
        display: block !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
    }

    .stButton > button:hover {
        background-color: #878380 !important;
        transform: scale(1.05) !important;
    }
    </style>
    """

    st.markdown(page_bg_image, unsafe_allow_html=True)

    st.components.v1.html("""
    <div style="display: flex; align-items: center; transform: translateX(-50px);">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
            h1 {
                font-family: 'Poppins', sans-serif !important;
            }
        </style>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player 
            src="https://lottie.host/217fcb11-858b-40e9-9a30-5f911e6c0588/uJXAuMBnDp.json"  
            background="transparent"  
            speed="1"  
            style="width: 150px; height: 150px;transform: translateY(-10px);"  
            loop  
            autoplay>
        </lottie-player>
        <h1 style="margin: 0; margin-bottom: 20px; font-size: 34px; font-weight: 700;">RAG Recipe Generator</h1>
    </div>
    """, height=100)


    st.markdown("Enter your available ingredients and any preferences. Get a recipe suggestion!")

    ingredients = st.text_input("Ingredients", placeholder="e.g., chicken, tomato, rice")
    preferences = st.text_area("Preferences / Description", placeholder="e.g., something spicy and quick")

    if preferences.strip():
        user_query = f"I have {ingredients}. I want {preferences}."
    else:
        user_query = f"I have {ingredients}. What can I make?"


    if st.button("Generate Recipe") and user_query.strip():
        with st.spinner("Searching and generating recipe..."):
            result = get_recipe_from_query(user_query)
            st.success("Here's a recipe for you!")
            st.markdown(result)