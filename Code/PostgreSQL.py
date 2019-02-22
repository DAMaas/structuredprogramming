# TODO: Get documents
#       Insert documents

# Import dependencies


from psycopg2.extensions import AsIs
import psycopg2 as pgc
from ConfigParser import getConfig


# Define functions


def connectPostgreSQL(configFile="Code/Config.ini", configSection="PostgreSQLLogin"):
    """
    Connect to the PostgreSQL daemon.

    Arguments:
        configFile:     The file to get the config from.
        configSection:  The section in the config file to use.

    Returns:
        client:         The client session that is made.
        cursor:         The cursor that is made.
    """

    client = None
    try:
        config = getConfig(configFile, configSection)
        host = config["address"]
        database = config["database"]
        username = config["username"]
        password = config["password"]
        port = config["port"]

        print('Connecting to the PostgreSQL database...')
        client = pgc.connect(host=host, database=database,
                             user=username, password=password, port=port)

        cursor = client.cursor()

        if client.closed == 0 and cursor.closed == 0:
            print("Connection succeeded.")
        else:
            print("Client closed: " + str(client.closed) +
                  " Cursor closed: " + str(cursor.closed))

    except (Exception, pgc.DatabaseError) as error:
        print(error)
    return client, cursor


def disconnectPostgreSQL(client, cursor):
    """
    Disconnect from the PostgreSQL daemon.

    Arguments:
        client: The client to close.
        cursor: The cursor to close.

    Returns:
        Nothing
    """

    cursor.close()
    client.close()
    print("Connection closed.")


def executeCommands(commands):
    """
    Connect to PostgreSQL, execute commands and disconnect.

    Arguments:
        commands: list of commands to execute.

    Returns:
        Nothing
    """

    client, cursor = connectPostgreSQL()

    for command in commands:
        cursor.execute(command)
        print()  # print output to check

    doIWantToCommit = None
    while doIWantToCommit not in ("yes", "no"):
        answer = input("Do you want to commit the changes? (yes/no) ")
        if answer == "yes":
            client.commit()
        elif answer == "no":
            pass
        else:
            print("Please enter yes or no.")

    disconnectPostgreSQL(client, cursor)


def createQuery(function="INSERT INTO", table="", dataDict={}):
    """
    Create a query to use with the executeCommands function.

    Arguments:
        function:   The SQL function to use.
        table:      Which table to use.
        dataDict:   Dictionary of key and value to use.

    Returns:
        Nothing
    """

    for key in dataDict:
        functionDefinition = str(function) + " " + \
            str(table) + "(" + str(key) + ")"
        values =


sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""

cur = conn.cursor()
cur.executemany(
    """INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)


song = {
    'title': 'song 1',
    'artist': 'artist 1'
}

columns = song.keys()
values = [song[column] for column in columns]

insert_statement = 'insert into song_table (%s) values %s'

# cursor.execute(insert_statement, (AsIs(','.join(columns)), tuple(values)))
print cursor.mogrify(insert_statement, (AsIs(','.join(columns)), tuple(values)))
