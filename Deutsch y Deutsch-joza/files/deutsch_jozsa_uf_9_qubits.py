from qiskit import QuantumCircuit, QuantumRegister

uf_dj_8_registry = QuantumRegister(9)
uf_dj_8 = QuantumCircuit(uf_dj_8_registry, name='U_f')

uf_dj_8_registry_2 = QuantumRegister(9)
uf_dj_8_2 = QuantumCircuit(uf_dj_8_registry_2, name='U_f_2')
uf_dj_8_2.cx(uf_dj_8_registry_2[8], uf_dj_8_registry_2[0])
uf_dj_8_2.cx(uf_dj_8_registry_2[8], uf_dj_8_registry_2[5])
uf_dj_8_2.cx(uf_dj_8_registry_2[5], uf_dj_8_registry_2[0])