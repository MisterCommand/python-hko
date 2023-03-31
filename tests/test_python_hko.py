from hko import __version__


import pytest
from hko import HKO, HKOError
import asyncio
from aiohttp import ClientSession

def test_version():
    assert __version__ == '0.3.2'

# WEATHER
class TestWeather:
    @pytest.mark.asyncio
    async def test_weather(self):
        async with ClientSession() as session:
            hko = HKO(session)
            assert "generalSituation" in await hko.weather("flw")

    @pytest.mark.asyncio
    async def test_invalid_dataType(self):
        with pytest.raises(HKOError):
            async with ClientSession() as session:
                hko = HKO(session)
                return await hko.weather("a")


# EARTHQUAKE
class TestEeathquake:
    @pytest.mark.asyncio
    async def test_earthquake(self):
        async with ClientSession() as session:
            hko = HKO(session)
            assert "updateTime" in await hko.earthquake("qem")

    @pytest.mark.asyncio
    async def test_invalid_dataType(self):
        with pytest.raises(HKOError):
            async with ClientSession() as session:
                hko = HKO(session)
                return await hko.earthquake("a")
            

# OPEN DATA
class TestOpenData:
    @pytest.mark.asyncio
    async def test_open_data_HHOT(self):
        """Valid case: HHOT"""
        async with ClientSession() as session:
            hko = HKO(session)
            assert "fields" in await hko.openData(dataType="HHOT", lang="en", station="CCH", year=2022)

    @pytest.mark.asyncio
    async def test_invalid_dataType(self):
        with pytest.raises(HKOError):
            async with ClientSession() as session:
                hko = HKO(session)
                return await hko.openData("a")