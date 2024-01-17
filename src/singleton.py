class DatabaseConnection:
    _instance = None

    def __new__(cls, host, username, password, database_name):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = f"Connected to {host}/{database_name} as {username}"
        return cls._instance

    def get_connection(self):
        return self.connection


db_connection1 = DatabaseConnection(host="localhost", username="user", password="pass", database_name="mydb")

# Connected to localhost/mydb as user
print(db_connection1.get_connection())

db_connection2 = DatabaseConnection(host="example.com", username="admin", password="adminpass",
                                    database_name="production")

# Connected to localhost/mydb as user (Same result as db_conn1)
print(db_connection2.get_connection())

# Both instances point to the same connection
print(db_connection1 is db_connection2)  # Output: True
