from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
import string


def createShareCode(length=8):
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choices(characters, k=length))

# --[[ Load Environment Variables ]]--
load_dotenv()
MONGO_DB_URI = os.getenv("MONGO_DB_URI")

client = MongoClient(MONGO_DB_URI)
db = client["nSIMON"]
users_collection = db["users"]
timetable_share_collection = db["timetableShares"]

def getUser(username: str):
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

def getTimetableShare(shareCode: str):
    """Check if a timetable share exists by shareCode."""
    return timetable_share_collection.find_one({"shareCode": shareCode})

def createTimetableShare(username, date, timetable):
    """Create a new timetable share."""
    shareCode = createShareCode()
    timetable_share_collection.insert_one({
        "shareCode": shareCode,
        "username": username,
        "date": date,
        "timetable": timetable
    })
    return shareCode