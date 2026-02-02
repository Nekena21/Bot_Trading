"""Configuration centrale du projet.

Contient la zone du chart fixe et les chemins.
"""

CHART_ZONE = {
    "top": 100,
    "left": 100,
    "width": 1200,
    "height": 600,
}

CONFIG = {
    'DEBUG': True,
    'CAPTURE_ZONE': CHART_ZONE,
    'LOG_PATH': 'trading_bot_cv/logs',
}
