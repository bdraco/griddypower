"""Main module."""

import dateutil.parser
import datetime

LOAD_ZONES = ["LZ_HOUSTON", "LZ_WEST", "LZ_NORTH", "LZ_SOUTH"]

GETNOW_API_URL = "https://app.gogriddy.com/api/v1/insights/getnow"
DEFAULT_REQUEST_TIMEOUT = 15


class GriddyPriceData:
    """Griddy price data."""

    def __init__(self, data):
        self._now = GriddyPricePoint(data["now"])
        self._forecast = []
        for price_point in data["forecast"]:
            self._forecast.append(GriddyPricePoint(price_point))

    @property
    def now(self):
        return self._now

    @property
    def forecast(self):
        return self._forecast


class GriddyPricePoint:
    """Object that represents griddy price data for a specific date time."""

    def __init__(self, data):
        self._price_ckwh = data["price_ckwh"]
        self._price_type = data["price_type"]
        self._datetime = as_utc_from_local(dateutil.parser.parse(data["date"]))

    @property
    def datetime(self):
        return self._datetime

    @property
    def price_cents_kwh(self):
        return self._price_ckwh

    @property
    def price_type(self):
        return self._price_type


class AsyncGriddy:
    """Async griddy api."""

    def __init__(
        self, websession, timeout=DEFAULT_REQUEST_TIMEOUT, settlement_point=None,
    ):
        """Create griddy async api object."""
        self._websession = websession
        self._settlement_point = settlement_point
        self._timeout = timeout

    async def async_getnow(self):
        """Call api to get the current price."""
        response = await self._websession.request(
            "post",
            GETNOW_API_URL,
            timeout=self._timeout,
            json={"settlement_point": self._settlement_point},
        )
        return GriddyPriceData(await response.json())


def as_utc_from_local(dtime):
    """Converts the datetime returned from an activity to UTC."""
    return dtime.astimezone(tz=datetime.timezone.utc)
