## Задача 3: Документирование и устранение ошибок

**Цель:** Проверить навыки написания документации и способность к анализу и устранению ошибок в коде.

### Задание
```python
import sqlite3

def connect_to_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Exception as e:
        print(f"An error occurred: {e}")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TEBLE users(
                    id INTEGER PRIMARY KAY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER)""")
    conn.commit()

def insert_user(conn, user_name, user_age):
    cursor = conn.cursor()
    cursor.execute("INSER INTO users (name, age) VALUES (?, ?)", (user_name, user_age))
    conn.commit()

# Usage example
db_connection = connect_to_db('my_database.db')
create_table(db_connection)
insert_user(db_connection, 'Alice', 30)
```