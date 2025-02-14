import os
from dotenv import load_dotenv
import requests
import json


def get_prowlarr_headers():
    """
    Load Radarr API details from a .env file and return the necessary headers for API requests.

    Returns:
        dict: A dictionary containing headers and the Radarr API URL.
    """
    # Load environment variables from .env
    load_dotenv('/app/compose/installed/prowlarr_app/.env')
    # Fetch Radarr details from environment variables
    prowlarr_ip = os.getenv("PROWLARR_IP")
    prowlarr_port = os.getenv("PROWLARR_PORT", "9696")
    prowlarr_apikey = os.getenv("PROWLARR_APIKEY")

    if not all([prowlarr_ip, prowlarr_port, prowlarr_apikey]):
        raise ValueError(
            "One or more required environment variables (prowlarr_ip, prowlarr_port, prowlarr_apikey) are missing.")

    # Construct the Radarr API base URL
    base_url = f"http://{prowlarr_ip}:{prowlarr_port}/api/v1"

    # Return headers and base URL
    return {
        "base_url": base_url,
        "headers": {
            "X-Api-Key": prowlarr_apikey,
            "Content-Type": "application/json"
        }
    }


def post_indexer():
    """
    Posts a hardcoded download client configuration to the Radarr API.
    """
    # Get Radarr headers and base URL
    prowlarr_config = get_prowlarr_headers()
    url = f"{prowlarr_config['base_url']}/indexer"
    headers = prowlarr_config['headers']

    # Hardcoded JSON payload
    payload = {
        "indexerUrls": [
            "https://zilean.elfhosted.com"
        ],
        "legacyUrls": [],
        "definitionName": "zilean",
        "description": "A custom indexer for Zilean the unofficial DMM indexer",
        "language": "en-US",
        "encoding": "Unicode (UTF-8)",
        "enable": True,
        "redirect": False,
        "supportsRss": True,
        "supportsSearch": True,
        "supportsRedirect": False,
        "supportsPagination": False,
        "appProfileId": 1,
        "protocol": "torrent",
        "privacy": "public",
        "capabilities": {
            "limitsMax": 100,
            "limitsDefault": 100,
            "categories": [
                {
                    "id": 2000,
                    "name": "Movies",
                    "subCategories": []
                },
                {
                    "id": 5000,
                    "name": "TV",
                    "subCategories": []
                }
            ],
            "supportsRawSearch": False,
            "searchParams": [
                "q",
                "q"
            ],
            "tvSearchParams": [
                "q",
                "season",
                "ep"
            ],
            "movieSearchParams": [
                "q",
                "imdbId"
            ],
            "musicSearchParams": [],
            "bookSearchParams": []
        },
        "priority": 25,
        "downloadClientId": 0,
        "added": "2024-11-16T02:57:35Z",
        "sortName": "zilean",
        "name": "Zilean",
        "fields": [
            {
                "order": 0,
                "name": "definitionFile",
                "value": "zilean",
                "type": "textbox",
                "advanced": False,
                "hidden": "hidden",
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 1,
                "name": "baseUrl",
                "label": "Base Url",
                "helpText": "Select which base url Prowlarr will use for requests to the site",
                "value": "https://zilean.elfhosted.com",
                "type": "select",
                "advanced": False,
                "selectOptionsProviderAction": "getUrls",
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 2,
                "name": "baseSettings.queryLimit",
                "label": "Query Limit",
                "helpText": "The number of max queries as specified by the respective unit that Prowlarr will allow to the site",
                "type": "number",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 3,
                "name": "baseSettings.grabLimit",
                "label": "Grab Limit",
                "helpText": "The number of max grabs as specified by the respective unit that Prowlarr will allow to the site",
                "type": "number",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 4,
                "name": "baseSettings.limitsUnit",
                "label": "Limits Unit",
                "helpText": "The unit of time for counting limits per indexer",
                "value": 0,
                "type": "select",
                "advanced": True,
                "selectOptions": [
                    {
                        "value": 0,
                        "name": "Day",
                        "order": 0,
                        "hint": "(0)"
                    },
                    {
                        "value": 1,
                        "name": "Hour",
                        "order": 1,
                        "hint": "(1)"
                    }
                ],
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 5,
                "name": "torrentBaseSettings.appMinimumSeeders",
                "label": "Apps Minimum Seeders",
                "helpText": "Minimum seeders required by the Applications for the indexer to grab, empty is Sync profile'\''s default",
                "type": "number",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 6,
                "name": "torrentBaseSettings.seedRatio",
                "label": "Seed Ratio",
                "helpText": "The ratio a torrent should reach before stopping, empty uses the download client'\''s default. Ratio should be at least 1.0 and follow the indexers rules",
                "type": "number",
                "advanced": False,
                "privacy": "normal",
                "isFloat": True
            },
            {
                "order": 7,
                "name": "torrentBaseSettings.seedTime",
                "label": "Seed Time",
                "unit": "minutes",
                "helpText": "The time a torrent should be seeded before stopping, empty uses the download client'\''s default",
                "type": "number",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 8,
                "name": "torrentBaseSettings.packSeedTime",
                "label": "Pack Seed Time",
                "unit": "minutes",
                "helpText": "The time a pack (season or discography) torrent should be seeded before stopping, empty is app'\''s default",
                "type": "number",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            },
            {
                "order": 9,
                "name": "torrentBaseSettings.preferMagnetUrl",
                "label": "Prefer Magnet URL",
                "helpText": "When enabled, this indexer will prefer the use of magnet URLs for grabs with fallback to torrent links",
                "value": True,
                "type": "checkbox",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            }
        ],
        "implementationName": "Cardigann",
        "implementation": "Cardigann",
        "configContract": "CardigannSettings",
        "infoLink": "https://wiki.servarr.com/prowlarr/supported-indexers#zilean",
        "tags": [],
        "id": 0
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 201:
        print("Download client configuration successfully added.")
    else:
        print(f"Failed to add download client: {response.status_code} - {response.text}")


def add_prowlarr_sync(server_name, server_ip, server_port, app_ip, app_port, api_key, app_sync):
    # Get headers and base URL from the dotenv loader
    prowlarr_config = get_prowlarr_headers()
    url = f"{prowlarr_config['base_url']}/applications"
    headers = prowlarr_config['headers']

    payload = {
        "syncLevel": "fullSync",
        "enable": True,
        "name": server_name,
        "fields": [
            {
                "order": 0,
                "name": "prowlarrUrl",
                "label": "Prowlarr Server",
                "helpText": f"Prowlarr server URL as {server_name} sees it, including http(s)://, port, and urlbase if needed",
                "value": f"http://{server_ip}:{server_port}",
                "type": "textbox",
                "advanced": False,
                "privacy": "normal",
                "placeholder": "http://localhost:9696",
                "isFloat": False
            },
            {
                "order": 1,
                "name": "baseUrl",
                "label": f"{server_name} Server",
                "helpText": f'"URL used to connect to {server_name} server, including http(s)://, port, and urlbase if required"',
                "value": f"http://{app_ip}:{app_port}",
                "type": "textbox",
                "advanced": False,
                "privacy": "normal",
                "placeholder": f"http://localhost:{app_port}",
                "isFloat": False
            },
            {
                "order": 2,
                "name": "apiKey",
                "label": "API Key",
                "helpText": f"The ApiKey generated by {server_name} in Settings/General",
                "value": api_key,
                "type": "textbox",
                "advanced": False,
                "privacy": "apiKey",
                "isFloat": False
            },
            app_sync,  # Pass the sync categories dynamically
            {
                "order": 4,
                "name": "syncRejectBlocklistedTorrentHashesWhileGrabbing",
                "label": "Sync Reject Blocklisted Torrent Hashes While Grabbing",
                "helpText": "If a torrent is blocked by hash it may not properly be rejected during RSS/Search for some indexers, enabling this will allow it to be rejected after the torrent is grabbed, but before it is sent to the client.",
                "value": False,
                "type": "checkbox",
                "advanced": True,
                "privacy": "normal",
                "isFloat": False
            }
        ],
        "implementationName": server_name,
        "implementation": server_name,
        "configContract": f"{server_name}Settings",
        "infoLink": f"https://wiki.servarr.com/prowlarr/supported#{server_name}",
        "tags": []
    }
    print(json.dumps(payload, indent=2))
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("APP client configuration successfully added.")
    else:
        print(f"Failed to add application: {response.status_code} - {response.text}")
    # return response.json()  # Return the JSON response from the API

if __name__ == "__main__":
    get_prowlarr_headers()
    post_indexer()
