from flask import Flask, render_template, request, redirect, url_for
from models import db
from services import UserService, ArtistService, PlaylistService, SongService

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    users = UserService.get_all()
    artists = ArtistService.get_all()
    playlists = PlaylistService.get_all()
    songs = SongService.get_all()

    return render_template(
        "index.html",
        users=users,
        artists=artists,
        playlists=playlists,
        songs=songs
    )


# USERS
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        subscription_type = request.form["subscription_type"]
        UserService.create(email, password, subscription_type)
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = UserService.get_by_id(user_id)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        subscription_type = request.form["subscription_type"]
        UserService.update(user_id, email, password, subscription_type)
        return redirect(url_for("index"))
    return render_template("edit_user.html", user=user)


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    UserService.delete(user_id)
    return redirect(url_for("index"))


# ARTISTS
@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        name = request.form["name"]
        ArtistService.create(name)
        return redirect(url_for("index"))
    return render_template("add_artist.html")


@app.route("/edit_artist/<int:artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):
    artist = ArtistService.get_by_id(artist_id)
    if request.method == "POST":
        name = request.form["name"]
        ArtistService.update(artist_id, name)
        return redirect(url_for("index"))
    return render_template("edit_artist.html", artist=artist)


@app.route("/delete_artist/<int:artist_id>")
def delete_artist(artist_id):
    ArtistService.delete(artist_id)
    return redirect(url_for("index"))


# PLAYLISTS
@app.route("/add_playlist", methods=["GET", "POST"])
def add_playlist():
    users = UserService.get_all()
    if request.method == "POST":
        name = request.form["name"]
        user_id = request.form["user_id"]
        PlaylistService.create(name, user_id)
        return redirect(url_for("index"))
    return render_template("add_playlist.html", users=users)


@app.route("/edit_playlist/<int:playlist_id>", methods=["GET", "POST"])
def edit_playlist(playlist_id):
    playlist = PlaylistService.get_by_id(playlist_id)
    users = UserService.get_all()

    if request.method == "POST":
        name = request.form["name"]
        user_id = request.form["user_id"]
        PlaylistService.update(playlist_id, name, user_id)
        return redirect(url_for("index"))

    return render_template("edit_playlist.html", playlist=playlist, users=users)


@app.route("/delete_playlist/<int:playlist_id>")
def delete_playlist(playlist_id):
    PlaylistService.delete(playlist_id)
    return redirect(url_for("index"))


# SONGS
@app.route("/add_song", methods=["GET", "POST"])
def add_song():
    artists = ArtistService.get_all()
    playlists = PlaylistService.get_all()

    if request.method == "POST":
        title = request.form["title"]
        duration = request.form["duration"]
        artist_id = request.form["artist_id"]
        playlist_id = request.form["playlist_id"]
        SongService.create(title, duration, artist_id, playlist_id)
        return redirect(url_for("index"))

    return render_template("add_song.html", artists=artists, playlists=playlists)


@app.route("/edit_song/<int:song_id>", methods=["GET", "POST"])
def edit_song(song_id):
    song = SongService.get_by_id(song_id)
    artists = ArtistService.get_all()
    playlists = PlaylistService.get_all()

    if request.method == "POST":
        title = request.form["title"]
        duration = request.form["duration"]
        artist_id = request.form["artist_id"]
        playlist_id = request.form["playlist_id"]
        SongService.update(song_id, title, duration, artist_id, playlist_id)
        return redirect(url_for("index"))

    return render_template(
        "edit_song.html",
        song=song,
        artists=artists,
        playlists=playlists
    )


@app.route("/delete_song/<int:song_id>")
def delete_song(song_id):
    SongService.delete(song_id)
    return redirect(url_for("index"))