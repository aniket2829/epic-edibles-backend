from fastapi import APIRouter
from routes.product_routes import get_json_data
from fastapi.exceptions import HTTPException


route = APIRouter()

@route.get("/{category}")
async def get_products_by_category(category: str):
    data = get_json_data()
    all_products = data["store"]["inventory"]
    products = list(filter(lambda x: x["category"] == category, all_products))
    if not products:
        raise HTTPException(404, "No such category")
    return products