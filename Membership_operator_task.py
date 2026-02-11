class Library:
    def __init__(self, books):
        self.books = books  
    def __contains__(self,item):
        return item in self.books

obj=Library(["Python","Java","C"])
print("Python" in obj) 
print("HTML" in obj) 
