
# Tunisia Geographic API
This API provides a list of cities and regions for any governorate in Tunisia, as well as zip codes for all Tunisian governorates.

This API made with [FastApi](https://fastapi.tiangolo.com/)

# Getting Started:
## Local development

1. clone project
2. install the requirements
````console
pip install -r requirements.txt
````
3. Use [uvicorn](https://www.uvicorn.org/) to run the FastAPI app:

```console
uvicorn api.main:app --reload --port=8000
```

3. Click 'http://127.0.0.1:8000' in the terminal, which should open the website in a new tab.
4. Append /docs (swagger ui) or /redoc to see the documentation


# API ROUTES :

# /region_gover
The Region endpoint is a GET request that returns a dictionary of regions for a given governorate. The endpoint takes a `governorate` parameter, which is the name of the governorate for which the regions are being requested.

### Endpoint URL
```
 GET /region
  ```
### Parameters

governorate (required): The name of the governorate for which regions are being requested.

### Usage

The endpoint returns a JSON object with a dictionary of regions for the specified city. Each key in the dictionary is an integer that represents the region's position in the list, starting from 1. The value associated with each key is a string that represents the name of the region.

### Example of Usage
```
 http://127.0.0.1:8000/region_gover?gover=Ariana
  ```
### Example of Response

````
{
  "1": "Ariana Ville",
  "2": "Ettadhamen",
  "3": "Kalaat Landlous",
  "4": "La Soukra",
  "5": "Mnihla",
  "6": "Raoued",
  "7": "Sidi Thabet"
}
````
# /gover

The Gover endpoint is a GET request that returns the governorate for a given region. The endpoint takes a `region` parameter, which is the name of the region for which the governorate is being requested.

### Endpoint URL
```
 GET /gover
  ```
### Parameters

region (required): The name of the region for which the governorate is being requested.

### Usage
The endpoint returns a JSON object with a single value pair , and the value is a string representing the name of the governorate that the region belongs to.

### Example of Usage
```
  http://127.0.0.1:8000/gover?region=Ariana Ville

  ```

### Example of Response

````
[
"Ariana"
]
````

# /cities

The Cities endpoint is a GET request that returns a dictionary of cities for a given region. The endpoint takes a `region` parameter, which is the name of the region for which the cities are being requested.

### Endpoint URL
```
 GET /cities
  ```

### Parameters

region (required): The name of the region for which cities are being requested.

### Usage
The endpoint returns a JSON object with a dictionary of cities for the specified region. Each key in the dictionary is an integer that represents the city's position in the list, starting from 1. The value associated with each key is a string that represents the name of the city.

### Example of Usage

```
  http://127.0.0.1:8000/gover?region=Ariana Ville

  ```

### Example of Response

````
{
  "1": "Ariana",
  "2": "Borj El Baccouche",
  "3": "Centre Commercial Ikram",
                .
                .   
                .
  "33": "Résidence Kortoba",
  "34": "Riadh Landlous"
}
````

# /region_city

The Region-City endpoint is a GET request that returns the region for a given city. The endpoint takes a `city` parameter, which is the name of the city for which the region is being requested.

## Endpoint URL

### Endpoint URL
```
 GET /region_city
  ```

### Parameters
city (required): The name of the city for which the region is being requested.

### Usage 
The endpoint returns a JSON object with a single key-value pair, where the key is "region" and the value is a string representing the name of the region that the city belongs to.

### Example of Usage


```
  http://127.0.0.1:8000/region_city?city=Cité Belvedere 2
  ```
### Example of Response

````
[
"Ariana Ville"
]
````

# /gover_city

The Gover-City endpoint is a GET request that returns the governorate for a given city. The endpoint takes a `city` parameter, which is the name of the city for which the governorate is being requested.

### Endpoint URL

```
  GET /gover_city
  ```

### Parameters

city (required): The name of the city for which the governorate is being requested.


### Usage 
The endpoint returns a JSON object with a single value pair, representing the name of the governorate that the city belongs to.

### Example of Usage

```
  http://127.0.0.1:8000/region_city?city=Cité Belvedere 2
  ```

### Example of Response

````
[
"Ariana"
]
````

# /zip_city

The Zip-City endpoint is a GET request that returns the zip code for a given city. The endpoint takes a ``city`` parameter, which is the name of the city for which the zip code is being requested. Additionally, it can also take an optional ``region`` and ``governorate`` parameter.
### Parameters

city (required): The name of the city for which the zip is being requested. <br>
region (optional): The name of the region to which the city belongs. <br>
governorate (optional): The name of the governorate to which the region belongs.

### Usage

The endpoint returns a JSON object with a single key-value pair, representing the key `zip` and value `zip code` of the city that was requested.
If both ``region`` and ``governorate`` parameters are provided, the endpoint returns the zip code of the city in that specific region and governorate. If only ``region`` parameter is provided, the endpoint returns the zip code of the city in that specific region, and if ``governorate`` is not provided, the endpoint tries to determine the governorate of the region and returns the zip code of the city.

### Example of Usage

```
  http://127.0.0.1:8000/region_city?city=Cité Belvedere 2
  ```
### Example of Usage with optionals

```
http://127.0.0.1:8000/zip_city?city=Cité du Jardin&region=Ariana Ville&governorate=Ariana
  ```



### Example of Response

````
{
  "zip": "2080"
}
````

# /cities_zip

The Cities-Zip endpoint is a GET request that returns the cities/city for a given zip code. The endpoint takes a `zip_code` parameter, which is the zip code for which the cities are being requested.

## Parameters

zip_code (required): The zip code for which the cities/city are being requested.

## Usage

The endpoint returns a JSON object with a single key-value pair, representing the key `number` and value `city` of the zip code that was requested.

## Example of Usage

````
  http://127.0.0.1:8000/cities_zip?zip=2080
````

## Example of Response 

```
{
  "1": "Ariana",
  "2": "Cité des Roses",
  "3": "Cité du Jardin",
  "4": "Cité du Printemps",
  "5": "Cité Ennouzha",
  "6": "Cité Essaada (ariana)",
  "7": "Cité Jaafar",
  "8": "Nouvelle Ariana",
  "9": "Résidence Ennour (ariana)"
}

```
# /region_zip

The Region-Zip endpoint is a GET request that returns the region of a zip code. The endpoint takes a `zip_code` parameter, which is the zip code for which the region is being requested.

## Parameters

zip_code (required): The zip code for which the region is being requested.

## Usage

The endpoint returns a JSON object with a single value pair, representing the region name of the zip code that was requested.

## Example of Usage

````
http://127.0.0.1:8000/region_zip?zip=2080
````
## Example of Response 

```
"Ariana Ville"
```

# /gover_zip

The gover-Zip endpoint is a GET request that returns the governorate of a zip code. The endpoint takes a `zip_code` parameter, which is the zip code for which the governorate is being requested.

## Parameters

zip_code (required): The zip code for which the governorate is being requested.

## Usage

The endpoint returns a JSON object with a single value pair, representing the governorate name of the zip code that was requested.

## Example of Usage

````
http://127.0.0.1:8000/gover_zip?zip=2080
````
## Example of Response 

```
"Ariana"
```

## /cityzip_region

The CityZip-Region endpoint is a GET request that returns the zip codes and cities within a given region. The endpoint takes a ``region`` parameter, which is the name of the region for which the zip codes and cities are being requested.

## Parameters

region (required): The name of the region for which the zip codes and cities are being requested.

## Usage

The endpoint returns a JSON object with key-value pairs, where the keys are integers and the values are dictionaries containing the city and corresponding zip code for each entry. The endpoint provides the zip codes and cities within the specified region.

## Example of Usage


````
http://127.0.0.1:8000/cityzip_region?region=Ariana Ville
````

## Example of Response 

```
{
  "1": {
    "Ariana": "2080"
  },
  "2": {
    "Borj El Baccouche": "2037"
  },
  "3": {
    "Centre Commercial Ikram": "2037"
  },
  "4": {
    "Cité Belvedere 2": "2091"
  },
  "5": {
    "Cité Borj Turki 1": "2058"
  },
  "6": {
    "Cité Borj Turki 2": "2058"
  },
  "7": {
    "Cité des Roses": "2080"
  },
  "8": {
    "Cité du Jardin": "2080"
  },
  "9": {
    "Cité du Printemps": "2080"
  },
```

# /details_gover


The Details-Gover endpoint is a GET request that returns the all details of a specified governing area (regions , cities , zip codes ). The endpoint takes a ``governorate`` parameter, which is the name of the governing area for which the details are being requested.

## Parameters

governorate (required): The name of the governorate for which regions are being requested.

## Usage

The endpoint returns a JSON object representing the details of the specified governing area. The endpoint provides information on the regions, cities, and zip codes within the specified governing area.

## Example of Usage

```
http://127.0.0.1:8000/details_gover?gover=Beja
```

## Example of Response

````
{
  "Amdoun": {
    "Adailia": {
      "zip": "9030"
    },
    "Ain El Goussa": {
      "zip": "9030"
    },
    "Ain Ghenem": {
      "zip": "9030"
    }
  }
}
````
