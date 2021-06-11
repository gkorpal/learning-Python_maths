import numpy as np
import matplotlib.pyplot as plt

#use stream plot to create the flow lines
x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
u = y
v = x
plt.streamplot(x,y,u,v)

#save as pdg and pgf
plt.savefig('v3.pdf')
plt.savefig('v3.pgf')
