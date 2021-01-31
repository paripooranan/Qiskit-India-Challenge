
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on two qubits
    circuit = QuantumCircuit(2)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    circuit.h(0)
    circuit.cx(0,1)
    circuit.x(1)
    circuit.rz(np.pi,1)
    # apply necessary gates
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
