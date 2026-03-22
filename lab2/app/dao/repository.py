from app.dao.interfaces import ISpotifyRepository
from app.config.db import SessionLocal
from app.models.entities import Playlist, Song, User, Artist


class SpotifyRepository(ISpotifyRepository):
    def get_playlist_by_id(self, playlist_id: int):
        session = SessionLocal()
        try:
            return session.query(Playlist).filter_by(id=playlist_id).first()
        finally:
            session.close()

    def get_song_by_id(self, song_id: int):
        session = SessionLocal()
        try:
            return session.query(Song).filter_by(id=song_id).first()
        finally:
            session.close()

    def get_user_by_email(self, email: str):
        session = SessionLocal()
        try:
            return session.query(User).filter_by(email=email).first()
        finally:
            session.close()

    def get_artist_by_name(self, name: str):
        session = SessionLocal()
        try:
            return session.query(Artist).filter_by(name=name).first()
        finally:
            session.close()

    def save_user(self, user):
        session = SessionLocal()
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        finally:
            session.close()

    def save_artist(self, artist):
        session = SessionLocal()
        try:
            session.add(artist)
            session.commit()
            session.refresh(artist)
            return artist
        finally:
            session.close()

    def save_playlist(self, playlist):
        session = SessionLocal()
        try:
            session.add(playlist)
            session.commit()
            session.refresh(playlist)
            return playlist
        finally:
            session.close()

    def save_song(self, song):
        session = SessionLocal()
        try:
            session.add(song)
            session.commit()
            session.refresh(song)
            return song
        finally:
            session.close()

    def save_listening_history(self, history):
        session = SessionLocal()
        try:
            session.add(history)
            session.commit()
            session.refresh(history)
            return history
        finally:
            session.close()