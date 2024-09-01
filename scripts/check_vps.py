import requests
import os

VPS_URL = os.getenv('VPS_URL', 'http://your-vps-url')  # Ganti dengan URL VPS Anda
EMAIL_API_URL = os.getenv('EMAIL_API_URL', 'http://email-api-url')  # Ganti dengan URL API email Anda
EMAIL_API_KEY = os.getenv('EMAIL_API_KEY', 'your-email-api-key')  # Ganti dengan API Key email Anda

def check_vps_status():
    try:
        response = requests.get(VPS_URL, timeout=10)
        response.raise_for_status()
        print("VPS is up and running!")
    except requests.RequestException:
        print("VPS is down!")
        send_email_notification("VPS Down", f"VPS at {VPS_URL} is down. Please check the server.")

def send_email_notification(subject, body):
    requests.post(
        EMAIL_API_URL,
        json={'subject': subject, 'body': body},
        headers={'Authorization': f'Bearer {EMAIL_API_KEY}'}
    )

if __name__ == "__main__":
    check_vps_status()
