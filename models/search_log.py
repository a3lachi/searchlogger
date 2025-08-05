from datetime import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class SearchLogModel:
    """Data model for search log entries"""
    user_id: str
    search_query: str
    session_id: str
    id: Optional[int] = None
    search_results: Optional[Dict[str, Any]] = None
    response_time_ms: Optional[int] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    created_at: Optional[datetime] = None


    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary to print results"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'search_query': self.search_query,
            'search_results': self.search_results,
            'session_id': self.session_id,
            'response_time_ms': self.response_time_ms,
            'ip_address': self.ip_address,
            'user_agent': self.user_agent,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    

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