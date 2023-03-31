__version__ = '0.3.2'

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


LOCATIONS = [
    {"LOCATION": "Hong Kong Observatory", "DISTRICT": "Yau Tsim Mong"},
    {"LOCATION": "King's Park", "DISTRICT": "Yau Tsim Mong"},
    {"LOCATION": "Wong Chuk Hang", "DISTRICT": "Southern District"},
    {"LOCATION": "Ta Kwu Ling", "DISTRICT": "North District"},
    {"LOCATION": "Lau Fau Shan", "DISTRICT": "Yuen Long"},
    {"LOCATION": "Tai Po", "DISTRICT": "Tai Po"},
    {"LOCATION": "Sha Tin", "DISTRICT": "Sha Tin"},
    {"LOCATION": "Tuen Mun", "DISTRICT": "Tuen Mun"},
    {"LOCATION": "Tseung Kwan O", "DISTRICT": "Sai Kung"},
    {"LOCATION": "Sai Kung", "DISTRICT": "Sai Kung"},
    {"LOCATION": "Cheung Chau", "DISTRICT": "Southern District"},
    {"LOCATION": "Chek Lap Kok", "DISTRICT": "Tuen Mun"},
    {"LOCATION": "Tsing Yi", "DISTRICT": "Kwai Tsing"},
    {"LOCATION": "Shek Kong", "DISTRICT": "Yuen Long"},
    {"LOCATION": "Tsuen Wan Ho Koon", "DISTRICT": "Tsuen Wan"},
    {"LOCATION": "Tsuen Wan Shing Mun Valley", "DISTRICT": "Tsuen Wan"},
    {"LOCATION": "Hong Kong Park", "DISTRICT": "Central & Western District"},
    {"LOCATION": "Shau Kei Wan", "DISTRICT": "Eastern District"},
    {"LOCATION": "Kowloon City", "DISTRICT": "Kowloon City"},
    {"LOCATION": "Happy Valley", "DISTRICT": "Wan Chai"},
    {"LOCATION": "Wong Tai Sin", "DISTRICT": "Wong Tai Sin"},
    {"LOCATION": "Stanley", "DISTRICT": "Southern District"},
    {"LOCATION": "Kwun Tong", "DISTRICT": "Kwun Tong"},
    {"LOCATION": "Sham Shui Po", "DISTRICT": "Sham Shui Po"},
    {"LOCATION": "Kai Tak Runway Park", "DISTRICT": "Kowloon City"},
    {"LOCATION": "Yuen Long Park", "DISTRICT": "Yuen Long"},
    {"LOCATION": "Tai Mei Tuk", "DISTRICT": "Tai Po"},
]