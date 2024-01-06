from fastapi import FastAPI
from routes.product_routes import route as product_routes  #importing the route file which we have created in the routes0 
from fastapi.middleware.cors import CORSMiddleware      #handling cross-origin resources sharing
from routes.recommendation_routes import route as recommendation_routes


app = FastAPI()  #instance of FASTAPI used to run FASTAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],   #send request from any origin
    allow_credentials = True,   #send cookies witht he request
    allow_methods = ["*"],   #allows any http method
    allow_headers = ["*"]   #allows any http header
)


@app.get("/")
async def index():
    x = {
        "msg":"Welcome to Epic Edible"
    }
    return x

app.include_router(product_routes, prefix="/product")  #end point for the JSON file
app.include_router(recommendation_routes, prefix="/recommendations")