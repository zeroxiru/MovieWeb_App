from abc import ABC, abstractmethod



class IDataManager(ABC):
    """Interface for DataManager class."""

    @abstractmethod
    def load_data(self):
        """Load data from the JSON file."""
        pass

    @abstractmethod
    def save_data(self):
        """Save data to the JSON file."""
        pass

    @abstractmethod
    def find_user_by_id(self, user_id):
        """Find a user by their ID."""
        pass

    @abstractmethod
    def add_user(self, user_id, user_data):
        """Add a new user."""
        pass

    @abstractmethod
    def update_user(self, user_id, updated_data):
        """Update user data."""
        pass

    @abstractmethod
    def delete_user(self, user_id):
        """Delete a user."""
        pass

    @abstractmethod
    def add_movie(self, user_id, movie_data):
        """Add a movie for a user."""
        pass

    @abstractmethod
    def update_movie(self, user_id, movie_id, updated_data):
        """Update movie data."""
        pass

    @abstractmethod
    def delete_movie(self, user_id, movie_id):
        """Delete a movie for a user."""
        pass

    @abstractmethod
    def list_movies(self, user_id):
        """List all movies for a user."""
        pass

    # Other methods can be added as needed