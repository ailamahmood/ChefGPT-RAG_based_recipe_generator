import streamlit as st
import landing_page
import recipe_page



# Initialize the session state variable for page routing
if "page" not in st.session_state:
    st.session_state.page = "landing"

# Simple page routing based on session state
if st.session_state.page == "landing":
    landing_page.show()
elif st.session_state.page == "recipe":
    recipe_page.show()
