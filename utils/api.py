import requests
import streamlit as st

def call_api(method, url, params=None, body=None):
    try:
        if method == "GET":
            response = requests.get(url, params=params)
        elif method == "POST":
            response = requests.post(url, json=body, params=params)
        elif method == "PUT":
            response = requests.put(url, json=body, params=params)
        elif method == "DELETE":
            response = requests.delete(url, params=params)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"API call failed: {e}")
        return {"error": str(e)}
