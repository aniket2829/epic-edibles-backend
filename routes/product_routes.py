from fastapi import APIRouter #organizes the APIRouter
import json   #interact with the JSON files
import os   #interacting with operating system
from fastapi.exceptions import HTTPException
# creating an instance route
route = APIRouter()

def get_json_data():
    var = os.path.dirname(__file__)    #get the directory containing the script
    file_path = os.path.join(var,"data.json")    #helps to get the complete path including (data.json) of the directory 
    file = open(file_path)    #open the JSON file in read only mode
    data = json.load(file)    #load the JSON data from the data.json into a python object
    file.close()    #close the file to free up the system resources
    return data     #return the loaded json data as the responce at "/"(endpoint) 
    

@route.get("/")
async def get_all_product():
    return get_json_data()

@route.get("/{product_id}")
async def get_one_product(product_id: int):
    data = get_json_data()
    all_products = data["store"]["inventory"]
    product = list(filter(lambda x: x["product_id"] == product_id, all_products))
    if not product:
        raise HTTPException(404, f"Product with id = {product_id} not found")
    return product[0]

@route.get("/category/{category}")
async def get_products_by_category(category: str):
    data = get_json_data()
    all_products = data["store"]["inventory"]
    
    # Filter products by category
    similar_products = [product for product in all_products if product["category"] == category]
    
    if not similar_products:
        raise HTTPException(404, "No similar products found")
    
    return {"store": {"inventory": similar_products}}