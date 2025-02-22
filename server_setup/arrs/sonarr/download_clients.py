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
                    "value": "172.22.0.11",
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
                    "value": apikey,
                    "type": "password",
                    "advanced": False,
                    "privacy": "password",
                    "isFloat": False
                },
                {
                    "order": 6,
                    "name": "tvCategory",
                    "label": "Category",
                    "helpText": "Adding a category specific to Sonarr avoids conflicts with unrelated non-Sonarr downloads. Using a category is optional, but strongly recommended.",
                    "value": "tv-sonarr",
                    "type": "textbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 7,
                    "name": "tvImportedCategory",
                    "label": "Post-Import Category",
                    "helpText": "Category for Sonarr to set after it has imported the download. Sonarr will not remove torrents in that category even if seeding finished. Leave blank to keep same category.",
                    "type": "textbox",
                    "advanced": True,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 8,
                    "name": "recentTvPriority",
                    "label": "Recent Priority",
                    "helpText": "Priority to use when grabbing episodes that aired within the last 14 days",
                    "value": 0,
                    "type": "select",
                    "advanced": False,
                    "selectOptions": [
                        {
                            "value": 0,
                            "name": "Last",
                            "order": 0
                        },
                        {
                            "value": 1,
                            "name": "First",
                            "order": 1
                        }
                    ],
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 9,
                    "name": "olderTvPriority",
                    "label": "Older Priority",
                    "helpText": "Priority to use when grabbing episodes that aired over 14 days ago",
                    "value": 0,
                    "type": "select",
                    "advanced": False,
                    "selectOptions": [
                        {
                            "value": 0,
                            "name": "Last",
                            "order": 0
                        },
                        {
                            "value": 1,
                            "name": "First",
                            "order": 1
                        }
                    ],
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 10,
                    "name": "initialState",
                    "label": "Initial State",
                    "helpText": "Initial state for torrents added to qBittorrent. Note that Forced Torrents do not abide by seed restrictions",
                    "value": 0,
                    "type": "select",
                    "advanced": False,
                    "selectOptions": [
                        {
                            "value": 0,
                            "name": "Start",
                            "order": 0
                        },
                        {
                            "value": 1,
                            "name": "ForceStart",
                            "order": 1
                        },
                        {
                            "value": 2,
                            "name": "Pause",
                            "order": 2
                        }
                    ],
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 11,
                    "name": "sequentialOrder",
                    "label": "Sequential Order",
                    "helpText": "Download in sequential order (qBittorrent 4.1.0+)",
                    "value": False,
                    "type": "checkbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 12,
                    "name": "firstAndLast",
                    "label": "First and Last First",
                    "helpText": "Download first and last pieces first (qBittorrent 4.1.0+)",
                    "value": False,
                    "type": "checkbox",
                    "advanced": False,
                    "privacy": "normal",
                    "isFloat": False
                },
                {
                    "order": 13,
                    "name": "contentLayout",
                    "label": "Content Layout",
                    "helpText": "Whether to use qBittorrent's configured content layout, the original layout from the torrent or always create a subfolder (qBittorrent 4.3.2+)",
                    "value": 0,
                    "type": "select",
                    "advanced": False,
                    "selectOptions": [
                        {
                            "value": 0,
                            "name": "Default",
                            "order": 0
                        },
                        {
                            "value": 1,
                            "name": "Original",
                            "order": 1
                        },
                        {
                            "value": 2,
                            "name": "Subfolder",
                            "order": 2
                        }
                    ],
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
