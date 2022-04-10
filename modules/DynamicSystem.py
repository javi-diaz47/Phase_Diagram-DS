from modules.CriticPoint import CriticPoint
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class DynamicSystem:

    def __init__(self):
        self.A = np.array([[1, 0],
                           [0, -3]])
        
#        self.get_A()

        self.cp = CriticPoint()

        self.det = np.linalg.det(self.A)

        if self.det == 0:
            print("El sistema de ecuaciones diferenciales posee infinitos puntos criticos")
            return

    def get_A(self):
        for i in range(2):
            for j in range(2):
                self.A[i][j] = input(f'\nInsert the A{i}{j}: ')


    def get_cp(self):
        self.cp.eigen = np.roots([1, - (self.A[0][0] + self.A[1][1]), self.det])
        self.cp.get_type()
        self.cp.get_stability()

    #isoclines 
    def iso_vert(self, x):
        return - (self.A[0][0]/self.A[0][1]) * x
    
    def iso_hori(self, x):
        return - (self.A[0][0]/self.A[0][1]) * x


    def first_integrate(self, y, x):
#        return  (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y)
         print( f'{self.A[1][0]*x + self.A[1][1]*y} / {(self.A[0][0]*x + self.A[0][1]*y)}')
         return (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y)


    def display_system(self):
        
        init_cond = [1, -1, 2, -3]

        x = np.linspace(-20, 20)
#        y = odeint(first_integrate, init_cond, x)

        around_cp = []

        for i in init_cond:
            around_cp.append({
                "x": x,
#                 "y": odeint(lambda y, x: (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y), i, x)
                 "y": odeint(lambda y, x: -3*y/x, i, x)
            })



        # Drawing the behavior around the critic point 
        for i in around_cp:
            plt.plot(i["x"], i["y"])
        
        plt.style.use('seaborn-poster')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.tight_layout()
        plt.autoscale()
        plt.show()

