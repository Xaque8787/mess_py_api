from server_setup.arrs.sonarr.sonarr_api import *
from dotenv import load_dotenv
from server_setup.arrs.sonarr.download_clients import *


def add_blackhole_sonarr():
    load_dotenv()
    load_dotenv('/app/compose/installed/sonarr_app/.env')
    apikey = os.getenv("SONARR_APIKEY", "")
    post_download_client(blackhole_client(apikey))


if __name__ == "__main__":
    add_blackhole_sonarr()