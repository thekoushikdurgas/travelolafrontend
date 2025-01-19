import streamlit as st
from utils.api import call_api

def fetch_advanced_place_details(place_id, base_url):
    """
    Fetch advanced details for a given place using the Ola Maps API.
    
    Parameters:
        place_id (str): The unique identifier of the place.
        base_url (str): The base URL for the API.
    
    Returns:
        dict: Advanced place details if available, otherwise None.
    """
    try:
        response = call_api("GET", f"{base_url}/places/details/advanced", params={"place_id": place_id})
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok" and data.get("result"):
                return data["result"]
        st.error(f"Failed to fetch details. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error fetching place details: {e}")
    return None

def place_details_page(place_id, base_url):
    """
    Streamlit page to display advanced details of a place.
    
    Parameters:
        place_id (str): The unique identifier of the place.
        base_url (str): The base URL for the API.
    """
    st.title("Place Details")
    
    if not place_id:
        st.error("No place_id provided. Please provide a valid place ID.")
        return

    st.info(f"Fetching details for place_id={place_id}...")
    details = fetch_advanced_place_details(place_id, base_url)
    
    if not details:
        st.warning("No details found for the provided place ID.")
        return
    
    # Display the fetched details
    st.subheader("Basic Information")
    st.write(f"**Name:** {details.get('name', 'N/A')}")
    st.write(f"**Address:** {details.get('formatted_address', 'N/A')}")
    
    st.subheader("Coordinates")
    location = details.get("geometry", {}).get("location", {})
    st.write(f"**Latitude:** {location.get('lat', 'N/A')}")
    st.write(f"**Longitude:** {location.get('lng', 'N/A')}")
    
    st.subheader("Other Details")
    for key, value in details.items():
        if key not in ["name", "formatted_address", "geometry"]:
            st.write(f"**{key.capitalize()}:** {value}")

    st.success("Details loaded successfully!")




# def place_details_page(base_url, place_id):
#     st.title("Place Details")

#     if not place_id:
#         st.error("No place_id provided.")
#         return

#     st.info(f"Loading details for place_id={place_id} ...")
#     details = fetch_advanced_place_details(place_id, base_url)
#     if not details:
#         st.warning("No advanced details found.")
#         return

#     # Display the entire details structure, or break it down:
#     st.subheader("Basic Info")
#     st.write(f"**Name**: {details.get('name', 'NA')}")
#     st.write(f"**Place ID**: {details.get('place_id', 'NA')}")
#     st.write(f"**Address**: {details.get('formatted_address', 'NA')}")
#     st.write(f"**Phone**: {details.get('formatted_phone_number', 'NA')}")
#     st.write(f"**Website**: {details.get('website', 'NA')}")
#     st.write(f"**Types**: {', '.join(details.get('types', []))}")

#     # Coordinates
#     if details.get("geometry"):
#         st.write(
#             f"**Coordinates**: lat={details['geometry']['location']['lat']}, "
#             f"lng={details['geometry']['location']['lng']}"
#         )

#     # Opening hours
#     oh = details.get("opening_hours", {})
#     if oh:
#         st.subheader("Opening Hours")
#         st.write(f"Open Now?  {oh.get('open_now', False)}")
#         for i, day_info in enumerate(oh.get("weekday_text", [])):
#             st.write(f"- {day_info}")

#     # Ratings & Reviews
#     st.subheader("Reviews & Ratings")
#     st.write(f"**Rating**: {details.get('rating', 0)} (out of 5)")
#     st.write(f"**User Ratings Total**: {details.get('user_ratings_total', 0)}")

#     revs = details.get("reviews", [])
#     if revs:
#         for r in revs:
#             st.write("---")
#             st.write(
#                 f"**Author**: {r.get('author_name', 'NA')} - rating {r.get('rating', 0)}"
#             )
#             st.write(r.get("text", "No review text"))

#     # Photos
#     photos = details.get("photos", [])
#     if photos:
#         st.subheader("Photos")
#         for p in photos:
#             st.write(f"- photo_reference: {p}")

#     # Show entire JSON if you want:
#     st.subheader("Raw JSON")
#     st.json(details)
