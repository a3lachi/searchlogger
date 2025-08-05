-- Create search_logs table
CREATE TABLE IF NOT EXISTS search_logs (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    search_query TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    search_results JSONB,
    session_id TEXT NOT NULL,
    response_time_ms INTEGER,
    ip_address INET,
    user_agent TEXT
);