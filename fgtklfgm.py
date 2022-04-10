import sqlite3

con = sqlite3.connect('users_database.db')
cur = con.cursor()
cur.execute('''UPDATE dict SET part_of_speech == "gerunds"
               WHERE part_of_speech = "gerund"''')
con.commit()
