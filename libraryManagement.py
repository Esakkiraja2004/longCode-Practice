users = []
admins = []
books =[]

class admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def __str__(self):
        return f"Admin Name: {self.name}, Password: {self.password}"
    
class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def __str__(self):
        return f"User Name: {self.name}, Password: {self.password}"
    
class validator:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def validate_admin(self):
        for  admin in admins:
            if admin.name == self.name and admin.password == self.password:
                print("________Login Successful________")
                print(f'\n __________Welcome Mr. {self.name}________')
                return True
            else:
                print("Incorrect admin credentials.")
                return False          

class add_book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        books.append(self)
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Book ID: {self.book_id}"
    
    


    
def main():

    #creteating admin
    a1 = admin("admin1", "123")
    a2 = admin("admin2", "123")

    admins.append(a1)
    admins.append(a2)

    while True:
        print("\nChoose an option:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            valid = validator(input("Enter admin name: "), input("Enter password: "))
            if valid.validate_admin():
                print('\n Add Books:')
                while True:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    book_id = input("Enter book ID: ")
                    add_book(title, author, book_id)
                    choice = input("Do you want to add another book? (yes/no): ")
                    if choice.lower()!= "yes":
                        break
            # Optional: Show all books added

        print("\nBooks in Library:")
        for book in books:
            print(book)




    

if __name__ == "__main__":
    main()