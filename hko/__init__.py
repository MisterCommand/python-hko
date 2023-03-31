__version__ = '0.2.0'

import logging
from aiohttp import ClientSession
from typing import Dict

_LOGGER = logging.getLogger(__name__)

class HKOError(Exception):
    pass

class HKO:
    """Main class to communicate with the HKO API."""

    def __init__(self, session: ClientSession):
        self._session = session

    async def _request(self, url:str) -> Dict:
        """Retreive data from HKO API"""
        async with self._session.get(url) as response:
            if response.status != 200:
                raise HKOError("Cannot connect to HKO API")
            try:
                content = await response.json()
            except Exception as e:
                raise HKOError(f"HKO API Error: {e}")
            return content

    async def weather(self, dataType:str, lang:str="en") -> Dict:
        """Weather Information"""
        data = await self._request(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang={lang}")
        return data

    async def earthquake(self, dataType:str, lang:str="en") -> Dict:
        """Earthquake Information"""
        data = await self._request(f"https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php?dataType={dataType}&lang={lang}")
        return data

    async def openData(self, dataType:str, lang:str="en", station:str=None, year:int=None, month:int=None, day:int=None, hour:int=None) -> Dict:
        """Open Data"""
        base_url = f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType={dataType}&rformat=json&lang={lang}&"
        params = {}
        if station is not None:
            params["station"] = station
        if year is not None:
            params["year"] = year
        if month is not None:
            params["month"] = month
        if day is not None:
            params["day"] = day
        if hour is not None:
            params["hour"] = hour
        if params:
            url = base_url + "&".join(f"{k}={v}" for k, v in params.items())
        else:
            url = base_url
        data = await self._request(url)
        return data