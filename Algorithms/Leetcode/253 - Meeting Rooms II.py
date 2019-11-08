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
        rooms = [[times[0]]]

        for index in range(1, len(times)):
            meeting_two = times[index]
            start = 0
            end = 1
            for room in rooms:
                if room[-1][end] < meeting_two[start]:
                    room.append(meeting_two)
                    meeting_two = None
                    break

            if meeting_two:
                rooms.append([meeting_two])
                

        return len(rooms)
            


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_true_meeting_rooms(self):
        times = [[7,10],[2,4]]
        answer = self.s.canAttendMeetings(times)
        self.assertEqual(answer, 1)

    def test_false_meeting_rooms(self):
        times = [[0,30],[5,10],[15,20]]
        answer = self.s.canAttendMeetings(times)
        self.assertEqual(answer, 2)

if __name__ == '__main__':
    unittest.main()
