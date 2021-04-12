'''
go right,
go down,
go left,
go up,
repeat
'''

class Solution:
    def spiralOrder(self, matrix):
        self.bounds = (len(matrix), len(matrix[0]))
        visited_values = []
        visited = set()


        next_pos = (0,0)

        # directions are 0,1,2,3: left,down,right,up
        direction = 0
        terminal_flag = 0 #if we change directions twice, we've reached the end of our search
        while not (terminal_flag > 1):
            if ((next_pos in visited) or self.out_of_bounds(next_pos)):
                direction = (direction+1) % 4
                terminal_flag += 1
            else:
                terminal_flag = 0
                curr_pos = next_pos
                visited.add(curr_pos)
                visited_values.append(matrix[curr_pos[0]][curr_pos[1]])
            next_pos = self.get_next_pos(curr_pos, direction)
        return visited_values


    def get_next_pos(self, curr_pos, direction):
        curr_pos = list(curr_pos)
        if (direction==0):
            curr_pos[1]+=1
        elif (direction==1):
            curr_pos[0]+=1
        elif (direction==2):
            curr_pos[1]-=1
        elif (direction==3):
            curr_pos[0]-=1
        return tuple(curr_pos)

    def out_of_bounds(self, pos):
        check1 = (pos[0] >= self.bounds[0]) or (pos[0] < 0)
        check2 = (pos[1] >= self.bounds[1]) or (pos[1] < 0)
        return any([check1, check2])
