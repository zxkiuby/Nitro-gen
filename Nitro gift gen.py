import random
import string
import requests
import time

def generate_nitro_code(length=16):
    """Generate a random string that mimics a Discord Nitro gift code format.
    Using only uppercase and lowercase letters to match the provided example.
    """
    characters = string.ascii_uppercase + string.ascii_lowercase
    code = ''.join(random.choice(characters) for _ in range(length))
    return f"https://discord.gift/{code}"

def send_to_webhook(webhook_url, message):
    """Send a message to a Discord webhook."""
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code != 204:
        print(f"Failed to send message: {response.status_code} - {response.text}")

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL: ")
    print("Starting ZxKiuby Nitro gift gen, sending...")
    counter = 1
    while True:
        nitro_link = generate_nitro_code()
        message = f"{counter}: {nitro_link}"
        send_to_webhook(webhook_url, message)
        print(f"Sent: {message}")
        counter += 1
        time.sleep(1)