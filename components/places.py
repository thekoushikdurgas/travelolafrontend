import streamlit as st
from utils.api import call_api

def places_component(base_url):
    st.header("Places API")
    
    endpoints = [
        "Autocomplete API",
        "Place Details API",
        "Advanced Place Details API",
        "Nearby Search API",
        "Advanced Nearby Search API",
        "Text Search API",
        "Address Validation API",
        "Photo API"
    ]
    action = st.radio("Choose Endpoint", endpoints)

    # Autocomplete API
    if action == "Autocomplete API":
        query = st.text_input("Search Query", value="Kempegowda")
        # location = st.text_input("Location (lat,lng)", placeholder="Optional location")
        location = st.text_input("Location (lat,lng)", "", placeholder="Optional location")
        if not location.strip():
            st.warning("Please provide a valid location.")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        strictbounds = st.checkbox("Strict Bounds")
        submit = st.button("Get Suggestions")
        
        if submit:
            params = {
                "input": query,
                "location": location,
                "radius": radius,
                "strictbounds": strictbounds
            }
            response = call_api("GET", f"{base_url}/places/autocomplete", params=params)
            st.json(response.json())

    # Place Details API
    elif action == "Place Details API":
        place_id = st.text_input("Place ID", value="ola-platform:a79ed32419962a11a588ea92b83ca78e")
        submit = st.button("Get Place Details")
        
        if submit:
            params = {"place_id": place_id}
            response = call_api("GET", f"{base_url}/places/details", params=params)
            st.json(response.json())

    # Advanced Place Details API
    elif action == "Advanced Place Details API":
        place_id = st.text_input("Place ID", value="ola-platform:a79ed32419962a11a588ea92b83ca78e")
        submit = st.button("Get Advanced Place Details")
        
        if submit:
            params = {"place_id": place_id}
            response = call_api("GET", f"{base_url}/places/details/advanced", params=params)
            st.json(response.json())

    # Nearby Search API
    elif action == "Nearby Search API":
        # location = st.text_input("Location (lat,lng)", value="12.931544865377818,77.61638622280486")
        location = st.text_input("Location (lat,lng)", value="12.931544865377818,77.61638622280486", placeholder="Optional location")
        if not location.strip():
            st.warning("Please provide a valid location.")
        types = st.text_input("Place Types", placeholder="e.g., restaurant, cafe")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        with_centroid = st.checkbox("Include Geometry Centroid")
        rank_by = st.selectbox("Rank By", ["popular", "distance"], index=0)
        limit = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search Nearby Places")
        
        if submit:
            params = {
                "location": location,
                "types": types,
                "radius": radius,
                "withCentroid": with_centroid,
                "rankBy": rank_by,
                "limit": limit
            }
            response = call_api("GET", f"{base_url}/places/nearbysearch", params=params)
            st.json(response.json())

    # Advanced Nearby Search API
    elif action == "Advanced Nearby Search API":
        # location = st.text_input("Location (lat,lng)", value="12.931544865377818,77.61638622280486")
        location = st.text_input("Location (lat,lng)", "", placeholder="Optional location")
        if not location.strip():
            st.warning("Please provide a valid location.")
        types = st.text_input("Place Types", placeholder="e.g., restaurant, cafe")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        with_centroid = st.checkbox("Include Geometry Centroid")
        rank_by = st.selectbox("Rank By", ["popular", "distance"], index=0)
        limit = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search Advanced Nearby Places")
        
        if submit:
            params = {
                "location": location,
                "types": types,
                "radius": radius,
                "withCentroid": with_centroid,
                "rankBy": rank_by,
                "limit": limit
            }
            response = call_api("GET", f"{base_url}/places/nearbysearch/advanced", params=params)
            st.json(response.json())

    # Text Search API
    elif action == "Text Search API":
        query = st.text_input("Search Query", value="Cafes in Koramangala")
        # location = st.text_input("Location (lat,lng)", "", placeholder="Optional location")
        location = st.text_input("Location (lat,lng)", "", placeholder="Optional location")
        if not location.strip():
            st.warning("Please provide a valid location.")
        # if not location.strip():
        #     st.warning("Please provide a valid location.")
        # location = st.text_input("Location (lat,lng)", "", placeholder="Optional location")
        # if not location.strip():
        #     st.warning("Please provide a valid location.")
        # location = st.text_input("Location (lat,lng)", placeholder="Optional location")
        radius = st.number_input("Radius (meters)", value=5000, min_value=1)
        types = st.text_input("Place Types", placeholder="e.g., restaurant, cafe")
        size = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search by Text")
        
        if submit:
            params = {
                "input": query,
                "location": location,
                "radius": radius,
                "types": types,
                "size": size
            }
            response = call_api("GET", f"{base_url}/places/textsearch", params=params)
            st.json(response.json())

    # Address Validation API
    elif action == "Address Validation API":
        address = st.text_input("Address to Validate", value="7, Lok Kalyan Marg, New Delhi, Delhi, 110011")
        submit = st.button("Validate Address")
        
        if submit:
            params = {"address": address}
            response = call_api("GET", f"{base_url}/places/addressvalidation", params=params)
            st.json(response.json())

    # Photo API
    elif action == "Photo API":
        photo_reference = st.text_input("Photo Reference", value="c3ae78ac452ec049f67b3cf9aee2b2e8")
        submit = st.button("Get Photo")
        
        if submit:
            params = {"photo_reference": photo_reference}
            response = call_api("GET", f"{base_url}/places/photo", params=params)
            st.json(response.json())
