import os
from dotenv import load_dotenv
import requests


def get_sonarr_headers():
    """
    Load Radarr API details from a .env file and return the necessary headers for API requests.

    Returns:
        dict: A dictionary containing headers and the Radarr API URL.
    """
    # Load environment variables from .env
    load_dotenv('/app/compose/installed/sonarr_app/.env')

    # Fetch Radarr details from environment variables
    sonarr_ip = os.getenv("SONARR_IP")
    sonarr_port = os.getenv("SONARR_PORT")
    sonarr_apikey = os.getenv("SONARR_APIKEY")

    if not all([sonarr_ip, sonarr_port, sonarr_apikey]):
        raise ValueError("One or more required environment variables (sonarr_ip, sonarr_port, sonarr_apikey) are missing.")

    # Construct the Radarr API base URL
    base_url = f"http://{sonarr_ip}:{sonarr_port}/api/v3"

    # Return headers and base URL
    return {
        "base_url": base_url,
        "headers": {
            "X-Api-Key": sonarr_apikey,
            "Content-Type": "application/json"
        }
    }


def get_download_clients():
    config = get_sonarr_headers()
    response = requests.get(f"{config['base_url']}/downloadclient", headers=config['headers'])
    response.raise_for_status()
    return response.json()


def post_root_folder(root_path):
    sonarr_config = get_sonarr_headers()
    url = f"{sonarr_config['base_url']}/rootfolder"
    headers = sonarr_config['headers']
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
    sonarr_config = get_sonarr_headers()
    url = f"{sonarr_config['base_url']}/downloadclient?forceSave=true"
    headers = sonarr_config['headers']
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

