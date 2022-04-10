from re import I
import numpy as np

class CriticPoint:

    def __init__(self):
        self.eigen = []
        self.type = ""
        self.stability = ""


    def show_props(self):
        print(f'Critic point')
        print(f'valores propios: {self.eigen}')
        print(self.type)
        print(self.stability)


    def get_type(self):
        if np.isreal(self.eigen[0]) and np.isreal(self.eigen[1]):
            if self.equal_signs():
                self.type = "nodo"
                return
            else:
                self.type = "silla"
                self.stability = "inestable"
                return
        else:
            if self.eigen[0].real == 0 and self.eigen[1].real == 0:
                self.type = "centro"
                self.stability = "estable"
                return
            else:
                self.type = "foco o espiral"
                return

    def get_stability(self):
        if self.eigen[0].real > 0 or self.eigen[1].real > 0:
            self.stability = "inestable"
            return
        
        if self.eigen[0].real < 0 and self.eigen[1].real < 0:
            self.stability = "asintoticamente estable"
            return

        if self.eigen[0].real == 0 and self.eigen[1].real == 0:
            self.stability = "estable"
            return


    def equal_signs(self):
        if (self.eigen[0] < 0 and self.eigen[1] < 0) or (self.eigen[0] > 0 and self.eigen[1] > 0):
            return True
        else:
            return False