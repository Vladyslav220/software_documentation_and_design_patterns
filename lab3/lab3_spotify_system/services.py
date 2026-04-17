from models import db, User, Artist, Playlist, Song


class UserService:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get_or_404(user_id)

    @staticmethod
    def create(email, password, subscription_type):
        user = User(email=email, password=password, subscription_type=subscription_type)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user_id, email, password, subscription_type):
        user = User.query.get_or_404(user_id)
        user.email = email
        user.password = password
        user.subscription_type = subscription_type
        db.session.commit()

    @staticmethod
    def delete(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()


class ArtistService:
    @staticmethod
    def get_all():
        return Artist.query.all()

    @staticmethod
    def get_by_id(artist_id):
        return Artist.query.get_or_404(artist_id)

    @staticmethod
    def create(name):
        artist = Artist(name=name)
        db.session.add(artist)
        db.session.commit()

    @staticmethod
    def update(artist_id, name):
        artist = Artist.query.get_or_404(artist_id)
        artist.name = name
        db.session.commit()

    @staticmethod
    def delete(artist_id):
        artist = Artist.query.get_or_404(artist_id)
        db.session.delete(artist)
        db.session.commit()


class PlaylistService:
    @staticmethod
    def get_all():
        return Playlist.query.all()

    @staticmethod
    def get_by_id(playlist_id):
        return Playlist.query.get_or_404(playlist_id)

    @staticmethod
    def create(name, user_id):
        playlist = Playlist(name=name, user_id=user_id)
        db.session.add(playlist)
        db.session.commit()

    @staticmethod
    def update(playlist_id, name, user_id):
        playlist = Playlist.query.get_or_404(playlist_id)
        playlist.name = name
        playlist.user_id = user_id
        db.session.commit()

    @staticmethod
    def delete(playlist_id):
        playlist = Playlist.query.get_or_404(playlist_id)
        db.session.delete(playlist)
        db.session.commit()


class SongService:
    @staticmethod
    def get_all():
        return Song.query.all()

    @staticmethod
    def get_by_id(song_id):
        return Song.query.get_or_404(song_id)

    @staticmethod
    def create(title, duration, artist_id, playlist_id):
        song = Song(
            title=title,
            duration=duration,
            artist_id=artist_id,
            playlist_id=playlist_id
        )
        db.session.add(song)
        db.session.commit()

    @staticmethod
    def update(song_id, title, duration, artist_id, playlist_id):
        song = Song.query.get_or_404(song_id)
        song.title = title
        song.duration = duration
        song.artist_id = artist_id
        song.playlist_id = playlist_id
        db.session.commit()

    @staticmethod
    def delete(song_id):
        song = Song.query.get_or_404(song_id)
        db.session.delete(song)
        db.session.commit()