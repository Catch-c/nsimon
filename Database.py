from pymongo import MongoClient
from dotenv import load_dotenv
import os

# --[[ Load Environment Variables ]]--
load_dotenv()
MONGO_DB_URI = os.getenv("MONGO_DB_URI")

client = MongoClient(MONGO_DB_URI)
db = client["nSIMON"]
users_collection = db["users"]

def getUser(username: str) -> bool:
    """Check if a user exists by username."""
    return users_collection.find_one({"username": username})

def createUser(username: str, password: str, cookie: str) -> bool:
    """Create a new user with username and cookie. Returns True if created, False if user already exists."""
    if getUser(username):
        return False
    users_collection.insert_one({
        "username": username,
        "password": password,
        "cookie": cookie
    })
    return True

def deleteUser(username: str) -> bool:
    """Delete a user by username. Returns True if a user was deleted, False otherwise."""
    result = users_collection.delete_one({"username": username})
    return result.deleted_count > 0
