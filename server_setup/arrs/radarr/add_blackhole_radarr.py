from server_setup.arrs.radarr.radarr_api import *
from dotenv import load_dotenv
from server_setup.arrs.radarr.download_clients import *


def add_blackhole_radarr():
    load_dotenv()
    load_dotenv('/app/compose/installed/radarr_app/.env')
    apikey = os.getenv("RADARR_APIKEY", "")
    app_ip = os.getenv("RADARR_IP")
    app_port = os.getenv("RADARR_PORT", "7878")
    post_download_client(blackhole_client(apikey, app_ip, app_port))


if __name__ == "__main__":
    add_blackhole_radarr()