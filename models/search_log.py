from datetime import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass


class SearchLogModel:
    """Data model for search log entries"""

    id: Optional[int] = None
    user_id: str
    search_query: str
    session_id: str
    search_results: Optional[Dict[str, Any]] = None
    response_time_ms: Optional[int] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    created_at: Optional[datetime] = None


    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SearchLogModel':
        """Create model from dictionary"""
        return cls(
            id=data.get('id'),
            user_id=data['user_id'],
            search_query=data['search_query'],
            search_results=data.get('search_results'),
            session_id=data['session_id'],
            response_time_ms=data.get('response_time_ms'),
            ip_address=data.get('ip_address'),
            user_agent=data.get('user_agent'),
            created_at=data.get('created_at')
        )