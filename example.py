import numpy as np
from forward_kinematics_dh import forward_kinematics_dh
from forward_kinematics_dh_symbolic import forward_kinematics_dh_symbolic
import sympy as sp

# Example: 2-joint planar robot (all revolute, a1=1, a2=1)
dh_params = [
    [np.pi/4, 0, 1, 0],  # theta1, d1, a1, alpha1
    [np.pi/4, 0, 1, 0],  # theta2, d2, a2, alpha2
]

H = forward_kinematics_dh(dh_params)
print("End-effector transformation matrix:")
print(H)


# Definir variables simbólicas para un robot planar de 2 grados de libertad
th1, th2 = sp.symbols('th1 th2')
a1, a2 = sp.symbols('a1 a2')

# Parámetros DH simbólicos: [theta, d, a, alpha]
dh_params_sym = [
    [th1, 0, 0, 0],
    [th2, 0, a2, 0],
]

H_sym = forward_kinematics_dh_symbolic(dh_params_sym)
print("\nMatriz de transformación simbólica del efector final:")
sp.pprint(H_sym, use_unicode=True)
