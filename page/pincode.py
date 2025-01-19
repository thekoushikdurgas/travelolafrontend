from components.pincode import main_search_page
import streamlit as st

def pincode_lookup_tab(BASE_URL):
    """
    Wrapper for the main search page for pincode-based place lookup.
    
    Parameters:
        BASE_URL (str): The base URL for API requests.
    """
    try:
        main_search_page(BASE_URL)
    except Exception as e:
        st.error(f"An error occurred while loading the Pincode Lookup page: {e}")
