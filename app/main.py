# main.py
import asyncio
from typing import Optional, Dict, Any
import ais_stream_producer
from trasform_enrich import ais_stream_enrich_and_filter

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
