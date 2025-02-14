from server_setup.arrs.prowlarr.prowlarr_api import *
from dotenv import load_dotenv
import os

def main():
    load_dotenv('/app/compose/installed/sonarr_app/.env')
    load_dotenv('/app/compose/installed/prowlarr_app/.env')
    server_name = 'Sonarr'
    server_ip = os.getenv("PROWLARR_IP")
    server_port = os.getenv("PROWLARR_PORT")
    app_ip = os.getenv("SONARR_IP")
    app_port = os.getenv("SONARR_PORT")
    api_key = os.getenv("SONARR_APIKEY")
    app_sync = {
        "order": 3,
        "name": "syncCategories",
        "label": "Sync Categories",
        "helpText": "Only Indexers that support these categories will be synced",
        "value": [
          5000,
          5010,
          5020,
          5030,
          5040,
          5045,
          5050,
          5090
        ],
        "type": "select",
        "advanced": True,
        "selectOptions": [
            {
                "value": 5000,
                "name": "TV",
                "order": 0,
                "hint": "(5000)"
            },
            {
                "value": 5010,
                "name": "TV/WEB-DL",
                "order": 0,
                "hint": "(5010)",
                "parentValue": 5000
            },
            {
                "value": 5020,
                "name": "TV/Foreign",
                "order": 0,
                "hint": "(5020)",
                "parentValue": 5000
            },
            {
                "value": 5030,
                "name": "TV/SD",
                "order": 0,
                "hint": "(5030)",
                "parentValue": 5000
            },
            {
                "value": 5040,
                "name": "TV/HD",
                "order": 0,
                "hint": "(5040)",
                "parentValue": 5000
            },
            {
                "value": 5045,
                "name": "TV/UHD",
                "order": 0,
                "hint": "(5045)",
                "parentValue": 5000
            },
            {
                "value": 5050,
                "name": "TV/Other",
                "order": 0,
                "hint": "(5050)",
                "parentValue": 5000
            },
            {
                "value": 5060,
                "name": "TV/Sport",
                "order": 0,
                "hint": "(5060)",
                "parentValue": 5000
            },
            {
                "value": 5070,
                "name": "TV/Anime",
                "order": 0,
                "hint": "(5070)",
                "parentValue": 5000
            },
            {
                "value": 5080,
                "name": "TV/Documentary",
                "order": 0,
                "hint": "(5080)",
                "parentValue": 5000
            },
            {
                "value": 5090,
                "name": "TV/x265",
                "order": 0,
                "hint": "(5090)",
                "parentValue": 5000
            }
        ],
        "privacy": "normal",
        "isFloat": False
    }
    add_prowlarr_sync(server_name, server_ip, server_port, app_ip, app_port, api_key, app_sync)


if __name__ == "__main__":
    main()