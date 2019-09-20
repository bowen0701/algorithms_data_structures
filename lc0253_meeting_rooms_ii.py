"""Leetcode 253. Meeting Rooms II (Premium)
Medium

URL: https://leetcode.com/problems/meeting-rooms-ii

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example1
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [[2,7]
Output: 1
Explanation: 
Only need one meeting room
"""

class SolutionMinHeap(object):
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    def minMeetingRooms(self, intervals):
        import heapq

        if not intervals or not intervals[0]:
            return 0

        # Sort intervals by start time.
        intervals.sort()

        # Use min heap to store end times.
        min_endtimes = []
        heapq.heappush(min_endtimes, intervals[0][1])

        for i in range(1, len(intervals)):
            # If start time is after min end time, remove the min end time.
            if min_endtimes[0] <= intervals[i][0]:
                heapq.heappop(min_endtimes)

            # Add end time to min heap.
            heapq.heappush(min_endtimes, intervals[i][1])

        return len(min_endtimes)


def main():
    # Output: 2.
    intervals = [[0,30],[5,10],[15,20]]
    print SolutionMinHeap().minMeetingRooms(intervals)

    # Output: 1.
    intervals = [[2,7]]
    print SolutionMinHeap().minMeetingRooms(intervals)


if __name__ == '__main__':
    main()