import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def get_connection():
    """Создание соединения с базой данных"""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def create_tables():
    """Создание таблиц базы данных"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            first_name VARCHAR(255),
            balance DECIMAL(10, 2) DEFAULT 0,
            status VARCHAR(50) DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Таблица заданий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            platform VARCHAR(50) NOT NULL,
            company_name VARCHAR(255),
            reward DECIMAL(10, 2),
            description TEXT,
            total_count INTEGER,
            completed_count INTEGER DEFAULT 0,
            status VARCHAR(50) DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Таблица выполнений
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS task_completions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            task_id INTEGER REFERENCES tasks(id),
            screenshot_url VARCHAR(500),
            status VARCHAR(50) DEFAULT 'pending',
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            verified_at TIMESTAMP
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Таблицы созданы успешно")

if __name__ == "__main__":
    create_tables()
