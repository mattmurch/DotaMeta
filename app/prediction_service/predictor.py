#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error

from .config import SQL_DATABASE_PATH

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all(conn):
    """
    Query all rows in the table table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM table")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_next_best_pick(conn, draft):
    """
    Query hero by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("""DECLARE @cnt INT = 0;
                            WHILE @cnt < ?
                            BEGIN
                                SELECT COUNT(win) FROM table WHERE pick_(@cnt+1)=?
                                SET @cnt = @cnt + 1;
                                END;""", (len(draft),))
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    # create a database connection
    conn = create_connection(SQL_DATABASE_PATH)
    with conn:
        print("Getting next best pick")
        select_next_best_pickconn,1)
 
        print("2. Query all")
        select_all(conn)
 
 
if __name__ == '__main__':
    main()
