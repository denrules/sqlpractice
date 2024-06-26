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

def orAndTask1():
    cursor.execute("SELECT * FROM workers WHERE age > 25 AND age <= 28")
    print(cursor.fetchall())

def orAndTask2():
    cursor.execute("SELECT * FROM workers WHERE Name == 'Аделинаджон'")
    print(cursor.fetchall())

def orAndTask3():
    cursor.execute("SELECT * FROM workers WHERE Name == 'Анюша' OR Name == 'Настюша (Шеф)'")
    print(cursor.fetchall())

def orAndTask4():
    cursor.execute("SELECT * FROM workers WHERE Name != 'Луизахон'")
    print(cursor.fetchall())

def orAndTask5():
    cursor.execute("SELECT * FROM workers WHERE age == 27 OR salary == 1000")
    print(cursor.fetchall())

def orAndTask6():
    cursor.execute("SELECT * FROM workers WHERE (age >= 23 AND age < 27) OR salary == 1000")
    print(cursor.fetchall())

def orAndTask7():
    cursor.execute("SELECT * FROM workers WHERE (age >= 23 AND age <= 27) OR (salary >= 400 AND salary <= 1000)")
    print(cursor.fetchall())

def orAndTask8():
    cursor.execute("SELECT * FROM workers WHERE age == 27 OR salary != 400")
    print(cursor.fetchall())

def insertTask1():
    cursor.execute("INSERT INTO workers (Name, age, salary) VALUES('Никита', 26, 300)")
    cursor.execute("SELECT * FROM workers")
    print(cursor.fetchall())
    cursor.execute("DELETE FROM workers WHERE id > 13")

def insertTask2():
    cursor.execute("INSERT INTO workers (Name, salary) VALUES('Светлана', 1200)")
    cursor.execute("SELECT * FROM workers")
    print(cursor.fetchall())
    cursor.execute("DELETE FROM workers WHERE id > 13")

def insertTask3():
    cursor.execute("INSERT INTO workers (Name, age, salary) VALUES ('Ярослав', 30, 1200), ('Петр', 31, 1000)")
    cursor.execute("SELECT * FROM workers")
    print(cursor.fetchall())
    cursor.execute("DELETE FROM workers WHERE id > 13")

def deleteTask1():
    cursor.execute('DELETE FROM workers WHERE id == 7')
    cursor.execute('SELECT * FROM workers')
    print(cursor.fetchall())
    cursor.execute("INSERT INTO workers (id, Name, age, salary) VALUES (7, 'Эльзахон', 17, 2000)")

def deleteTask2():
    cursor.execute("DELETE FROM workers WHERE Name == 'Коля'")

def deleteTask3():
    cursor.execute("DELETE FROM workers WHERE age == 23")

def updateTask1():
    cursor.execute("UPDATE workers SET salary = 300 WHERE Name == 'Вася'")

def updateTask2():
    cursor.execute("UPDATE workers SET age = 35 WHERE Id == 4")

def updateTask3():
    cursor.execute("UPDATE workers SET salary = 700 WHERE salary == 500")

def updateTask4():
    cursor.execute("UPDATE workers SET age = 23 WHERE Id >= 2 AND Id <= 5")

def updateTask5():
    cursor.execute("UPDATE workers SET Name = 'Женя', salary = 900 WHERE Name == 'Вася'")

def inTask1():
    cursor.execute("SELECT * FROM workers WHERE Id IN (1, 2, 3, 5, 14)")
    print(cursor.fetchall())

def inTask2():
    cursor.execute("SELECT * FROM workers WHERE Name IN ('eee', 'bbb', 'zzz')")
    print(cursor.fetchall())

def inTask3():
    cursor.execute("SELECT * FROM workers WHERE Id IN(1, 2, 3, 7, 9) AND Name IN ('user', 'admin', 'ivan') AND salary > 300")
    print(cursor.fetchall())

def betweenTask1():
    cursor.execute('SELECT * FROM workers WHERE salary BETWEEN 100 AND 1000')
    print(cursor.fetchall())

def betweenTask2():
    cursor.execute('SELECT * FROM workers WHERE Id BETWEEN 3 AND 10 AND salary BETWEEN 300 AND 500')
    print(cursor.fetchall())

def asTask1():
    cursor.execute('SELECT Id AS userId, Name AS userName, salary AS userSalary FROM workers ')
    print(cursor.fetchall())

def distinctTask1():
    cursor.execute('SELECT DISTINCT salary FROM workers')
    print(cursor.fetchall())

def distinctTask2():
    cursor.execute('SELECT DISTINCT age FROM workers')
    print(cursor.fetchall())

def minMaxTask1():
    cursor.execute('SELECT MIN(salary) FROM workers')
    print(cursor.fetchall())

def minMaxTask2():
    cursor.execute('SELECT MAX(salary) FROM workers')
    print(cursor.fetchall())

def sumTask1():
    cursor.execute('SELECT SUM(salary) FROM workers')
    print(cursor.fetchall())

def sumTask2():
    cursor.execute('SELECT SUM(salary) FROM workers WHERE age >= 21 AND age <= 25')
    print(cursor.fetchall())

def sumTask3():
    cursor.execute('SELECT SUM(salary) FROM workers WHERE Id IN (1, 2, 3, 5)')
    print(cursor.fetchall())

def avgTask1():
    cursor.execute('SELECT AVG(salary) FROM workers')
    print(cursor.fetchall())

def avgTask2():
    cursor.execute('SELECT AVG(age) FROM workers')
    print(cursor.fetchall())

avgTask2()
con.commit()