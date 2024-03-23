import numpy as np

X = np.array([[0, 1],
            [1, 0]])

Y = np.array([[0, 1j],
            [1j, 0]])

Z = np.array([[1, 0],
            [0, -1]])
            
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

def controlled_e_u(u, e):
    length = u.shape[0]
    ket_0 = np.array([[1], [0]])
    ket_1 = np.array([[0], [1]])
    if e == 1:
        return np.add(np.kron(np.outer(ket_0, ket_0), np.eye(length)), np.kron(np.outer(ket_1, ket_1), u))
    else:
        return np.add(np.kron(np.outer(ket_0, ket_0), u), np.kron(np.outer(ket_1, ket_1), np.eye(length)))