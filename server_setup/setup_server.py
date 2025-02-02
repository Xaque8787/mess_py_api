import os
from dotenv import load_dotenv
from server_setup.jellyfin_api import *
from server_setup.decryption import *


def server_setup():
    load_dotenv('/app/compose/installed/media_server/.env')
    # load_dotenv()
    url = os.getenv("server_ip")
    user = os.getenv("AdminUser")
    # passwrd = os.getenv("admin_pass")
    passwrd = decrypt_password(os.getenv("AdminPassword"))
    host_path_enabled = os.getenv("ADD_MEDIA_PATH", "")
    print(url)
    print(user)
    print(passwrd)
    configure_server(url, user, passwrd)
    client = create_client(url, user, passwrd)
    if host_path_enabled:
        try:
            movie_library_path = '/data/movies'
            tv_library_path = '/data/tvshows'  # Removed extra space at the beginning
            add_media_libraries(client, movie_library_path, tv_library_path)
            library_options(client, url)
        except Exception as e:
            print(f"Error adding media libraries: {e}")

    user_id = find_user_mainID(client, user)
    update_policy(client, user_id, url)


if __name__ == "__main__":
    server_setup()
