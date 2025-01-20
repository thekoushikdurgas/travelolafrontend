import json
import streamlit as st
from utils.api import call_api

def routing_component(base_url: str):
    st.header("Routing API")
    
    endpoints = [
        "Get Directions (Basic)",
        "Get Directions with Details",
        "Distance Matrix",
        "Basic Distance Matrix",
        "Route Optimization",
        "Fleet Planner"
    ]
    choice = st.radio("Select Endpoint", endpoints)
    
    # ----------------------------------------------------------------
    # 1) Get Directions (Basic)
    # ----------------------------------------------------------------
    if choice == "Get Directions (Basic)":
        st.subheader("Get Basic Directions")
        
        origin = st.text_input("Origin (lat,lng)", value="12.993103152916301,77.54332622119354")
        destination = st.text_input("Destination (lat,lng)", value="12.972006793201695,77.5800850011884")
        waypoints = st.text_area(
            "Waypoints (lat,lng|lat,lng)",
            placeholder="Optional waypoints, separated by '|'",
            value="12.938399,77.632873|12.938041,77.628285"
        )
        submit = st.button("Get Directions")
        
        if submit:
            with st.spinner("Fetching basic directions..."):
                try:
                    payload = {
                        "origin": origin,
                        "destination": destination,
                        "waypoints": waypoints if waypoints.strip() else None
                    }
                    response = call_api(
                        method="POST",
                        url=f"{base_url}/directions/basic",
                        body=payload
                    )
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Directions fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching directions: {str(e)}")

    # ----------------------------------------------------------------
    # 2) Get Directions with Details
    # ----------------------------------------------------------------
    elif choice == "Get Directions with Details":
        st.subheader("Get Detailed Directions")
        
        origin = st.text_input("Origin (lat,lng)", value="12.931544865377818,77.61638622280486")
        destination = st.text_input("Destination (lat,lng)", value="12.9352,77.6245")
        waypoints = st.text_area(
            "Waypoints (lat,lng|lat,lng)",
            placeholder="Optional waypoints, separated by '|'"
        )
        submit = st.button("Get Detailed Directions")
        
        if submit:
            with st.spinner("Fetching detailed directions..."):
                try:
                    payload = {
                        "origin": origin,
                        "destination": destination,
                        "waypoints": waypoints if waypoints.strip() else None
                    }
                    response = call_api(
                        method="POST",
                        url=f"{base_url}/directions",
                        body=payload
                    )
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Detailed directions fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching detailed directions: {str(e)}")

    # ----------------------------------------------------------------
    # 3) Distance Matrix
    # ----------------------------------------------------------------
    elif choice == "Distance Matrix":
        st.subheader("Get Distance Matrix")
        
        origins = st.text_input(
            "Origins (lat,lng|lat,lng)",
            value="12.931544865377818,77.61638622280486|12.9352,77.6245"
        )
        destinations = st.text_input(
            "Destinations (lat,lng|lat,lng)",
            value="12.9352,77.6245|12.9391,77.6341"
        )
        submit = st.button("Get Distance Matrix")
        
        if submit:
            with st.spinner("Fetching distance matrix..."):
                try:
                    params = {
                        "origins": origins,
                        "destinations": destinations
                    }
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/distanceMatrix",
                        params=params
                    )
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Distance matrix fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching distance matrix: {str(e)}")

    # ----------------------------------------------------------------
    # 4) Basic Distance Matrix
    # ----------------------------------------------------------------
    elif choice == "Basic Distance Matrix":
        st.subheader("Get Basic Distance Matrix")
        
        origins = st.text_input(
            "Origins (lat,lng|lat,lng)",
            value="12.931544865377818,77.61638622280486|12.9352,77.6245"
        )
        destinations = st.text_input(
            "Destinations (lat,lng|lat,lng)",
            value="12.9352,77.6245|12.9391,77.6341"
        )
        submit = st.button("Get Basic Distance Matrix")
        
        if submit:
            with st.spinner("Fetching basic distance matrix..."):
                try:
                    params = {
                        "origins": origins,
                        "destinations": destinations
                    }
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/distanceMatrix/basic",
                        params=params
                    )
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Basic distance matrix fetched successfully!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error fetching basic distance matrix: {str(e)}")

    # ----------------------------------------------------------------
    # 5) Route Optimization
    # ----------------------------------------------------------------
    elif choice == "Route Optimization":
        st.subheader("Optimize Route")
        
        locations = st.text_area(
            "Waypoints (lat,lng|lat,lng)",
            placeholder="Enter waypoints separated by '|'",
            value="12.931544865377818,77.61638622280486|12.9352,77.6245|12.9391,77.6341"
        )
        submit = st.button("Optimize Route")
        
        if submit:
            with st.spinner("Optimizing route..."):
                try:
                    payload = {
                        "locations": locations
                    }
                    response = call_api(
                        method="POST",
                        url=f"{base_url}/routeOptimizer",
                        body=payload
                    )
                    resp_json = response.json()
                    
                    if "error" in resp_json:
                        st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                    else:
                        st.success("Route optimization completed!")
                        st.json(resp_json)
                except Exception as e:
                    st.error(f"Error optimizing route: {str(e)}")

    # ----------------------------------------------------------------
    # 6) Fleet Planner
    # ----------------------------------------------------------------
    elif choice == "Fleet Planner":
        st.subheader("Fleet Planner")
        
        strategy = st.selectbox(
            "Strategy",
            options=["optimal", "fair"],
            index=0,
            help="Choose the strategy for route optimization."
        )
        input_file = st.file_uploader(
            "Upload Fleet Planner Configuration (JSON)",
            type=["json"],
            help="Upload a JSON file containing fleet planner configuration."
        )
        submit = st.button("Execute Fleet Planner")
        
        if submit:
            if not input_file:
                st.warning("Please upload a JSON configuration file.")
            else:
                with st.spinner("Executing fleet planner..."):
                    try:
                        # Read and parse the uploaded JSON file
                        file_content = input_file.read()
                        json_content = json.loads(file_content)
                        
                        # Prepare payload
                        payload = {
                            "strategy": strategy
                        }
                        
                        # Send POST request with multipart/form-data
                        files = {
                            "input_file": (input_file.name, file_content, "application/json")
                        }
                        response = call_api(
                            method="POST",
                            url=f"{base_url}/fleetPlanner",
                            params=payload,
                            files=files
                        )
                        resp_json = response.json()
                        
                        if "error" in resp_json:
                            st.error(f"Error {resp_json['code']}: {resp_json['details']}")
                        else:
                            st.success("Fleet planning completed successfully!")
                            st.json(resp_json)
                    except json.JSONDecodeError:
                        st.error("Uploaded file is not a valid JSON.")
                    except Exception as e:
                        st.error(f"Error executing fleet planner: {str(e)}")
