__version__ = '0.1.0'

from aiohttp import ClientSession, ClientResponse

class Rhrread:
    """Class that represents a weather object in the HKO API."""

    def __init__(self, data: dict):
        self.data = data
    
    @property
    def temperature(self):
        """Return tempertures"""
        return [Temperature(item) for item in self.data["temperature"]["data"]]

class Temperature:
    """Class that represents a temperature object in the HKO API."""

    def __init__(self, data: dict):
        self.data = data
    
    @property
    def place(self) -> str:
        """Return place"""
        return self.data["place"]

    @property
    def value(self) -> int:
        """Return value"""
        return self.data["value"]
        
    @property
    def unit(self) -> str:
        """Return unit"""
        return self.data["unit"]


class HKO:
    """Class to communicate with the HKO API."""

    def __init__(self, websession: ClientSession):
        self.websession = websession

    async def request(self, url:str) -> ClientResponse:
        return await self.websession.request("get", url)

    async def async_get_rhrread(self) -> Rhrread:
        response = await self.request("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en")
        return Rhrread(await response.json())