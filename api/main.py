import random
import fastapi
import data

import sys

print(sys.path)

app = fastapi.FastAPI()
db = data.data





@app.get("/region")
async def region(ville: str):
    print(ville)
    ville_list = (db[ville]['region2'].keys())
    dict={
    }
    for i, item in enumerate(ville_list):
        dict[i + 1] = item
    return dict
