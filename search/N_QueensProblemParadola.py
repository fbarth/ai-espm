#
# TODO implement a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#

from SearchAlgorithms import SubidaMontanha
from Graph import State
from random import randrange
from collections import Counter

class N_QueensProblem(State):

    def __init__(self, v):
        self.value = v
    
    def sucessors(self):
        sucessors = []
        for i in range(1,5):
            print(self.value)
            v = self.value - randrange(0,3)
            sucessors.append(N_QueensProblem(v))
        return sucessors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        pass

    def printEnv(self):
        return self.value
    
    def h(self):
        # verificar se possui alguma rainha na coluna, na linha ou nas diagonais 
        # (diagonal 1 = col+1 lin+1; diagonal 2 = col+1 lin-1; diagonal 3 = col-1 lin+1) 
        return self.value
        
def main():
    print('Subidamontanha')

    state = N_QueensProblem(4)
    algorithm = SubidaMontanha()
    result = algorithm.search(state)
    
    if result != None:
        print('Achou!')
        print(result.printEnv())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()