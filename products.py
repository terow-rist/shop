from fastapi import  APIRouter, HTTPException
from lab3.database import db, format_document
from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId
router = APIRouter()

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    description: str
    category: str
    stock: int = Field(..., gt=0, description="Stock must be greater than zero")

# Product Endpoints
@router.post("/products/")
async def add_product(product: Product):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id), **product.dict()}

@router.get("/products/{product_id}")
async def get_product(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return format_document(product)

@router.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    result = await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}

@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = await db.products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}