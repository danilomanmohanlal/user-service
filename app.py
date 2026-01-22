from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database: A list of dictionaries for more flexibility
users_db = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# 1. READ: Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users_db})

# 2. READ: Get a specific user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 3. CREATE: Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    new_data = request.get_json()
    
    if not new_data or "name" not in new_data:
        return jsonify({"error": "Missing name"}), 400
    
    new_user = {
        "id": len(users_db) + 1,
        "name": new_data["name"]
    }
    users_db.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)