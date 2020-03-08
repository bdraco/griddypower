"""Main module."""

LOAD_ZONES = ["LZ_HOUSTON", "LZ_WEST", "LZ_NORTH", "LZ_SOUTH"]

GETNOW_API_URL = "https://app.gogriddy.com/api/v1/insights/getnow"
DEFAULT_REQUEST_TIMEOUT = 15



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
        return await response.json()
