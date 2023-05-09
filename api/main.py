import fastapi
import data
from typing import Optional

app = fastapi.FastAPI()
db = data.data


def find_parent(child):
    for governorate in db:
        if db[governorate].get(child):
            return governorate


def find_children(mother):
    up = find_parent(mother)
    return db[up][mother].keys()


def find_child(mother, child):
    up = find_parent(mother)
    return db[up][mother].get(child)


def get_region_by_city(city):
    for governorate in db:
        for region in db[governorate]:
            if find_child(region, city):
                return region


def get_gover_by_city(city):
    if get_region_by_city(city) is not None:
        region = get_region_by_city(city)
        governorate = find_parent(region)
        return governorate


def zip_by_city(city):
    code = None
    if get_region_by_city(city) is not None:
        region = get_region_by_city(city)
        governorate = find_parent(region)
        code = db[governorate][region][city]["zip"]
    return {"zip": code}


def get_cities_by_zip(zip_code):
    i = 0
    dictionary = {}
    for governorate in db:
        for region in db[governorate]:
            for city in find_children(region):
                g = governorate
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip_code:
                    i += 1
                    dictionary[i] = city

    return dictionary


def get_region_by_zip(zip_code):
    for governorate in db:
        for region in db[governorate]:
            for city in find_children(region):
                g = governorate
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip_code:
                    return region


def get_gover_by_zip(zip_code):
    for governorate in db:
        for region in db[governorate]:
            for city in find_children(region):
                g = governorate
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip_code:
                    return governorate


@app.get("/")
async def all_data():
    return db


@app.get("/details_gover")
async def details_gover(governorate: str):
    return db[governorate]


@app.get("/cityzip_region")
async def cityzip_region(region: str):
    governorate = find_parent(region)
    dictionary = {}

    for i, item in enumerate(db[governorate][region]):
        dictionary[i + 1] = {item: db[governorate][region][item]["zip"]}
    return dictionary


@app.get("/gover_zip")
async def gover_zip(zip_code: str):
    return get_gover_by_zip(zip_code)


@app.get("/region_zip")
async def region_zip(zip_code: str):
    return get_region_by_zip(zip_code)


@app.get("/cities_zip")
async def cities_zip(zip_code: str):
    return get_cities_by_zip(zip_code)


@app.get("/zip_city")
async def zip_city(city: str, region: Optional[str] = None, governorate: Optional[str] = None):
    if region is not None:
        if governorate is not None:
            return {"zip": db[governorate][region][city]["zip"]}
        else:
            governorate = find_parent(region)
            return {"zip": db[governorate][region][city]["zip"]}
    else:
        return zip_by_city(city)


@app.get("/region_gover")
async def region_gover(governorate: str):
    region_list = (db[governorate].keys())
    dictionary = {}
    for i, item in enumerate(region_list):
        dictionary[i + 1] = item
    return dictionary


@app.get("/gover")
async def gover(region: str):
    governorat = find_parent(region)
    return {governorat}


@app.get("/cities")
async def cities(region: str):
    cities_list = find_children(region)
    dictionary = {}
    for i, item in enumerate(cities_list):
        dictionary[i + 1] = item
    return dictionary


@app.get("/region_city")
async def region_city(city: str):
    return {get_region_by_city(city)}


@app.get("/gover_city")
async def gover_city(city: str):
    return {get_gover_by_city(city)}


@app.get("/city_zip")
async def city_zip(zip_code: str):
    return get_cities_by_zip(zip_code)
