import os
from dotenv import load_dotenv
from server_setup.jellyfin_api import *
from server_setup.decryption import *


def server_setup():
    load_dotenv('/app/compose/installed/media_server/.env')
    # load_dotenv()
    url = os.getenv("jellyfin_url")
    user = os.getenv("admin_user")
    # passwrd = os.getenv("admin_pass")
    movie_library_path = '/mnt/vods/Movie_VOD'
    tv_library_path = '/mnt/vods/TV_VOD'
    passwrd = decrypt_password(os.getenv("AdminPassword"))
    print(url)
    print(user)
    print(passwrd)
    configure_server(url, user, passwrd)
    client = create_client(url, user, passwrd)
    add_media_libraries(client, movie_library_path, tv_library_path)
    library_options(client, url)
    user_id = find_user_mainID(client, user)
    update_policy(client, user_id, url)


if __name__ == "__main__":
    server_setup()
