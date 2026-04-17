from app import app
from models import db, User, Artist, Playlist, Song

with app.app_context():
    db.create_all()

    if not User.query.first():
        users = [
            User(email="user1@mail.com", password="pass1", subscription_type="Family"),
            User(email="user2@mail.com", password="pass2", subscription_type="Premium"),
            User(email="user3@mail.com", password="pass3", subscription_type="Student"),
            User(email="user4@mail.com", password="pass4", subscription_type="Free")
        ]
        db.session.add_all(users)
        db.session.commit()

    if not Artist.query.first():
        artists = [
            Artist(name="Imagine Dragons"),
            Artist(name="Adele"),
            Artist(name="Coldplay"),
            Artist(name="Taylor Swift"),
            Artist(name="Ed Sheeran")
        ]
        db.session.add_all(artists)
        db.session.commit()

    if not Playlist.query.first():
        playlists = [
            Playlist(name="Top Hits", user_id=1),
            Playlist(name="Relax Music", user_id=2),
            Playlist(name="Workout Mix", user_id=3),
            Playlist(name="My Favorites", user_id=4)
        ]
        db.session.add_all(playlists)
        db.session.commit()

    if not Song.query.first():
        songs = [
            Song(title="Song 1", duration=204, artist_id=1, playlist_id=1),
            Song(title="Song 2", duration=217, artist_id=2, playlist_id=2),
            Song(title="Song 3", duration=163, artist_id=3, playlist_id=3),
            Song(title="Song 4", duration=190, artist_id=4, playlist_id=4)
        ]
        db.session.add_all(songs)
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)