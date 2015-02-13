#!/usr/bin/env
# Import modules
import sqlite3
# Connect to a database and create tables
db = sqlite3.connect('fillandsearch.sql')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS stuff (name TEXT, location TEXT, box TEXT)''')
db.commit()
# All the options in a function
def main():
    def organize(option):
        # Create option
        if option == 'Create':
            name = raw_input("Type the name of the item: ")
            location = raw_input("Type the name of the location: ")
            box = raw_input("Type the name of the box: ")
            cur.execute("INSERT INTO stuff VALUES (?, ?, ?);", (name, location, box))
            db.commit()
            print('Item is now stored in the database')
        # Search option
        elif option == 'Search':
            name = raw_input("Type the name of the item: ")
            cur.execute("SELECT * FROM stuff WHERE name=? OR box=? OR location=?", (name, name, name))
            print cur.fetchall()
        # Backup option
        elif option == 'Backup':
            con = sqlite3.connect('fillandsearch.sql')
            with open('dump.sql', 'w') as f:
                for line in con.iterdump():
                    f.write('%s\n' % line)
            print('Database is backed up and saved as dump.sql')
        # Delete option
        elif option == 'Delete':
            name = raw_input("Name of the item you want to delete: ")
            cur.execute("DELETE FROM stuff WHERE name=?", (name,))
            print "Total numbers of rows deleted: ", db.total_changes
            db.commit()
        else:
            print('Please choose from Create/Search/Backup or Delete')
    organize(raw_input('would you like to do create an item, search the database, make a backup, or delete an item? [Create/Search/Backup/Delete]: '))
if __name__ == "__main__":
    main()
