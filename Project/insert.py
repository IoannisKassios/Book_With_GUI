from connection import get_connection

def insert_book(title,author,publication_year,genre):
  connection = get_connection()
  cursor = connection.cursor()
  query = "INSERT INTO books(title,author,publication_year,genre) VALUES (%s,%s,%s,%s,)"
  values = (title, author, publication_year,genre)
  cursor.execute(query,values)
  connection.commit()
  print("The book is connected to the database")
  cursor.close()
  connection.close()

title = input("Insert the title")
author = input("Insert the author")
publication_year = int(input("Insert the date the book was made"))
genre = input("Insert the type of book")


insert_book(title,author,publication_year,genre)