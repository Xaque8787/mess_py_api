import os
from dotenv import load_dotenv
from server_setup.jellyfin_api import *
from server_setup.decryption import *


def m3uparser_add_library():
    load_dotenv('/app/compose/installed/media_server/.env')
    url = os.getenv("server_ip")
    user = os.getenv("AdminUser")
    movie_library_path = '/mnt/vods/Movie_VOD'
    tv_library_path = '/mnt/vods/TV_VOD'
    passwrd = decrypt_password(os.getenv("AdminPassword"))
    client = create_client(url, user, passwrd)
    add_media_libraries(client, movie_library_path, tv_library_path)
    library_options(client, url)


if __name__ == "__main__":
    m3uparser_add_library()
