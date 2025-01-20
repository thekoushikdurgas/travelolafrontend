import json
import streamlit as st
from utils.api import call_api

def geofence_component(base_url: str):
    st.title("Geofence API with Session State")

    # ----------------------------------------------------------------
    # 1) Initialize session state variables if they don't exist
    # ----------------------------------------------------------------
    if "geofence_id" not in st.session_state:
        st.session_state["geofence_id"] = ""
    if "project_id" not in st.session_state:
        st.session_state["project_id"] = ""

    # ----------------------------------------------------------------
    # 2) Radio buttons for selecting which action to perform
    # ----------------------------------------------------------------
    actions = [
        "Create Geofence",
        "Update Geofence",
        "Get Geofence",
        "Delete Geofence",
        "List Geofences",
        "Check Status"
    ]
    action = st.radio("Choose Action", actions)

    # ----------------------------------------------------------------
    # 3) Create Geofence
    # ----------------------------------------------------------------
    if action == "Create Geofence":
        st.subheader("Create a New Geofence")

        # Provide default or typed values
        name = st.text_input("Geofence Name", value="Sample Geofence")
        geofence_type = st.radio("Geofence Type", ["circle", "polygon"])
        coordinates_text = st.text_area(
            "Coordinates (lat,lng on each line)",
            value="12.9314,77.6152\n12.9305,77.6145" if geofence_type == "polygon" else "12.9314,77.6152",
            help="Enter one [lat,lng] per line for polygon or one line for circle."
        )
        radius = st.number_input("Radius (meters, only for circle)", value=100.0, step=10.0) if geofence_type == "circle" else None
        status = st.selectbox("Status", ["active", "inactive"])
        
        # Default project to whatever is stored in session; user can override
        project_id = st.text_input("Project ID", value=st.session_state["project_id"] or "project123")

        if st.button("Create Geofence"):
            # Build payload
            try:
                coords_list = []
                for line in coordinates_text.splitlines():
                    if line.strip():
                        lat_str, lng_str = line.split(",")
                        coords_list.append([float(lat_str.strip()), float(lng_str.strip())])

                payload = {
                    "name": name,
                    "type": geofence_type,
                    "coordinates": coords_list,
                    "radius": radius,
                    "status": status,
                    "projectId": project_id
                }

                # Send request
                with st.spinner("Creating geofence..."):
                    response = call_api(
                        method="POST",
                        url=f"{base_url}/geofence",
                        body=payload
                    )
                resp_data = response.json()

                if "error" in resp_data:
                    st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                else:
                    st.success("Geofence created successfully!")
                    st.json(resp_data)

                    # Store returned geofence ID and projectId in session if available
                    if "geofenceId" in resp_data:
                        st.session_state["geofence_id"] = resp_data["geofenceId"]
                    if "projectId" in resp_data:
                        st.session_state["project_id"] = resp_data["projectId"]

            except ValueError:
                st.error("Invalid coordinates format. Ensure each line has 'lat,lng'.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 4) Update Geofence
    # ----------------------------------------------------------------
    elif action == "Update Geofence":
        st.subheader("Update an Existing Geofence")

        # Default geofence ID from session
        geofence_id = st.text_input("Geofence ID to Update", value=st.session_state["geofence_id"])
        name = st.text_input("New Geofence Name", value="Updated Geofence")
        geofence_type = st.radio("Geofence Type", ["circle", "polygon"])
        coordinates_text = st.text_area(
            "Coordinates (lat,lng on each line)",
            value="12.9314,77.6152\n12.9305,77.6145" if geofence_type == "polygon" else "12.9314,77.6152",
            help="Enter one [lat,lng] per line for polygon or one line for circle."
        )
        radius = st.number_input("Radius (meters, only for circle)", value=150.0, step=10.0) if geofence_type == "circle" else None
        status = st.selectbox("Status", ["active", "inactive"])
        # We can default project_id from session for reference
        project_id = st.text_input("Project ID", value=st.session_state["project_id"] or "project123")

        if st.button("Update Geofence"):
            # Validate geofence ID
            if not geofence_id.strip():
                st.warning("Please enter a valid Geofence ID.")
            else:
                try:
                    coords_list = []
                    for line in coordinates_text.splitlines():
                        if line.strip():
                            lat_str, lng_str = line.split(",")
                            coords_list.append([float(lat_str.strip()), float(lng_str.strip())])

                    payload = {
                        "name": name,
                        "type": geofence_type,
                        "coordinates": coords_list,
                        "radius": radius,
                        "status": status,
                        "projectId": project_id
                    }

                    # Send request
                    with st.spinner("Updating geofence..."):
                        response = call_api(
                            method="PUT",
                            url=f"{base_url}/geofence/{geofence_id}",
                            body=payload
                        )
                    resp_data = response.json()

                    if "error" in resp_data:
                        st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                    else:
                        st.success("Geofence updated successfully!")
                        st.json(resp_data)

                        # Optionally update session state with new ID, if returned
                        if "geofenceId" in resp_data:
                            st.session_state["geofence_id"] = resp_data["geofenceId"]
                        if "projectId" in resp_data:
                            st.session_state["project_id"] = resp_data["projectId"]

                except ValueError:
                    st.error("Invalid coordinates format. Ensure each line has 'lat,lng'.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 5) Get Geofence
    # ----------------------------------------------------------------
    elif action == "Get Geofence":
        st.subheader("Retrieve Geofence Details")

        # Default to session state geofence_id
        geofence_id = st.text_input("Geofence ID to Fetch", value=st.session_state["geofence_id"])
        
        if st.button("Fetch Details"):
            if not geofence_id.strip():
                st.warning("Please enter a valid Geofence ID.")
            else:
                try:
                    with st.spinner("Fetching geofence details..."):
                        response = call_api(
                            method="GET",
                            url=f"{base_url}/geofence/{geofence_id}"
                        )
                    resp_data = response.json()

                    if "error" in resp_data:
                        st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                    else:
                        st.success("Geofence details retrieved!")
                        st.json(resp_data)

                        # Optionally update session ID if returned in the data
                        if "geofenceId" in resp_data:
                            st.session_state["geofence_id"] = resp_data["geofenceId"]

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 6) Delete Geofence
    # ----------------------------------------------------------------
    elif action == "Delete Geofence":
        st.subheader("Delete a Geofence")

        # Default geofenceId from session
        geofence_id = st.text_input("Geofence ID to Delete", value=st.session_state["geofence_id"])
        if st.button("Delete"):
            if not geofence_id.strip():
                st.warning("Please enter a valid Geofence ID.")
            else:
                try:
                    with st.spinner("Deleting geofence..."):
                        response = call_api(
                            method="DELETE",
                            url=f"{base_url}/geofence/{geofence_id}"
                        )
                    resp_data = response.json()

                    if "error" in resp_data:
                        st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                    else:
                        st.success("Geofence deleted!")
                        st.json(resp_data)

                        # Clear the geofence_id from session if delete was successful
                        if resp_data.get("status") == "deleted":
                            st.session_state["geofence_id"] = ""

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 7) List Geofences
    # ----------------------------------------------------------------
    elif action == "List Geofences":
        st.subheader("List Geofences")

        # By default, show the project_id from session
        project_id = st.text_input("Project ID", value=st.session_state["project_id"] or "project123")
        page = st.number_input("Page", min_value=1, value=1)
        size = st.number_input("Size", min_value=1, max_value=100, value=10)
        if st.button("List"):
            try:
                params = {"page": page, "size": size}
                if project_id:
                    params["projectId"] = project_id

                with st.spinner("Fetching geofence list..."):
                    response = call_api(
                        method="GET",
                        url=f"{base_url}/geofences",
                        params=params
                    )
                resp_data = response.json()

                if "error" in resp_data:
                    st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                else:
                    st.success("Geofences retrieved!")
                    st.json(resp_data)

                    # Optionally store or update project_id in session
                    st.session_state["project_id"] = project_id

            except Exception as e:
                st.error(f"Error: {str(e)}")

    # ----------------------------------------------------------------
    # 8) Check Geofence Status
    # ----------------------------------------------------------------
    elif action == "Check Status":
        st.subheader("Check Geofence Status")
        # Default to session geofenceId
        geofence_id = st.text_input("Geofence ID", value=st.session_state["geofence_id"])
        coords = st.text_input("Coordinates (lat,lng)", value="12.931544865377818,77.61638622280486")

        if st.button("Check Status"):
            if not geofence_id.strip() or not coords.strip():
                st.warning("Please provide both Geofence ID and coordinates.")
            else:
                try:
                    # Validate coordinates format
                    lat_str, lng_str = coords.split(",")
                    lat = float(lat_str)
                    lng = float(lng_str)
                    if not (-90 <= lat <= 90 and -180 <= lng <= 180):
                        st.warning("Latitude must be between -90 and 90 and Longitude between -180 and 180.")
                    else:
                        params = {
                            "geofenceId": geofence_id.strip(),
                            "coordinates": coords.strip()
                        }
                        with st.spinner("Checking geofence status..."):
                            response = call_api(
                                method="GET",
                                url=f"{base_url}/geofence/status",
                                params=params
                            )
                        resp_data = response.json()

                        if "error" in resp_data:
                            st.error(f"Error {resp_data['code']}: {resp_data['details']}")
                        else:
                            st.success("Geofence status retrieved!")
                            st.json(resp_data)

                except ValueError:
                    st.error("Invalid coordinates format. Use 'lat,lng'.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
