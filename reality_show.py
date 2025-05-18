import datetime

# Data Classes
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Contestant:
    def __init__(self, name, performance_score):
        self.name = name
        self.votes = 0
        self.performance_score = performance_score
        self.eliminated = False
        self.elimination_date = None

    def __str__(self):
        status = f"ELIMINATED on {self.elimination_date}" if self.eliminated else "ACTIVE"
        return f"{self.name} | Votes: {self.votes} | Score: {self.performance_score} | {status}"

class RealityShow:
    def __init__(self, name):
        self.name = name
        self.contestants = []

    def add_contestant(self, contestant):
        self.contestants.append(contestant)

    def view_contestants(self):
        for c in self.contestants:
            print(c)

    def sort_contestants(self, by):
        active = [c for c in self.contestants if not c.eliminated]
        if by == "votes":
            sorted_list = sorted(active, key=lambda c: c.votes, reverse=True)
        else:
            sorted_list = sorted(active, key=lambda c: c.performance_score, reverse=True)
        for c in sorted_list:
            print(c)

    def eliminate_lowest_voted(self):
        active = [c for c in self.contestants if not c.eliminated]
        if not active:
            print("No contestants to eliminate.")
            return
        lowest = min(active, key=lambda c: c.votes)
        lowest.eliminated = True
        lowest.elimination_date = datetime.date.today()
        print(f"{lowest.name} has been eliminated this week.")

    def get_eliminated(self):
        return [c for c in self.contestants if c.eliminated]

    def show_insights(self):
        for c in self.contestants:
            print(f"{c.name}: Votes = {c.votes}, Performance = {c.performance_score}")


# Data Seeding
users = {
    "alice": User("alice", "pass123"),
    "bob": User("bob", "1234")
}

shows = []

def seed_data():
    s1 = RealityShow("Dance Battle")
    s1.add_contestant(Contestant("Liam", 8.5))
    s1.add_contestant(Contestant("Emma", 9.0))
    s1.add_contestant(Contestant("Noah", 7.8))

    s2 = RealityShow("Singing Stars")
    s2.add_contestant(Contestant("Olivia", 9.2))
    s2.add_contestant(Contestant("Mason", 8.1))
    s2.add_contestant(Contestant("Ava", 8.7))

    shows.extend([s1, s2])


# App Logic
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = users.get(username)
        if user and user.password == password:
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid credentials. Try again.")

def choose_show():
    print("\nAvailable Shows:")
    for i, show in enumerate(shows):
        print(f"{i + 1}. {show.name}")
    choice = int(input("Select a show: ")) - 1
    return shows[choice]

def vote_contestant(show):
    name = input("Enter contestant name to vote for: ")
    for c in show.contestants:
        if c.name.lower() == name.lower() and not c.eliminated:
            c.votes += 1
            print(f"Voted for {c.name}")
            return
    print("Invalid name or contestant is eliminated.")

def view_eliminated(show):
    eliminated = show.get_eliminated()
    if not eliminated:
        print("No eliminated contestants.")
    else:
        for c in eliminated:
            print(c)

def vote_wildcard(show):
    eliminated = show.get_eliminated()
    if not eliminated:
        print("No eliminated contestants.")
        return
    print("\nEliminated Contestants:")
    for i, c in enumerate(eliminated):
        print(f"{i + 1}. {c.name} (eliminated on {c.elimination_date})")

    choice = int(input("Select one to bring back: ")) - 1
    c = eliminated[choice]
    if (datetime.date.today() - c.elimination_date).days >= 30:
        c.eliminated = False
        c.elimination_date = None
        print(f"{c.name} has been brought back to the show!")
    else:
        print("Contestant is not eligible (30 days wait not completed).")


def main():
    seed_data()
    print("=== Welcome to the Reality Show Voting System ===")
    login()
    show = choose_show()

    while True:
        print("\n1. View Contestants")
        print("2. Vote for Contestant")
        print("3. Sort Contestants by Votes")
        print("4. Sort Contestants by Performance")
        print("5. Weekly Elimination")
        print("6. View Eliminated Contestants")
        print("7. Vote to Bring Back a Contestant")
        print("8. View Insights")
        print("9. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            show.view_contestants()
        elif choice == "2":
            vote_contestant(show)
        elif choice == "3":
            show.sort_contestants("votes")
        elif choice == "4":
            show.sort_contestants("performance")
        elif choice == "5":
            show.eliminate_lowest_voted()
        elif choice == "6":
            view_eliminated(show)
        elif choice == "7":
            vote_wildcard(show)
        elif choice == "8":
            show.show_insights()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
