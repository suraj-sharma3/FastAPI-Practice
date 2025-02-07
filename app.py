from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    available: str

# products = {
#     1 : {"name" : "Tea",
#         "price" : 50,
#         "brand" : "Society",
#         "available" : "Yes"
#     },
#     2: {"name" : "Chips",
#         "price" : 30,
#         "brand" : "Lays",
#         "available" : "No"
#     }
# }

products = {}

# print(products[2]['price'])

@app.get("/")
def home():
    return {"Home Page Data" : "Welcome to Home Page of the Web App"}

@app.get("/about")
def about():
    return {"About Page Data" : "This is the about page"}

@app.get("/get-item/{item_id}") # Passing path parameters
def get_item(item_id : int): # Type Hint, the name of the function parameter here should be exactly the same as the path parameter passed above in the endpoint
    return products[item_id]

# @app.get("/get-item-detail/{item_id}/{detail}") # Passing multiple path parameters
# def get_item(item_id : int, detail : str):
#     return products[item_id], products[item_id][detail]

@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(description="This is the ID of the product that you want to view", gt=0)): # description parameter is used to provide a description of the path parameter that is being passed to the API, gt here means greater than, similarly you can also use lt which means less than 
    return products[item_id]

# Endpoint with a query parameter
# @app.get("/get-by-name")
# def get_item_name(name: Optional[str] = None):
#     for product in products:
#         if products[product]['name'] == name:
#             return products[product]
#     return {"Data" : "Not Found"}

# Endpoint with multiple query parameters
@app.get("/get-by-name")
def get_item_name(test : int, name: Optional[str] = None):
    for product in products:
        if products[product].name == name: # products[product]['name'] == name: this was used when we didn't have Item
            return products[product]
    return {"Data" : "Not Found"}

# Combining Path & Query Parameters
@app.get("/get-by-name/{item_id}")
def get_item_name(item_id : int, test : int, name: Optional[str] = None):
    for product in products:
        if products[product].name == name: # products[product]['name'] == name: this was used when we didn't have Item
            return products[product]
    return {"Data" : "Not Found"}

# @app.post("/create-item/{item_id}") # this API will post/create/add the item to the products dictionary
# def create_item(item_id : int, item: Item):
#     if item_id in products:
#         return {"Error" : "Item with the provided ID already exists in products."}
#     products[item_id] = {"name" : item.name, "price" : item.price, "available" : item.available}
#     return products[item_id]

@app.post("/create-item/{item_id}") # this API will post/create/add the item to the products dictionary
def create_item(item_id : int, item: Item):
    if item_id in products:
        return {"Error" : "Item with the provided ID already exists in products."}
    products[item_id] = item
    return products[item_id]