graph = {}
graph['you'] = ["Bob", "Claire", "Alice"]
graph['Alice'] = ['Peggy']
graph['Bob'] = ['Peggy', 'Anuj']
graph['Claire'] = ['Thom', 'Johnny']
graph['Peggy'] = []
graph['Anuj'] = []
graph['Thom'] = []
graph['Johnny'] = []

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

search_queue = deque()

# graph["you"] returns a list with Bob, Claire, Alice
# below adds them to the queue

search_queue += graph["you"]

while search_queue:     # while queue isnt empty
    person = search_queue.popleft()  # grabs first person off queue
    if person_is_seller(person):        # checks whether the person is a mango seller
        print(person + ' is a mango seller')
    else:
        search_queue += graph[person]       # Add all of this person's friends to the search queue

