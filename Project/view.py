from connection import get_connection

def view_book():
  connection = get_connection()
  cursor = connection.cursor()
  sql = "SELECT * FROM books"
  cursor.execute(sql)
  books = cursor.fetchall()

  if books:
    print("List of books")
    for book in books:
      print(f"ID: {book[0]}, title: {book[1]}, author: {book[2]}")
  else:
   print("No books in base")

   cursor.close()
   connection.close()

view_book() 