import numpy as N
import pylab as pl
dados_x = N.array([0,1,2,3,4,5])
dados_y=N.array([0.,0.8,0.9,0.1,-0.8,-1.])
z = N.polyfit(dados_x,dados_y,3)
p = N.poly1d(z)
p
print p
xs=N.arange(-1,8,0.1)
ys=p(xs)
pl.plot(dados_x, dados_y, '*', label='dados')
pl.plot(xs, ys, label='curva fitada')
pl.xlabel('x')
pl.ylabel('y')
pl.legend()
pl.show()


