from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint


def dydt(y, x):
    return -3*y + 1


y0 = 0

x = np.linspace(0, 0.5, 100)

sol = odeint(dydt, y0, x)
y_sol = sol.T[0]

plt.plot(x, y_sol, color="red")
plt.grid()
plt.show()

print("result of Differential Equations with scipy is: \n", y_sol)

#############################################################################
# base on RK-4 (Fourth-Order Runge-Kutta)

delX = 0.1


def dydt(y, x):
    return -3*y + 1


def k1(x0, y0):
    res = delX * (dydt(x0, y0))
    return res


def k2(x0, y0):
    X = (delX/2) + x0
    Y = (k1(x0, y0)/2) + y0
    res = delX * (dydt(X, Y))
    return res


def k3(x0, y0):
    X = (delX/2) + x0
    Y = (k2(x0, y0)/2) + y0
    res = delX * (dydt(X, Y))
    return res


def k4(x0, y0):
    X = delX + x0
    Y = k3(x0, y0) + y0
    res = delX * (dydt(X, Y))
    return res


y0 = float(input("please enter a number as y0: "))

y1 = y0 + (1/6 * (k1(0, 0) + 2*(k2(0, 0)) + 2*(k3(0, 0)) + k4(0, 0)))


print("result of Differential Equations based on RK-4 is: ", y1)
