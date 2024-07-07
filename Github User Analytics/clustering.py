from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pymongo import MongoClient

# Function to fetch and preprocess user data for clustering
def fetch_and_preprocess_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['github_data']
    users_collection = db['users']
    
    # Fetch all user data from MongoDB
    cursor = users_collection.find({})
    user_data = [user for user in cursor]
    
    features = []
    for user in user_data:
        features.append([
            user['public_repos'],
            user['followers'],
            user['total_commits']
        ])
    
    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    return scaled_features

def recommend_similar_users():
    # Preprocess data
    data = fetch_and_preprocess_data()
    
    kmeans = KMeans(n_clusters=5, random_state=0)
    kmeans.fit(data)
    
    cluster_labels = kmeans.labels_
    
recommend_similar_users()
