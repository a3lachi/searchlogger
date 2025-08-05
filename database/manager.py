import psycopg2
import psycopg2.extras
from typing import List, Dict, Any, Optional, Tuple
from contextlib import contextmanager

from config.database import DatabaseConfig
from utils.logger import get_logger

logger = get_logger(__name__)

class DatabaseManager:
    """Database connection and query management"""
    
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.connection = None

    def connect(self) -> bool:
        """Establish database connection"""
        try:
            self.connection = psycopg2.connect(
                **self.config.get_connection_params(),
                cursor_factory=psycopg2.extras.RealDictCursor # return rows as dictionaries instead of tuples.
            )
            logger.info("Database connection established")
            return True
        except psycopg2.Error as e:
            logger.error(f"Database connection failed: {e}")
            return False

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
        logger.info("Database connection closed")

    @contextmanager
    def get_cursor(self):
        """Context manager for database cursors"""
        cursor = self.connection.cursor()
        try:
            yield cursor
        except Exception as e:
            self.connection.rollback()
            logger.error(f"Database operation failed: {e}")
            raise
        else:
            self.connection.commit()
        finally:
            cursor.close()

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> Optional[List[Dict]]:
        """Execute a database query"""
        try:
            with self.get_cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return [dict(row) for row in results] if results else []
                    
        except psycopg2.Error as e:
            logger.error(f"Query '{query}' execution failed: {e}")
            raise

    def execute_single(self, query: str, params: Optional[Tuple] = None) -> Optional[Dict]:
        """Execute query and return single result"""
        results = self.execute_query(query, params)
        return results[0] if results else None

    def health_check(self) -> bool:
        """Check if database connection is healthy"""
        try:
            result = self.execute_query("SELECT 1")
            return bool(result)
        except Exception:
            return False