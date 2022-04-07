from CriticPoint import CriticPoint
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from main import first_integrate

class DynamicSystem:

    def __init__(self):
        self.A = np.array([[1, 2],
                           [2, 4]])
            # fill the matrix A
        #    for i in range(2):
        #       for j in range(2):
        #          A[i][j] = input(f'\nInsert the A{i}{j}: ')

        self.cp = CriticPoint()

        self.det = np.linalg.det(self.A)

        if self.det == 0:
            print("El sistema de ecuaciones diferenciales posee infinitos puntos criticos")
            return

    def get_cp(self):
        self.cp.eigen = np.roots([1, - (self.A[0][0] + self.A[1][1]), self.det])
        self.cp.get_type()
        self.cp.get_stability()


    def first_integrate(self, y, x):
#        return  (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y)
         print( f'{self.A[1][0]*x + self.A[1][1]*y} / {(self.A[0][0]*x + self.A[0][1]*y)}')
         return (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y)


    def display_system(self):
        
        init_cond = [1, -1, 2, -3]

        x = np.linspace(-1, 1 )
#        y = odeint(first_integrate, init_cond, x)

        around_cp = []

        for i in init_cond:
            around_cp.append({
                "x": x,
                 "y": odeint(lambda y, x: (self.A[1][0]*x + self.A[1][1]*y) / (self.A[0][0]*x + self.A[0][1]*y), i, x)
            })


        # Drawing the behavior around the critic point 
        for i in around_cp:
            plt.plot(i["x"], i["y"])

        plt.xlabel('x')
        plt.ylabel('y')
        plt.autoscale()
        plt.show()

