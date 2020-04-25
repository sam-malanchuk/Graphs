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

def earliest_ancestor(ancestors, starting_node):
    # var to hold oldest ancestor
    oldest_ancestor = -1
    # create an empty dictionary to hold relationships
    relationships = {}
    # grab each pair of relationships and store in dict
    for rel_pair in ancestors:
        # if the child not already saved
        if rel_pair[1] not in relationships:
            # create a set for it
            relationships[rel_pair[1]] = set()
            relationships[rel_pair[1]].add(rel_pair[0])
        # if child exists
        else: 
            # add a parent to set
            relationships[rel_pair[1]].add(rel_pair[0])
    # create a queue to track the individuals I need to check
    plan_to_visit = Queue()
    # add the starting node to the queue
    plan_to_visit.enqueue(starting_node)

    # while the plan to visit queue is not empty
    while plan_to_visit.size() > 0:
        # grab the first item from the queue
        curr_node = plan_to_visit.dequeue()
        # if the current individual has parents
        if curr_node in relationships:
            # get his parents
            get_parents = relationships[curr_node]
            # for each parent individual has
            for parent in get_parents:
                # add to queue
                plan_to_visit.enqueue(parent)
        # if no parents found, individual is oldest ancestor
        else:
            # if the individual is starting node, don't add
            if curr_node != starting_node:
                oldest_ancestor = curr_node
    # return the oldest ancestor
    return oldest_ancestor

# Understand: Given an individual, locate the oldest
# ancestor or if tied, the one with the lowest numeric ID.
# If individual has no parents listed return -1.

# How do I find the neighbor ancestors?

# Plan: Transverse through each individual keeping track
# of the path until you find the input individual, return the
# individual at the beginning of the path.
