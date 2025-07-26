from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["testdb"]
users_collection = db["users"]

async def create_indexes():
    await users_collection.create_index("email", unique=True)
    await users_collection.create_index("username", unique=True)