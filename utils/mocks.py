from models.search_log import SearchLogModel
from datetime import datetime, timedelta
from typing import List
import random


search_queries = [
    "python contextmanager",
    "dataclass vs pydantic",
    "how to write unit tests",
    "python multiprocessing vs threading",
    "SQL injection prevention",
    "asyncio gather vs wait",
    "difference between list and tuple",
    "flask vs django",
    "fastapi performance tips",
    "REST vs GraphQL",
    "JWT authentication python",
    "PostgreSQL JSONB usage",
    "docker compose tutorial",
    "linux chmod explained",
    "python logging best practices",
    "mocking in pytest",
    "python decorators examples",
    "class vs staticmethod",
    "redis pub sub example",
    "nginx reverse proxy setup"
]

user_agents = [
    "Mozilla/5.0",
    "curl/7.79.1",
    "PostmanRuntime/7.32.2",
    "python-requests/2.25.1",
    "Googlebot/2.1",
    "Safari/537.36",
    "Opera/9.80",
    "Edge/91.0"
]


class SearchLogsMock :
    logs : List[SearchLogModel]

    def __init__(self) :
        self.logs=[]
        for i in range(1, 21):
            log = SearchLogModel.from_dict({
                "id": i,
                "user_id": random.randint(1000, 9999),
                "search_query": search_queries[i - 1],
                "session_id": f"sess_{random.randint(100, 999)}",
                "search_results": {f"result_1": f"Search result for '{search_queries[i - 1]}'"},
                "response_time_ms": random.randint(50, 300),
                "ip_address": f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}",
                "user_agent": random.choice(user_agents),
                "created_at": datetime.now() - timedelta(minutes=random.randint(0, 1000))
            })
            self.logs.append(log)
