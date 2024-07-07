import requests
import time
from pymongo import MongoClient

# Function to fetch user data from GitHub API
def fetch_user_data(username):
    url = f'https://github.com/Danielmoses1996'
    headers = {'Authorization': 'token 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'} 
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to handle rate limits and fetch multiple users
def fetch_users(usernames):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['github_data']
    users_collection = db['users']
    
    for username in usernames:
        user_data = fetch_user_data(username)
        if user_data:
            users_collection.insert_one(user_data)
        time.sleep(1)  # Rate limit: 1 request per second


usernames = ['John', 'David', 'Jessy']  
fetch_users(usernames)
