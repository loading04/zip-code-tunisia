
# Tunisia Geographic API
This API provides a list of cities and regions for any governorate in Tunisia, as well as zip codes for all Tunisian governorates.

This API made by [FastApi](https://fastapi.tiangolo.com/) 

# API ROUTES :

# /region_gover
The Region endpoint is a GET request that returns a dictionary of regions for a given governorate. The endpoint takes a `gover` parameter, which is the name of the governorate for which the regions are being requested.

### Endpoint URL
```
 GET /region
  ```
### Parameters

gover (required): The name of the governorate for which regions are being requested.

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

The Zip-City endpoint is a GET request that returns the zip code for a given city. The endpoint takes a `city` parameter, which is the name of the city for which the zip code is being requested.

### Parameters

city (required): The name of the city for which the zip is being requested.

### Usage

The endpoint returns a JSON object with a single key-value pair, representing the key `zip` and value `zip code` of the city that was requested.

### Example of Usage

```
  http://127.0.0.1:8000/region_city?city=Cité Belvedere 2
  ```

### Example of Response

````
{
  "zip": "2091"
}
````

# /cities_zip

The Cities-Zip endpoint is a GET request that returns the cities/city for a given zip code. The endpoint takes a `zip` parameter, which is the zip code for which the cities are being requested.

## Parameters

zip (required): The zip code for which the cities/city are being requested.

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