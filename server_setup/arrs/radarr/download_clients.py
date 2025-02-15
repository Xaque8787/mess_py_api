def blackhole_client(apikey, app_ip, app_port):
    return {
            "id": 0,
            "enable": True,
            "protocol": "torrent",
            "priority": 1,
            "removeCompletedDownloads": True,
            "removeFailedDownloads": True,
            "name": "qBittorrent",
            "fields": [
                {
                    "order": 0,
                    "name": "host",
                    "label": "Host",
                    "value": "10.21.12.21",
                    "type": "textbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 1,
                    "name": "port",
                    "label": "Port",
                    "value": 8484,
                    "type": "textbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 2,
                    "name": "useSsl",
                    "label": "Use SSL",
                    "helpText": "Use a secure connection. See Options -> Web UI -> 'Use HTTPS instead of HTTP' in qBittorrent.",
                    "value": False,
                    "type": "checkbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 3,
                    "name": "urlBase",
                    "label": "URL Base",
                    "helpText": "Adds a prefix to the qBittorrent url, such as http://[host]:[port]/[urlBase]/api",
                    "type": "textbox",
                    "advanced": True,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 4,
                    "name": "username",
                    "label": "Username",
                    "value": f"http://{app_ip}:{app_port}",
                    "type": "textbox",
                    "advanced": False,
                    "privacy": "userName",
                    "isFloat": False
                },
                {
                    "order": 5,
                    "name": "password",
                    "label": "Password",
                    "value": apikey,  # Replace password with Radarr API key
                    "type": "password",
                    "advanced": False,
                    "privacy": "password",
                    "isFloat": False
                },
                {
                    "order": 6,
                    "name": "movieCategory",
                    "label": "Category",
                    "helpText": "Adding a category specific to Radarr avoids conflicts with unrelated non-Radarr downloads. Using a category is optional, but strongly recommended.",
                    "value": "movie-radarr",
                    "type": "textbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 7,
                    "name": "movieImportedCategory",
                    "label": "Post-Import Category",
                    "helpText": "Category for Radarr to set after it has imported the download. Radarr will not remove torrents in that category even if seeding finished. Leave blank to keep same category.",
                    "type": "textbox",
                    "advanced": True,
                    "privacy": "normal",
                    "isFloat": False
                }
            ],
            "implementationName": "qBittorrent",
            "implementation": "QBittorrent",
            "configContract": "QBittorrentSettings",
            "infoLink": "https://wiki.servarr.com/radarr/supported#qbittorrent",
            "tags": []
        }
