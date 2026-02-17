class Library:   #bluefprint for library
    def __init__(self, Library_name, books):
        self.Library_name = Library_name
        self.books = books
        self.total_books = 0  
    
    def set_total_books(self, total_books):  
        self.total_books = int(total_books)  
        return self
    
# object
library1 = Library("Indian Library", ["Indian History", "Geography of India"])
library2 = Library("World Library", ["World History", "Geography of World"])


total1 = input("Enter total books for Indian library: ")
library1.set_total_books(total1)

total2 = input("Enter total books for World library: ")
library2.set_total_books(total2)

# Print results
print(f"{library1.Library_name} has total books: {library1.total_books} and it is related to {library1.books}")
print(f"{library2.Library_name} has total books: {library2.total_books} and it is related to {library2.books}")
