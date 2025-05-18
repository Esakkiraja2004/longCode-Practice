users =[]
routes = []
buses =[]

class user:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def __str__(self):
        return f"User Name: {self.name}, Password: {self.password}"

class userValidator:
    def __init__(self,name, password):
        self.name = name
        self.password = password

    def validate_user(self):
        for u in users:
            if self.name  == u.name and self.password == u.password:
                print("________Login Successful________")
                print(f'\n __________Welcome Mr . {self.name}________')
                return True
            else:
                print("_________Login Failed_________")
                return False
        
class route:
    def __init__(self, origin, destination, distance, time, fare):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.time = time
        self.fare = fare
    
    def __str__(self):
        return f"Origin: {self.origin}, Destination: {self.destination}, Distance: {self.distance} km, Time: {self.time} hours, Fare: {self.fare}"

class bus:
    def __init__(self, busName, busNumber, route):
        self.busName = busName
        self.busNumber = busNumber
        self.route = route

    def __str__(self):
        return f"Bus Name: {self.busName}, Bus Number: {self.busNumber}, Route: {self.route}"
    
class booking:
    def __init__(self,name , route, bus, date, time,seat):
        self.name = name
        self.route = route
        self.bus = bus
        self.date = date
        self.time = time
        self.seat = seat

    def display_booking_details(self):
        if self.bus.route == self.route:
            print(f"Booking Details: \n \nName: {self.name} \nRoute: {self.route} \nBus: {self.bus} \nDate: {self.date} \nTime: {self.time} \nSeat: {self.seat}")
            print(f"Total Fare: {self.bus.route.fare}")
            print("_______________________________")
            return True
        
def main():

    # Add user credentials

    u1  = user("raja", 123)
    users.append(u1)

    u2 = user("ramesh", 456)
    users.append(u2)

    # Add routes and buses

    r1 = route("NELLAI" , "CHENNAI" , 700 , 9 , 1000)
    r2 = route("CHENNAI" , "NELLAI" , 700 , 10, 1000)

    routes.append(r1)
    routes.append(r2)

    b1 = bus("InterCity", 1, r1)
    b2 = bus("National", 2, r2)

    buses.append(b1)
    buses.append(b2)

    # User Login Interface

    i1 = input("Enter your name: ")
    i2 =   int(input("Enter your password: "))

    validator = userValidator(i1, i2)
    validator.validate_user()

    # Booking Interface
    print("\nChoose your route:")
    for i, r in enumerate(routes):
        print(f"{i+1}. {r}")

    print("\n")

    choice = int(input("Enter your choice: ")) -1
    r = routes[choice]
    b = buses[choice]
    name = input("Enter your name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    s = input("Enter seat number: ")
    
    book = booking(name, r, b, date, time , s)
    print('\n Booking Successful!  \n')
    book.display_booking_details()

if __name__ == "__main__":
    main()