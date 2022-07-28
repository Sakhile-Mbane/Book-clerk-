# Create a program that can be used by a bookstore clerk. The program
# should allow the clerk to:
# ○ add new books to the database
# ○ update book information
# ○ delete books from the database
# ○ search the database to find a specific book.
# Create a database called ebookstore and a table called books. The table
# Populate the table with the above values. You can also add your own values
# if you wish.
# The program should present the user with the following menu:
# 1. Enter book
# 2. Update book
# 3. Delete book
# 4. Search books
# 0. Exit

import sqlite3

database = sqlite3.connect('ebookstore.db')

cursor = database.cursor()

# Create a table with the attributes id, Title, Author, Qty
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookstore (id PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')

database.commit()

# Populate the table with the below values.
id1 = 3001
Title1 = '''A Tale of Two
            Cities'''
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = '''Harry Potter and
            the
            Philosopher's
            Stone'''
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003
Title3 = '''The Lion, the
            Witch and the
            Wardrobe'''
Author3 = 'C. S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = '''The Lord of the
            Rings'''
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005
Title5 = '''Alice in
            Wonderland'''
Author5 = 'Lewis Carroll'
Qty5 = 12

table_values = [(id1, Title1, Author1, Qty1), (id2, Title2, Author2, Qty2), (id3, Title3, Author3, Qty3),
                (id4, Title4, Author4, Qty4), (id5, Title5, Author5, Qty5)]

cursor.executemany('''
    INSERT OR IGNORE INTO bookstore (id, Title, Author, Qty)
    VALUES (?,?,?,?)''', table_values
                   )
database.commit()


# The program should present the user with the following menu:
# 1. Enter book
# 2. Update book
# 3. Delete book
# 4. Search books
# 0. Exit


# ====== Functions ======

def enter_book(T, A, Q):
    cursor.execute('''
        INSERT OR IGNORE INTO bookstore (Title, Author, Qty)
        VALUES (?,?,?)''', (T, A, Q)
                   )
    database.commit()


def update_book(ID, B):
    update_attribute = input('Which attribute/ column to update id/ title / author or qty: ').lower()
    if update_attribute == 'id':
        cursor.execute('''
            UPDATE bookstore SET id = ?
            WHERE id = ?''', (ID, B)
                       )
        database.commit()
    elif update_attribute == 'title':
        cursor.execute('''
                    UPDATE bookstore SET Title = ?
                    WHERE title = ?''', (ID, B)
                       )
        database.commit()
    elif update_attribute == 'author':
        cursor.execute('''
                    UPDATE bookstore SET Author = ?
                    WHERE author = ?''', (ID, B)
                       )
        database.commit()
    elif update_attribute == 'qty':
        cursor.execute('''
                        UPDATE bookstore SET Qty = ?
                        WHERE Qty = ?''', (ID, B)
                       )
        database.commit()


def delete_book(ID__):
    cursor.execute('''
    DELETE FROM bookstore
    WHERE id = ?''', (ID__,))

    database.commit()


def search_book(ID_):
    if search_attribute == 'id':
        cursor.execute('''
            SELECT * FROM bookstore
            WHERE id = ? ''', (int(ID_))
                       )
        database.commit()
    elif search_attribute == 'author':
        cursor.execute('''
                    SELECT * FROM bookstore
                    WHERE Author = ? ''', (str(ID_))
                       )
        database.commit()


# Program to call the above functions

user = int(input('''1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit 
'''))

if user == 1:
    title = input('Enter the title of book: ')
    author = input('Enter the author of book: ')
    qty = int(input('Enter the qty of book: '))

    enter_book(title, author, qty)

elif user == 2:
    ID_ = int(input('Enter the id/ title / author or qty  of the book to update:'))
    to_be_restore = input('Enter the current value or entry to update')
    update_book(ID_, to_be_restore)
elif user == 3:
    id_delete = int(input('id to delete: '))
    delete_book(id_delete)
elif user == 4:
    search_attribute = input('Enter which attribute/ Column to search for a book (id/ author): ').lower()
    id_ = input('Search the book: ')

    search_book(id_)
elif user == 0:
    print('The program has quit.')
    exit()
else:
    print('The entered option does not exist.')
