# TODO: Get documents
#       Insert documents

# Import dependencies

from VariableStore import tableDict
import psycopg2 as pgc
from ConfigParser import getConfig


# Define functions


def connectPostgreSQL(database="", configFile="Code/Config.ini", configSection="PostgreSQLLogin"):
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
        username = config["username"]
        password = config["password"]
        port = config["port"]

        if database == "":
            database = config["database"]

        print('Connecting to the PostgreSQL database: %s' % database)
        client = pgc.connect(host=host, database=database,
                             user=username, password=password, port=port)

        cursor = client.cursor()

        if client.closed == 0 and cursor.closed == 0:
            print("Connection succeeded.\n")
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
    print("Connection closed.\n")


def executeCommand(client, cursor, commands):
    """
    Execute commands with the cursor.

    Arguments:
        client:   The client session.
        cursor:   The cursor session.
        commands: List of commands to execute.

    Returns:
        Nothing
    """

    for command in commands:
        cursor.execute(command)
        client.commit()
        print("Ran command: " + str(command))


def initDatabase(database):
    print("<-> Starting database initialization <->")

    client, cursor = connectPostgreSQL(database="postgres")
    client.set_isolation_level(0)
    print("Initializing database...")

    cursor.execute(
        """SELECT EXISTS(SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('%s'));""" % database)
    exists = cursor.fetchone()[0]

    if exists:
        cursor.execute("""DROP DATABASE IF EXISTS %s;""" % database)
        print("Dropped database: %s" % database)

    cursor.execute("""CREATE DATABASE %s;""" % database)
    print("Created database: %s\n" % database)

    disconnectPostgreSQL(client, cursor)

    addTables(database)

    print("<-> Succesfully initialized " + database + " <->\n")


def addTables(database):
    client, cursor = connectPostgreSQL(database=database)

    cursor.execute(
        """select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';""")
    print("Current tables: " + str(cursor.fetchall()) + "\n")

    executeCommand(client, cursor, tableDict[database])

    cursor.execute(
        """select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';""")
    print("Tables now: " + str(cursor.fetchall()) + "\n")

    disconnectPostgreSQL(client, cursor)
