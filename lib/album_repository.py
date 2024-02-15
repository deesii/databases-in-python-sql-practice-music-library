from lib.album import *

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection #establish a connection with the database

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])    
            albums.append(album)
        return albums


    




