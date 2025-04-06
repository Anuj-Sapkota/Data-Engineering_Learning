# TODO: Create a basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret  = "This is a secret attribute"
    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    # TODO: Create discount
    def setDiscount(self, amount):
        self._discount = amount
# TODO: Create instance of the class
book1 = Book("Brave new world", "Leo Tolstoy" ,1225, 39.95)
book2 = Book("War and peace", "JD Salinger", 234, 29.25)

# TODO: print the price of the book1
# print(book1.getPrice())
book2.setDiscount(0.25)
# print(book2.getPrice())
# TODO: print the class and property
# print(book1)
# print(book1.title)
print(book2._Book__secret)