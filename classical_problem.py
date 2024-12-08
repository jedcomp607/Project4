from sympy import *
import matplotlib.pyplot as plt

# Just to make it look pretty
latexReplaceRules = {
    # r'{\left(t \right)}':r' ',
    r'\frac{d}{d t}':r'\dot',
    r'\frac{d^{2}}{d t^{2}}':r'\ddot',
}
def latexNew(expr,**kwargs):
    retStr = latex(expr,**kwargs)
    for _,__ in latexReplaceRules.items():
        retStr = retStr.replace(_,__)
    return retStr
init_printing(latex_printer=latexNew)


# Declaring symbolic variables and functions:
g = Symbol('g')
m = Symbol('m')
t = Symbol('t')
theta = Function("theta")(t)
phi = Function("phi")(t)

# position vector components
Rx = sin(theta)*cos(phi)
Ry = sin(theta)*sin(phi)
Rz = cos(theta)

# finding Energies
R_dot_squared = simplify(diff(Rx,t)**2 + diff(Ry,t)**2 + diff(Rz,t)**2)
R_dot_squared
T = (1/2)*m*R_dot_squared
V = -m*g*Rz
L = T-V
L

# finding conserved quantities
'''
phi is cyclic so there is a conserved quantity - angular momentum
'''
l_z = simplify(diff(L,diff(phi,t)))
l_z
'''
for theta, we can substitute in our conserved quantity 
'''
l = Symbol('l')
L = -g*m*cos(theta) + 0.5*(l**2)/(m*sin(theta)**2) + 0.5*diff(theta,t)**2
diff((diff(L,(diff(theta,t)))),t)-diff(L,theta)
'''
when we multiply through by theta_dot, we realize another conserved quantity - energy
'''
E = integrate(diff(theta,t)*(diff((diff(L,(diff(theta,t)))),t)-diff(L,theta)),t)
