'''
Search strategy:
    start at target[0] and iterate through to target[len(target)-1]:
        convert target[i] to it's number form
        iterate through the moves UDLR to see which move will decrease the distance to target[i]
        take the move that decreases the distance, and append the char to the path string that corresponds to the move taken
        when the distance to the target string is 0, append a ! to the path string, and i++

'''

class Solution:
    def alphabetBoardPath(self, target):
        # create a letter to number map
        # this will allow us to make quick comparisons between the number we want to find and our current position
        # use this map to do a optimized search along the board for the numbers
        self.letterToCoordMap = {}

        _alphabet_string = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(_alphabet_string)):
            self.letterToCoordMap[_alphabet_string[i]] = {
                "x": i % 5,
                "y": i // 5
            }

            #     self.letterToNumberMap[_alphabet_string[i]] = i+1
        #
        # self.board = [
        #     [1, 2, 3, 4, 5],
        #     [6, 7, 8, 9, 10],
        #     [11, 12, 13, 14, 15],
        #     [16, 17, 18, 19, 20],
        #     [21, 22, 23, 24, 25],
        #     [26]
        # ]

        _x = 0
        _y = 0
        _i = 0
        path_string = ""

        while (_i < len(target)):
            _t = self.letterToCoordMap[target[_i]]
            row_length = 1 if (_t["y"] == 5) else 5
            distance_to_target = abs(_t["x"] - _x) + abs(_t["y"] - _y)

            if distance_to_target == 0:
                path_string += "!"
                _i += 1

            else:
                _distanceToTargetAfterAction = {}

                if ((_y - 1) >= 0):
                    _distanceToTargetAfterAction["U"] = abs(_t["x"] - _x) + abs(_t["y"]  -1*(_y - 1))
                if ((_x + 1) < row_length):
                    _distanceToTargetAfterAction["R"] = abs(_t["x"] -1*(_x + 1)) + abs(_t["y"] - _y)
                if ( ((_y + 1) <= 4) or (((_y + 1)==5) and (_x == 0)) ):
                    _distanceToTargetAfterAction["D"] = abs(_t["x"] - _x) + abs(_t["y"] -1*(_y + 1))
                if ((_x - 1) >= 0):
                    _distanceToTargetAfterAction["L"] = abs(_t["x"] -1*(_x -1)) + abs(_t["y"] - _y)

                _best_action = None
                for action_key in _distanceToTargetAfterAction:
                    if ((type(_best_action) == type(None)) or (
                            _distanceToTargetAfterAction[action_key] < _distanceToTargetAfterAction[_best_action])):
                        _best_action = action_key

                path_string += _best_action

                if _best_action == "U":
                    _y -= 1
                elif _best_action == "R":
                    _x += 1
                elif _best_action == "D":
                    _y += 1
                elif _best_action == "L":
                    _x -= 1
        return path_string

sol = Solution()
# print(sol.alphabetBoardPath("leet"))
print(sol.alphabetBoardPath("zdz")=="DDDDD!UUUUURRR!DDDDLLLD!")