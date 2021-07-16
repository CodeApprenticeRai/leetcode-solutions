'''
model the state space, 
search solutions;
return the minimum solution 


for each position we want to compute the
minimum number of sidesteps to reach there
from the start position.


'''

class Solution:
    def minSideJumps(self, obstacles):
        self.state_space = [[obstacles[j]==i for i in range(1,4)] for j in range(len(obstacles))]
        self.transitions = [[None for i in range(4)] for j in range(len(obstacles))]
        self.min_sidestep = {}
        self.n = len(obstacles)
        
        sidestep_count = 0
        queue = deque([((1,0),0)])
        
        while (len(queue) > 0):
            #compute transitions,
            curr = queue.popleft()
            print(curr)
            
            if (curr[0][1] == (self.n-1)):
                return curr[1]
            
            #update min_step 
            if (curr[0] not in self.min_sidestep):
                self.min_sidestep[curr[0]] = curr[1]
            else:
                self.min_sidestep[curr[0]] = min(curr[1], self.min_sidestep[curr[0]])
            
            next_states = self.get_next_states(curr)
            
            for state in next_states:
                queue.append(state)    
        return -1
            
    def get_next_states(self, curr):
        if (self.transitions[curr[0][0]][curr[0][1]] == None):
            available_states = []        
            #check if we can move right
            if (curr[0][0] < (self.n-1)):
                if (self.state_space[curr[0][0]+1][curr[0][1]] != 1):
                    available_states.append( ((curr[0][0]+1, curr[0][1]), curr[1]) )
            #check if we can move up
            if (curr[0][1] > 0):
                # check if there is an obstacle 
                if (self.state_space[curr[0][0]][curr[0][1]-1]==1):
                    #if there is an obstacle, 
                    #we can only side jump if position[1]==2 
                    if (curr[0][1]==2):
                        available_states.append( ((curr[0][0], curr[0][1]-2), curr[1] + 1) )
                else:
                    #if there is no obstacle we can move up
                    available_states.append( ((curr[0][0], curr[0][1]-1), curr[1] + 1) )
            #check if we can move down
            if (curr[0][1] < 3):
                # check if there is an obstacle 
                if (self.state_space[curr[0][0]][curr[0][1]+1]==1):
                    #if there is an obstacle, 
                    #we can only side jump if position[1]==2 
                    if (curr[0][1]==0):
                        available_states.append( ((curr[0][0], curr[0][1]+2),  curr[1] + 1) )
                else:
                    #if there is no obstacle we can move up
                    available_states.append( ((curr[0][0], curr[0][1]+1),  curr[1] + 1) )    
            self.transitions[curr[0][0]][curr[0][1]] = available_states
        return self.transitions[curr[0][0]][curr[0][1]]