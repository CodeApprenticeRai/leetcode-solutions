'''
Idea: breadth first search / dfs the paths to see which has the minimum distance
'''


class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        pathsum1 = 0
        pathsum2 = 0

        i1 = start
        i2 = start

        while (((i1 % len(distance)) != destination) and ((i2 % len(distance)) != destination)):
            pathsum1 += distance[i1 % len(distance)]
            i1 += 1  # !!

            pathsum2 += distance[(i2 % len(distance)) - 1]
            i2 -= 1  # !!
            debug_condition1 = i1 % len(distance)
            debug_condition2 = i2 % len(distance)

        if ( destination == (i1 % len(distance)) ):
            return pathsum1
        else:
            return pathsum2

sol = Solution()
print( sol.distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7, 2) == 17 )