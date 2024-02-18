from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all albums
album_repository = AlbumRepository(connection) # creates an instance of the album repository, whilst opening and ensuring the connection of the database so that there can a place to store that connection and output of the queries
albums = album_repository.all()

# List them out
for album in albums:
    print(album)
