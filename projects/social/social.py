from random import shuffle

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # create a list to hold all possible relationships
        rel_list = []

        # Add users: for the total number of users needed
        for x in range(1, num_users+1):
            # create a user with the name of it's request index
            self.add_user(x)
            # Create friendships: for every x, y in total of users created, generate all the possible sets
            for y in range(1, num_users+1):
                # add the possible relationship to the list
                rel_list.append((x, y))

        # shuffle the list of relationship possibilities
        shuffle(rel_list)

        # for every item to have an avg_friendships amount go over range
        for i in range((num_users * avg_friendships) // 2):
            # create a variable to keep track if it added
            added = False
            # if I haven't confirmed the add, repeat
            while added is not True:
                # pop off the first item in the relationship list
                curr_rel = rel_list.pop()
                # if the user has 2 more friends than average
                if len(self.friendships[curr_rel[0]]) < (avg_friendships + 2) and len(self.friendships[curr_rel[1]]) < (avg_friendships + 2):
                    # as long as the item friend ID is not larger than his friend
                    if curr_rel[0] > curr_rel[1]:
                        # add the relationship
                        self.add_friendship(curr_rel[0], curr_rel[1])
                        # set the added boolean to true 
                        added = True

    def get_neighbors(self, user_id):
        # if the user exists in the social network
        if user_id in self.friendships:
            # get the list of friends of this user
            return self.friendships[user_id]
        # if user does not exist, give error
        else:
            raise IndexError("That user does not exist!")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create a dictionary to store the relationships and paths
        visited = {}
        # create a queue to keep track of the user's I need to check
        to_visit = Queue()
        # add the start user to the queue as a list
        to_visit.enqueue([user_id])

        # while the to_visit queue is not empty
        while to_visit.size() > 0:
            # dequeue the first path from queue
            curr_path = to_visit.dequeue()
            # grab the last item in the path provided
            curr_user = curr_path[-1]
            # if the user has not been visited yet
            if curr_user not in visited:
                # add the user to the visited
                visited[curr_user] = curr_path
                # get the users related to the current user
                for neightbor in self.get_neighbors(curr_user):
                    # create a new path
                    new_path = curr_path.copy()
                    # add the current neighbor to new path
                    new_path.append(neightbor)
                    # add the new path with the new neighbor to queue
                    to_visit.enqueue(new_path)

        return visited

"""
populate_graph()
Understand: take in an integer as the amount of users and another one as the average amount of relationships.
Add a user for the amount of users requested. Create a list of all possible relationships. Add the relationships

get_all_social_paths()
Understand: given a user ID, return a dictionary containing all the extended relationships and their shortest path
Plan: BFS; Create a queue and enqueue the current user. Go through all the relationships adding
each to the queue and adding it and it's shortest path to the returned dictionary. 

"""

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
