import os
from server_setup.arrs.sonarr.sonarr_api import *
from dotenv import load_dotenv


def main():
    load_dotenv()
    load_dotenv('/app/compose/installed/media_server/.env')
    root_path = "/mess_media/jellyfin/tv"
    post_root_folder(root_path)


if __name__ == "__main__":
    main()