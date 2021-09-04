# python-hko
A python warpper for getting Hong Kong SAR local weather from Hong Kong Observatory Open Data API.
Please refer to the Official Documentation for request parameters and response details.
[Official Documentation](https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf)

## Usage Example
`
from hko import HKO
import asyncio
from aiohttp import ClientSession, ClientResponse
from aiohttp import ClientConnectorError

async def main():
    async with ClientSession() as websession:
        try:
            hko = HKO(websession)
            fnd = await hko.get("fnd")
        except ClientConnectorError as error:
            print(error)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
`