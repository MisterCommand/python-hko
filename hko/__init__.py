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

    async def _get_data(self, url:str) -> Dict:
        """Retreive data from HKO API"""
        async with self._session.get(url) as response:
            if response.status != 200:
                error_text = json.loads(await response.text())
            return await response.json()

    async def get_rhrread(self) -> Dict:
        """Retreive rhrread data from HKO API"""
        data = await self._get_data("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en")
        return data

    async def get_fnd(self) -> Dict:
        """Retreive fnd data from HKO API"""
        data = await self._get_data("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en")
        return data