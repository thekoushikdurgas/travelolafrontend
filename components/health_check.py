import streamlit as st
from utils.api import call_api
import json

def health_check_component(base_url):
    st.header("Health Check")
    submit = st.button("Check Health")
    if submit:
        response = call_api("GET", f"{base_url}/health")
        try:
            # Attempt to display the JSON from the response
            # st.json(response)
            st.json(response.json())
        except TypeError:
            # Handle cases where the response is not JSON serializable
            st.error("Failed to receive a valid JSON response.")
