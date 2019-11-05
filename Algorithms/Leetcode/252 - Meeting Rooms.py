import unittest

class Solution:

    def __init__(self):
        pass

    def canAttendMeetings(self, times):
        """
        input: [[list]] -> List of Lists containing start/end times
        output: Bool -> True if no times overlap, False is there is overlap
        
        [[2,4], [7,10]]
        
        """

        times.sort()

        for index in range(1, len(times)):
            meeting_one = times[index-1]
            meeting_two = times[index]
            start = 0
            end = 1
            # If meeting 2 starts after meeting one, and meeting one ends after meeting 2 starts, False
            if meeting_one[end] > meeting_two[start]:
                return False

        return True
            


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_true_meeting_rooms(self):
        times = [[7,10],[2,4]]
        answer = self.s.canAttendMeetings(times)
        self.assertTrue(answer)

    def test_false_meeting_rooms(self):
        times = [[0,30],[5,10],[15,20]]
        answer = self.s.canAttendMeetings(times)
        self.assertFalse(answer)

if __name__ == '__main__':
    unittest.main()
