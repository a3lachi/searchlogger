from config.database import DatabaseConfig
from database.manager import DatabaseManager


dbconfig = DatabaseConfig()

dbmanager = DatabaseManager(dbconfig)

dbmanager.connect()

results = dbmanager.execute_query("SELECT * from users;")


print(results)

dbmanager.disconnect()


