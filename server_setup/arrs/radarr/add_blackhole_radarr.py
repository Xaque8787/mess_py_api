from server_setup.arrs.radarr.radarr_api import *
from dotenv import load_dotenv
from server_setup.arrs.radarr.download_clients import *


def add_blackhole_radarr():
    load_dotenv()
    load_dotenv('/app/compose/installed/radarr_app/.env')
    apikey = os.getenv("RADARR_APIKEY", "")
    post_download_client(blackhole_client(apikey))


if __name__ == "__main__":
    add_blackhole_radarr()