class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Book:{self.title} by {self.author}, Price ₹{self.price}"
    
    def __repr__(self):
         return f"Book(title='{self.title}', author='{self.author}', price={self.price})"
    
obj=Book("Love story","Yuva",5000)
obj1=Book("Lonely","Jagan",2000)

print(obj)
print(obj1)
print([obj, obj1])