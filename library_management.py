#Fatih Öter
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def book_adding(self):
        name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        release_date = input("Enter the release date of the book: ")
        number_of_pages = input("Enter the number of pages: ")
        book_info = name + "," + author + "," + release_date + "," + number_of_pages + "\n"
        self.file.write(book_info)
        print("Book added successfully.")        

    def books_listing(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = []
        if not lines or all(line == '' for line in lines):
            print("There are no books in the library.")
            return
        for line in lines:
            book_info = line.split(',')
            books.append(book_info)
        for book in books:
            print("Book: " + book[0] + ", Author: " + book[1])

    def book_remove(self):
        name = input("Enter the name of the book you want to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        updated_lines = []
        for line in lines:
            if name not in line:
                updated_lines.append(line)
        self.file.seek(0)
        self.file.truncate()
        for updated_line in updated_lines:
            self.file.write(updated_line)
        print("Book removed successfully.")

 

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")
    choice = input("Enter your choice (1-3, or Q): ").upper()

    if choice == '1':
        lib.books_listing()
    elif choice == '2':
        lib.book_adding()
    elif choice == '3':
        lib.book_remove()
    elif choice == 'Q':
        print("Exiting the library. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
