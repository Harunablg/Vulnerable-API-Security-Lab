from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
users = {
    "101": {"name": "Haruna", "email": "haruna@email.com"},
    "102": {"name": "Ali", "email": "ali@email.com"}
}

# 🔓 Broken Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")

    # Weak token (predictable)
    token = f"{username}-token"

    return jsonify({"token": token})

# 🔓 BOLA Vulnerability
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    return jsonify(users.get(id, "User not found"))

if __name__ == '__main__':
    app.run(debug=True)