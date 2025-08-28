import asyncio
import websockets
import json
from datetime import datetime, timezone
from config.config import Settings

S = Settings()

class AISStreamProducer:
    async def ais_stream_producer(MessageTypeChoice: str="PositionReport"):

        async with websockets.connect(S.ais_api_url) as websocket:
            subscribe_message = {"APIKey": S.ais_api_key,
                                "BoundingBoxes": [[[-180, -90], [180, 90]]],
                                #"FiltersShipMMSI": ["368207620", "367719770", "211476060"], # Optional!
                                "FilterMessageTypes": [MessageTypeChoice]} 

            await websocket.send(json.dumps(subscribe_message))
            print("Connected and waiting for data...")

            async for message_json in websocket:
                try:
                    msg = json.loads(message_json)
                except Exception:
                    continue
                # You can optionally filter here too, but we'll forward all raw
                yield msg
                

