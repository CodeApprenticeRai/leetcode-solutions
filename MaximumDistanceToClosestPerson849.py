class Solution:
    def maxDistToClosest(self, seats):
        self.seats = seats
        self.maxDists = {}
        self.i_of_global_max = None
        self.global_max = None

        # calculate distanced to closest person on the left
        for i in range(len(self.seats)):
            leftDist = None
            if (self.seats[i] == 1):
                leftDist = 0
            elif (i == 0):
                leftDist = float('inf')
            else:
                leftDist = 1 + self.maxDists[i - 1]["left"]

            self.maxDists[i] = {"left": leftDist}

        # calculate distance to closest person on the right
        for i in range(len(self.seats) - 1, -1, -1):
            rightDist = None
            if (self.seats[i] == 1):
                rightDist = 0
            elif (i == len(self.seats) - 1):
                rightDist = float('inf')
            else:
                rightDist = 1 + self.maxDists[i + 1]["right"]

            self.maxDists[i]["right"] = rightDist
            self.maxDists[i]["global"] = min(self.maxDists[i]["left"], self.maxDists[i]["right"])

            if ((self.seats[i] != 1) and ((not self.global_max) or (self.maxDists[i]["global"] > self.global_max)) ):
                self.i_of_global_max = i
                self.global_max = self.maxDists[i]["global"]
        return self.global_max

sol = Solution()
print(sol.maxDistToClosest([1,0,0,0,1,0,1]) == 2)
print(sol.maxDistToClosest([1,0,0,0]) == 3)
print(sol.maxDistToClosest([0,0,1]) == 2)


# class Solution:
#     def _maxDistToClosest(self, i):
#         #memiozed solution case
#         if i in self.maxDists:
#             if "global" in self.maxDists[i]:
#                 return self.maxDists[i]["global"]
#
#         #boundary base case
#         if ((i < 0) or (i >= len(self.seats))):
#             return 0
#
#         #person in seat base case
#         if (self.seats[i] == 1):
#             if i not in self.maxDists:
#                 self.maxDists[i] = {}
#                 self.maxDists[i]["left"] = 0
#                 self.maxDists[i]["right"] = 0
#                 self.maxDists[i]["global"] = 0
#             return self.maxDists[i]["global"]
#
#         self.maxDists[i] = {}
#         self.maxDists[i]["left"] = 1 + self._maxDistToClosest(i - 1)
#         self.maxDists[i]["right"]= 1 + self._maxDistToClosest(i + 1)
#         self.maxDists[i]["global"] = min(self.maxDists[i]["left"], self.maxDists[i]["right"])
#
#         if ((not self.global_max) or (self.maxDists[i]["global"] > self.global_max)):
#             self.i_of_global_max = i
#             self.global_max = self.maxDists[i]["global"]
#
#         return self.maxDists[i]["global"]
#
#     def maxDistToClosest(self, seats):
#         self.seats = seats
#         self.maxDists = {}
#         self.i_of_global_max = None
#         self.global_max = None
#
#         for i in range(len(self.seats)):
#             self._maxDistToClosest(i)
#
#         return self.i_of_global_max

# class Solution:
#     def compute_distance_to_closest_person(self, i, direction):
#         if (self.seats[i] == 1):
#             self.maxDists[i] = {}
#             self.maxDists[i]["left"] = 0
#             self.maxDists[i]["right"] = 0
#             self.maxDist[i]["global"] = 0
#             return self.maxDist[i]["global"]
#
#         if direction == "left":
#             if (i < 0):
#                 return 0
#             else:
#                 if i not in self.maxDists:
#                     self.maxDists[i] = {}
#                     self.maxDists[i]["left"] = 1 + self.compute_distance_to_closest_person(i - 1, "left")
#                     self.maxDists[i]["right"] = 1 + self.compute_distance_to_closest_person(i - 1, "right")
#                     self.maxDist[i]["global"] = max(self.maxDists[i]["left"], self.maxDists[i]["right"])
#                     return self.maxDist[i]["global"]
#         else:
#             if (i >= len(self.seats)):
#                 return 0
#             else:
#                 else:
#                 if i not in self.maxDists:
#                     self.maxDists[i] = {}
#                     self.maxDists[i]["left"] = 1 + self.compute_distance_to_closest_person(i - 1, "left")
#                     self.maxDists[i]["right"] = 1 + self.compute_distance_to_closest_person(i - 1, "right")
#                     self.maxDist[i]["global"] = max(self.maxDists[i]["left"], self.maxDists[i]["right"])
#                     return self.maxDist[i]["global"]
#
#     def maxDistToClosest(self, seats):
#         self.seats = seats
#         self.maxDists = {}
#         i_of_global_max = None
#         _global_max = None
#
#         for i in range(len(seats)):
#             # compute the  distance to closest person on the left
#             if i not in self.maxDists:
#                 self.maxDists[i] = {}
#                 self.maxDists[i]["left"] = self.compute_distance_to_closest_person(i, "left")
#                 self.maxDists[i]["right"] = self.compute_distance_to_closest_person(i, "right")
#                 self.maxDist[i]["global"] = max(self.maxDists[i]["left"], self.maxDists[i]["right"])
#
#             if ((not _global_max) or (self.maxDist[i]["global"] < _global_max)):
#                 i_of_global_max = i
#                 _global_max = self.maxDist[i]["global"]
#
#             return i_of_global_max