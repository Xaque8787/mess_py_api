from server_setup.arrs.prowlarr.prowlarr_api import *
from dotenv import load_dotenv
import os

def main():
    load_dotenv('/app/compose/installed/radarr_app/.env')
    load_dotenv('/app/compose/installed/prowlarr_app/.env')
    server_name = 'Radarr'
    server_ip = os.getenv("PROWLARR_IP")
    server_port = os.getenv("PROWLARR_PORT")
    app_ip = os.getenv("RADARR_IP")
    app_port = os.getenv("RADARR_PORT")
    api_key = os.getenv("RADARR_APIKEY")
    app_sync = {
        "order": 3,
        "name": "syncCategories",
        "label": "Sync Categories",
        "helpText": "Only Indexers that support these categories will be synced",
        "value": [2000, 2010, 2020, 2030, 2040, 2045, 2050, 2060, 2070, 2080, 2090],
        "type": "select",
        "advanced": True,
        "selectOptions": [
            {"value": 2000, "name": "Movies", "order": 0, "hint": "(2000)"},
            {"value": 2010, "name": "Movies/Foreign", "order": 0, "hint": "(2010)", "parentValue": 2000},
            {"value": 2020, "name": "Movies/Other", "order": 0, "hint": "(2020)", "parentValue": 2000},
            {"value": 2030, "name": "Movies/SD", "order": 0, "hint": "(2030)", "parentValue": 2000},
            {"value": 2040, "name": "Movies/HD", "order": 0, "hint": "(2040)", "parentValue": 2000},
            {"value": 2045, "name": "Movies/UHD", "order": 0, "hint": "(2045)", "parentValue": 2000},
            {"value": 2050, "name": "Movies/BluRay", "order": 0, "hint": "(2050)", "parentValue": 2000},
            {"value": 2060, "name": "Movies/3D", "order": 0, "hint": "(2060)", "parentValue": 2000},
            {"value": 2070, "name": "Movies/DVD", "order": 0, "hint": "(2070)", "parentValue": 2000},
            {"value": 2080, "name": "Movies/WEB-DL", "order": 0, "hint": "(2080)", "parentValue": 2000},
            {"value": 2090, "name": "Movies/x265", "order": 0, "hint": "(2090)", "parentValue": 2000}
        ],
        "privacy": "normal",
        "isFloat": False
    }
    add_prowlarr_sync(server_name, server_ip, server_port, app_ip, app_port, api_key, app_sync)


if __name__ == "__main__":
    main()