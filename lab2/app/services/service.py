from app.services.interfaces import ISpotifyService
from app.models.entities import User, Artist, Playlist, Song, ListeningHistory


class SpotifyService(ISpotifyService):
    def __init__(self, repository, csv_reader):
        self.repository = repository
        self.csv_reader = csv_reader

    def process_csv(self, file_path: str):
        rows = self.csv_reader.read(file_path)

        if not rows:
            print("CSV файл порожній. Дані не завантажено.")
            return

        for row in rows:
            playlist_id = int(row["playlist_id"])
            song_id = int(row["song_id"])

            existing_playlist = self.repository.get_playlist_by_id(playlist_id)
            if existing_playlist:
                print(f"Плейлист {playlist_id} вже існує, пропускаємо.")
                continue

            existing_user = self.repository.get_user_by_email(row["email"])
            if existing_user:
                saved_user = existing_user
            else:
                user = User(
                    email=row["email"],
                    password=row["password"],
                    subscription_type=row["subscription_type"]
                )
                saved_user = self.repository.save_user(user)

            existing_artist = self.repository.get_artist_by_name(row["artist_name"])
            if existing_artist:
                saved_artist = existing_artist
            else:
                artist = Artist(
                    name=row["artist_name"]
                )
                saved_artist = self.repository.save_artist(artist)

            playlist = Playlist(
                id=playlist_id,
                name=row["playlist_name"],
                user_id=saved_user.id
            )
            saved_playlist = self.repository.save_playlist(playlist)

            existing_song = self.repository.get_song_by_id(song_id)
            if existing_song:
                print(f"Пісня {song_id} вже існує, пропускаємо.")
                continue

            song = Song(
                id=song_id,
                title=row["song_title"],
                duration=int(row["duration"]),
                artist_id=saved_artist.id,
                playlist_id=saved_playlist.id
            )
            saved_song = self.repository.save_song(song)

            history = ListeningHistory(
                user_id=saved_user.id,
                song_id=saved_song.id,
                duration_played=int(row["duration_played"])
            )
            self.repository.save_listening_history(history)

        print("Дані успішно завантажено в базу.")