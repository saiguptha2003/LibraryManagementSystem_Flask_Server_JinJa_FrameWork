import pymysql

# Establishing a connection to the database
def connect():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Pandusai@2003', db='libManagement')
        return conn
    except:
        return False
def insert_book(book_id, title, author_id, isbn, published_year, quantity):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Book (Book_ID, Title, Author_ID, ISBN, Published_Year, Quantity) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (book_id, title, author_id, isbn, published_year, quantity))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()
    else:
        return False

# Inserting data into the Author table
def insert_author(author_id, author_name, birth_date, nationality):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Author (Author_ID, Author_Name, Birth_Date, Nationality) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (author_id, author_name, birth_date, nationality))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()
    else:
        return False

# Inserting data into the Member table
def insert_member(member_id, name, address, email, phone):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Member (Member_ID, Name, Address, Email, Phone) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (member_id, name, address, email, phone))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()
    else:
        return False

# Inserting data into the Loan table
def insert_loan(loan_id, book_id, member_id, loan_date, return_date):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Loan (Loan_ID, Book_ID, Member_ID, Loan_Date, Return_Date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (loan_id, book_id, member_id, loan_date, return_date))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()
    else:
        return False

# Inserting data into the Genre table
def insert_genre(genre_id, genre_name):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Genre (Genre_ID, Genre_Name) VALUES (%s, %s)"
            cursor.execute(query, (genre_id, genre_name))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()
    else:
        return False


# Function to retrieve data from the Book table
def get_books():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Book"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Function to retrieve data from the Author table
def get_authors():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Author"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Function to retrieve data from the Member table
def get_members():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Member"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Function to retrieve data from the Loan table
def get_loans():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Loan"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Function to retrieve data from the Genre table
def get_genres():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Genre"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

# Example usage
books_data = get_books()
authors_data = get_authors()
members_data = get_members()
loans_data = get_loans()
genres_data = get_genres()

# Use the retrieved data as needed
print("Books:", books_data)
print("Authors:", authors_data)
print("Members:", members_data)
print("Loans:", loans_data)
print("Genres:", genres_data)