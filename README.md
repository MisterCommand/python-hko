[![GitHub Release][releases-shield]][releases]
[![PyPI][pypi-releases-shield]][pypi-releases]

# python-hko
A python warpper for getting Hong Kong SAR local weather from Hong Kong Observatory Open Data API.
Please refer to the Official Documentation for request parameters and response details.
[Official API Documentation][hko-documentation]

## Reference
### HKO Module
`hko.HKO(websession)`
Manage and perform requests
Return: hko.HKO class

Parameter | Optional | Type | Description
--- | --- | --- | ---
websession | no | ClientSession | see [aiphttp](https://docs.aiohttp.org/en/stable/client_reference.html)

`hko.HKO.weather(type, lang="en")`
Retrieve weather data from Weather Information API
Return: dictionary

Parameter | Optional | Type | Description | Accepted values
--- | --- | --- | --- | ---
dataType | no | string | type of data requested | see [Official API Documentation][hko-documentation]
lang | yes | string| language used in response | see [Official API Documentation][hko-documentation]

## Usage Example
Get and print local weather forcast general situation in English
```python
from hko import HKO
import asyncio
from aiohttp import ClientSession, ClientResponse
from aiohttp import ClientConnectorError

async def main():
    async with ClientSession() as websession:
        try:
            hko = HKO(websession)
            fnd = await hko.weather("fnd")
            print(fnd["generalSituation"])
        except ClientConnectorError as error:
            print(error)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```





[hko-documentation]: https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf
[releases]: https://github.com/MisterCommand/python-hko
[releases-shield]: https://img.shields.io/github/release/MisterCommand/python-hko.svg?style=popout
[pypi-releases]: https://pypi.org/project/hko/
[pypi-releases-shield]: https://img.shields.io/pypi/v/hko