import os
from dotenv import load_dotenv
from server_setup.jellyfin_api import *
from server_setup.decryption import *


def server_setup():
    load_dotenv('/app/compose/installed/media_server/.env')
    url = os.getenv("server_ip")
    user = os.getenv("AdminUser")
    passwrd = decrypt_password(os.getenv("AdminPassword"))
    # passwrd = decrypt_password(os.getenv("AdminPassword"))
    print(url)
    print(user)
    print(passwrd)
    configure_server(url, user, passwrd)
    client = create_client(url, user, passwrd)
    add_media_libraries(client)
    library_options(client, url)
    user_id = find_user_mainID(client, user)
    update_policy(client, user_id, url)


if __name__ == "__main__":
    server_setup()
