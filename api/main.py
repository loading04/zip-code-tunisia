# TODO get region by zip code
# TODO get governorat by zip code
# TODO get all city and zip by region
# TODO get all city and zip by governorat


import fastapi
import data


app = fastapi.FastAPI()
db = data.data


def find_parent(tree, child):
    for gover in tree:
        if db[gover].get(child):
            return gover
    return 0


def find_children(tree, mother):
    up = find_parent(tree, mother)
    return tree[up][mother].keys()


def find_child(tree, mother, child):
    up = find_parent(tree, mother)
    return tree[up][mother].get(child)


def get_region_by_city(city):
    for gover in db:
        for region in db[gover]:
            if find_child(db, region, city):
                return region


def get_gover_by_city(city):
    if get_region_by_city(city) is not None:
        region = get_region_by_city(city)
        gover = find_parent(db, region)
        return gover

def zip_by_city(city):
    if get_region_by_city(city) is not None:
        region = get_region_by_city(city)
        gover = find_parent(db, region)
        zip = db[gover][region][city]["zip"]
    return {"zip":zip}

def get_cities_by_zip(zip):
    i = 0
    dict = {}
    for gover in db:
        for region in db[gover]:
            for city in find_children(db, region):
                g = gover
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip:
                    i += 1
                    dict[i] = city

    return dict


def get_region_by_zip(zip):
    i = 0
    for gover in db:
        for region in db[gover]:
            for city in find_children(db, region):
                g = gover
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip:
                    return region

def get_gover_by_zip(zip):
    i = 0
    for gover in db:
        for region in db[gover]:
            for city in find_children(db, region):
                g = gover
                r = region
                c = city
                code = db[g][r][c]["zip"]
                if code == zip:
                    return gover




@app.get("/gover_zip")
async def gover_zip(zip: str):
    return get_gover_by_zip(zip)


@app.get("/region_zip")
async def region_zip(zip: str):
    return get_region_by_zip(zip)


@app.get("/cities_zip")
async def cities_zip(zip: str):
    return get_cities_by_zip(zip)

@app.get("/zip_city")
async def zip_city(city: str):
    return zip_by_city(city)

@app.get("/region_gover")
async def region_gover(gover: str):
    region_list = (db[gover].keys())
    dict = {}
    for i, item in enumerate(region_list):
        dict[i + 1] = item
    return dict


@app.get("/gover")
async def gover(region: str):
    governorat = find_parent(db, region)
    return {governorat}


@app.get("/cities")
async def cities(region: str):
    cities_list = find_children(db, region)
    dict = {}
    for i, item in enumerate(cities_list):
        dict[i + 1] = item
    return dict


@app.get("/region_city")
async def region_city(city: str):
    return {get_region_by_city(city)}


@app.get("/gover_city")
async def gover_city(city: str):
    return {get_gover_by_city(city)}


@app.get("/city_zip")
async def city_zip(zip: str):
    return get_cities_by_zip(zip)


