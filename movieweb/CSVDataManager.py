import csv
from IDataManager import IDataManager

class CSVDataManager(IDataManager):
    def __init__(self, filename):
        self.filename = filename

    def get_all_users(self):
        """
        Get all users from the CSV file.

        Returns:
            dict: Dictionary containing user data.
        """
        users = {}
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = int(row['id'])
                users[user_id] = {
                    'name': row['name'],
                    'movies': {}  # Assuming movies are initially empty in the CSV
                }
        return users

    def get_user_movies(self, user_id):
        """
        Get movies for a given user from the CSV file.

        Args:
            user_id (int): ID of the user.

        Returns:
            dict: Dictionary containing movie data.
        """
        movies = {}
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) == user_id:
                    movie_id = int(row['movie_id'])
                    movies[movie_id] = {
                        'name': row['movie_name'],
                        'director': row['director'],
                        'year': int(row['year']),
                        'rating': float(row['rating'])
                    }
        return movies

    def add_user_movie(self, user_id, movie_data):
        """
        Add a movie for a given user in the CSV file.

        Args:
            user_id (int): ID of the user.
            movie_data (dict): Dictionary containing movie data.
        """
        # Read existing data from the CSV file
        users = self.get_all_users()

        # Check if the user exists
        if user_id not in users:
            raise ValueError(f"User with ID {user_id} not found.")

        # Add the movie data to the user's movies
        user_movies = users[user_id]['movies']
        new_movie_id = max(user_movies.keys(), default=0) + 1
        movie_data['id'] = new_movie_id
        user_movies[new_movie_id] = movie_data

        # Update the CSV file with the new data
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['id', 'name', 'movie_id', 'movie_name', 'director', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header if the file is empty
            if file.tell() == 0:
                writer.writeheader()

            # Write user and movie data
            for user_id, user_data in users.items():
                for movie_id, movie_data in user_data['movies'].items():
                    writer.writerow({
                        'id': user_id,
                        'name': user_data['name'],
                        'movie_id': movie_id,
                        'movie_name': movie_data['name'],
                        'director': movie_data['director'],
                        'year': movie_data['year'],
                        'rating': movie_data['rating']
                    })

        print(f"Movie added successfully for User ID {user_id}.")

    def update_user_movie(self, user_id, movie_id, updated_data):
        """
                   Update a movie for a given user in the CSV file.

                   Args:
                       user_id (int): ID of the user.
                       movie_id (int): ID of the movie.
                       updated_data (dict): Dictionary containing updated movie data.
                   """
        # Read existing data from the CSV file
        users = self.get_all_users()

        # Check if the user and movie exist
        if user_id not in users:
            raise ValueError(f"User with ID {user_id} not found.")
        user = users[user_id]
        if movie_id not in user['movies']:
            raise ValueError(f"Movie with ID {movie_id} not found for User ID {user_id}.")

        # Update the movie data
        user['movies'][movie_id].update(updated_data)

        # Update the CSV file with the new data
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['id', 'name', 'movie_id', 'movie_name', 'director', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header if the file is empty
            if file.tell() == 0:
                writer.writeheader()

            # Write user and movie data
            for user_id, user_data in users.items():
                for movie_id, movie_data in user_data['movies'].items():
                    writer.writerow({
                        'id': user_id,
                        'name': user_data['name'],
                        'movie_id': movie_id,
                        'movie_name': movie_data['name'],
                        'director': movie_data['director'],
                        'year': movie_data['year'],
                        'rating': movie_data['rating']
                    })

        print(f"Movie updated successfully for User ID {user_id}, Movie ID {movie_id}.")

    def delete_user_movie(self, user_id, movie_id):
        """
        Delete a movie for a given user from the CSV file.

        Args:
            user_id (int): ID of the user.
            movie_id (int): ID of the movie to be deleted.
        """
        # Read existing data from the CSV file
        users = self.get_all_users()

        # Check if the user and movie exist
        if user_id not in users:
            raise ValueError(f"User with ID {user_id} not found.")
        user = users[user_id]
        if movie_id not in user['movies']:
            raise ValueError(f"Movie with ID {movie_id} not found for User ID {user_id}.")

        # Delete the movie data
        del user['movies'][movie_id]

        # Update the CSV file with the new data
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['id', 'name', 'movie_id', 'movie_name', 'director', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header if the file is empty
            if file.tell() == 0:
                writer.writeheader()

            # Write user and movie data, excluding the deleted movie
            for user_id, user_data in users.items():
                for movie_id, movie_data in user_data['movies'].items():
                    writer.writerow({
                        'id': user_id,
                        'name': user_data['name'],
                        'movie_id': movie_id,
                        'movie_name': movie_data['name'],
                        'director': movie_data['director'],
                        'year': movie_data['year'],
                        'rating': movie_data['rating']
                    })

        print(f"Movie deleted successfully for User ID {user_id}, Movie ID {movie_id}.")
