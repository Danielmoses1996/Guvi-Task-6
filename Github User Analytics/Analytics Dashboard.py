from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['github_data']
users_collection = db['users']

# Route to display user analytics
@app.route('/user/<username>')
def user_profile(username):
    user_data = users_collection.find_one({'login': username})
    return render_template('profile.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
