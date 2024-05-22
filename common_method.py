import json
import requests

global CONFIG
global SETTING

def load_config():
    with open("config.json", 'r') as file:
        global CONFIG
        CONFIG = json.load(file)

def get_setting_json_server():
    try:
        json_server_ip = CONFIG["jsonServerIp"]
        json_server_port = CONFIG["jsonServerPort"]
        channel_number = CONFIG["channelNumber"]

        response = requests.get(f"http://{json_server_ip}:{json_server_port}/{channel_number}")
        response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생

        data = response.json()

        global SETTING
        SETTING = data["ai"]
    except Exception as e:
        print(f"setting-json-server get 오류 발생: {e}")