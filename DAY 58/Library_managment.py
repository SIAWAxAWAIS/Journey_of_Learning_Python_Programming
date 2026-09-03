class Library:
    def __init__(self):
        self.noOfBooks  = 0
        self.books = []

    def addBook(self , book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noOfBooks} Books. The books are:-")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("Tuba Tul Nasu")
l1.showInfo()
