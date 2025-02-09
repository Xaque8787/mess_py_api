import os
from server_setup.arrs.radarr.radarr_api import *
import dotenv
from server_setup.arrs.radarr.download_clients import *


def main():
    load_dotenv()
    load_dotenv('/app/compose/installed/media_server/.env')
    root_path = os.getenv("ADD_MEDIA_PATH", "/mnt/jellyfin/movies")

    post_root_folder(root_path)


if __name__ == "__main__":
    main()

