import sqlite3
from sqlite3 import Connection


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключунно!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa(id INTEGER PRIMERY KEY, username TEXT, name TEXT, age INTEGER, gender TEXT, region TEXT, photo TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES(?,?,?,?,?,?,?)", tuple(data.values()))    
        db.commit()