# QuanticArt

## For Launch Steps:
 - Install Blender
 - Run `pip install -r {path_to_file}/requirements.txt` from Blender's Python environment
 - Open the file RQGA.blend

## For generation from a complex model object:
 - Import the model object, ensuring it is of MESH type and its vertices have positive integer coordinates (it will also work with negative or decimal numbers, but the result may not exactly match the model)
 - On lines 122 of the script, change the name of the model object (currently: "Suzanne") to your object's name
 - For very large objects, you can also modify the number of qubits defined in the variable qubits_number on line 29 of the script (currently: 7, so 2 to the power of 7 = 128, our object will be a maximum of 128x128x128)
 - Run the script

## To see the animation:
 - Go to the Animation tab on Blender
 - Press Play

## To export the animation:
 - Add a camera and a light on the scene
 - In the Render menu, press Render Animation