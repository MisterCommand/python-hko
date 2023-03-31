[![GitHub Release][releases-shield]][releases]
[![PyPI][pypi-releases-shield]][pypi-releases]

# python-hko
A python warpper for retrieving Hong Kong SAR local weather from Hong Kong Observatory Open Data API.
Please refer to the Official Documentation for request parameters and response details.
[Official API Documentation][hko-documentation]

## Reference
### HKO Module
`hko.HKO(session)`
Manage and perform requests
Return: hko.HKO class

Parameter | Optional (default value) | Type | Description
--- | --- | --- | ---
session | no | ClientSession | see [aiohttp](https://docs.aiohttp.org/en/stable/client_reference.html)

`hko.HKO.weather(dataType, lang)`
Retrieve weather data from Weather Information API
Return: dictionary

Parameter | Optional (default value) | Type | Description
--- | --- | --- | ---
dataType | no | string | type of data requested
lang | yes (en) | string | language used in response

`hko.HKO.earthquake(dataType, lang)`
Retrieve weather data from Earthquake Information API
Return: dictionary

Parameter | Optional (default value) | Type | Description
--- | --- | --- | ---
dataType | no | string | type of data requested
lang | yes (en) | string | language used in response

`hko.HKO.openData(dataType, lang)`
Retrieve weather data from Earthquake Information API
Return: dictionary

Parameter | Optional (default value) | Type | Description
--- | --- | --- | ---
dataType | no | string | type of data requested
lang | yes (en) | string | language used in response
station | - | string | refer to [Official API Documentation][hko-documentation]
year | - | string | refer to [Official API Documentation][hko-documentation]
month | - | string |refer to [Official API Documentation][hko-documentation]
day | - | string | refer to [Official API Documentation][hko-documentation]
hour | - | string | refer to [Official API Documentation][hko-documentation]


## Usage Example
Get and print local weather forcast general situation in English
```python
from hko import HKO, HKOError
import asyncio
from aiohttp import ClientSession
from aiohttp import ClientConnectorError

async def main():
    async with ClientSession() as session:
        try:
            hko = HKO(session)
            fnd = await hko.weather(dataType="fnd")
            print(fnd["generalSituation"])
        except HKOError as error:
            print(error)

asyncio.run(main())
```





[hko-documentation]: https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf
[releases]: https://github.com/MisterCommand/python-hko
[releases-shield]: https://img.shields.io/github/release/MisterCommand/python-hko.svg?style=popout
[pypi-releases]: https://pypi.org/project/hko/
[pypi-releases-shield]: https://img.shields.io/pypi/v/hko