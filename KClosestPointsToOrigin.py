import bisect, math

class Solution:
    def kClosest(self, points, K):
        def _distance_to_origin(point):
            return math.sqrt( point[0]**(2) + abs(point[1])**(2) )

        newArrayPoints = []
        newArrayDists = []

        for i in range(len(points)):
            _dist = _distance_to_origin(points[i])
            _i = bisect.bisect_left(newArrayDists, _dist)
            newArrayDists.insert(_i, _dist)
            newArrayPoints.insert(_i, points[i])
        return newArrayPoints[:K]

sol = Solution()
print( sol.kClosest([[1,3],[-2,2]], 1) )
print( sol.kClosest([[3,3],[5,-1],[-2,4]], 2) )