# utils/constants.py
# Centralized definition of reusable constants for the project

import os

# Base API Configuration
BASE_API_URL = os.getenv("BASE_API_URL", "https://api.olamaps.com/v1")
"""
The base URL for all API requests.
Can be overridden using the environment variable `BASE_API_URL`.
"""

APP_DESCRIPTION = "A FastAPI backend for Ola Maps integration, providing routing, geocoding, places, and more."
APP_TITLE="Ola Maps API Backend"
APP_VERSION="1.0.0"
# Geofence Types
GEOFENCE_TYPES = [
    "Circle",  # Circular geofence
    "Polygon",  # Polygonal geofence
]
"""
Supported geofence types:
- Circle: A circular boundary defined by a center and radius.
- Polygon: A multi-vertex boundary.
"""

# Supported Languages
SUPPORTED_LANGUAGES = [
    "en",  # English
    "es",  # Spanish
    "fr",  # French
    "de",  # German
]
"""
Languages supported by the application.
Defined using ISO 639-1 language codes.
"""

# Place Types (categorized for clarity)
PLACE_TYPES = [
    "accounting", "airport", "atm", "bakery", "bank", "bar", "beauty_salon",
    "book_store", "bus_station", "cafe", "car_dealer", "car_repair", "church",
    "clothing_store", "dentist", "doctor", "drugstore", "electronics_store",
    "embassy", "finance", "food", "furniture_store", "gas_station",
    "general_contractor", "gym", "hair_care", "hardware_store", "health",
    "hindu_temple", "home_goods_store", "hospital", "insurance_agency",
    "jewelry_store", "laundry", "lodging", "mosque", "movie_theater", "park",
    "parking", "pharmacy", "place_of_worship", "point_of_interest",
    "post_office", "primary_school", "real_estate_agency", "restaurant",
    "school", "shoe_store", "shopping_mall", "spa", "storage", "store",
    "subway_station", "supermarket", "tourist_attraction", "train_station",
    "transit_station", "travel_agency", "university",
]
"""
Supported types of places for search and categorization.
Refer to the application's API documentation for usage and constraints.
"""

# Notes:
# - Ensure constants align with API or business requirements.
# - Consider loading long lists like PLACE_TYPES dynamically if they are subject to frequent updates.
