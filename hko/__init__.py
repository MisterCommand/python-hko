__version__ = '0.1.0'

import json
import logging
from aiohttp import ClientSession, ClientResponse
from typing import Dict

_LOGGER = logging.getLogger(__name__)

class HKO:
    """Main class to communicate with the HKO API."""

    def __init__(self, session: ClientSession):
        self._session = session

    async def _request(self, url:str) -> Dict:
        """Retreive data from HKO API"""
        async with self._session.get(url) as response:
            return await response.json()

    async def weather(self, dataType, lang = "en") -> Dict:
        """Get data"""
        data = await self._request(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang={lang}")
        return data