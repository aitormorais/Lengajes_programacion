from qiskit import QuantumCircuit, QuantumRegister, Aer, execute, ClassicalRegister
from qiskit.visualization import plot_histogram
import numpy as np
      
def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    if a not in [2,7,8,11,13]:
        raise ValueError("'a' must be 2,7,8,11 or 13")
    U = QuantumCircuit(4) 
    name = "%i^%i mod 15" % (a, power)
    power = power % 4 
    for iteration in range(power):
        if a in [2,13]:
            U.swap(0,1)
            U.swap(1,2)
            U.swap(2,3)
        if a in [7,8]:
            U.swap(2,3)
            U.swap(1,2)
            U.swap(0,1)
        if a == 11:
            U.swap(1,3)
            U.swap(0,2)
        if a in [7,11,13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = name
    return U
    
def ax_mod_21(x):
    x_str = x
    ax_mod_N_registry = QuantumRegister(5)
    ax_mod_N = QuantumCircuit(ax_mod_N_registry, name='a^' + str(x_str) + ' mod N')
    
    #a^x mod N
    ax_mod_N.cswap(0, 3, 4)
    ax_mod_N.cswap(0, 1, 2)
    ax_mod_N.cx(4, 2)
    ax_mod_N.cx(4, 0)
    ax_mod_N.swap(3, 4)
    ax_mod_N.swap(0, 3)
    ax_mod_N.swap(2, 3)
    ax_mod_N.swap(1, 2)
    
    x = x % 6
    #Result circ
    circ_registry = QuantumRegister(5)
    circ = QuantumCircuit(circ_registry, name='Circuito a^' + str(x_str) + ' mod N')

    if x == 0:
        return circ.id()
    else:
        for i in range(x):
            circ.append(ax_mod_N.to_gate(), [i for i in range(5)])
        return circ
    
def pqk(coefs_a):
    if len(coefs_a) == 0:
        return None
    elif len(coefs_a) == 1:
        p = coefs_a[0]
        q = 1
        return p, q
    elif len(coefs_a) == 2:
        p = coefs_a[0] * coefs_a[1] + 1
        q = coefs_a[1]
        return p, q
    else:
        p_minus_1, q_minus_1 = pqk(coefs_a[0:len(coefs_a) - 1])
        p_minus_2, q_minus_2 = pqk(coefs_a[0:len(coefs_a) - 2])
        return coefs_a[-1] * p_minus_1 + p_minus_2, coefs_a[-1] * q_minus_1 + q_minus_2