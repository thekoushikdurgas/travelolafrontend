import streamlit as st

def ola_maps_api_tab(BASE_URL):
    """
    Central interface for Ola Maps API.
    Allows navigation and interaction with various API components dynamically.
    
    Parameters:
        BASE_URL (str): Base URL for API endpoints.
    """
    st.title("OLA Maps API Interface")
    st.subheader("API Navigation")

    # Define available API components and their module paths
    api_sections = {
        "Elevation API": "components.elevation.elevation_component",
        "Geocode API": "components.geocode.geocode_component",
        "Geofence API": "components.geofence.geofence_component",
        "Places API": "components.places.places_component",
        "Roads API": "components.roads.roads_component",
        "Routing API": "components.routing.routing_component",
        "Tiles API": "components.tiles.tiles_component",
        "Health Check": "components.health_check.health_check_component",
    }

    # Dropdown for API selection
    api_choice = st.selectbox("Choose an API", list(api_sections.keys()))
    
    # Dynamically load and execute the selected component
    try:
        component_module_path = api_sections[api_choice]
        module_name, function_name = component_module_path.rsplit(".", 1)
        
        # Dynamically import the module and function
        component_module = __import__(module_name, fromlist=[function_name])
        component_function = getattr(component_module, function_name)
        
        # Execute the component function
        st.write(f"### {api_choice}")
        component_function(BASE_URL)
    
    except ImportError:
        st.error(f"Failed to load module: {module_name}")
    except AttributeError:
        st.error(f"Module '{module_name}' does not contain function '{function_name}'.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
