import os
from fastapi import HTTPException
import requests
from utils.olatoken import get_access_token
from utils.logger import logger


BASE_URL = "https://api.olamaps.io"

# API_KEY = os.getenv("OLA_MAPS_API_KEY", "SxJhsrEpqjBqIdicTM7OsQcaFSRC0KRoq43BiRQf")
API_KEY = "SxJhsrEpqjBqIdicTM7OsQcaFSRC0KRoq43BiRQf"
if not API_KEY:
    raise RuntimeError("OLA_MAPS_API_KEY not set in environment variables")
try:
    access_token = get_access_token()
except Exception as e:
    print("Failed to fetch access token:", e)
    exit()


def make_request(endpoint: str, method: str, params=None):
    try:
        url = f"{BASE_URL}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
            "origin": "https://maps.olakrutrim.com",
        }
        params["api_key"] = API_KEY
        # logger.info(f"url: {url} params:{params}")
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")

        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        ) from e
