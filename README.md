
# Tunisia Geographic API
This API provides a list of cities and regions for any governorate in Tunisia, as well as zip codes for all Tunisian governorates.

This API made by [FastApi](https://fastapi.tiangolo.com/) 

# API ROUTES :

# /region
The Region endpoint is a GET request that returns a dictionary of regions for a given city. The endpoint takes a `ville` parameter, which is the name of the city for which the regions are being requested.

### Endpoint URL
```
 GET /region
  ```
### Parameters

ville (required): The name of the city for which regions are being requested.

### Usage

The endpoint returns a JSON object with a dictionary of regions for the specified city. Each key in the dictionary is an integer that represents the region's position in the list, starting from 1. The value associated with each key is a string that represents the name of the region.

### Example of Usage
```
 http://127.0.0.1:8000/region?ville=Ariana
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


