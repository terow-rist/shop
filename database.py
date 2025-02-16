from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")  # Default to localhost if not set
client = AsyncIOMotorClient(MONGO_URI)
db = client.ecommerce

# Helper function to convert MongoDB object to dictionary
def format_document(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc