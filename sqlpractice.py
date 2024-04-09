import sqlite3

con = sqlite3.connect("workers.db")
cursor = con.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS workers(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,
age INTEGER,
salary INTEGER)
""")

def init():
    workers = [("Ладюша", 18, 400), ("Дилярушка", 17, 500), ("Лейладжон", 14, 500), ("Аделинаджон", 16, 1000),
               ("Элинушка", 19, 500), ("Анюша", 15, 1000), ("Эльзахон", 17, 2000), ("Амалишка", 18, 1700), ("Сонюша", 16, 2540), ("Каринушка", 16, 1890),
               ("Луизахон", 18, 2570), ("Настюша (Шеф)", 14, 1698), ("Иделябону", 19, 2578)]
    cursor.executemany("INSERT INTO workers (Name, age, salary) VALUES (?, ?, ?)", workers)

def limittask1():
    cursor.execute("SELECT * FROM workers LIMIT 6")
    print(cursor.fetchall())

def limittask2():
    cursor.execute("SELECT * FROM workers LIMIT 3 OFFSET 1")
    print(cursor.fetchall())

def orderByTask1():
    cursor.execute("SELECT * FROM workers ORDER BY salary")
    print(cursor.fetchall())

def orderByTask2():
    cursor.execute("SELECT * FROM workers ORDER BY salary DESC")
    print(cursor.fetchall())

def orderByTask3():
    cursor.execute("SELECT * FROM workers WHERE Id >= 2 AND Id <= 6 ORDER BY age")
    print(cursor.fetchall())

def countTask1():
    cursor.execute("SELECT COUNT(*) FROM workers")
    print(cursor.fetchall())

def countTask2():
    cursor.execute("SELECT COUNT(*) FROM workers WHERE salary == 300")
    print(cursor.fetchall())

def likeTaskInit():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pages(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT,
    article TEXT)
    """)
    pages = [("Архипов Артем", "В своей статье рассказывает о машинах."),
             ("Бабаджанов Камолджон", "Написал статью об инфляции."),
             ("Веткин Даниил", "Придумал новый химический элемент."),
             ("Коснырев Лев", "Также писал о машинах."),
             ("Низамов Ильнар", "Написал статью о том, как разрабатывать элементы дизайна."),
             ("Мубаракшин Булат", "Написал статью о своей девушке."),
             ("Трифонов Илья", "Также писал о девушке")]
    cursor.executemany("INSERT INTO pages (author, article) VALUES (?, ?)", pages)
def likeTask1():
    cursor.execute("SELECT * FROM pages WHERE author LIKE '%ов %'")
    print(cursor.fetchall())

def likeTask2():
    cursor.execute("SELECT * FROM pages WHERE article LIKE '%элемент%'")
    print(cursor.fetchall())

def likeTask3():
    cursor.execute("SELECT * FROM workers WHERE age LIKE '3_'")
    print(cursor.fetchall())

def likeTask4():
    cursor.execute("SELECT * FROM workers WHERE Name LIKE '%я'")
    print(cursor.fetchall())

def selectTask1():
    cursor.execute("SELECT * FROM workers WHERE Id == 3")
    print(cursor.fetchall())

def selectTask2():
    cursor.execute("SELECT * FROM workers WHERE salary == 1000")
    print(cursor.fetchall())

def selectTask3():
    cursor.execute("SELECT * FROM workers WHERE age == 23")
    print(cursor.fetchall())

def selectTask4():
    cursor.execute("SELECT * FROM workers WHERE salary > 400")
    print(cursor.fetchall())

def selectTask5():
    cursor.execute("SELECT * FROM workers WHERE salary >= 500")
    print(cursor.fetchall())

def selectTask6():
    cursor.execute("SELECT * FROM workers WHERE salary != 500")
    print(cursor.fetchall())

def selectTask7():
    cursor.execute("SELECT * FROM workers WHERE salary <= 900")
    print(cursor.fetchall())

def selectTask8():
    cursor.execute("SELECT age, salary FROM workers WHERE Name == 'Вася'")
    print(cursor.fetchall())

selectTask8()
con.commit()