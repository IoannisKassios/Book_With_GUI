from connection import get_connection
import tkinter as tk
from tkinter import messagebox



def insert_book(title,author,publication_year,genre):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO books(title,author,publication_year,genre) VALUES (%s,%s,%s,%s,)"
    values = (title, author, publication_year,genre)
    #INSERT INTO books(title,author,publication_year,genre) VALUES (title,author,publication_year,genre)
    cursor.execute(query,values)
    connection.commit()
    messagebox.showinfo("Success!", "The book was added.")
    cursor.close()
    connection.close()
  except Exception as e:
    messagebox.showerror("Error", f"An error has been occured: {e}.")


def submit():
  title = entry_title.get()
  author = entry_author.get()
  genre = entry_genre.get()

  try:
    publication_year = int(entry_year.get())
  except ValueError:
    messagebox.showerror("Error", "Insert all variables!")
    return
  
  insert_book(title,author,publication_year,genre)

  entry_title.delete(0)
  entry_author.delete(0)
  entry_genre.delete(0)

root = tk.Tk()
root.title("Insert book")
root.geometry("400x400")

tk.Label(root,text="Book Title: ").pack(pady=10)
entry_title = tk.Entry(root, width = 40)
entry_title.pack()

tk.Label(root,text="Author: ").pack(pady=10)
entry_author = tk.Entry(root, width = 40)
entry_author.pack()

tk.Label(root,text="Year: ").pack(pady=10)
entry_year = tk.Entry(root, width = 40)
entry_year.pack()

tk.Label(root,text="Genre: ").pack(pady=10)
entry_genre = tk.Entry(root, width = 40)
entry_genre.pack()

tk.Button(root, text="Book entry", command=submit).pack(pady=10)

root.mainloop()