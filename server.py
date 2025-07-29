import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/principalapis/api/universities-and-colleges'

mcp = FastMCP('universities-and-colleges')

@mcp.tool()
def universities(page: Annotated[Union[int, float, None], Field(description='Default is 0. Default: 20')] = None,
                 includeUniversityDetails: Annotated[Union[bool, None], Field(description='Include additional university details such as school colors, mascot, website, address, and more. Including details costs $0.01. Default value is false.')] = None,
                 countryCode: Annotated[Union[str, None], Field(description='Ex/ US')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='Default is 10. Max page size 50. Default: 10')] = None,
                 search: Annotated[Union[str, None], Field(description='Filter results by searching / autocompleting the name value.')] = None) -> dict: 
    '''Retrieve a list of universities'''
    url = 'https://universities-and-colleges.p.rapidapi.com/universities'
    headers = {'x-rapidapi-host': 'universities-and-colleges.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
        'includeUniversityDetails': includeUniversityDetails,
        'countryCode': countryCode,
        'limit': limit,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def university_details_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieve a single university by ID. Automatically includes any available University details (University details cost $0.01 if additional details like school colors, mascot, website, address, and more are present in response).'''
    url = 'https://universities-and-colleges.p.rapidapi.com/universities-by-id'
    headers = {'x-rapidapi-host': 'universities-and-colleges.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")
