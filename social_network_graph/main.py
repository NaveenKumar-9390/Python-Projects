class SocialNetwork:

    def __init__(self):
        self.graph = {}

    # add user
    def add_user(self, user):

        if user not in self.graph:
            self.graph[user] = []
            print(user, "added to network")

        else:
            print("User already exists")

    # add friendship
    def add_friend(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("User not found")
            return

        if user2 not in self.graph[user1]:

            self.graph[user1].append(user2)
            self.graph[user2].append(user1)

            print(user1, "and", user2, "are now friends")

        else:
            print("They are already friends")

    # show friends
    def show_friends(self, user):

        if user in self.graph:
            print("Friends of", user, ":", self.graph[user])

        else:
            print("User not found")

    # mutual friends
    def mutual_friends(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("User not found")
            return

        mutual = set(self.graph[user1]).intersection(self.graph[user2])

        print("Mutual friends:", list(mutual))

    # display network
    def display_network(self):

        print("\nSocial Network Graph")

        for user in self.graph:
            print(user, "->", self.graph[user])


def main():

    sn = SocialNetwork()

    while True:

        print("\n1 Add User")
        print("2 Add Friend")
        print("3 Show Friends")
        print("4 Mutual Friends")
        print("5 Show Network")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            user = input("Enter username: ")
            sn.add_user(user)

        elif choice == "2":

            u1 = input("User1: ")
            u2 = input("User2: ")

            sn.add_friend(u1, u2)

        elif choice == "3":

            user = input("Enter username: ")
            sn.show_friends(user)

        elif choice == "4":

            u1 = input("User1: ")
            u2 = input("User2: ")

            sn.mutual_friends(u1, u2)

        elif choice == "5":

            sn.display_network()

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
