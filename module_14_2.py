import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age  INTEGER NOT NULL,
balance INTEGER
)
''')

for num in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{num}", f"example{num}@gmail.com", num * 10, 1000))

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute("SELECT COUNT (*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM (balance) FROM Users")
all_balances = cursor.fetchone()[0]

if total_users > 0:
    average_balance = all_balances / total_users
    print(f'Средний баланс всех пользователей: {average_balance}')
else:
    print('Нет пользователей для расчета среднего баланса.')

connection.commit()
connection.close()