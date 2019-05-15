from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

class TaxiDriver(State):

    def __init__(self, op):
        self.operator = op
        #TODO
    
    def sucessors(self):
        sucessors = []
        #TODO
        return sucessors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        pass


def main():
    print('Busca em profundidade iterativa')
    state = TaxiDriver('')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()