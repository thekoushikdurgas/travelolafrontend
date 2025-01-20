import json
import base64
import streamlit as st
from utils.api import call_api

def places_component(base_url: str):
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

    # ----------------------------------------------------------------
    # 1) AUTOCOMPLETE API
    # ----------------------------------------------------------------
    if action == "Autocomplete API":
        st.subheader("Autocomplete API")

        query = st.text_input("Search Query", value="Central Park")
        location = st.text_input("Location (lat,lng)", "", placeholder="Optional: 40.785091,-73.968285")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        strictbounds = st.checkbox("Strict Bounds")
        submit = st.button("Get Suggestions")

        if submit:
            params = {
                "input": query,
                "location": location if location.strip() else None,
                "radius": radius if radius > 0 else None,
                "strictbounds": strictbounds
            }
            with st.spinner("Fetching autocomplete suggestions..."):
                try:
                    response = call_api("GET", f"{base_url}/autocomplete", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Autocomplete suggestions retrieved!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 2) PLACE DETAILS API
    # ----------------------------------------------------------------
    elif action == "Place Details API":
        st.subheader("Place Details API")

        place_id = st.text_input("Place ID", value="ola-platform:a79ed32419962a11a588ea92b83ca78e")
        submit = st.button("Get Place Details")

        if submit:
            params = {"place_id": place_id}
            with st.spinner("Fetching place details..."):
                try:
                    response = call_api("GET", f"{base_url}/details", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Place details retrieved!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 3) ADVANCED PLACE DETAILS API
    # ----------------------------------------------------------------
    elif action == "Advanced Place Details API":
        st.subheader("Advanced Place Details API")

        place_id = st.text_input("Place ID", value="ola-platform:a79ed32419962a11a588ea92b83ca78e")
        submit = st.button("Get Advanced Place Details")

        if submit:
            params = {"place_id": place_id}
            with st.spinner("Fetching advanced place details..."):
                try:
                    response = call_api("GET", f"{base_url}/details/advanced", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Advanced place details retrieved!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 4) NEARBY SEARCH API
    # ----------------------------------------------------------------
    elif action == "Nearby Search API":
        st.subheader("Nearby Search API")

        location = st.text_input("Location (lat,lng)", value="40.785091,-73.968285", placeholder="e.g., 40.785091,-73.968285")
        types = st.text_input("Place Types", placeholder="e.g., restaurant,cafe")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        rank_by = st.selectbox("Rank By", ["popular", "distance"])
        limit = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search Nearby Places")

        if submit:
            params = {
                "location": location,
                "types": types if types.strip() else None,
                "radius": radius,
                "rankBy": rank_by,
                "limit": limit
            }
            with st.spinner("Performing nearby search..."):
                try:
                    response = call_api("GET", f"{base_url}/nearbysearch", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Nearby places retrieved!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 5) ADVANCED NEARBY SEARCH API
    # ----------------------------------------------------------------
    elif action == "Advanced Nearby Search API":
        st.subheader("Advanced Nearby Search API")

        location = st.text_input("Location (lat,lng)", value="", placeholder="e.g., 40.785091,-73.968285")
        types = st.text_input("Place Types", placeholder="e.g., restaurant,cafe")
        radius = st.number_input("Radius (meters)", value=1000, min_value=1)
        with_centroid = st.checkbox("Include Geometry Centroid")
        rank_by = st.selectbox("Rank By", ["popular", "distance"])
        limit = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search Advanced Nearby Places")

        if submit:
            if not location.strip():
                st.warning("Please provide a valid location.")
            else:
                params = {
                    "location": location,
                    "types": types if types.strip() else None,
                    "radius": radius,
                    "withCentroid": with_centroid,
                    "rankBy": rank_by,
                    "limit": limit
                }
                with st.spinner("Performing advanced nearby search..."):
                    try:
                        response = call_api("GET", f"{base_url}/nearbysearch/advanced", params=params)
                        resp_json = response.json()
                        if "error" in resp_json:
                            st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                        else:
                            st.success("Advanced nearby places retrieved!")
                            st.json(resp_json)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 6) TEXT SEARCH API
    # ----------------------------------------------------------------
    elif action == "Text Search API":
        st.subheader("Text Search API")

        query = st.text_input("Search Query", value="Cafes in Koramangala")
        location = st.text_input("Location (lat,lng)", value="", placeholder="Optional: 12.9716,77.5946")
        radius = st.number_input("Radius (meters)", value=5000, min_value=1)
        types = st.text_input("Place Types", placeholder="e.g., restaurant,cafe")
        size = st.slider("Number of Results", min_value=1, max_value=50, value=5)
        submit = st.button("Search by Text")

        if submit:
            params = {
                "input": query,
                "location": location if location.strip() else None,
                "radius": radius,
                "types": types if types.strip() else None,
                "size": size
            }
            with st.spinner("Performing text search..."):
                try:
                    response = call_api("GET", f"{base_url}/textsearch", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Text search results retrieved!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 7) ADDRESS VALIDATION API
    # ----------------------------------------------------------------
    elif action == "Address Validation API":
        st.subheader("Address Validation API")

        address = st.text_input("Address to Validate", value="7, Lok Kalyan Marg, New Delhi, Delhi, 110011")
        submit = st.button("Validate Address")

        if submit:
            params = {"address": address}
            with st.spinner("Validating address..."):
                try:
                    response = call_api("GET", f"{base_url}/addressvalidation", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Address validated!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 8) PHOTO API
    # ----------------------------------------------------------------
    elif action == "Photo API":
        st.subheader("Photo API")

        photo_reference = st.text_input("Photo Reference", value="c3ae78ac452ec049f67b3cf9aee2b2e8")
        maxwidth = st.number_input("Max Width (pixels)", value=400, min_value=1)
        maxheight = st.number_input("Max Height (pixels)", value=400, min_value=1)
        submit = st.button("Get Photo")

        if submit:
            params = {
                "photo_reference": photo_reference,
                "maxwidth": maxwidth,
                "maxheight": maxheight
            }
            with st.spinner("Fetching photo..."):
                try:
                    response = call_api("GET", f"{base_url}/photo", params=params)
                    resp_json = response.json()
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        if "photo_data" in resp_json:
                            # Decode base64 and display image
                            photo_data = base64.b64decode(resp_json["photo_data"])
                            st.image(photo_data, caption="Fetched Photo")
                        elif "photoUrl" in resp_json:
                            # Display image from URL
                            st.image(resp_json["photoUrl"], caption="Fetched Photo")
                        else:
                            st.json(resp_json)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
