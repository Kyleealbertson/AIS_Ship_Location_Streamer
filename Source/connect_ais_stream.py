import asyncio
import websockets
import json
from datetime import datetime, timezone

async def connect_ais_stream(MessageTypeChoice: str="PositionReport"):

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "a07afc829e58c75ca32938ee0951ed37c5bf8509",
                             "BoundingBoxes": [[[-93, 41], [-75, 50]]],  # Required !
                             #"FiltersShipMMSI": ["368207620", "367719770", "211476060"], # Optional!
                             "FilterMessageTypes": [MessageTypeChoice]} 

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)
        print("Connected and waiting for data...")
        async for message_json in websocket:
            message = json.loads(message_json)

            '''if "MessageType" not in message:
                print("Non-data message:", message)
                continue'''
            message_type = message["MessageType"]

            if message_type == MessageTypeChoice:
                print(message)
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message'][MessageTypeChoice]
                print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Latitude: {ais_message['Longitude']}")

if __name__ == "__main__":
    asyncio.run((connect_ais_stream()))