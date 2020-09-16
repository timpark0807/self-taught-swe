def MostImprovedStudent(students, scores):
    """
    @input 
        students :  arr[str]
        scores   :  arr[int]
        
    @output
        answer   :  int 
    
    @approach
        # hold a globalMax answer variable 
        # dictionary to map person to their lowest score 
        
        # iterate over the input arrays
            # if we have seen the persons test score
                # check if this persons improvement is the max improvement
                # update the dictionary if this score is lower than what is stored 
            # if we have NOT seen the persons test score
                # store this first score in a dictionary 
                # key = name , value = score 
    """
    n = len(students) 
    lowestScores = {}
    globalMaxImprovement = 0 
    
    for index in range(n):
        currStudent, currScore = students[index], scores[index]
        
        if currStudent in lowestScores:
            currImprovement = currScore - lowestScores[currStudent] 
            globalMaxImprovement = max(globalMaxImprovement, currImprovement) 
            lowestScores[currStudent] = min(lowestScores[currStudent], currScore)
        else:
            lowestScores[currStudent] = currScore 
            
    return globalMaxImprovement
    
    
    
    
    
    
    
    
