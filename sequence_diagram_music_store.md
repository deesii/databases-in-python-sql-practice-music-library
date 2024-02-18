:::mermaid

sequenceDiagram
    participant t as terminal
    participant app as Main program (in app_album.py)
    participant ar as album_repository class <br /> (in lib/album_repository.py)
    participant db_conn as database_connection class in (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python app_album.py`
    app->>db_conn: Opens connection to database by calling .connect method on database_connection
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls all method on album_repository
    ar->>db_conn: Sends SQL query by calling execute method on database_connection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the album table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the album table
    loop 
        ar->>ar: Loops through list and creates a album object for every row
    end
    ar->>app: Returns list of album objects
    app->>t: Prints list of albums to terminal

:::