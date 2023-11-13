from flask import Flask, request, jsonify
from DataManager import DataManager
from CSVDataManager import CSVDataManager

app = Flask(__name__)

# Choose the data manager implementation (use either DataManager or CSVDataManager)
data_manager = DataManager('movies.json')

#data_manager = CSVDataManager('data/movies.csv')

# Routes

@app.route('/users', methods=['GET'])
def get_all_users():
    users = data_manager.get_all_users()
    print(f"{users}")
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_movies(user_id):
    user = data_manager.get_user_movies(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/user/<int:user_id>/add_user_movie', methods=['POST'])
def add_user_movie(user_id):
    movie_data = request.json
    print(f"Received payload: {movie_data}")
    response = data_manager.add_movie(user_id, movie_data)
    if "error" in response:
        return jsonify({"error": response["error"]}), 400
    else:
        return jsonify({"message": "Movie added successfully"}), 201

@app.route('/user/<int:user_id>/movie/<int:movie_id>', methods=['PUT'])
def update_user_movie(user_id, movie_id):
    updated_data = request.json
    try:
        data_manager.update_user_movie(user_id, movie_id, updated_data)
        return jsonify({"message": "Movie updated successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/user/<int:user_id>/movie/<int:movie_id>', methods=['DELETE'])
def delete_user_movie(user_id, movie_id):
    try:
        data_manager.delete_user_movie(user_id, movie_id)
        return jsonify({"message": "Movie deleted successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
