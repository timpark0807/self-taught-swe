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

def search(name):
    search_queue = deque()
    
    # graph["you"] returns a list with Bob, Claire, Alice
    # below adds them to the queue
    search_queue += graph["you"]
    
    # list to add people we have searched
    searched = []
    
    # while queue is not empty
    while search_queue:   
        
        # person we are checking is most left, first in queue
        person = search_queue.popleft()  
        
        # if this person has not been searched, go through indented
        # if this person has been searched, skip
        if not person in searched:
            
            # is this person equal to the name we are searching?
            if person == name:        
                print('Found person')
                
            # if not 
            else:
                # add the checked person's relationships to queue
                search_queue += graph[person]
                
                # add the the checked person to the searched list
                searched.append(person)

search('Thom')
