class Solution:
    def areOverlapped(self, interval1, interval2):
        areOverlapped = (interval1[0] <= interval2[0]) and (interval1[1] >= interval2[0])  #interval1 ends after interval2 starts but starts before interval2 starts
        areOverlapped = areOverlapped or (interval2[0] <= interval1[0]) and (interval2[1] >= interval1[0])  #interval2 ends after interval1 starts but starts before interval1 starts
        areOverlapped = areOverlapped or (interval1[0] >= interval2[0]) and (interval1[1] <= interval2[1])  # interval1 contained within interval2
        areOverlapped = areOverlapped or (interval2[0] >= interval1[0]) and (interval2[1] <= interval1[1])  # interval2 contained within interval1
        return areOverlapped

    def merge(self, interval1, interval2):
        choice_space = []
        for i in range(2):
            choice_space.append(interval1[i])
            choice_space.append(interval2[i])
        return [min(choice_space), max(choice_space)]

    def insert(self, intervals, newInterval):
        i = 0
        _intervals = []

        while ((i < len(intervals))):
            if (newInterval):
                if self.areOverlapped(newInterval, intervals[i]):
                    _intervals.append(self.merge(newInterval, intervals[i]))
                    newInterval = None
                    i += 1
                else:
                    if (newInterval[1] < intervals[i][0]):
                        _intervals.append(newInterval)
                        newInterval = None
                    else:
                        _intervals.append(intervals[i])
                        i += 1
            else:
                if self.areOverlapped(_intervals[-1], intervals[i]):
                    _intervals.append(self.merge(_intervals.pop(), intervals[i]))
                else:
                    _intervals.append(intervals[i])
                i += 1
        if newInterval:
            _intervals.append(newInterval)
        if ( intervals and (intervals[-1][1] > _intervals[-1][1]) ):
            _intervals.append( intervals[-1] )
        return _intervals

#tests
sol = Solution()

# print( sol.insert( intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] ) )
# print( sol.insert([[1,5]], [0,0]) )
# print( sol.insert( [], [5,7] ) )
print( sol.insert( [[2,5],[6,7],[8,9]], [0,1]) )