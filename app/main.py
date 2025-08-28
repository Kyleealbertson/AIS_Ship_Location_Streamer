# main.py
import asyncio
import sys
from typing import Optional, Dict, Any
from ais_stream_producer import AISStreamProducer
from ais_stream_enrich_and_filter import ais_stream_enrich_and_filter

async def run_demo(max_print: int = 100) -> None:
    printed = 0
    async for raw in AISStreamProducer.ais_stream_producer("PositionReport"):
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
