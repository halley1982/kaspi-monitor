import mysql.connector

# Настройки БД — замени на свои
db_config = {
    'host': 'your-db-host.com',  # Например, IP или хост через Plesk
    'user': 'your_db_user',
    'password': 'your_db_password',
    'database': 'your_db_name',
    'port': 3306
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Пример запроса
    cursor.execute("SELECT NOW()")
    print("Текущая дата/время на сервере:", cursor.fetchone())

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("Ошибка подключения к БД:", err)
