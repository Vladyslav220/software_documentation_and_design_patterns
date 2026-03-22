from abc import ABC, abstractmethod


class ISpotifyRepository(ABC):
    @abstractmethod
    def get_playlist_by_id(self, playlist_id: int):
        pass

    @abstractmethod
    def get_song_by_id(self, song_id: int):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        pass

    @abstractmethod
    def get_artist_by_name(self, name: str):
        pass

    @abstractmethod
    def save_user(self, user):
        pass

    @abstractmethod
    def save_artist(self, artist):
        pass

    @abstractmethod
    def save_playlist(self, playlist):
        pass

    @abstractmethod
    def save_song(self, song):
        pass

    @abstractmethod
    def save_listening_history(self, history):
        pass