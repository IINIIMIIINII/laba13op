from numpy import *
import matplotlib.pyplot as plt
import math

x = linspace(1, 7)
y = (5*sin(10*x)*sin(3*x))/(x**0.5)
plt.plot(x, y, 'g', label='(5*sin(10*x)*sin(3*x))/(x**0.5)')
plt.axis([-5, 10, -5, 10]) # [xmin, xmax, ymin, ymax]
plt.xlabel('x') # позначення вісі абсцис
plt.ylabel('y') # позначення е вісі ординат
plt.title('Task 1') # назва графіка
plt.legend() # вставка легенди (тексту в Label)
plt.show()