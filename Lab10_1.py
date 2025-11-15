import matplotlib.pyplot as pl
import numpy as nmp
x = nmp.linspace(-3, 3, 500)
y = (2 ** x) * nmp.sin(10 * x)
pl.plot(x, y, linewidth=3, color='green', label='Y(x)=2^x*sin(10x)')
pl.title('Function', fontsize=25)
pl.xlabel('x', fontsize=30)
pl.ylabel('Y(x)', fontsize=30)
pl.legend(fontsize=15)
pl.grid(True)
pl.show()
