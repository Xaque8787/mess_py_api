from server_setup.threadfin import *
from dotenv import load_dotenv
import os
import re
from server_setup.decryption import *

def process_env_variable(env_var_value):
    if isinstance(env_var_value, str):
        # Use regex to split on commas not preceded by a backslash
        items = re.split(r'(?<!\\),', env_var_value.strip('"'))

        # Remove any backslashes used for escaping commas and strip whitespace
        processed_value = [item.replace(r'\,', ',').strip() for item in items if item.strip()]

        return processed_value
    return env_var_value


def extract_first_url(url_list):
    if not url_list:  # Check if the list is empty
        return None, url_list  # Return None and the unchanged list

    main_m3u = url_list[0]  # Get the first URL
    m3u_urls = url_list[1:]  # Get the rest of the list
    return main_m3u, m3u_urls


def threadfin_setup():
    # load_dotenv()
    load_dotenv('/app/compose/installed/threadfin_proxy/.env')
    URLS = process_env_variable(os.getenv('M3U_URL', ""))
    main_m3u, m3u_urls = extract_first_url(URLS)
    thread_user = os.getenv('thread_user', "")
    # thread_pass = os.getenv('thread_pass', "")
    thread_pass = decrypt_password(os.getenv("thread_pass"))
    host = os.getenv('thread_host', "")
    port = os.getenv('thread_port', "")
    epg_path = process_env_variable(os.getenv('EPG_URL', ""))
    # print(main_m3u)
    # print(m3u_urls)
    print(thread_user)
    # print(thread_pass)
    print(host)
    print(port)
    # print(epg_path)
    run_websocket_operations(m3u_url=main_m3u, epg_url=epg_path, port=port, thread_user=thread_user,
                             thread_pass=thread_pass, token=None, host=host, remaining_m3u=m3u_urls)
    run_reload_operations(port=port, thread_user=thread_user, thread_pass=thread_pass, host=host)


if __name__ == "__main__":
    threadfin_setup()
