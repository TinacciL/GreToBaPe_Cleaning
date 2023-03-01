# Cleaning Astrochemical Reaction network via Thermodynamics principles
This is a Python 3.8 script that permits to read and work with an astrochemical reaction network in [KIDA format](https://kida.astrochem-tools.org/) .

## Installation

This program used a python3 interface, to run this code you must install on your machine this list of packages:

* ```networkx```
* ```numpy```
* ```pandas```

## Script Structure
All the codes for the cleaning are inside the ```Cleaning_script.ipynb``` ipython notebook, the ```lib.py``` python file is where many functions are stored.
An example on how encode a KIDA Reaction Network and visualize is in the ```reaction_network_to_graph.ipynb``` file.

## Database
Networks and molecules information are inside the ```Database``` directory. A dedicated ```ReadMe``` file is inside the directory.

## The paper Supporting Info of paper (temporary)
All the paper supporting info are inside the ```SI```  folder.

## Associated publications
Please reffer to the following publication to cite our work or retrieve the info:

[The GRETOBAPE gas-phase reaction network: the importance of being exothermic, L.Tinacci et al 2023 Arxiv](https://doi.org/10.48550/arXiv.2302.14799)

(https://doi.org/10.48550/arXiv.2302.14799)

[Structures and Properties of Known and Postulated Interstellar Cations, L.Tinacci et al 2021 ApJS 256 35](https://doi.org/10.3847/1538-4365/ac194c)

(https://doi.org/10.3847/1538-4365/ac194c)

## Acknowledgments
This project has received funding within the European Union’s Horizon 2020 research and innovation programme from the Marie Sklodowska-Curie for the project ”Astro-Chemical Origins” (ACO), grant agreement No 811312.
