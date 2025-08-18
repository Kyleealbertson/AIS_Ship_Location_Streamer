import asyncio
import websockets
import json
from datetime import datetime, timezone
from Config.config import S

async def connect_ais_stream(MessageTypeChoice: str="PositionReport"):

    async with websockets.connect(S.ais_api_url) as websocket:
        subscribe_message = {"APIKey": S.ais_api_key,
                              "BoundingBoxes": [[[-180, -90], [180, 90]]],
                             #"FiltersShipMMSI": ["368207620", "367719770", "211476060"], # Optional!
                             "FilterMessageTypes": [MessageTypeChoice]} 

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)
        print("Connected and waiting for data...")
        async for message_json in websocket:
            message = json.loads(message_json)

            message_type = message["MessageType"]

            if message_type == MessageTypeChoice:
                print(message)
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message'][MessageTypeChoice]
                print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Latitude: {ais_message['Longitude']}")

if __name__ == "__main__":
    asyncio.run((connect_ais_stream(MessageTypeChoice="PositionReport")))