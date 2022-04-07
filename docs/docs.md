# Diagrama de fase - Sistemas dinamicos

## Dependencias
Para la correcta ejecución del programa es necesario
contar con ciertas librerias

1. numpy
1. scipy
1. matplotlib

## Explicacion del codigo

En un primer momento se importan todas las librerias
necesarias.

```python
    from operator import truediv
    import numpy as np
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt

```
## Funcioes

1. ### **equal_signs(root)**
    Esta funcion recibe por parametros un arreglo de numeros de dos posiciones que fungen como las raices de la ecuacion caracteristica de una matriz y devuelve verdadero o falso si ambos valores tienen mismo signo o no.
1. ### **get_stability(cp)**
    Toma por parametros un objeto *cp* que hace referencia a un punto critico y por medio de la evaluacion de sus valores propios (eigenvalores) retorna el tipo de estabilidad concerniente a dicho punto.
1. ### **get_type(cp)**
    Al igual que la anterior funcion esta tambien recibe por parametros un objeto *cp* y a traves de la evaluacion de los eigenvalores asociados al punto devuelve su tipo y en ciertas situaciones puntuales tambien retorna la estabilidad.
