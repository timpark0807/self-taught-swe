def optimal_block(resources,requirements):
    # Preprocess 
    preprocess = get_preprocess(resources) 

    # Iterate over resources	
    answer=float(‘inf’) 
    for block in range(len(resources)): # block -> integer 
            # Get the minimum furthest value 
            local_furthest = 0 
            for requirement in requirements:
                    curr_requirement_distance=get_distance(block, preprocess)
                    local_furthest=max(local_furthest, curr_requirement_distance)
            answer = min(answer, local_furthest)
    return answer # minimum furthest value 
