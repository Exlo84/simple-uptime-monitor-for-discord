# config.py
import logging

DISCORD_WEBHOOK_URL = 'your_discord_webhook_url'
MONITORING_INTERVAL = 5  # minutes
HOSTS_TO_MONITOR = [
    {
        'ip': '85.176.105.10',
        'port': 8451,
        'name': 'Exlo_ETHO_RPC'
    },
    {
        'ip': '192.168.1.223',
        'port': 30305,
        'name': 'ETHO-MN-Pine64'
    }
]

LOG_LEVEL = logging.DEBUG  # Change this to logging.INFO, logging.WARNING, etc. to adjust the log level
