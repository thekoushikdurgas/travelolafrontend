import streamlit as st
from utils.api import call_api
from utils.constants import PLACE_TYPES  # Centralized place types

def forward_geocode(pincode, base_url):
    """Geocode pincode to (lat, lng)."""
    try:
        response = call_api("GET", f"{base_url}/geocode/geocode", params={"address": pincode})
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok" and data.get("geocodingResults"):
                loc = data["geocodingResults"][0]["geometry"]["location"]
                return loc["lat"], loc["lng"]
        st.error("Failed to geocode pincode.")
    except Exception as e:
        st.error(f"Geocoding error: {e}")
    return None

def perform_search(lat, lng, search_type, params, base_url):
    """Perform type-based or text-based search."""
    try:
        endpoint = "/places/nearbysearch" if search_type == "type" else "/places/textsearch"
        response = call_api("GET", f"{base_url}{endpoint}", params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                return data.get("predictions", [])
        st.error(f"{search_type.capitalize()} search failed.")
    except Exception as e:
        st.error(f"Search error: {e}")
    return []

def display_results(results, label=""):
    """Display search results in Streamlit."""
    if results:
        st.success(f"Found {len(results)} place(s) for {label}.")
        for idx, place in enumerate(results):
            place_name = place.get("description", "Unknown Place")
            types = place.get("types", [])
            distance = place.get("distance_meters", "N/A")
            with st.expander(f"- **{place_name}** [{', '.join(types)}] (~{distance} m away)"):
                if st.button("View Details", key=f"details_{idx}"):
                    st.write("Details functionality to be implemented.")
    else:
        st.warning(f"No places found for {label}.")

def main_search_page(base_url):
    """Main Streamlit page for pincode-based place search."""
    st.title("Find Places by Pincode")
    pincode = st.text_input("Enter Pincode:", placeholder="e.g., 560001")
    if st.button("Geocode Pincode"):
        if not pincode.isdigit() or len(pincode) != 6:
            st.warning("Please enter a valid 6-digit pincode.")
        else:
            coords = forward_geocode(pincode, base_url)
            if coords:
                st.session_state["lat"], st.session_state["lng"] = coords
                st.success(f"Coordinates: {coords[0]}, {coords[1]}")

    if "lat" in st.session_state and "lng" in st.session_state:
        lat, lng = st.session_state["lat"], st.session_state["lng"]
        st.subheader("Search Options")
        radius = st.number_input("Radius (meters):", min_value=100, max_value=10000, value=3000)
        
        # Type-based Search
        st.markdown("### Type-based Search")
        selected_types = [t for t in PLACE_TYPES if st.checkbox(t)]
        if st.button("Search by Types"):
            if selected_types:
                params = {"location": f"{lat},{lng}", "radius": radius, "types": ",".join(selected_types)}
                results = perform_search(lat, lng, "type", params, base_url)
                display_results(results, f"Types: {', '.join(selected_types)}")
            else:
                st.warning("No types selected.")

        # Text-based Search
        st.markdown("### Text-based Search")
        query = st.text_input("Enter Query:", placeholder="e.g., pizza")
        if st.button("Search by Text"):
            params = {"location": f"{lat},{lng}", "radius": radius, "input": query}
            results = perform_search(lat, lng, "text", params, base_url)
            display_results(results, f"Query: {query}")
