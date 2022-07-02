class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        id = []
        lth = len(intervals)
        i = 0
        j = 0
        max = 0
        intervals.sort()
        # for i in range(0,len(intervals)-1):
        while i + 1 < lth:
            if intervals[i][1] >= intervals[i + 1][0] and intervals[i + 1][1] >= intervals[i][0]:
                if intervals[i][1] >= intervals[i + 1][1]:
                    max = intervals[i][1]
                else:
                    max = intervals[i + 1][1]
                if intervals[i][0] <= intervals[i + 1][0]:
                    min = intervals[i][0]
                else:
                    min = intervals[i + 1][0]
                intervals[i + 1][1] = max
                intervals[i + 1][0] = min
                # id.append(i+1)
                intervals.pop(i)
                lth -= 1
                i -= 1
            i += 1

        #         l=len(intervals)
        #         for i in range(0,l):
        #             # print(intervals[i])
        #             for j in range(0,l):
        #                 if i!=j:
        #                     if intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
        #                         id.append(j)
        #         id.reverse()
        #         for j in id:
        #             print(intervals)
        #             print(j)
        #             intervals.pop(j)
        #             print(intervals)

        return intervals