import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH

# Numeric example: 2-joint planar robot (all revolute, a1=1, a2=1)
#print("Numeric example:")
dh_params = [
    [np.pi/4, 0, 1, 0],
    [np.pi/4, 0, 1, 0],
]
H_class = ForwardKinematicsDH.numeric(dh_params)
#print("End-effector transformation matrix:")
#print(H_class)

# symbolic example: 2-joint planar robot 
print("\nSymbolic example:")
q1, q2 = sp.symbols('q1 q2')
l1, l2 = sp.symbols('l1 l2')
d3 = sp.symbols('d3')
dh_params_sym = [
    # q  d  l   a
    [q1, 0, l1, 0],
    [q2, 0, l2, 180],   #Se añadio una 3ra fila para el 3er GdL y se sustituyo el 180 como lo indicaba la matriz del libro
    [0, d3, 0, 0],
]
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_sym)
print("End-effector transformation matrix:")
sp.pprint(H_sym_class, use_unicode=True)
