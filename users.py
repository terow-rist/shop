from fastapi import  APIRouter, HTTPException
from lab3.database import db, format_document
from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId

router = APIRouter()

class User(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")
    role: str = Field(default="customer")

    @validator("role")
    def validate_role(cls, value):
        allowed_roles = {"customer", "admin"}
        if value not in allowed_roles:
            raise ValueError("Role must be 'customer' or 'admin'")
        return value
# User Endpoints
@router.post("/users/")
async def add_user(user: User):
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "name": user.name, "email": user.email, "role": user.role}

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return format_document(user)

@router.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    result = await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
