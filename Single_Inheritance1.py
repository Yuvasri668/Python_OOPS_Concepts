#Single Inheritance

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("Book details:")
        print("The title  of the book is:",self.title)
        print("The author of the book is:",self.author)


class IssuedBook(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    

    def display_issued_book_details(self):
        print("Issued book details:")
        print("The title of the book is:",self.title)
        print("The author of the book is:",self.author)
        print("The name of the person issued to is:",self.issued_to)
        print("The date of issued is:",self.issued_date)

class_obj=IssuedBook("python","yuva","students","04-02-26")
class_obj.display_issued_book_details()
class_obj.display_book_details()