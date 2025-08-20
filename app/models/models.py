from typing import TypedDict, Optional

class RawAIS(TypedDict, total=False):
    # adapt to your vendor’s message format
    mmsi: int
    shipid: int
    ship_name: str
    ts: float          # epoch seconds
    lat: float
    lon: float
    sog: float         # speed over ground
    cog: float         # course over ground
    heading: Optional[float]
    ship_type: Optional[str]

class Canonical(TypedDict, total=False):
    mmsi: int
    shipid: int
    ship_name: Optional[str]
    ts: int            # integer epoch seconds
    lat: float
    lon: float
    sog: float
    cog: float
    ship_type: Optional[str]
    area: Optional[str]
