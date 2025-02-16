from fastapi import  APIRouter, HTTPException
from shop.database import db, format_document
from pydantic import BaseModel, EmailStr, Field, validator
from typing import List
from bson import ObjectId

router = APIRouter()

class Order(BaseModel):
    user_id: str
    product_ids: List[str]
    status: str = Field(default="pending")

    @validator("product_ids")
    def validate_product_ids(cls, value):
        if not value:
            raise ValueError("Order must contain at least one product")
        return value

    @validator("status")
    def validate_status(cls, value):
        allowed_statuses = {"pending", "shipped", "delivered"}
        if value not in allowed_statuses:
            raise ValueError("Status must be 'pending', 'shipped', or 'delivered'")
        return value

# Order Endpoints
@router.post("/orders/")
async def create_order(order: Order):
    result = await db.orders.insert_one(order.dict())
    return {"id": str(result.inserted_id), **order.dict()}

@router.get("/orders/{user_id}")
async def get_orders(user_id: str):
    orders = await db.orders.find({"user_id": user_id}).to_list(length=100)
    return [format_document(order) for order in orders]

@router.put("/orders/{order_id}")
async def update_order(order_id: str, order: Order):
    result = await db.orders.update_one({"_id": ObjectId(order_id)}, {"$set": order.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order updated successfully"}

@router.delete("/orders/{order_id}")
async def delete_order(order_id: str):
    result = await db.orders.delete_one({"_id": ObjectId(order_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
