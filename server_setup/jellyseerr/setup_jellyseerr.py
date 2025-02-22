import requests
jellyseerr_ip = jellyseerr_port = radarr_ip = radarr_port = None
sonarr_ip = sonarr_port = radarr_apikey = sonarr_apikey = None
BASE_URL = jellyfin_ip = username = password = None

def load_env_variables():
    """Load environment variables when the module is called directly."""
    from dotenv import load_dotenv
    import os
    from server_setup.decryption import decrypt_password

    load_dotenv('/app/compose/installed/jellyseerr_app/.env')
    load_dotenv('/app/compose/installed/radarr_app/.env')
    load_dotenv('/app/compose//installed/sonarr_app/.env')
    load_dotenv('/app/compose/installed/media_server/.env')

    global jellyseerr_ip, jellyseerr_port, radarr_ip, radarr_port
    global sonarr_ip, sonarr_port, radarr_apikey, sonarr_apikey
    global BASE_URL, jellyfin_ip, username, password

    jellyseerr_ip = os.getenv("JELLYSEERR_IP", "10.21.12.5")
    jellyseerr_port = os.getenv("JELLYSEERR_PORT", "5055")
    radarr_ip = os.getenv("RADARR_IP", "10.21.12.11")
    radarr_port = int(os.getenv("RADARR_PORT", "7878"))
    sonarr_ip = os.getenv("SONARR_IP", "10.21.12.12")
    sonarr_port = int(os.getenv("SONARR_PORT", "8989"))
    radarr_apikey = os.getenv("RADARR_APIKEY", "")
    sonarr_apikey = os.getenv("SONARR_APIKEY", "")
    BASE_URL = f"http://{jellyseerr_ip}:{jellyseerr_port}/api/v1"
    jellyfin_ip = os.getenv("JELLYFIN_IP", "10.21.12.3")
    username = os.getenv("AdminUser", "")
    password = decrypt_password(os.getenv("AdminPassword"))
def authenticate():
    """Authenticate and retrieve session cookies."""
    auth_url = f"{BASE_URL}/auth/jellyfin"
    credentials = {
        "username": username,
        "password": password,
        "hostname": jellyfin_ip,
        "port": 8096,
        "useSsl": False,
        "urlBase": "",
        "email": "fake@mail.com",
        "serverType": 2
    }
    session = requests.Session()
    response = session.post(auth_url, json=credentials)
    if response.status_code == 200:
        print("Authentication successful.")
        return session
    else:
        print(f"Authentication failed: {response.text}")
        exit()


def reauthenticate(session):
    """Perform a second authentication to get a new session."""
    auth_url = f"{BASE_URL}/auth/jellyfin"
    credentials = {"username": username, "password": password}
    response = session.post(auth_url, json=credentials)
    if response.status_code == 200:
        print("Reauthentication successful.")
        return session
    else:
        print(f"Reauthentication failed: {response.text}")
        exit()

def get_api_key(session):
    """Fetch the correct API key using session cookies."""
    settings_url = f"{BASE_URL}/settings/jellyfin"
    response = session.get(settings_url)
    if response.status_code == 200:
        return response.json().get("apiKey")
    else:
        print(f"Failed to retrieve API Key: {response.text}")
        exit()

def initialize_application(session, api_key):
    """Initialize the application."""
    init_url = f"{BASE_URL}/settings/initialize"
    headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
    response = session.post(init_url, headers=headers, json={"initialized": True})
    if response.status_code == 200:
        print("Application initialized successfully.")
    else:
        print(f"Failed to initialize application: {response.text}")
        exit()


def get_libraries(session):
    """Retrieve available libraries using session."""
    library_url = f"{BASE_URL}/settings/jellyfin/library?sync=true"
    response = session.get(library_url)
    if response.status_code == 200:
        return [library["id"] for library in response.json()]
    else:
        print(f"Failed to retrieve libraries: {response.text}")
        exit()


def enable_libraries(session, library_ids):
    """Enable all retrieved libraries using session."""
    enable_url = f"{BASE_URL}/settings/jellyfin/library?enable={','.join(library_ids)}"
    response = session.get(enable_url)
    if response.status_code == 200:
        print("Libraries enabled successfully.")
    else:
        print(f"Failed to enable libraries: {response.text}")


def start_library_sync(session):
    """Trigger the library sync using session."""
    sync_url = f"{BASE_URL}/settings/jellyfin/sync"
    response = session.post(sync_url, json={"start": True})
    if response.status_code == 200:
        print("Library sync started successfully.")
    else:
        print(f"Failed to start library sync: {response.text}")

def enable_sonarr(session):
    """Enable Sonarr integration using session."""
    sonarr_url = f"{BASE_URL}/settings/sonarr"
    # Payload for enabling Sonarr (adapt this as per the required fields in API docs)
    payload = {
        "name": "Sonarr Main",
        "hostname": sonarr_ip,
        "port": sonarr_port,
        "apiKey": sonarr_apikey,  # Use the correct API key here
        "useSsl": False,
        "activeProfileId": 1,
        "activeProfileName": "720p/1080p",
        "activeDirectory": "/mess_media/jellyfin/tv",
        "is4k": False,
        "enableSeasonFolders": True,
        "isDefault": True,
        "syncEnabled": True,
        "preventSearch": False
    }
    response = session.post(sonarr_url, json=payload)
    if response.status_code == 201:
        print("Sonarr enabled successfully.")
    else:
        print(f"Failed to enable Sonarr: {response.text}")

def enable_radarr(session):
    """Enable Radarr integration using session."""
    radarr_url = f"{BASE_URL}/settings/radarr"
    # Payload for enabling Radarr (adapt this as per the required fields in API docs)
    payload = {
        "name": "Radarr Main",
        "hostname": radarr_ip,
        "port": radarr_port,
        "apiKey": radarr_apikey,  # Use the correct API key here
        "useSsl": False,
        "activeProfileId": 1,
        "activeProfileName": "720p/1080p",
        "activeDirectory": "/mess_media/jellyfin/movies",
        "is4k": False,
        "minimumAvailability": "Released",
        "isDefault": True,
        "syncEnabled": True,
        "preventSearch": False
    }
    response = session.post(radarr_url, json=payload)
    if response.status_code == 201:
        print("Radarr enabled successfully.")
    else:
        print(f"Failed to enable Radarr: {response.text}")


if __name__ == "__main__":
    load_env_variables()
    session = authenticate()
    api_token = get_api_key(session)
    if api_token:
        initialize_application(session, api_token)
        session = reauthenticate(session)
        library_ids = get_libraries(session)
        if library_ids:
            enable_libraries(session, library_ids)
            start_library_sync(session)
        enable_sonarr(session)
        enable_radarr(session)
