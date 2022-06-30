================================================================================
Title: 
Authors: 
================================================================================
Description of contents: This tar.gz archive file contains XXX .XYZ formatted
    files, providing extended information of all the species studied in the accepted
    version of the manuscript listed above. A complete listing of all these files is given
    at the bottom of this ReadMe
    
    Scripts are provided to allow to encode each .XYZ chemical data in a
    molecular graph and viceversa and moreover control if diffent species have
    same connectivity (i.e. are isomorphic). Each script has a markdown 
    README file that provides additional information:
    
    README_Connectivity_chemical_graph.md
    isomorphism_molecules.py
    
    README_FromGraphToXYZ.md
    FromGraphToXYZ.py
    
    The scripts are also available on the following website:
    
    https://aco-itn.oapd.inaf.it/aco-public-datasets/theoretical-chemistry-calculations/software-packages/cations-structures-scripts


System requirements: The files are stored in the XYZ chemical file format.
    The files can be read using the Jmol molecular viewer or other chemical
    visualization tool. More info about the .XYZ format can be found here:
    https://en.wikipedia.org/wiki/XYZ_file_format

    Here below an example of .XYZ file and the info provided in this work:
    
        *********************************************************************************   
        6
        c-C3H3+_1 (1-A1' / D3H)
        H     0.000000     1.862863     0.000000
        H     1.613287    -0.931432     0.000000
        H    -1.613287    -0.931432     0.000000
        C     0.000000     0.782824     0.000000
        C     0.677946    -0.391412     0.000000
        C    -0.677946    -0.391412     0.000000

        -------- ENERGY AND PROPERTIES --------

        Rotational constants:       31.0491098       31.0491098       15.5245549 GHz

        ECCSD(T)/aug-cc-pVTZ = -115.5144869 Eh

        MU_X      MU_Y      MU_Z       MU
         -0.000    0.000    0.000    0.000
        *********************************************************************************

    where: 
    c-C3H3+_1 is the chemical name
    1-A1'     is the electronic state (1 is ms, A1' the electronic state symmetry)
    D3H       is the spatial group symmetry
    -115.5144869 is the absolute electronic energy in Hartree computed at CCSD(T)/aug-cc-pVTZ level
    MU_X, MU_Y, MU_X are the dipole moment vectorial component and MU the module


Additional comments: The full list of XYZ files is given below:

C10+_2.xyz        C10H+_3.xyz     C10H2+_2.xyz     C10H3+_1.xyz   C10N+_1.xyz
C11+_2.xyz        C2+_4.xyz       C2H+_3.xyz       C2H2+_2.xyz    C2H3+_1.xyz
C2H3CO+_1.xyz     C2H4+_2.xyz     C2H4O+_2.xyz     C2H5+_1.xyz    C2H5OH+_2.xyz
C2H5OH2+_1.xyz    C2H6+_2.xyz     C2H6CO+_2.xyz    C2HO+_1.xyz    C2N+_1.xyz
C2N2+_2.xyz       C2O+_2.xyz      C2S+_2.xyz       C3+_2.xyz      C3H+_1.xyz
C3H3N+_2.xyz      C3H3NH+_1.xyz   C3H4+_2.xyz      C3H5+_1.xyz    C3H6OH+_1.xyz
C3N+_3.xyz        C3O+_2.xyz      C3S+_2.xyz       C4+_2.xyz      C4H+_3.xyz
C4H2+_2.xyz       C4H3+_1.xyz     C4H4+_2.xyz      C4H5+_1.xyz    C4H7+_1.xyz
C4N+_1.xyz        C4P+_1.xyz      C4S+_2.xyz       C5+_2.xyz      C5H+_1.xyz
C5H2+_2.xyz       C5H3+_1.xyz     C5H3N+_2.xyz     C5H4+_2.xyz    C5H4N+_1.xyz
C5H5+_1.xyz       C5N+_3.xyz      C6+_2.xyz        C6H+_3.xyz     C6H2+_2.xyz
C6H3+_1.xyz       C6H4+_2.xyz     C6H5+_1.xyz      C6H7+_1.xyz    C6N+_1.xyz
C7+_2.xyz         C7H+_1.xyz      C7H2+_2.xyz      C7H2N+_1.xyz   C7H3+_1.xyz
C7H4+_2.xyz       C7H5+_1.xyz     C7N+_3.xyz       C8+_2.xyz      C8H+_3.xyz
C8H2+_2.xyz       C8H3+_1.xyz     C8H4+_2.xyz      C8H4N+_1.xyz   C8H5+_1.xyz
C8N+_1.xyz        C9+_2.xyz       C9H+_1.xyz       C9H2+_2.xyz    C9H2N+_1.xyz
C9H3+_1.xyz       C9H4+_2.xyz     C9H5+_1.xyz      C9HN+_2.xyz    C9N+_3.xyz
CCP+_1.xyz        CCl+_1.xyz      CF+_1.xyz        CH+_1c.xyz     CH2+_2.xyz
CH2CN+_1.xyz      CH2NH2+_1.xyz   CH2Si+_2.xyz     CH3+_1.xyz     CH3CHOH+_1.xyz
CH3CN+_2.xyz      CH3CNH+_1.xyz   CH3CO+_1.xyz     CH3NH2+_2.xyz  CH3NH3+_1.xyz
CH3O2+_1.xyz      CH3OCH3+_2.xyz  CH3OCH4+_1.xyz   CH3OH+_2.xyz   CH3OH2+_1.xyz
CH4+_2.xyz        CH5+_1.xyz      CHSi+_3.xyz      CN+_1c.xyz     CNC+_1.xyz
CO+_2.xyz         CO2+_2.xyz      COOCH4+_2.xyz    CP+_3.xyz      CS+_2.xyz
ClO+_3.xyz        H2+_2.xyz       H2C10N+_1.xyz    H2C3O+_2.xyz   H2C4N+_1.xyz
H2C5N+_1.xyz      H2C6N+_1.xyz    H2C8N+_1.xyz     H2CCO+_2.xyz   H2CCl+_1.xyz
H2CO+_2.xyz       H2COH+_1.xyz    H2CS+_2.xyz      H2Cl+_1.xyz    H2F+_1.xyz
H2NC+_1.xyz       H2NO+_1.xyz     H2O+_2.xyz       H2PO+_1.xyz    H2S+_2.xyz
H2S2+_2.xyz       H2SiO+_2.xyz    H3+_1.xyz        H3C4N+_2.xyz   H3C4NH+_1.xyz
H3C6NH+_1.xyz     H3C7N+_2.xyz    H3CS+_3.xyz      H3O+_1.xyz     H3S+_1.xyz
H3S2+_1.xyz       H3SiO+_1.xyz    H5C2O2+_1.xyz    HC10N+_2.xyz   HC2N+_2.xyz
HC2NCH+_1.xyz     HC2S+_3.xyz     HC3N+_2.xyz      HC3NH+_1.xyz   HC3O+_1.xyz
HC3S+_1.xyz       HC4N+_2.xyz     HC4O+_3.xyz      HC4S+_3.xyz    HC5N+_2.xyz
HC5O+_1.xyz       HC6N+_2.xyz     HC7N+_2.xyz      HC7O+_1.xyz    HC8N+_2.xyz
HC9O+_1.xyz       HCCCHOH+_1.xyz  HCN+_2.xyz       HCNH+_1.xyz    HCO+_1.xyz
HCOCH2OH2+_1.xyz  HCOOH+_2.xyz    HCP+_2.xyz       HCS+_1.xyz     HCl+_2.xyz
HF+_2.xyz         HN2O+_1.xyz     HNC+_2.xyz       HNCO+_2.xyz    HNO+_2.xyz
HNS+_2.xyz        HNSi+_2.xyz     HO2+_3.xyz       HOC+_1.xyz     HOCO+_1.xyz
HOCS+_1.xyz       HPN+_1.xyz      HPO+_2.xyz       HS+_3.xyz      HS2+_1.xyz
HSO+_1.xyz        HSO2+_1.xyz     HSiNH+_1.xyz     HSiO+_1.xyz    HSiO2+_1.xyz
HSiS+_1.xyz       HeH+_1.xyz      N2+_2.xyz        N2H+_1.xyz     NCO+_3.xyz
NH+_2.xyz         NH2+_3.xyz      NH2CH2O+_1.xyz   NH2CNH+_1.xyz  NH3+_2.xyz
NH4+_1.xyz        NO+_1.xyz       NO2+_1.xyz       NS+_1.xyz      NaH2+_1.xyz
NaH2O+_1.xyz      O2+_2.xyz       OCS+_2.xyz       OH+_3.xyz      PC2H+_2.xyz
PC2H2+_1.xyz      PC2H3+_2.xyz    PC2H4+_1.xyz     PC3H+_2.xyz    PC4H+_2.xyz
PC4H2+_1.xyz      PCH2+_1.xyz     PCH3+_2.xyz      PCH4+_3.xyz    PH+_2.xyz
PH2+_1.xyz        PH3+_2.xyz      PN+_2.xyz        PNH2+_2.xyz    PNH3+_1.xyz
PO+_1.xyz         S2+_2.xyz       SO+_2.xyz        SO2+_2.xyz     SiC+_4.xyz
SiC2+_2.xyz       SiC2H+_1.xyz    SiC2H2+_2.xyz    SiC2H3+_1.xyz  SiC3H+_3.xyz
SiC3H2+_2.xyz     SiC4+_2.xyz     SiC4H+_1.xyz     SiCH3+_1.xyz   SiCH4+_2.xyz
SiF+_1.xyz        SiH+_1.xyz      SiH2+_2.xyz      SiH3+_1.xyz    SiH4+_2.xyz
SiH5+_1.xyz       SiN+_3.xyz      SiNC+_1.xyz      SiNCH+_2.xyz   SiO+_2.xyz
SiS+_2.xyz        c-C3H2+_2.xyz   c-C3H2OH+_1.xyz  c-C3H3+_1.xyz  l-C3H2+_2.xyz
l-C3H3+_1.xyz     l-SiC3+_2.xyz   


================================================================================

