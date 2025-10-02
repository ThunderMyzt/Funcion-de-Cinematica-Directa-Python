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
q1, q2, q3 = sp.symbols('q1 q2 q3')
l1, l2, l3 = sp.symbols('l1 l2 l3')
dh_params_sym = [
    # q  d  l   a
    [q1, 0, l1, np.pi/2],
    [q2, 0, l2, 0],
    [q3, 0, l2, 0],
]
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_sym)
print("End-effector transformation matrix:")
sp.pprint(H_sym_class, use_unicode=True)
