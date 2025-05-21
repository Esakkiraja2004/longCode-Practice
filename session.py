users = []
admin = []
groceries = []
cart_details= []

class UserDetails:
    def __init__(self, id: int, Name: str, Email: str, Password: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        
class AdminDetails:
    def __init__(self, id: int, Name: str, Email: str, Password: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
        
class userValidation:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validateUser(self):
    
        for user in users:
            if user.name == self.username and user.password == self.password:
                print("User is valid")
                return user
            
class adminValidation:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validateUser(self):
    
        for user in admin:
            if user.name == self.username and user.password == self.password:
                print("Admin is valid")
                return user
        
class GroceryList:
    def __init__(self, id: int, name: str, quantity: str, price: str):
        self.groceryID = id
        self.name = name
        self.quantity = quantity
        self.price = price
        
class Category:
    def __init__(self, categoryId, categoryName, shopName, supplierName):
        self.categoryId = categoryId
        self.categoryName = categoryName    
        self.shopName = shopName
        self.supplierName = supplierName 
        
class categoriesList:
    def __init__(self):
        self.categories = [
            Category(1, "Fruits", 'palamudhir', 'Raju'),
            Category(2, "Vegetables", 'palamudhir nilayam', 'Mano'),
            Category(3, "Snacks", 'Anandha store', 'Ravi'),
        ]
        
class Grocery:
    def __init__(self, id: int, name: str, quantity: str, price: str, categoryId: int):
        self.groceryID = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.categoryId = categoryId
        
class GroceryLists(categoriesList):
    def __init__(self):
        super().__init__()
        self.groceries = [
            Grocery(1, "Apple", "1kg", 100, 1),
            Grocery(2, 'Cauliflower', '1kg', '40', 2),
            Grocery(3, 'Cabbage', '1kg', '30',2),
            Grocery(4, 'Potato', '1kg', '10', 2),
            Grocery(5, 'Onion', '1kg', '20',2),
            Grocery(6, 'Tomato', '1kg', '30', 2),
            Grocery(7, 'Chips', '1kg', '10', 3),
            
        ]
        
    def combine_grocery_and_category(self):
        for items in self.groceries:
            for category in self.categories:
                if category.categoryId == items.groceryID:
                    print(f"ID: {items.groceryID}, Name: {items.name}, Qty: {items.quantity}, Price: ₹{items.price}, Category: {category.categoryName}, Shop: {category.shopName}, Supplier: {category.supplierName}")
     
class cartItems:
    def __init__(self, cart_id, user_id, grocery_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.grocery_id = grocery_id
                   

class toBuyProducts(GroceryLists):
    def __init__(self, userId):
        super().__init__()
        self.userId = userId
    
    def products_to_customer(self):

        stayInCustomerMenu = True
        while stayInCustomerMenu:
            print("\n------------------")
            print("Customer Menu")
            print("1. display the products")
            print("2. Add to cart")
            print("3. Payment")
            print("4. Logout")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print("Products available:")
                self.combine_grocery_and_category()
                
            if choice == 2:
                #cart id, ussser id, grocery id
                selected_id = int(input('Enter the Grocery Item you like:'))
                cart_id = 1
                cart_items = cartItems(cart_id, self.userId, selected_id)
                cart_details.append(cart_items)
                print('....................', cart_details, vars(cart_details[0]))
                
                
                
                
            
    
        

if __name__ == "__main__":
    
    #creating objects of user
    user1 = UserDetails(1, "Kamali", "kamali@gmail.com", "kamali123")
    users.append(user1)
    user2 = UserDetails(2, "priya", "priya@gmail.com", "3456")
    users.append(user2)
    
    
    #creating objects of admin
    admin1 = AdminDetails(1, "swetha", "swetha@gmail.com", "swetha123")
    admin.append(admin1)
    admin2 = AdminDetails(2, "bawya", "bawya@gmail.com", "1234")
    admin.append(admin2)
    
    role = int(input("Enter your choice (1. admin/ 2. user): "))
    if role == 1:
        validate = adminValidation("swetha", "swetha123")
        validate.validateUser()
    
    elif role == 2:
        validate = userValidation("Kamali", "kamali123") #trying to log in 
        user_data = validate.validateUser()
        print('validate', vars(user_data))
        a = toBuyProducts(user_data.userID)
        a.products_to_customer()
    
