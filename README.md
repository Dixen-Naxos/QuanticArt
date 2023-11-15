# QuanticArt

## For Launch Steps:
 - Install Blender
 - Install qiskit and qiskit-aer on Blender's Python environment
 - Open the file Rendu_spaghetti
 - Delete all objects

## For generation from a complex model object :
 - Load the script "rqga_mesh"
 - Import the model object, ensuring it is of MESH type and its vertices have positive integer coordinates (it will also work with negative or decimal numbers, but the result may not exactly match the model)
 - When your model is on the scene set first_step to true it will resize the model
 - After that set first_step to false to run the algorithme.
 - On lines 93 of the script, change the name of the model object (currently: "Suzanne") to your object's name
 - For very large objects, you can also modify the number of qubits used on lines 79, 80, 81 (currently: 7, so 2 to the power of 7 = 128, our object will be a maximum of 128x128x128)
Run the script
 - Run the script

## For a random object:
 - Load the script "rqga_random"
 - Replace the object name on lines 10 (currently: "Cube") to your object's name
 - You can modify the parameters of the function on line 97 to vary the number of vertices and the size of the object
 - Run the script