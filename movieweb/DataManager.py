import json
import os
from IDataManager import IDataManager


class DataManager(IDataManager):
    """Class for managing user and movie data."""

    def __init__(self, filename):
        """Initialize the DataManager."""
        self._filename = filename
        self.users = self.load_data()



    # def load_data(self):
    #     """Load data from the JSON file."""
    #     try:
    #         with open(self._filename, 'r') as file:
    #             self.users = json.load(file)
    #
    #     except FileNotFoundError:
    #         self.users = {}

    def load_data(self):
        """Load data from the JSON file."""
        try:
            absolute_path = os.path.join(os.path.dirname(__file__), self._filename)
            with open(absolute_path, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_data(self):
        """Save data to the JSON file."""
        try:
            with open(self._filename, 'w') as file:
                json.dump(self.users, file, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def find_user_by_id(self, user_id):
        """Find a user by their ID."""
        try:
            return self.users.get(str(user_id), None)
        except Exception as e:
            print(f"Error finding user: {e}")
    def get_all_users(self):
        """
        Retrieve all users from the data source.

        Returns:
            dict: A dictionary representing all users.
        """
        with open(self._filename, 'r') as file:
            data = json.load(file)
            print(data)
        return data

    def get_user_movies(self, user_id):
        """
        Retrieve movies for a given user from the data source.

        Args:
            user_id (int): The identifier of the user.

        Returns:
            dict: A dictionary representing the movies for the specified user.
        """
        all_users = self.get_all_users()
        user = all_users.get(str(user_id), {})
        return user.get("movies", {})

    def add_user(self, user_id, user_data):
        """Add a new user."""
        try:
            user_id = str(user_id)
            self.users[user_id] = user_data
            self.save_data()
        except Exception as e:
            print(f"Error adding user: {e}")

    def update_user(self, user_id, updated_data):
        """Update user data."""
        try:
            user_id = str(user_id)
            if user_id in self.users:
                self.users[user_id].update(updated_data)
                self.save_data()
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        """Delete a user."""
        try:
            user_id = str(user_id)
            if user_id in self.users:
                del self.users[user_id]
                self.save_data()
        except Exception as e:
            print(f"Error deleting user: {e}")

    # def add_movie(self, user_id, movie_data):
    #     """Add a movie for a user."""
    #     try:
    #         user_id = str(user_id)
    #         if user_id not in self.users:
    #             self.users[user_id] = {"name": "", "movies": {}}
    #         elif self.users[user_id]["movies"] is None:
    #             self.users[user_id]["movies"] = {}
    #
    #         movies_data = self.users[user_id]["movies"]
    #         if movie_data is not None:
    #             new_movie_id = str(len(movies_data) + 1)
    #             movies_data[new_movie_id] = movie_data
    #             # self.users[user_id]["movies"][str(len(self.users[user_id]["movies"]) + 1)] = movie_data
    #             self.save_data()
    #             print(f"Movie added. Updated data: {self.users}")
    #         else:
    #             print("Error adding movie: movie_data is None")
    #
    #     except Exception as e:
    #         print(f"Error adding movie: {e}")

    def add_movie(self, user_id, movie_data):
        """Add a movie for a user."""
        try:
            user_id = str(user_id)
            if user_id not in self.users:
                self.users[user_id] = {"name": "", "movies": {}}
            # elif self.users[user_id]["movies"] is None:
            #     self.users[user_id]["movies"] = {}

            movies_data = self.users[user_id]["movies"]
            if movies_data is not None:
                new_movie_id = str(len(movies_data) + 1)
                movies_data[new_movie_id] = movie_data
                self.save_data()
                print(f"Movie added. Updated data: {self.users}")
                return {"message": "Movie added successfully"}
            else:
                print("Error adding movie: movies_data is None")
                return {"error": "Failed to add movie. User movies data is invalid."}

        except Exception as e:
            print(f"Error adding movie: {e}")
            return {"error": str(e)}

    def update_movie(self, user_id, movie_id, updated_data):
        """Update movie data."""
        try:
            user_id, movie_id = str(user_id), str(movie_id)
            if user_id in self.users and movie_id in self.users[user_id]["movies"]:
                self.users[user_id]["movies"][movie_id].update(updated_data)
                self.save_data()
        except Exception as e:
            print(f"Error updating movie: {e}")

    def delete_movie(self, user_id, movie_id):
        """Delete a movie for a user."""
        try:
            user_id, movie_id = str(user_id), str(movie_id)
            if user_id in self.users and movie_id in self.users[user_id]["movies"]:
                del self.users[user_id]["movies"][movie_id]
                self.save_data()
        except Exception as e:
            print(f"Error deleting movie: {e}")

    def list_movies(self, user_id):
        """List all movies for a user."""
        try:
            user = self.find_user_by_id(user_id)
            return user.get("movies", {})
        except Exception as e:
            print(f"Error listing movies: {e}")

