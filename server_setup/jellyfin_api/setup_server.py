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
    movie_path = os.getenv("HOST_MOVIE", "")
    tv_path = os.getenv("HOST_TV", "")
    print(url)
    print(user)
    print(passwrd)
    configure_server(url, user, passwrd)
    client = create_client(url, user, passwrd)
    if host_path_enabled:
        try:
            movie_library_path = '/data/movies'
            tv_library_path = '/data/tvshows'
            add_media_libraries(client, movie_library_path, tv_library_path)
        except Exception as e:
            print(f"Error setting host paths: {e}")
    else:
        try:
            add_media_libraries(client)  # Call function without paths
        except Exception as e:
            print(f"Error adding media libraries without paths: {e}")

    library_options(client, url)
    user_id = find_user_mainID(client, user)
    update_policy(client, user_id, url)


if __name__ == "__main__":
    server_setup()
