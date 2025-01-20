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
                        params = {"location": location}
                        # Calls GET /elevation/single?location=<location>
                        response = call_api("GET", f"{base_url}/single", params=params)
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    elif choice == "Get Multi Elevations":
        locations_text = st.text_area(
            "Locations (lat,lng)",
            placeholder="Enter one location per line (lat,lng)",
            value='{\n"locations": [\n"12.93126,77.61638",\n"12.89731,77.65136"\n]\n}'
        )
        submit = st.button("Get Elevations")
        
        if submit:
            if not locations_text.strip():
                st.warning("Please provide at least one location.")
            else:
                with st.spinner("Fetching elevations..."):
                    try:
                        # Attempt to parse the user-provided JSON
                        # e.g. the default example is a JSON with "locations": ["12.93,77.61","12.89,77.65",...]
                        data = json.loads(locations_text)
                        
                        # The endpoint expects a dict with "locations": [{"lat":12.93,"lng":77.61},...]
                        # So we must transform each lat,lng string into a dict
                        location_dicts = []
                        for item in data["locations"]:
                            lat_str, lng_str = item.split(",")
                            location_dicts.append({
                                "lat": float(lat_str.strip()),
                                "lng": float(lng_str.strip())
                            })
                        
                        payload = {"locations": location_dicts}
                        
                        # Calls POST /elevation/multiple with JSON body
                        response = call_api("POST", f"{base_url}/multiple", body=payload)
                        st.json(response.json())

                    except json.JSONDecodeError:
                        st.error("Invalid JSON. Please provide valid JSON input.")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
