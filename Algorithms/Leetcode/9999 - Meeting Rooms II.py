def meetingRooms(schedules):

    arr = [0] * 25

    for schedule in schedules:
        for time in range(schedule[0], schedule[1]+1):
            arr[time] += 1

    return max(arr)

schedules = [[2,7],[1,5],[3,5]]
print(meetingRooms(schedules))

    
