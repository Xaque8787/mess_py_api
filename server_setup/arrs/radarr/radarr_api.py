import os
from dotenv import load_dotenv
import requests


def get_radarr_headers():
    """
    Load Radarr API details from a .env file and return the necessary headers for API requests.

    Returns:
        dict: A dictionary containing headers and the Radarr API URL.
    """
    # Load environment variables from .env
    load_dotenv('/app/compose/installed/radarr_app/.env')

    # Fetch Radarr details from environment variables
    radarr_ip = os.getenv("RADARR_IP")
    radarr_port = os.getenv("RADARR_PORT")
    radarr_apikey = os.getenv("RADARR_APIKEY")

    if not all([radarr_ip, radarr_port, radarr_apikey]):
        raise ValueError("One or more required environment variables (radarr_ip, radarr_port, radarr_apikey) are missing.")

    # Construct the Radarr API base URL
    base_url = f"http://{radarr_ip}:{radarr_port}/api/v3"

    # Return headers and base URL
    return {
        "base_url": base_url,
        "headers": {
            "X-Api-Key": radarr_apikey,
            "Content-Type": "application/json"
        }
    }


def get_download_clients():
    config = get_radarr_headers()
    response = requests.get(f"{config['base_url']}/downloadclient", headers=config['headers'])
    response.raise_for_status()
    return response.json()


def post_root_folder(root_path):
    radarr_config = get_radarr_headers()
    url = f"{radarr_config['base_url']}/rootfolder"
    headers = radarr_config['headers']
    payload = {
        "id": 0,
        "path": root_path,
        "accessible": True,
        "freeSpace": 0,
        "unmappedFolders": []
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 201:
        print("Root folder configuration successfully added.")
    else:
        print(f"Failed to add root folder: {response.status_code} - {response.text}")

def post_download_client(payload):
    """
    Posts a hardcoded download client configuration to the Radarr API.
    """
    # Get Radarr headers and base URL
    radarr_config = get_radarr_headers()
    url = f"{radarr_config['base_url']}/downloadclient?forceSave=true"
    headers = radarr_config['headers']
    # Hardcoded JSON payload

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 201:
        print("Download client configuration successfully added.")
    else:
        print(f"Failed to add download client: {response.status_code} - {response.text}")


if __name__ == "__main__":
    #download_clients = get_download_clients()
    #print(download_clients)
    post_root_folder()

