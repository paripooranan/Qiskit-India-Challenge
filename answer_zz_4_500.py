# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap


    


def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the feature map
    feature_dim = 3     # equal to the dimension of the data

    feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=4)
    feature_map.draw()
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map# the write_and_run function writes the content in this cell into the file "variational_circuit.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import  RealAmplitudes, EfficientSU2
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def variational_circuit():
    # BUILD VARIATIONAL CIRCUIT HERE - START
    
    # import required qiskit libraries if additional libraries are required
    num_qubits = 3
    # build the variational circuit
    var_circuit = RealAmplitudes(num_qubits, entanglement='full', reps=3)
    var_circuit.draw()
    # BUILD VARIATIONAL CIRCUIT HERE - END
    
    # return the variational circuit which is either a VaritionalForm or QuantumCircuit object
    return var_circuit# # the write_and_run function writes the content in this cell into the file "optimal_params.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def return_optimal_params():
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    
    optimal_parameters = [ 0.93955905,  1.22812267,  1.64654955, -0.01192144,  0.65616099,
       -0.61020318, -0.21939937,  0.28867516, -1.86335921,  1.51716785,
        0.52331223, -0.83299047]
    
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    return np.array(optimal_parameters)