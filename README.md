# griddypower
Python API for Griddy Wholesale Electricity

Example
```
import pprint
import asyncio
import aiohttp

from griddypower.async_api import AsyncGriddy

async def main():
	websession = aiohttp.ClientSession()
	data = await AsyncGriddy(
	    websession, settlement_point="LZ_HOUSTON"
 	).async_getnow()
        pprint.pprint(["The current power price for Load Zone LZ_HOUSTON", data.now.price_cents_kwh])
        await websession.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

['The current power price for Load Zone LZ_HOUSTON', '1.15000000000000000000']

