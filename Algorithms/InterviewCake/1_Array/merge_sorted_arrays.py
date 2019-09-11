def merge_meetings(meetings):

    # Sort meetigs 
    sorted_meetings = sorted(meetings)

    # Add first meeting to the output list
    merged = [sorted_meetings[0]]

    # Iterate through non-merged meetings    
    for current_start, current_end in sorted_meetings[1:]:

        # Last meeting we will check against 
        last_start, last_end = merged[-1]

        # If meetings overlap
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged
    

meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
answer = merge_meetings(meetings)
