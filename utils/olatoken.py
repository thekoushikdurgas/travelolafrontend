import os
import requests
from requests.auth import HTTPBasicAuth
from utils.logger import logger

def get_access_token():
    # Token URL
    token_url = "https://account.olamaps.io/realms/olamaps/protocol/openid-connect/token"
    
    # Client Credentials
    client_id = 'd4cd55fa-a8d7-4287-b65e-507dc45727b1'       
    client_secret = 'bQzMgcE1XCdd1kh8LWQwBFdzRg6hs4UD'  
    
    # client_id = os.getenv('CLIENT_ID')
    # client_secret = os.getenv('CLIENT_SECRET')
    # logger.info(f"client_id: {client_id} client_secret:{client_secret}")
    # Data for token request
    data = {
        'grant_type': 'client_credentials',
        'scope': 'openid olamaps'
    }
    
    # Make the POST request to obtain the token
    response = requests.post(token_url, data=data, auth=HTTPBasicAuth(client_id, client_secret))
    
    if response.status_code == 200:
        token_data = response.json()
        return token_data['access_token']
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
