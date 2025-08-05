import json
import uuid
import time
from typing import Optional, Dict, Any, List

from database.manager import DatabaseManager
from models.search_log import SearchLogModel
from utils.logger import get_logger

logger = get_logger(__name__)

class SearchLogger:
    """Service for logging search queries and results"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def log_search(self, search_log: SearchLogModel) -> Dict[str, Any]:
        """Log a search query to the database"""
        try:
            insert_query = """
                INSERT INTO search_logs 
                (user_id, search_query, search_results, session_id, response_time_ms, ip_address, user_agent)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id, created_at;
            """
            
            params = (
                search_log.user_id,
                search_log.search_query.strip(),
                json.dumps(search_log.search_results) if search_log.search_results else None,
                search_log.session_id,
                search_log.response_time_ms,
                search_log.ip_address,
                search_log.user_agent
            )

            result = self.db.execute_query(insert_query, params)

            if len(result) == 1 :
                result = result[0]
                logger.info(f"Search logged successfully: ID {result['id']}")
                return {
                    'success': True, 
                    'log_id': result['id'],
                    'created_at': result['created_at']
                }
            else : 
                return {
                    'success': False
                }
            
        except Exception as e:
            logger.error(f"Failed to log search: {e}")
            return {'success': False, 'error': str(e)}

    def get_user_search_history(self, user_id: str, limit: int = 50) -> List[SearchLogModel]:
        """Get search history for a specific user"""
        query = """
            SELECT id, user_id, search_query, created_at, search_results, 
                   session_id, response_time_ms, ip_address, user_agent
            FROM search_logs 
            WHERE user_id = %s 
            ORDER BY created_at DESC 
            LIMIT %s;
        """
        
        try:
            results = self.db.execute_query(query, (user_id, limit))
            return [SearchLogModel.from_dict(row) for row in results] if results else []
        except Exception as e:
            logger.error(f"Failed to get search history: {e}")
            return []

    @staticmethod
    def generate_session_id() -> str:
        """Generate a unique session ID"""
        return f"session_{int(time.time())}_{str(uuid.uuid4())[:8]}"