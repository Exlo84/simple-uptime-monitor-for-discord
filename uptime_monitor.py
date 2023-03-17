import socket
import schedule
import time
import logging
from discord_webhook import DiscordWebhook, DiscordEmbed
from config import DISCORD_WEBHOOK_URL, MONITORING_INTERVAL, HOSTS_TO_MONITOR, LOG_LEVEL

# Configure logging
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

def check_uptime(ip, port, name):
    try:
        with socket.create_connection((ip, port), timeout=10):
            logging.info(f"{name} ({ip}:{port}) is up.")
    except (socket.timeout, ConnectionRefusedError) as e:
        logging.warning(f"{name} ({ip}:{port}) is down. Error: {e}")
        send_notification(ip, port, name, "down")

def send_notification(ip, port, name, status):
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)
    embed = DiscordEmbed(title=f"Host {status.capitalize()}",
                         description=f"{name} ({ip}:{port}) is {status}.",
                         color=0xFF0000 if status == "down" else 0x00FF00)
    webhook.add_embed(embed)
    webhook.execute()

def main():
    logging.debug("Starting uptime monitoring...")

    for host in HOSTS_TO_MONITOR:
        schedule.every(MONITORING_INTERVAL).minutes.do(check_uptime, host['ip'], host['port'], host['name'])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
