import os
from dotenv import load_dotenv
from server_setup.jellyfin_api import *
from server_setup.decryption import *
import re

def process_env_variable(env_var_value):
    if isinstance(env_var_value, str):
        # Use regex to split on commas not preceded by a backslash
        items = re.split(r'(?<!\\),', env_var_value.strip('"'))

        # Remove any backslashes used for escaping commas and strip whitespace
        processed_value = [item.replace(r'\,', ',').strip() for item in items if item.strip()]

        return processed_value
    return env_var_value
def main():
    load_dotenv('/app/compose/installed/threadfin_proxy/.env')
    load_dotenv('/app/compose/installed/media_server/.env')
    url = os.getenv("server_ip")
    user = os.getenv("AdminUser")
    passwrd = decrypt_password(os.getenv("AdminPassword"))
    client = create_client(url, user, passwrd)
    application_version = "threadfin"
    main_user = os.getenv('thread_user', "")
    # thread_pass = os.getenv('thread_pass', "")
    main_pass = decrypt_password(os.getenv("thread_pass"))
    host = os.getenv('thread_host', "")
    port = os.getenv('thread_port', "")
    epg_path = process_env_variable(os.getenv('EPG_URL', ""))
    live_tv = True
    add_tuner_host(client, url, live_tv, application_version, host, port, main_user, main_pass)
    add_epg_xml(client, epg_path, url, live_tv, application_version, host, port, main_user, main_pass)


if __name__ == "__main__":
    main()