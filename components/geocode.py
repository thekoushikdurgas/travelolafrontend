import streamlit as st
from utils.api import call_api

def geocode_component(base_url):
    st.title("Geocode API")
    
    endpoint = st.radio("Select Endpoint", ["Forward Geocode", "Reverse Geocode"])

    if endpoint == "Forward Geocode":
        address = st.text_input("Address", value="Bangalore, India", placeholder="Enter a full address")
        submit = st.button("Fetch Coordinates")
        
        if submit:
            if not address.strip():
                st.warning("Address cannot be empty.")
            else:
                with st.spinner("Fetching geocode data..."):
                    try:
                        response = call_api("GET", f"{base_url}/geocode/geocode", params={"address": address})
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    elif endpoint == "Reverse Geocode":
        latlng = st.text_input("Lat,Lng", value="12.931544865377818,77.61638622280486", placeholder="Enter coordinates (lat,lng)")
        submit = st.button("Fetch Address")
        
        if submit:
            if not latlng.strip() or "," not in latlng:
                st.warning("Invalid format. Use 'latitude,longitude'.")
            else:
                with st.spinner("Fetching reverse geocode data..."):
                    try:
                        response = call_api("GET", f"{base_url}/geocode/geocode/reverse", params={"latlng": latlng})
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
