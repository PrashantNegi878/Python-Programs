class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        total = 0
        arr = []
        for i in range(len(start)):
            arr.append([end[i], start[i]])
        arr.sort()
        # print(start,end)
        endval = 0
        for i in range(len(end)):
            if arr[i][1] > endval:
                # print(start[i],endval)
                total += 1
                endval = arr[i][0]
            i += 1
        return (total)