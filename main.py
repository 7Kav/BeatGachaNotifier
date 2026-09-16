import http
import sys, subprocess
from time import sleep
from os import getenv


# Set to "True" If you don't need the download

Skipdownload = True
if Skipdownload == False:
    try:
        print("Attempting Dependency install")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("ERROR")
        print("Dependancy install failed. Please try again or run this command below")
        print("pip install -m -r requirements.txt")
        sys.exit()

from dotenv import load_dotenv
import requests
load_dotenv()


url = "https://beatgacha.com/api/auth/me"

api_key = getenv("API_KEY")
if api_key is None or api_key == "":
    raise Exception("API key not set")

userID = getenv("USER_ID")

headers = {
    "accept": "application/json",
    "x-api-key": api_key,
    "x-user-id": userID,
}

ShardCount = 0
CardCount = 0


def CardPackNotify():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()

        username = data['user']['username']
        ShardCount = f"{data['user']['card_shards']}"
        CardCount = f"{data['user']['current_packs']} / {data['user']['max_packs']}"

        return username, CardCount, ShardCount
    except requests.exceptions.HTTPError == 404 as e:
        if e.response.status_code == 404:
            print("Data not found...?")
        elif e.response.status_code == 401:
            print("Access Denied.")
            print("Did you enter both your API key and User ID?")
        elif e.response.status_code == 405:
            print("This shouldnt happen. Please report to the github repo.")
        elif e.response.status_code == 500:
            print("A server error occurred!")
            print("Please check the BeatGacha Discord for any status updates!")
        else:
            print("A HTTP Exception occured when grabbing data!")
            print(e)
        return None, 0, 0
    except requests.exceptions.Timeout as e:
        print("Timeout Occured!")
        print("No data was gathered")
        return None, 0, 0
    except requests.exceptions.ConnectionError as e:
        print("Connection Error!")
        print("Check your internet connection and try again")
        return None, 0, 0
    except Exception as e:
        print(e)
        return 0, 0

username, CardCount, ShardCount = CardPackNotify()

print(username)
print(f"CardCount: {CardCount}")
print(f"ShardCount: {ShardCount}")
