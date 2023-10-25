from qiskit import *
from collections import Counter
import numpy as np


def ia(size):
    ia_mat = 2 * np.ones(size) / size
    ia_mat = ia_mat - np.identity(size)
    return ia_mat


def oracle(size, val_array):
    _oracle = np.identity(size)
    for val in val_array:
        _oracle[val][val] = -1
    return _oracle


def rqga(current_val):
    n = 8
    predictions = 100

    circuit = QuantumCircuit(n)
    circuit.h(range(n))
    rand_theta = np.random.uniform(0, np.pi / n, n)
    for i in range(n):
        circuit.rz(rand_theta[i], i)

    GIM = ia(2 ** n)

    circuit.unitary(oracle(2**n, [current_val]), range(n), label='Oracle')
    circuit.unitary(GIM, range(n), label='Grover Inv')

    circuit.measure_all()

    sim = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=sim, shots=predictions).result().get_counts()

    return max(result)
    #return average(result, predictions, n)


def average(result, predictions, size):
    sum = 0
    div = 0

    for key in result.keys():
        if result[key] > predictions * 2 / 2**size:
            sum += int(key, 2)
            div += 1

    if div == 0:
        return max(result)

    return sum // div


def max(result):
    max_key = next(iter(result.keys()))

    for key in result.keys():
        if result[key] > result[max_key]:
            max_key = key

    return int(max_key, 2)
