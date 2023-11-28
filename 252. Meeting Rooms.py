class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        end_time = -1
        for interval in sorted(intervals, key = lambda interval: interval[0]):
            if interval[0] < end_time:
                return False
            end_time = interval[1]
        return True