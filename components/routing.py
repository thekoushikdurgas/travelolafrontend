import streamlit as st
from utils.api import call_api

def routing_component(base_url):
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

    # 1) Basic Directions
    if choice == "Get Directions (Basic)":
        st.subheader("Get Basic Directions")
        origin = st.text_input("Origin (lat,lng)", value="12.993103152916301,77.54332622119354")
        destination = st.text_input("Destination (lat,lng)", value="12.972006793201695,77.5800850011884")
        waypoints = st.text_area("Waypoints (lat,lng|lat,lng)", placeholder="Optional waypoints", value="12.938399,77.632873|12.938041,77.628285")
        submit = st.button("Get Directions")

        if submit:
            with st.spinner("Fetching directions..."):
                try:
                    params = {
                        "origin": origin,
                        "destination": destination,
                        "waypoints": waypoints
                    }
                    response = call_api("POST", f"{base_url}/directions/basic", params=params)
                    st.success("Directions fetched successfully!")
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error fetching directions: {str(e)}")

    # 2) Detailed Directions
    elif choice == "Get Directions with Details":
        st.subheader("Get Detailed Directions")
        origin = st.text_input("Origin (lat,lng)", value="12.931544865377818,77.61638622280486")
        destination = st.text_input("Destination (lat,lng)", value="12.9352,77.6245")
        waypoints = st.text_area("Waypoints (lat,lng|lat,lng)", placeholder="Optional waypoints")
        submit = st.button("Get Detailed Directions")

        if submit:
            with st.spinner("Fetching detailed directions..."):
                try:
                    params = {
                        "origin": origin,
                        "destination": destination,
                        "waypoints": waypoints
                    }
                    response = call_api("POST", f"{base_url}/directions", params=params)
                    st.success("Detailed directions fetched successfully!")
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error fetching detailed directions: {str(e)}")

    # 3) Distance Matrix
    elif choice == "Distance Matrix":
        st.subheader("Get Distance Matrix")
        origins = st.text_input("Origins (lat,lng|lat,lng)", 
                                value="12.931544865377818,77.61638622280486|12.9352,77.6245")
        destinations = st.text_input("Destinations (lat,lng|lat,lng)", 
                                     value="12.9352,77.6245|12.9391,77.6341")
        submit = st.button("Get Distance Matrix")

        if submit:
            with st.spinner("Fetching distance matrix..."):
                try:
                    params = {"origins": origins, "destinations": destinations}
                    response = call_api("GET", f"{base_url}/distanceMatrix", params=params)
                    st.success("Distance matrix fetched successfully!")
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error fetching distance matrix: {str(e)}")

    # 4) Basic Distance Matrix
    elif choice == "Basic Distance Matrix":
        st.subheader("Get Basic Distance Matrix")
        origins = st.text_input("Origins (lat,lng|lat,lng)", 
                                value="12.931544865377818,77.61638622280486|12.9352,77.6245")
        destinations = st.text_input("Destinations (lat,lng|lat,lng)", 
                                     value="12.9352,77.6245|12.9391,77.6341")
        submit = st.button("Get Basic Distance Matrix")

        if submit:
            with st.spinner("Fetching basic distance matrix..."):
                try:
                    params = {"origins": origins, "destinations": destinations}
                    response = call_api("GET", f"{base_url}/distanceMatrix/basic", params=params)
                    st.success("Basic distance matrix fetched successfully!")
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error fetching basic distance matrix: {str(e)}")

    # 5) Route Optimization
    elif choice == "Route Optimization":
        st.subheader("Optimize Route")
        locations = st.text_area("Waypoints (lat,lng|lat,lng)",
                                 placeholder="Enter waypoints separated by '|'")
        submit = st.button("Optimize Route")

        if submit:
            with st.spinner("Optimizing route..."):
                try:
                    params = {"locations": locations}
                    response = call_api("POST", f"{base_url}/routeOptimizer", params=params)
                    st.success("Route optimization completed!")
                    st.json(response.json())
                except Exception as e:
                    st.error(f"Error optimizing route: {str(e)}")

    # 6) Fleet Planner
    elif choice == "Fleet Planner":
        st.subheader("Fleet Planner")
        strategy = st.selectbox("Strategy", ["optimal", "fair"], index=0)
        input_file = st.file_uploader("Upload Fleet Planner Configuration (JSON)", type=["json"])
        submit = st.button("Execute Fleet Planner")

        if submit:
            if not input_file:
                st.warning("Please upload a JSON configuration file.")
            else:
                with st.spinner("Executing fleet planner..."):
                    try:
                        files = {"input": input_file}
                        params = {"strategy": strategy}
                        # Must pass 'files' for multipart/form-data
                        response = call_api("POST", f"{base_url}/fleetPlanner", params=params, files=files)
                        st.success("Fleet planning completed successfully!")
                        st.json(response.json())
                    except Exception as e:
                        st.error(f"Error executing fleet planner: {str(e)}")
