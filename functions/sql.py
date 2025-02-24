import sqlite3

def connect_db(db_name:str):
    
    """
    Connect to an existent database.
    If not exist, it will create one.
    
    Parameters:
        db_name (str): A database name.
    
    Returns:
        Connection: Database connection.
    """
    conn = sqlite3.connect(db_name)
    
    return conn