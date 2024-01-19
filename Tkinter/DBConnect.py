import sqlite3

class DBconnect:
    def __init__(self):
        self.connection = sqlite3.connect('mybase.db')
        self.cursor = self.connection.cursor()

    def ShowData(self):
        printer = self.cursor.execute('''SELECT * FROM example_table''')
        print(printer.fetchall())

dbconnect = DBconnect()