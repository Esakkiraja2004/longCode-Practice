users =[]
admins =[]
service_providers =['1 : BASIC WASH RS : 100' , "2 : DETAILING RS : 200" , "3 : INTERIOR CLEANING RS : 1000"]
services =[]

class admin:
    def __init__(self,admin_id,  name , password):
        self.admin_id = admin_id
        self.name = name
        self.password = password

    def __str__(self):
        return(f"ADMIN ID : {self.admin_id} , NAME : {self.name}")
    

class user:
    def __init__(self,user_id,  name , password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def __str__(self):
        return(f"USER ID : {self.user_id} , NAME : {self.name}")
    
class providers:
    def __init__(self,provider_id , name , password ):
        self.provider_id = provider_id
        self.name = name
        self.password = password

    def __str__(self):
        return (F"PROVIDER ID : {self.provider_id} , NAME : {self.name}")
    
class adminvalidator :
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def valid(self):
        for a in admins:
            if self.name == a.name and self.password == a.password:
                print("\n")
                print("\n_________WELCOME TO THE ADMIN PAGE_________ ")
                return True
            else:
                print("invalid Data")
                return False

class userValidator:

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def valid(self):
        for a in users:
            if self.name == a.name and self.password == a.password:
                print("\n")
                print("\n_________WELCOME TO THE USER PAGE_________ ")
                return True
            else:
                print("invalid Data")
                return False
            
class ProviderValidator:

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def valid(self):
        for a in users:
            if self.name == a.name and self.password == a.password:
                print("\n")
                print("\n_________WELCOME TO THE USER PAGE_________ ")
                return True
            else:
                print("invalid Data")
                return False

class list_Service:
    def __init__(self):
        for i in service_providers:
            print(i)

class list_user:
    def __init__(self):
        for i in users:
            print(i)


def main():
    a1 = admin(1,"cooper",123)
    admins.append(a1)

    u1 = user(1,"raja",123)
    u2 = user(1,"manoji",123)
    users.append(u1)
    users.append(u2)

    p1 = providers(1,"MC CARS",123)
    p2 = providers(2,"DC CARS",123)
    service_providers.append(p1)
    service_providers.append(p2)

    while True:
        print("\n 1 : ADMIN")
        print("\n 2 : USER")
        print("\n 3 : PROVIDER")
        print("\n 4 : List USER :")
        c = int(input("Choose Login Type :"))
        if c == 1:
            name = input("Enter your name:")
            password = int(input("Enter your password:"))
            a = adminvalidator(name,password)
            a.valid()
            
            print("ADD PROVIDER : ")
            add_user_choice  = input("YES OR NO")
            if add_user_choice  == "YES":
                pro_id = int(input("Enter user ID: "))
                pro_name = input("Enter User Name:")
                pro_password = int(input("Enter Password"))
                p = providers(pro_id,pro_name,pro_password)
                service_providers.append(p)
                for i in service_providers:
                    print(i)


        if c == 2 :
            name = input("Enter your name:")
            password = int(input("Enter your password:"))
            u = userValidator(name,password)
            u.valid()
            s = list_Service()
            
            # c == int(input("Choose Services : "))
            # if c == 1:



        if c == 3 :
            name = input("Enter your name:")
            password = int(input("Enter your password:"))
            p = userValidator(name,password)
            p.valid()

        if c == 4:
            l = list_user()
            




if __name__ == "__main__":
    main()