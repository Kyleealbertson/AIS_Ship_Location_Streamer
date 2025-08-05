import asyncio
import websockets
import json
from datetime import datetime, timezone

async def connect_ais_stream():

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "a07afc829e58c75ca32938ee0951ed37c5bf8509",  # Required !
                             "BoundingBoxes": [[[-92.951985,41.278138],[-75.681477,49.482688]]], # Required!
                             #"FiltersShipMMSI": ["368207620", "367719770", "211476060"], # Optional!
                             "FilterMessageTypes": ["PositionReport"]} 

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)
        print("Connected and waiting for data...")
        async for message_json in websocket:
            message = json.loads(message_json)

            if "MessageType" not in message:
                print("Non-data message:", message)
                continue
            message_type = message["MessageType"]

            if message_type == "PositionReport":
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message']['PositionReport']
                print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Latitude: {ais_message['Longitude']}")

if __name__ == "__main__":
    asyncio.run((connect_ais_stream()))