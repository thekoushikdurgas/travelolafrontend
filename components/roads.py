import streamlit as st
from utils.api import call_api

def roads_component(base_url):
    st.header("Roads API")

    endpoints = ["Snap to Road API", "Nearest Roads API", "Speed Limits API"]
    action = st.radio("Choose Endpoint", endpoints)

    # ----------------------------------------------------------------
    # 1) Snap to Road
    # ----------------------------------------------------------------
    if action == "Snap to Road API":
        points = st.text_area(
            "Coordinates (lat,lng|lat,lng)",
            placeholder="Enter points separated by '|'. e.g.: 12.931544865377818,77.61638622280486|12.9352,77.6245",
            value="12.99927894246456,77.67323803525812|12.992086564113583,77.65899014102202"
        )
        enhance_path = st.checkbox("Enhance Path", value=False)
        submit = st.button("Snap to Road")

        if submit:
            params = {
                "points": points,
                "enhance_path": enhance_path
            }
            with st.spinner("Snapping to road..."):
                try:
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/snapToRoad",
                        params=params
                    )
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error: {str(e)}")


    # ----------------------------------------------------------------
    # 2) Nearest Roads
    # ----------------------------------------------------------------
    elif action == "Nearest Roads API":
        points = st.text_area(
            "Coordinates (lat,lng|lat,lng)",
            placeholder="Enter points separated by '|'. e.g.: 12.931544865377818,77.61638622280486|12.9352,77.6245",
            value="12.931544865377818,77.61638622280486|12.9352,77.6245"
        )
        radius = st.number_input("Search Radius (meters)", value=500, min_value=1, max_value=20000)
        submit = st.button("Get Nearest Roads")

        if submit:
            params = {
                "points": points,
                "radius": radius
            }
            with st.spinner("Fetching nearest roads..."):
                try:
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/nearestRoads",
                        params=params
                    )
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error: {str(e)}")


    # ----------------------------------------------------------------
    # 3) Speed Limits
    # ----------------------------------------------------------------
    elif action == "Speed Limits API":
        points = st.text_area(
            "Coordinates (lat,lng|lat,lng)",
            placeholder="Enter points separated by '|'. e.g.: 12.931544865377818,77.61638622280486|12.9352,77.6245",
            value="13.0630227,77.5930842|13.063479498221085,77.59321523175956"
        )
        snap_strategy = st.selectbox(
            "Snapping Strategy",
            options=["snaptoroad", "nearestroad"],
            index=0,
            help="Choose the snapping strategy to use."
        )
        submit = st.button("Get Speed Limits")

        if submit:
            params = {
                "points": points,
                "snapStrategy": snap_strategy
            }
            with st.spinner("Fetching speed limits..."):
                try:
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/speedLimits",
                        params=params
                    )
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error: {str(e)}")
