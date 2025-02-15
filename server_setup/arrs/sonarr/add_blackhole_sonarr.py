from server_setup.arrs.sonarr.sonarr_api import *
from dotenv import load_dotenv



def add_blackhole_sonarr():
    from server_setup.arrs.sonarr.sonarr_api import post_download_client
    from server_setup.arrs.sonarr.download_clients import blackhole_client
    load_dotenv()
    load_dotenv('/app/compose/installed/sonarr_app/.env')
    apikey = os.getenv("SONARR_APIKEY", "")
    app_ip = os.getenv("SONARR_IP")
    app_port = os.getenv("SONARR_PORT", "8989")
    post_download_client(blackhole_client(apikey, app_ip, app_port))


if __name__ == "__main__":
    add_blackhole_sonarr()