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

## Associated publications
Please refer to the following publication to cite our work or retrieve the info:

[The GRETOBAPE gas-phase reaction network: the importance of being exothermic, L.Tinacci et al 2023 Arxiv](https://doi.org/10.48550/arXiv.2302.14799)

```bibtex
@article{Tinacci_Gretobape,
  title={The GRETOBAPE gas-phase reaction network: the importance of being exothermic},
  author={Tinacci, Lorenzo and Ferrada-Chamorro, Sim{\'o}n and Ceccarelli, Cecilia and Pantaleone, Stefano and Ascenzi, Daniela and Maranzana, Andrea and Balucani, Nadia and Ugliengo, Piero},
  journal={arXiv preprint arXiv:2302.14799},
  year={2023}
}
```

[Structures and Properties of Known and Postulated Interstellar Cations, L.Tinacci et al 2021 ApJS 256 35](https://doi.org/10.3847/1538-4365/ac194c)

```bibtex
@article{Tinacci_ISM_cations,
title={Structures and Properties of Known and Postulated Interstellar Cations},
author={Tinacci, Lorenzo and Pantaleone, Stefano and Maranzana, Andrea and Balucani, Nadia and Ceccarelli, Cecilia and Ugliengo, Piero},
journal={The Astrophysical Journal Supplement Series},
volume={256},
number={2},
pages={35},
year={2021},
doi={10.3847/1538-4365/ac194c},
publisher={IOP Publishing}
}
```

All the data are store in the following ZENODO link:
DOI:[10.5281/zenodo.7799421](https://zenodo.org/record/7799421)

## Acknowledgments
This project has received funding within the European Union’s Horizon 2020 research and innovation programme from the Marie Sklodowska-Curie for the project ”Astro-Chemical Origins” (ACO), grant agreement No 811312.
