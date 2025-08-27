# main.py
import asyncio
import sys
sys.path.append("/Users/kyle_albertson/AIS_Ship_Location_Streamer/app")
from typing import Optional, Dict, Any
import ais_stream_producer
import ais_stream_enrich_and_filter  # Import the missing function

async def run_demo(max_print: int = 10) -> None:
    printed = 0
    async for raw in ais_stream_producer("PositionReport"):
        canon = await ais_stream_enrich_and_filter(raw)
        if canon is None:
            continue
        print(canon)
        printed += 1
        if printed >= max_print:
            print(f"...printed {printed} canonical messages; stopping demo.")
            break

if __name__ == "__main__":
    asyncio.run(run_demo())
