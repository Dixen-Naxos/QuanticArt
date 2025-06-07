# QuanticArt

## Overview

This repository contains the official implementation of the paper **"Quantum Genetic Algorithms for Generative 3D Creations"**, presented at the **Generative Art Conference 2023**.

The project explores the intersection of quantum computing and generative art through the use of **Quantum Genetic Algorithms (QGAs)**. Inspired by Darwinian evolution and quantum mechanics, these algorithms are used to generate and manipulate 3D mesh structures, fractals, and cellular automata-based patterns. By leveraging quantum principles such as superposition and Grover’s search, we introduce new creative possibilities in digital sculpture and algorithmic art.

We also implement and experiment with a variant known as the **Reduced Quantum Genetic Algorithm (RQGA)**, optimized for mesh deformation and fractal evolution. The result is a collection of unique, computationally evolved 3D forms that merge scientific rigor with aesthetic exploration.

## Usage Instructions

### Launch Steps

- Install Blender
- Run `pip install -r {path_to_file}/requirements.txt` from Blender's Python environment
- Open the file RQGA.blend

### Generation from a complex model object

- Import the model object, ensuring it is of MESH type and its vertices have positive integer coordinates (it will also work with negative or decimal numbers, but the result may not exactly match the model)
- On lines 122 of the script, change the name of the model object (currently: "Suzanne") to your object's name
- For very large objects, you can also modify the number of qubits defined in the variable qubits_number on line 29 of the script (currently: 7, so 2 to the power of 7 = 128, our object will be a maximum of 128x128x128)
- Run the script

### See the animation

- Go to the Animation tab on Blender
- Press Play

### Export the animation

- Add a camera and a light on the scene
- In the Render menu, press Render Animation

## License

This project is licensed under the Apache License (Version 2.0).

See [LICENSE](LICENSE) for details.

## Citation

If you use or reference this work, please cite it as follows:

```bibtex
@inproceedings{lioret2023quantum,
  title={Quantum Genetic Algorithms for Generative 3D Creations},
  author={Lioret, Alain and Hennou, Kamal and Dailly, Armand and Ejarque, Jean-Baptiste and Foschiani, Louis and Jourdain, Arnaud and Maubras, Juan},
  booktitle={Generative Art Conference 2023},
  year={2023}
}
```
