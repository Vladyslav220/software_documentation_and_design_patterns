from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    subscription_type = Column(String, nullable=False)

    playlists = relationship("Playlist", back_populates="user")
    listening_history = relationship("ListeningHistory", back_populates="user")


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    songs = relationship("Song", back_populates="artist")


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="playlists")
    songs = relationship("Song", back_populates="playlist")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=False)

    artist = relationship("Artist", back_populates="songs")
    playlist = relationship("Playlist", back_populates="songs")
    listening_history = relationship("ListeningHistory", back_populates="song")


class ListeningHistory(Base):
    __tablename__ = "listening_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False)
    duration_played = Column(Integer, nullable=False)

    user = relationship("User", back_populates="listening_history")
    song = relationship("Song", back_populates="listening_history")