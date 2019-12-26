import unittest

class Solution:

    def calendars(self, timeslot, calendar1, calendar2, bound1, bound2):
        # Combine all times to a single calendar array
        calendar = calendar1 + calendar2

        # Convert all times into an integer
        # Format: hour.minutes where minutes = minutes/60
        for index, interval in enumerate(calendar):
            calendar[index] = self.time_to_integer(interval)

        calendar.sort()
        temp = [calendar[0]]

        # Check Overlaps, Merge when necessary 
        for index in range(1, len(calendar)):
            curr_interval = calendar[index]
            check_interval = temp[-1]
            if self.overlap(check_interval, curr_interval):
                temp[-1] = self.merge(check_interval, curr_interval)
            else:
                temp.append(curr_interval)
        
        # Instantiate lower and higher bound for meeting times
        temp_bound1 = self.time_to_integer(bound1)
        temp_bound2 = self.time_to_integer(bound2)
        low = max(temp_bound1[0], temp_bound2[0])
        high = min(temp_bound1[1], temp_bound2[1])
        timeslot_ = timeslot/60
        
        retval = []

        # Edge Case: Before
        # If earliest start time minus lower bound is greater than time slot, we can fit a meeting before any meetings.
        if temp[0][0] - low >= timeslot_:
            retval.append([low, temp[0][0]])
        
        for index in range(1, len(temp)):
            curr = temp[index]
            prev = temp[index-1]
            if curr[0] - prev[1] >= timeslot_:
                retval.append([prev[1], curr[0]])

        # Edge Case: After 
        # If higher bound minus latest end time is greater than timeslot, we can fit a meeting after the last meeting. 
        if high - temp[-1][1] >= timeslot_:
            retval.append([temp[-1][1], high])

        # Convert values back to string
        for index, interval in enumerate(retval):
            retval[index] = self.integer_to_time(interval)

        return retval

    def overlap(self, check_interval, curr_interval):
        front = max(check_interval[0], curr_interval[0])
        back = min(check_interval[1], curr_interval[1])
        return back - front >= 0

    def merge(self, interval1, interval2):
        front = min(interval1[0], interval2[0])
        back = max(interval1[1], interval2[1])
        return [front, back]

    def time_to_integer(self, interval):
        retval = []
        for time in interval:
            temp = time.split(':')
            hour = int(temp[0])
            minute = int(temp[1])/60
            retval.append(hour + minute)
        return retval

    def integer_to_time(self, interval):
        retval = []
        for integer in interval:
            hour, minute = divmod(integer, 1)
            minute *= 60
            if minute == 0:
                minute = '00'
            else:
                minute = str(int(minute))
            retval.append(str(int(hour))+':'+minute)
        return retval
        

class TestSolution(unittest.TestCase):

    def test_one(self):
        calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00','18:00']]
        calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
        bound1 = ['9:00', '20:00']
        bound2 = ['10:00', '18:30']
        timeslot = 30

        self.s = Solution()
        ans = self.s.calendars(timeslot, calendar1, calendar2, bound1, bound2)
        self.assertEqual(ans, [['11:30', '12:00'], ['15:00','16:00'], ['18:00', '18:30']])


if __name__ == '__main__':
    unittest.main()
