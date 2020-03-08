#!/usr/bin/env python

"""Tests for `griddypower` package."""

import pytest
import asynctest

from aiohttp import ClientError, ClientSession
from aioresponses import aioresponses

from griddypower import griddypower


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path) as fptr:
        return fptr.read()


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


@aioresponses()
async def test_async_getnow(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
