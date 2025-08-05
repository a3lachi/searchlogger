# 🔍 SearchLogger

SearchLogger is a simple and efficient logging system for tracking search queries. It’s designed to help developers or businesses store, analyze, and understand user search behavior.



## 🚀 Features

- ✅ Logs search terms in real-time
- 📅 Stores timestamps for each query
- 🌐 IP or user-based tracking (optional)
- 📊 Easy integration with analytics or dashboards
- 🧩 Simple to plug into existing applications


## 🛠️ Technologies Used

 - Python
 - PostgreSQL


## 📦 Setup Instructions
```bash
git clone https://github.com/a3lachi/searchlogger.git
cd searchlogger
pip install -r requirements.txt
cp .env.example .env # Edit .env with your database credentials
psql -d searchdb -f database/schema.sql
python main.py
```

## 🏗️ Project Structure
```bash
searchlogger/
├── requirements.txt
├── .env
├── README.md
├── config/
│   ├── __init__.py
│   └── database.py
├── models/
│   ├── __init__.py
│   └── search_log.py
├── database/
│   ├── __init__.py
│   ├── manager.py
│   └── schema.sql
├── services/
│   ├── __init__.py
│   ├── search_logger.py
│   └── analytics.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   └── routes.py
├── utils/
│   ├── __init__.py
│   └── logger.py
└── main.py
```