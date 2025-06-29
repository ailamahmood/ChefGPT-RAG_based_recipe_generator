import streamlit as st
import json

# Function to show the landing page content
def show():
    st.set_page_config(page_title="RAG Recipe Generator", page_icon="🍲")

    # Custom CSS for background, fonts, shadows, button styling, and layout adjustments
    page_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    /* Apply font to everything */
    html, body, [data-testid="stAppViewContainer"] *, .stMarkdown, .stButton, .stTextInput {
        font-family: 'Poppins', sans-serif !important;
    }

    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/free-photo/3d-wooden-table-against-defocussed-sunny-room-interior_1048-10411.jpg?t=st=1747043029~exp=1747046629~hmac=3f58e1cfbd0d95aee5205c4dc7d1e34050602a2cc7474241fce5f4223e439409&w=826");
        background-size: cover;
        color: black;
        margin-top: -40px;  
    }

    h1, p, div, span, .stText, .stMarkdown {
        color: black !important;
        text-align: center !important;
    }

    h1 {
        font-size: 3em;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);

    }

    p {
        margin-bottom: -10px;
        font-size: 1.2em;
        font-weight: 500;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }

    .stButton > button {
        background-color: #f24935 !important;
        color: white !important;
        border: none !important;
        padding: 1em 3em !important;  /* Increased horizontal padding */
        border-radius: 12px !important;
        font-size: 16px !important;   /* Increased font size */
        font-weight: 800 !important;
        transition: all 0.3s ease !important;
        margin: 0px auto !important;
        display: block !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
    }

    .stButton > button:hover {
        background-color: #faa73d !important;
        transform: scale(1.05) !important;
    }
    </style>
    """
    st.markdown(page_styles, unsafe_allow_html=True)

    # Session state setup
    if "page" not in st.session_state:
        st.session_state.page = "landing"

    if st.session_state.page == "search":
        st.experimental_rerun()

    # Centered heading and paragraph
    st.markdown("<h1>Welcome to Recipe Generator!</h1>", unsafe_allow_html=True)
    st.markdown("<p>Click below to start your cooking journey!</p>", unsafe_allow_html=True)

    # Lottie animation with upward shift
    st.components.v1.html("""
        <div style="display: flex; justify-content: center; align-items: center; transform: translateY(-40px);">
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player 
                src="https://lottie.host/716bdacb-1e8f-4c68-a219-c3aefcb86b9a/5eWmUFZYbv.json"  
                background="transparent"  
                speed="1"  
                style="height: 300px;"  
                loop  
                autoplay>
            </lottie-player>
        </div>
    """, height=250)

    # Centered animated button
    with st.container():
        st.markdown('<div class="centered-button">', unsafe_allow_html=True)
        if st.button("Start Cooking!"):
            st.session_state.page = "recipe"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
