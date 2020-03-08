#!/usr/bin/env python

"""Tests for `griddypower` package."""

import datetime
import os
import aiounittest

from aiohttp import ClientError, ClientSession
from aioresponses import aioresponses

from griddypower.async_api import GETNOW_API_URL, AsyncGriddy, LOAD_ZONES


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path) as fptr:
        return fptr.read()


class TestApiAsync(aiounittest.AsyncTestCase):
    @aioresponses()
    async def test_async_getnow(self, aiomock):
        """Test for parsing getnow into objects."""
        aiomock.post(GETNOW_API_URL, body=load_fixture("getnow.json"))

        griddy = AsyncGriddy(ClientSession(), settlement_point=LOAD_ZONES[0])
        data = await griddy.async_getnow()
        assert data.now.price_cents_kwh == "1.26900000000000000000"
        assert data.now.price_type == "lmp"
        assert data.now.datetime == datetime.datetime(
            2020, 3, 8, 18, 10, 16, tzinfo=datetime.timezone.utc
        )

        assert data.forecast[0].price_cents_kwh == "1.32000000"
        assert data.forecast[0].price_type == "dam"
        assert data.forecast[0].datetime == datetime.datetime(
            2020, 3, 8, 19, 0, tzinfo=datetime.timezone.utc
        )
