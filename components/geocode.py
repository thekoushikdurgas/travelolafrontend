import json
import streamlit as st
from utils.api import call_api

def geocode_component(base_url: str):
    st.title("Geocode API")

    endpoints = ["Forward Geocode", "Reverse Geocode"]
    choice = st.radio("Select Endpoint", endpoints)

    if choice == "Forward Geocode":
        address = st.text_input(
            "Address", 
            value="Bangalore, India", 
            placeholder="Enter a full address"
        )
        submit = st.button("Fetch Coordinates")
        
        if submit:
            if not address.strip():
                st.warning("Address cannot be empty.")
            else:
                with st.spinner("Fetching geocode data..."):
                    try:
                        params = {"address": address, "language": "en"}
                        # Calls GET /geocode
                        response = call_api("GET", f"{base_url}/geocode", params=params)
                        response_json = response.json()
                        
                        if "error" in response_json:
                            st.error(f"Error {response_json['code']}: {response_json['details']}")
                        else:
                            st.success("Geocoding successful!")
                            st.json(response_json)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    elif choice == "Reverse Geocode":
        latlng = st.text_input(
            "Lat,Lng", 
            value="12.9716,77.5946", 
            placeholder="Enter coordinates (lat,lng)"
        )
        submit = st.button("Fetch Address")
        
        if submit:
            if not latlng.strip() or "," not in latlng:
                st.warning("Invalid format. Use 'latitude,longitude'.")
            else:
                with st.spinner("Fetching reverse geocode data..."):
                    try:
                        params = {"latlng": latlng}
                        # Calls GET /geocode/reverse
                        response = call_api("GET", f"{base_url}/geocode/reverse", params=params)
                        response_json = response.json()
                        
                        if "error" in response_json:
                            st.error(f"Error {response_json['code']}: {response_json['details']}")
                        else:
                            st.success("Reverse Geocoding successful!")
                            st.json(response_json)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
