from sympy import *

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
m = 
t = 
theta = Function("theta")(t)
phi = 

# position vector components
Rx = sin(theta)*cos(phi)
Ry = 
Rz = 

# finding Energies
V_squared = simplify()
V_squared
T = (1/2)*m*V_squared  # kinetic energy
V = -m*g*Rz  # potential energy
L = T-V
L

# finding conserved quantities
'''
phi is cyclic so there is a conserved quantity - angular momentum
'''
l_z = 
l_z
'''
for theta, we can substitute in our conserved quantity 
'''
l = Symbol('l')
L = -g*m*cos(theta) + 0.5*(l**2)/(m*sin(theta)**2) + 0.5*diff(theta,t)**2
# using the new Lagrangian, find the new equation of motion for theta via the algorithm above.

'''
If we multiply through by theta_dot (i.e. 'diff(theta,t)'), we realize another conserved quantity - energy
'''
E = integrate(,t)  # input diff(theta,t)*eqn of motion for theta
