import streamlit as st
from utils.logger import logger
from components.routing import routing_component
from components.elevation import elevation_component
from components.geocode import geocode_component
from components.geofence import geofence_component
from components.places import places_component
from components.roads import roads_component
from components.tiles import tiles_component
from components.health_check import health_check_component

# BASE_URL = "http://localhost:8000"
# BASE_URL = "https://travelbackend-4snf.onrender.com/"
BASE_URL = "https://travelbackend-4snf.onrender.com"

# BASE_URL = "http://localhost:8000"

# App Title
st.title("OLA Maps API Interface")
st.sidebar.title("API Navigation")

# Define API sections
api_sections = [
    "Elevation API",
    "Geocode API",
    "Geofence API",
    "Places API",
    "Roads API",
    "Routing API",
    "Tiles API",
    "Health Check"
]
api_choice = st.sidebar.selectbox("Choose an API", api_sections)

# Load the selected component
if api_choice == "Elevation API":
    elevation_component(BASE_URL+"/elevation")
elif api_choice == "Routing API":
    routing_component(BASE_URL+"/routing")
elif api_choice == "Geocode API":
    geocode_component(BASE_URL)
elif api_choice == "Geofence API":
    geofence_component(BASE_URL+"/geofence")
elif api_choice == "Places API":
    places_component(BASE_URL)
elif api_choice == "Roads API":
    roads_component(BASE_URL+"/roads")
elif api_choice == "Tiles API":
    tiles_component(BASE_URL)
elif api_choice == "Health Check":
    health_check_component(BASE_URL)
