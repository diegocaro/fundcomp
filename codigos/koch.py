import turtle
from math import sqrt, cos, sin, pi

#
# Función recursiva para dibujar la curva de Koch.
# 
# Recibe 2 parámetros como entrada: a, b
#   a y b representan los extremo del segmento
# 
#
# Caso base: cuando el tamaño del segmento a-b es menor a 10
# Caso recursivo: 4 llamadas recursivas por cada segmento
#
def koch(a, b):    
    s = (b[0]-a[0], b[1]-a[1])
    
    ss = sqrt(s[0]*s[0]+s[1]*s[1])
    
    if ss < 10: return
    
    c = (a[0]+s[0]/3, a[1]+s[1]/3)
    d = (a[0]+2*s[0]/3, a[1]+2*s[1]/3)
    
    x = d[0]-c[0]
    y = d[1]-c[1]
    # el punto e es el vector (d-c) rotado en 60 grados
    # esto es porque es un triangulo equilatero
    alpha = pi/3 # 60 grados
    e = (c[0]+x*cos(alpha)-y*sin(alpha), 
         c[1]+x*sin(alpha)+y*cos(alpha))
    
    print('c', c)
    print('d', d)
    print('e', e)
    
    t.pencolor('black')

    # dibuja segmento a-b
    t.setpos(*a)
    t.down()
    t.goto(*b) 
    t.up()
    
    # dibuja segmentos del triangulo
    t.goto(*c) 
    t.down()
    t.goto(*e) # dibuja segmento c-e
    t.goto(*d) # dibuja segmento e-d
    t.up()
    
    t.pencolor('white')
    t.setpos(*c)
    t.down()
    t.goto(*d) # borrar segmento c-d
    t.up()
    
    koch(a, c)
    koch(c, e)
    koch(e, d)
    koch(d, b)
    
    return
    



s = turtle.getscreen()
t = turtle.Turtle()
t.up()

koch((-300,0), (300,0))

s.mainloop()