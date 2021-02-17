import motor.motor_asyncio

# setup the database
async def setupDB():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.chat_db
    return db