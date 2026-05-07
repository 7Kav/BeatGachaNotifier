import websocket-client
from time import sleep
import msgpack
from os import getenv
import asyncio
import io

from requests import api

url = "https://beatgacha.com"

def authenticate(username: str, password: str):
    api_key = getenv("API_KEY")
    if api_key is None:
        raise Exception("API key not set")
    else:
        return api_key

headers = {
    "x-api-key": getenv("API_KEY"),
    "x-user-id": getenv("USER_ID"),
}

ws = websocket.WebSocket()
ws.connect(url, headers=headers)
ws.send(url, headers=headers, "join_room", "pack_given")
def CardPackNotify(ws, url, headers):
    try:
        while True:
            sleep(30)


            msg = ws.recv()


    except exit:
        ws.close()
        print("Connection closed")
    except KeyboardInterrupt:
        ws.close()
        print("Connection closed")
        print("Graceful shutdown")
        exit()