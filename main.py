from config.database import DatabaseConfig
from database.manager import DatabaseManager
from models.search_log import SearchLogModel
from services.search_logger import SearchLogger
from utils.mocks import SearchLogsMock
from datetime import datetime

dbconfig = DatabaseConfig()

dbmanager = DatabaseManager(dbconfig)

dbmanager.connect()

searchlogger = SearchLogger(dbmanager)

# logs = SearchLogsMock()
# for log in logs.logs :
#     logresult = searchlogger.log_search(log)

user_log = searchlogger.get_user_search_history(2875,10)

for log in user_log :
    print("++==++ : ",log.to_dict())

# results = dbmanager.execute_query("SELECT * from search_logs;")



# print(results)

dbmanager.disconnect()