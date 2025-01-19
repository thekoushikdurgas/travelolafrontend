import json
import streamlit as st
from utils.api import call_api

def elevation_component(base_url):
    st.header("Elevation API")
    
    endpoints = ["Get Single Elevation", "Get Multi Elevations"]
    choice = st.radio("Select Endpoint", endpoints)

    if choice == "Get Single Elevation":
        location = st.text_input(
            "Location (lat,lng)", 
            value="12.931544865377818,77.61638622280486"
        )
        submit = st.button("Get Elevation")
        
        if submit:
            if not location.strip():
                st.warning("Please provide a valid location in 'lat,lng' format.")
            else:
                with st.spinner("Fetching elevation..."):
                    try:
                        # Pass the location directly (without JSON-wrapping) as a query param
                        params = {"location": location}
                        response = call_api("GET", f"{base_url}/single", params=params)
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    elif choice == "Get Multi Elevations":
        locations_text = st.text_area(
            "Locations (lat,lng)",
            placeholder="Enter one location per line (lat,lng)",
            value="12.93126,77.61638\n12.89731,77.65136"
        )
        submit = st.button("Get Elevations")
        
        if submit:
            if not locations_text.strip():
                st.warning("Please provide at least one location.")
            else:
                with st.spinner("Fetching elevations..."):
                    try:
                        # Parse each line as "lat,lng"
                        location_list = []
                        for line in locations_text.splitlines():
                            line = line.strip()
                            if line:
                                lat_str, lng_str = line.split(",")
                                location_list.append({
                                    "lat": float(lat_str), 
                                    "lng": float(lng_str)
                                })

                        payload = {"locations": location_list}
                        
                        response = call_api("POST", f"{base_url}/multiple", body=payload)
                        st.json(response.json())

                    except Exception as e:
                        st.error(f"Error: {str(e)}")
