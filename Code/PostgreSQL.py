# TODO: Connect to database
#       Get documents
#       Insert documents

# Import dependencies


import psycopg2 as pgc
from ConfigParser import getConfig


# Define functions


def connectPostgreSQL(configFile="config.ini", configSection="test"):
    """
    Connect to the PostgreSQL daemon.

    Arguments:
        address:    URL to connect to.
        port:       The port to use.
        database:   The database to use.
        user:       The user to login as.
        password:   The password to use.

    Returns:
        client:     The session that is made.
    """
    client = None
    try:
        parameters = getConfig()

        print('Connecting to the PostgreSQL database...')
        client = pgc.connect(**parameters)

        cursor = client.cursor()

        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        pgVersion = cursor.fetchone()
        print(pgVersion)

        cursor.close()

    except (Exception, pgc.DatabaseError) as error:
        print(error)

    finally:
        if client is not None:
            client.close()
            print('Database connection closed.')

    return client


print(connectPostgreSQL())
