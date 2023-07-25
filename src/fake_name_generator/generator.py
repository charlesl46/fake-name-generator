from bs4 import BeautifulSoup
import aiohttp
import asyncio
from enum import Enum

class NameSet(Enum):
    FRENCH = "fr"
    ENGLISH = "en"
    UNITED_STATES = "us"
    ARABIC = "ar"
    AUSTRALIA = "au"
    BRAZIL = "br"
    CHECHEN = "celat"
    CHINA = "ch"
    CHINA_TRADITIONAL = "zhtw"
    CROATIA = "hr"
    CZECH_REPUBLIC = "cs"
    DENMARK = "dk"
    NETHERLANDS = "nl"
    ERITREA = "er"
    FINLAND = "fi"
    GERMANY = "gr"
    GREENLAND = "gl"
    SPAIN = "sp"
    HOBBIT = "hobbit"
    HUNGARY = "hu"
    ICELAND = "is"
    IGBO = "ig"
    ITALIAN = "it"
    JAPAN = "jpja"
    JAPAN_ANGLICIZED = "jp"
    KLINGON = "tlh"
    NINJA = "ninja"
    NORWAY = "no"
    PERSIAN = "fa"
    POLAND = "pl"
    RUSSIA = "ru"
    RUSSIA_CYRILLIC = "rucyr"
    SCOTLAND = "gd"
    SLOVENIA = "sl"
    SWEDEN = "sw"
    THAILAND = "th"
    VIETNAM = "vn"

class Gender(Enum):
    RANDOM = "random"
    MALE = "male"
    FEMALE = "female"

async def __fetch_data(url, session):
    async with session.get(url) as response:
        return await response.text()

async def async_get_random_names(gender : Gender = Gender.RANDOM,nameset : NameSet = NameSet.FRENCH,k : int = 1):
    urls = [
        f"https://www.fakenamegenerator.com/gen-{gender.value}-{nameset.value}-fr.php"
        for _ in range(k) 
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [__fetch_data(url, session) for url in urls]
        responses = await asyncio.gather(*tasks)

    for response_text in responses:
        soup = BeautifulSoup(response_text, "html.parser")
        print(soup.find("div", {"class": "address"}).find("h3").text)

def generate_random_names(gender : Gender = Gender.RANDOM,nameset : NameSet = NameSet.FRENCH,k : int = 1):
    asyncio.run(async_get_random_names(gender,nameset,k))

generate_random_names(k = 50)




