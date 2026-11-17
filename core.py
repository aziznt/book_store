import pymysql
from pymysql import MySQLError

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="library_db"
    )


def add_book(book):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
        cursor.execute(query, book)
        connection.commit()
        print("✅ Kitob qo'shildi.")
    except MySQLError as e:
        print("❌ Xato (add_book):", e)
    finally:
        cursor.close()
        connection.close()

def list_books():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, author, year FROM books")
        rows = cursor.fetchall()
        return rows
    
    except MySQLError as e:
        print("❌ Xato (list_books):", e)
    finally:
        cursor.close()
        connection.close()

def update_book():
    book_id = int(input("Qaysi ID dagi kitobni yangilaysiz? "))

    new_title = input("Yangi nom (bo'sh qoldirsangiz o'zgarmaydi): ")
    new_author = input("Yangi muallif (bo'sh qoldirsangiz o'zgarmaydi): ")
    year_input = input("Yangi yil (bo'sh qoldirsangiz o'zgarmaydi): ")

    fields = []
    values = []

    if new_title:
        fields.append("title = %s")
        values.append(new_title)
    if new_author:
        fields.append("author = %s")
        values.append(new_author)
    if year_input:
        fields.append("year = %s")
        values.append(int(year_input))

    if not fields:
        print("⚠️ Hech narsa o'zgartirilmadi.")
        return

    values.append(book_id)  # WHERE uchun

    query = f"UPDATE books SET {', '.join(fields)} WHERE id = %s"

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()

        if cursor.rowcount == 0:
            print("❌ Bunday ID topilmadi.")
        else:
            print("✅ Kitob yangilandi.")
    except MySQLError as e:
        print("❌ Xato (update_book):", e)
    finally:
        cursor.close()
        connection.close()

def delete_book():
    book_id = int(input("Qaysi ID dagi kitobni o'chirasiz? "))

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM books WHERE id = %s"
        cursor.execute(query, (book_id,))
        connection.commit()

        if cursor.rowcount == 0:
            print("❌ Bunday ID topilmadi.")
        else:
            print("🗑️ Kitob o'chirildi.")
    except MySQLError as e:
        print("❌ Xato (delete_book):", e)
    finally:
        cursor.close()
        connection.close()

