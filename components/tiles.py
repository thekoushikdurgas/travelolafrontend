import json
import base64
import streamlit as st
from utils.api import call_api

def tiles_component(base_url: str):
    st.header("Tiles API")
    
    endpoints = [
        "Get All Styles",
        "Get Style Details",
        "Get Static Map by Center Point",
        "Get Static Map by Bounding Box",
        "Get 3D Tiles"
    ]
    action = st.radio("Choose Endpoint", endpoints)

    # ----------------------------------------------------------------
    # 1) Get All Styles
    # ----------------------------------------------------------------
    if action == "Get All Styles":
        st.subheader("Get All Styles")
        submit = st.button("Fetch All Styles")
        
        if submit:
            with st.spinner("Fetching all styles..."):
                try:
                    response = call_api("GET", f"{base_url}/tiles/styles.json")
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Styles fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching styles: {str(e)}")

    # ----------------------------------------------------------------
    # 2) Get Style Details
    # ----------------------------------------------------------------
    elif action == "Get Style Details":
        st.subheader("Get Style Details")
        style_name = st.text_input("Style Name", value="default-light-standard")
        submit = st.button("Fetch Style Details")
        
        if submit:
            with st.spinner(f"Fetching details for style '{style_name}'..."):
                try:
                    endpoint = f"/tiles/styles/{style_name}/style.json"
                    response = call_api("GET", f"{base_url}{endpoint}")
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success(f"Style '{style_name}' details fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching style details: {str(e)}")

    # ----------------------------------------------------------------
    # 3) Get Static Map by Center Point
    # ----------------------------------------------------------------
    elif action == "Get Static Map by Center Point":
        st.subheader("Get Static Map by Center Point")
        
        style_name = st.text_input("Style Name", value="default-light-standard")
        lon = st.number_input("Longitude", value=77.61, format="%.6f")
        lat = st.number_input("Latitude", value=12.93, format="%.6f")
        zoom = st.slider("Zoom Level", min_value=0, max_value=23, value=15)
        width = st.number_input("Width (pixels)", min_value=1, max_value=2048, value=800)
        height = st.number_input("Height (pixels)", min_value=1, max_value=2048, value=600)
        image_format = st.selectbox("Image Format", ["png", "jpg"], index=0)
        marker = st.text_area(
            "Marker (optional)",
            placeholder="Format: lng,lat|color|options",
            help="Example: 77.61,12.93|red|scale:0.9"
        )
        path = st.text_area(
            "Path (optional)",
            placeholder="Format: lng,lat|lng,lat|options",
            help="Example: 77.61,12.93|77.6119,12.9376|width:6|stroke:#00ff44"
        )
        submit = st.button("Fetch Static Map")
        
        if submit:
            with st.spinner("Fetching static map by center point..."):
                try:
                    params = {
                        "marker": marker if marker.strip() else None,
                        "path": path if path.strip() else None
                    }
                    endpoint = f"/tiles/v1/styles/{style_name}/static/{lon},{lat},{zoom}/{width}x{height}.{image_format}"
                    response = call_api("GET", f"{base_url}{endpoint}", params=params)
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        if "image_data" in resp_json:
                            # Decode base64 and display image
                            image_bytes = base64.b64decode(resp_json["image_data"])
                            st.image(image_bytes, caption="Static Map by Center Point")
                        else:
                            st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching static map by center point: {str(e)}")

    # ----------------------------------------------------------------
    # 4) Get Static Map by Bounding Box
    # ----------------------------------------------------------------
    elif action == "Get Static Map by Bounding Box":
        st.subheader("Get Static Map by Bounding Box")
        
        style_name = st.text_input("Style Name", value="default-light-standard")
        minx = st.number_input("Min Longitude", value=77.611182, format="%.6f")
        miny = st.number_input("Min Latitude", value=12.932198, format="%.6f")
        maxx = st.number_input("Max Longitude", value=77.615135, format="%.6f")
        maxy = st.number_input("Max Latitude", value=12.935739, format="%.6f")
        width = st.number_input("Width (pixels)", min_value=1, max_value=2048, value=800)
        height = st.number_input("Height (pixels)", min_value=1, max_value=2048, value=600)
        image_format = st.selectbox("Image Format", ["png", "jpg"], index=0)
        marker = st.text_area(
            "Marker (optional)",
            placeholder="Format: lng,lat|color|options",
            help="Example: 77.61,12.93|red|scale:0.9"
        )
        path = st.text_area(
            "Path (optional)",
            placeholder="Format: lng,lat|lng,lat|options",
            help="Example: 77.61,12.93|77.6119,12.9376|width:6|stroke:#00ff44"
        )
        submit = st.button("Fetch Static Map by Bounding Box")
        
        if submit:
            with st.spinner("Fetching static map by bounding box..."):
                try:
                    params = {
                        "marker": marker if marker.strip() else None,
                        "path": path if path.strip() else None
                    }
                    endpoint = f"/tiles/v1/styles/{style_name}/static/{minx},{miny},{maxx},{maxy}/{width}x{height}.{image_format}"
                    response = call_api("GET", f"{base_url}{endpoint}", params=params)
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        if "image_data" in resp_json:
                            # Decode base64 and display image
                            image_bytes = base64.b64decode(resp_json["image_data"])
                            st.image(image_bytes, caption="Static Map by Bounding Box")
                        else:
                            st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching static map by bounding box: {str(e)}")

    # ----------------------------------------------------------------
    # 5) Get 3D Tiles
    # ----------------------------------------------------------------
    elif action == "Get 3D Tiles":
        st.subheader("Get 3D Tiles")
        submit = st.button("Fetch 3D Tiles")
        
        if submit:
            with st.spinner("Fetching 3D tiles..."):
                try:
                    response = call_api("GET", f"{base_url}/tiles/3dtiles/tileset.json")
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("3D Tiles fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching 3D tiles: {str(e)}")
