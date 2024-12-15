# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # This list will act as a simple in-memory database
# items = []

# # Create - POST method to add new item
# @app.route("/item", methods=["POST"])
# def add_item():
#     item = request.json
#     items.append(item)
#     return jsonify(item), 201

# # Read - GET method to retrieve items
# @app.route("/items", methods=["GET"])
# def get_items():
#     return jsonify(items)

# # Update - PUT method to update an item
# @app.route("/item/<int:index>", methods=["PUT"])
# def update_item(index):
#     if index >= len(items):
#         return "Item not found.", 404
#     item = request.json
#     items[index] = item
#     return jsonify(item)

# # Delete - DELETE method to delete an item
# @app.route("/item/<int:index>", methods=["DELETE"])
# def delete_item(index):
#     if index >= len(items):
#         return "Item not found.", 404
#     items.pop(index)
#     return "Item deleted.", 204

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB server
client = MongoClient('mongodb+srv://pankaj1234kashyap:8CBHXU23ht5OgvwG@cluster0.lfu3n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']  # Access the database
collection = db['items']  # Access the collection

# Create - POST method to add a new item
@app.route("/item", methods=["POST"])
def add_item():
    item = request.json
    result = collection.insert_one(item)  # Insert into MongoDB collection
    item['_id'] = str(result.inserted_id)  # Convert ObjectId to string
    return jsonify(item), 201

# Read - GET method to retrieve items
@app.route("/items", methods=["GET"])
def get_items():
    items = list(collection.find())  # Find all items in the collection
    for item in items:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(items)

# Update - PUT method to update an item
@app.route("/item/<id>", methods=["PUT"])
def update_item(id):
    item = request.json
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': item})
    if result.matched_count == 0:
        return "Item not found.", 404
    return jsonify(item)

# Delete - DELETE method to delete an item
@app.route("/item/<id>", methods=["DELETE"])
def delete_item(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return "Item not found.", 404
    return "Item deleted.", 204

if __name__ == "__main__":
    app.run(debug=True)
