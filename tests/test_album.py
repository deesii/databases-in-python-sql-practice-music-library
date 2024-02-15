from lib.album import *
'''
When I construct an album
With the fields title, release_year and artist_id
It is reflected in the instance variables

'''

def test_constructs_album_properties_with_fields():
    album = Album(1, 'Doolittle', 1989, 1)
    assert album.id == 1
    assert album.title == 'Doolittle'
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_album_equality():
    album_1 = Album(1, 'Doolittle', 1989, 1)
    album_2 = Album(1, 'Doolittle', 1989, 1)
    assert album_1 == album_2


'''
When i construct an album and when i format it to a string, and it will format into a friendly way
'''
def test_album_string():
    album = Album(1, 'Doolittle', 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"