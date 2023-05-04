import random
import fastapi
import data

import sys

print(sys.path)

app = fastapi.FastAPI()
db = data.data


def find_parent(tree, child):
    for gover in tree:
        if db[gover].get(child):
            return gover
    return 0


@app.get("/region")
async def region(ville: str):
    ville_list = (db[ville].keys())
    dict = {
    }
    for i, item in enumerate(ville_list):
        dict[i + 1] = item
    return dict


@app.get("/gover")
async def gover(region: str):
    governorat = find_parent(db, region)
    return {governorat}


