__version__ = '0.1.0'

import logging
import json
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
                content = json.loads(response)
            except Exception as e:
                raise HKOError("HKO API Error")
            return content

    async def weather(self, dataType, lang = "en") -> Dict:
        """Get data"""
        data = await self._request(f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang={lang}")
        return data