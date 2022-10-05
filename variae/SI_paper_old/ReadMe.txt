================================================================================
Title: The GreToBaPe gas-phase reaction network: the importance of being exothermic
Authors: L.Tinacci, S.Ferrada-Chamorro, C.Ceccarelli, S.Pantaleone, D.Ascenzi, A.Maranzana, N.Balucani, P.Ugliengo
================================================================================
Description of contents: This tar.gz archive file contains:
    - In the species folder XXX .XYZ formatted files, providing extended 
    information of all the species studied in the accepted version of the 
    manuscript listed above. A complete listing of all these files is given at 
    the bottom of this ReadMe
    
    - In the Database_Molecules.csv file there are all the extracted and organized 
    information of all the species in the above mentioned folder (i.e. species).
    The csv columns are: 
    species (the codification name), 
    Name (chemical name, if present), 
    Formula (number of atoms per element), 
    Mass (molecular mass, in a.u.), 
    N_atoms (total numer of atom inside the species), 
    Charge (electric charge), 
    Detected (detected in space?), 
    pwd_xyz (pwd to "species/" folder), 
    SpinMultiplicity (electronic spin multiplicity), 
    Energy_Eh (electronic energy in Eh, 
    computed at CCSD(T)/aug-cc-pVTZ//M06-2X/cc-pVTZ), 
    ZPE_Eh (Harmonic zero-point-energy in Eh, computed at M06-2X/cc-pVTZ)
    
    - The following files are Reaction Networks, the file format used for these file
     is reported in details at the bottom of this ReadMe.
        -- Gretobape_ReactionNetwork.dat is the clean and new Reaction Networks 
        -- Gretobape_ReactionNetwork_reduced.dat is the reduced version of the clean and new Reaction Networks 
        -- Gretobape_ReactionNetwork_pre_endo_cleaning.dat is the original Reaction Networks before cleaning process
        -- Gretobape_ReactionNetwork_endo.dat report all the reaction found to be endothermic 
        -- Gretobape_ReactionNetwork_endo_0_10_kjmol.dat report all the reaction kept in the clean network that have a reaction enthalpy between 0 and 10 kJ/mol
        -- Gretobape_ReactionNetwork_domino_endo.dat report all the reaction found to be endothermic and the reaction deleted from domino effect
        -- Gretobape_ReactionNetwork_domino_endo_Si.dat report all the reaction found to be endothermic involving Si-bearing species
        -- Gretobape_ReactionNetwork_domino_endo_S.dat report all the reaction found to be endothermic involving S-bearing species
    
    The scripts to perform cleaning processes and the data are available on the following website:
    
    https://github.com/TinacciL/GreToBaPe_Cleaning
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

H+_0.xyz          H_2Sigma.xyz     H-_1.xyz         He+_2.xyz        He_1Sigma.xyz    C+_2.xyz
C_3Pi.xyz         C-_4.xyz         N+_3.xyz         N_4Sigma.xyz     O+_4.xyz         O_3Sigma.xyz
O-_2.xyz          F+_3.xyz         F_2Pi.xyz        Na+_1.xyz        Na_2S.xyz        Mg+_2.xyz
Mg_1Sigma.xyz     Si+_2.xyz        Si_3Pi.xyz       P+_3.xyz         P_4Sigma.xyz     S+_4.xyz
S_3Pi.xyz         S-_2.xyz         Cl+_3.xyz        Cl_2Pi.xyz       H2+_2.xyz        H2_1Sigma.xyz
HeH+_1.xyz        LiH_1Sigma.xyz   CH+_1c.xyz       CH_2Pi.xyz       NH+_2.xyz        NH_3Sigma.xyz
OH+_3.xyz         OH_2Pi.xyz       OH-_1.xyz        HF+_2.xyz        HF_1Sigma.xyz    NaH_1Sigma.xyz
C2+_4.xyz         C2_1Sigma.xyz    MgH_2Sigma.xyz   CN+_1c.xyz       CN_2Sigma.xyz    CN-_1.xyz
CO+_2.xyz         CO_1Sigma.xyz    N2+_2.xyz        N2_1Sigma.xyz    SiH+_1.xyz       SiH_2Pi.xyz
NO+_1.xyz         NO_2Pi.xyz       CF+_1.xyz        PH+_2.xyz        PH_3Sigma.xyz    O2+_2.xyz
O2_3Sigma.xyz     HS+_3.xyz        HS_2Pi.xyz       HCl+_2.xyz       HCl_1Sigma.xyz   SiC+_4.xyz
SiC_3Pi.xyz       SiN+_3.xyz       SiN_2Sigma.xyz   AlO_2Sigma.xyz   CP+_3.xyz        CP_2Sigma.xyz
CS+_2.xyz         CS_1Sigma.xyz    SiO+_2.xyz       SiO_1Sigma.xyz   PN+_2.xyz        PN_1Sigma.xyz
AlF_1Sigma.xyz    NS+_1.xyz        NS_2Pi.xyz       PO+_1.xyz        PO_2Pi.xyz       SiF+_1.xyz
CCl+_1.xyz        CCl_2Pi.xyz      SO+_2.xyz        SO_3Sigma.xyz    ClO+_3.xyz       OCl_2Pi.xyz
SiS+_2.xyz        SiS_1Sigma.xyz   AlCl_1Sigma.xyz  S2+_2.xyz        S2_3Sigma.xyz    H3+_1.xyz
CH2+_2.xyz        CH2_3B1.xyz      NH2+_3.xyz       NH2_2B1.xyz      H2O+_2.xyz       H2O_1A1.xyz
H2F+_1.xyz        NaH2+_1.xyz      C2H+_3.xyz       C2H_2Sigma.xyz   HCN+_2.xyz       HNC+_2.xyz
HCN_1Sigma.xyz    HNC_1Sigma.xyz   HCO+_1.xyz       HOC+_1.xyz       HCO_2Ap.xyz      N2H+_1.xyz
SiH2+_2.xyz       SiH2_1A1.xyz     HNO+_2.xyz       HNO_1Ap.xyz      PH2+_1.xyz       PH2_2B1.xyz
HO2+_3.xyz        HO2_2App.xyz     H2S+_2.xyz       H2S_1A1.xyz      C3+_2.xyz        C3_1Sigma.xyz
C3-_2.xyz         H2Cl+_1.xyz      CNC+_1.xyz       C2N+_1.xyz       C2N_2Pi.xyz      NaOH_1Sigma.xyz
C2O+_2.xyz        C2O_3Sigma.xyz   CHSi+_3.xyz      HCSi_2Pi.xyz     NCO+_3.xyz       NCO_2Pi.xyz
HNSi+_2.xyz       HNSi_1Sigma.xyz  HCP+_2.xyz       HCP_1Sigma.xyz   CO2+_2.xyz       CO2_1Sigma.xyz
N2O_1Sigma.xyz    HCS+_1.xyz       HCS_2Ap.xyz      HSiO+_1.xyz      SiOH+_1.xyz      HPN+_1.xyz
NO2+_1.xyz        NO2_2A1.xyz      HNS+_2.xyz       POH+_2.xyz       HPO+_2.xyz       HPO_1Ap.xyz
HSO+_1.xyz        H2CCl+_1.xyz     SiC2+_2.xyz      c-SiC2_1A1.xyz   SiNC+_1.xyz      SiNC_2Pi.xyz
CCP+_1.xyz        C2P_2Pi.xyz      C2S+_2.xyz       C2S_3Sigma.xyz   OCS+_2.xyz       OCS_1Sigma.xyz
SiO2_1Sigma.xyz   HSiS+_1.xyz      HSiS_2Ap.xyz     SO2+_2.xyz       SO2_1A1.xyz      HS2+_1.xyz
HS2_2App.xyz      CH3+_1.xyz       CH3_2B2.xyz      NH3+_2.xyz       NH3_1Ap.xyz      H3O+_1.xyz
C2H2+_2.xyz       C2H2_1Sigma.xyz  HCNH+_1.xyz      H2NC+_1.xyz      H2CN_2B2.xyz     H2CO+_2.xyz
H2CO_1A1.xyz      SiH3+_1.xyz      SiH3_2Ap.xyz     H2NO+_1.xyz      PH3+_2.xyz       HOOH_1A1.xyz
H3S+_1.xyz        C3H+_1.xyz       c-C3H_2Ap.xyz    l-C3H_2Pi.xyz    HC2N+_2.xyz      NaH2O+_1.xyz
C2HO+_1.xyz       CH2Si+_2.xyz     H2CSi_1A1.xyz    HNCO+_2.xyz      HNCO_1Ap.xyz     HOCN_1Ap.xyz
HCNO_1Ap.xyz      HONC_1Ap.xyz     HSiNH+_1.xyz     PCH2+_1.xyz      HOCO+_1.xyz      HN2O+_1.xyz
H2CS+_2.xyz       H2CS_1A1.xyz     H2SiO+_2.xyz     H2SiO_1A1.xyz    PNH2+_2.xyz      C4+_2.xyz
C4_3Sigma.xyz     C4-_2.xyz        H2PO+_1.xyz      C3N+_3.xyz       C3N_2Sigma.xyz   C3N-_1.xyz
C3O+_2.xyz        C3O_1Sigma.xyz   C2N2+_2.xyz      SiC2H+_1.xyz     SiC2H_2Pi.xyz    SiNCH+_2.xyz
PC2H+_2.xyz       HC2P_3Sigma.xyz  HC2S+_3.xyz      HCNS_1Ap.xyz     HSNC_1Ap.xyz     HSCN_1Ap.xyz
HOCS+_1.xyz       HSiO2+_1.xyz     H2SiS_1A1.xyz    l-SiC3+_2.xyz    SiC3_1Sigma.xyz  c-SiC3_1A1.xyz
HSO2+_1.xyz       H2S2+_2.xyz      HSSH_1A1.xyz     C3P_2Pi.xyz      C3S+_2.xyz       C3S_1Sigma.xyz
CH4+_2.xyz        CH4_1A1.xyz      NH4+_1.xyz       C2H3+_1.xyz      C2H3_2Ap.xyz     CH2NH_1Ap.xyz
H2COH+_1.xyz      CH3O_2A.xyz      CH3O+_1.xyz      SiH4+_2.xyz      SiH4_1A1.xyz     l-C3H2+_2.xyz
c-C3H2+_2.xyz     c-C3H2_1A1.xyz   H2C3_1A1.xyz     HC3H_3B.xyz      CH2CN+_1.xyz     CH2CN_2B1.xyz
H2CCO+_2.xyz      H2CCO_1A1.xyz    NH2CN_1Ap.xyz    SiCH3+_1.xyz     SiCH3_2App.xyz   PCH3+_2.xyz
CH2PH_1Ap.xyz     HCOOH+_2.xyz     HCOOH_1Ap.xyz    H3CS+_3.xyz      H3SiO+_1.xyz     PNH3+_1.xyz
C4H+_3.xyz        C4H_2Sigma.xyz   C4H-_1.xyz       HC3N+_2.xyz      HC3N_1Sigma.xyz  HCNCC_1Sigma.xyz
HNCCC_1Ap.xyz     HCCNC_1Sigma.xyz HC3O+_1.xyz      SiC2H2+_2.xyz    c-SiC2H2_1A1.xyz HCOCN_1Ap.xyz
PC2H2+_1.xyz      C5+_2.xyz        C5_1Sigma.xyz    C5-_2.xyz        C4N+_1.xyz       C4N_2Pi.xyz
C4O_3Sigma.xyz    SiC3H+_3.xyz     SiC3H_2Pi.xyz    H3S2+_1.xyz      PC3H+_2.xyz      HC3S+_1.xyz
SiC4+_2.xyz       SiC4_1Sigma.xyz  C4P+_1.xyz       C4P_2Pi.xyz      C4S+_2.xyz       C4S_3Sigma.xyz
CH5+_1.xyz        C2H4+_2.xyz      C2H4_1A1.xyz     CH2NH2+_1.xyz    CH3OH+_2.xyz     CH3OH_1Ap.xyz
SiH5+_1.xyz       l-C3H3+_1.xyz    c-C3H3+_1.xyz    CH2C2H_2B1.xyz   CH3CC_2Ap.xyz    CH3CN+_2.xyz
CH3CN_1Ap.xyz     CH2CNH_1Ap.xyz   CH3CO+_1.xyz     NH2CNH+_1.xyz    SiCH4+_2.xyz     HCONH2_1Ap.xyz
PCH4+_3.xyz       CH3O2+_1.xyz     C4H2+_2.xyz      C4H2_1Sigma.xyz  H2C4_1A1.xyz     HC2NCH+_1.xyz
HC3NH+_1.xyz      H2C3O+_2.xyz     HCOC2H_1Ap.xyz   c-C3H2O_1A1.xyz  H2CCCO_1Ap.xyz   SiC2H3+_1.xyz
H2SiC2H_2Ap.xyz   PC2H3+_2.xyz     C5H+_1.xyz       C5H_2Pi.xyz      C5H-_3.xyz       HC4N+_2.xyz
HC4N_3Sigma.xyz   HC4O+_3.xyz      SiC3H2+_2.xyz    C6+_2.xyz        C6_3Sigma.xyz    C6-_2.xyz
C5N+_3.xyz        C5N_2Sigma.xyz   C4N2_1Sigma.xyz  C5O_1A.xyz       SiC4H+_1.xyz     SiC4H_2Pi.xyz
PC4H+_2.xyz       HC4S+_3.xyz      C2H5+_1.xyz      C2H5_2Ap.xyz     CH3NH2+_2.xyz    CH3NH2_1Ap.xyz
CH3OH2+_1.xyz     C3H4+_2.xyz      CH3C2H_1Ap.xyz   CH2CCH2_1A1.xyz  CH3CNH+_1.xyz    C2H4O+_2.xyz
CH3CHO_1Ap.xyz    NH2CH2O+_1.xyz   C4H3+_1.xyz      C4H3_2A.xyz      CH3C3_2Ap.xyz    C3H3N+_2.xyz
CH2CHCN_1Ap.xyz   c-C3H2OH+_1.xyz  HCCCHOH+_1.xyz   C2H3CO+_1.xyz    PC2H4+_1.xyz     C5H2+_2.xyz
H2C5_1A1.xyz      H2C4N+_1.xyz     CH3C2Si_2Ap.xyz  C6H+_3.xyz       C6H_2Pi.xyz      C6H-_1.xyz
HC5N+_2.xyz       HC5N_1Sigma.xyz  HC5O+_1.xyz      PC4H2+_1.xyz     C7+_2.xyz        C7_1Sigma.xyz
C7-_2.xyz         C6N+_1.xyz       C6N_2A.xyz       C2H6+_2.xyz      C2H6_1A1g.xyz    CH3NH3+_1.xyz
C3H5+_1.xyz       C3H5_2A2.xyz     CH3CHOH+_1.xyz   CH3OCH2_2A2.xyz  CH3CHOH_2A.xyz   CH2CH2OH_2A.xyz
C4H4+_2.xyz       CH2CHC2H_1Ap.xyz C3H3NH+_1.xyz    CH3NHCN_1A.xyz   COOCH4+_2.xyz    CH3OCHO_1Ap.xyz
HCOCH2OH_1Ap.xyz  CH3COOH_1Ap.xyz  C5H3+_1.xyz      C5H3_2A.xyz      H3C4N+_2.xyz     CH3C3N_1Ap.xyz
CH2CCHCN_1Ap.xyz  HCCCH2CN_1Ap.xyz C6H2+_2.xyz      C6H2_1Sigma.xyz  H2C6_1A1.xyz     H2C5N+_1.xyz
C7H+_1.xyz        C7H_2Pi.xyz      C7H-_3.xyz       HC6N+_2.xyz      HC6N_3Sigma.xyz  C8+_2.xyz
C8_3Sigma.xyz     C8-_2.xyz        C7N+_3.xyz       C7N_2Pi.xyz      C7O_1A.xyz       C6N2_1Sigma.xyz
SiC6H_2Pi.xyz     CH3CHCH2_1Ap.xyz CH3OCH3+_2.xyz   C2H5OH+_2.xyz    CH3OCH3_1A1.xyz  CH3CH2OH_1Ap.xyz
C4H5+_1.xyz       C4H5_2A.xyz      CH3CONH2_1Ap.xyz H5C2O2+_1.xyz    HCOCH2OH2+_1.xyz C5H4+_2.xyz
CH3C4H_1Ap.xyz    H3C4NH+_1.xyz    SiC3H5_2Ap.xyz   C6H3+_1.xyz      C5H3N+_2.xyz     C7H2+_2.xyz
H2C7_1A1.xyz      H2C6N+_1.xyz     C8H+_3.xyz       C8H_2Pi.xyz      C8H-_1.xyz       HC7N+_2.xyz
HC7N_1Sigma.xyz   HC7O+_1.xyz      C9+_2.xyz        C9_1Sigma.xyz    C9-_2.xyz        C8N+_1.xyz
C8N_2A.xyz        C3H7_2A.xyz      CH3OCH4+_1.xyz   C2H5OH2+_1.xyz   C4H6_1A1.xyz     CH3CH2C2H_1Ap.xyz
CH3CHCCH2_1Ap.xyz C2H6CO+_2.xyz    C2H6CO_1A1.xyz   C5H5+_1.xyz      C5H5_2A.xyz      C6H4+_2.xyz
C6H4_1Ag.xyz      C5H4N+_1.xyz     C7H3+_1.xyz      CH3C5N_1Ap.xyz   C8H2+_2.xyz      C8H2_1Sigma.xyz
H2C8_1A1.xyz      C7H2N+_1.xyz     C9H+_1.xyz       C9H_2Pi.xyz      C9H-_3.xyz       HC8N+_2.xyz
HC8N_3Sigma.xyz   C10+_2.xyz       C10_3Sigma.xyz   C10-_2.xyz       C9N+_3.xyz       C9N_2Pi.xyz
C9O_1A.xyz        C8N2_1Sigma.xyz  SiC8H_2Pi.xyz    C3H8_1A1.xyz     C4H7+_1.xyz      C3H6OH+_1.xyz
C5H6_1Ap.xyz      c-C6H5+_1.xyz    C7H4+_2.xyz      CH3C6H_1Ap.xyz   H3C6NH+_1.xyz    C8H3+_1.xyz
H3C7N+_2.xyz      C9H2+_2.xyz      H2C9_1A1.xyz     H2C8N+_1.xyz     C10H+_3.xyz      C10H_2Pi.xyz
C10H-_1.xyz       C9HN+_2.xyz      HC9N_1Sigma.xyz  HC9O+_1.xyz      C11+_2.xyz       C11_1Sigma.xyz
C10N+_1.xyz       C10N_2Ap.xyz     c-C6H6_1A1.xyz   C7H5+_1.xyz      C8H4+_2.xyz      C9H3+_1.xyz
CH3C7N_1Ap.xyz    C10H2+_2.xyz     C10H2_1S.xyz     C9H2N+_1.xyz     HC10N+_2.xyz     HC10N_3Sigma.xyz
C10N2_1Sigma.xyz  C5H8_1Ap.xyz     C6H7+_1.xyz      C7H6_1A.xyz      C8H5+_1.xyz      C9H4+_2.xyz
C8H4N+_1.xyz      C10H3+_1.xyz     H2C10N+_1.xyz    C9H5+_1.xyz      C7H8_1A.xyz      C6H10_1A.xyz
l-C3H3+_1.xyz     l-SiC3+_2.xyz   



System requirements: The file format of the reaction network files.

    The format and columns of the kida.uva file is the following (as for kida networks downloaded from kida):
    
    Format: 3(a10 1x) 1x 5(a10 1x) 1x 3(e10.3 1x) i5 1x i5 1x a4 1x i2 1x i6 1x i6 1x i2 1x i5 1x i2 1x i1
    Reactants   Products  alpha  beta  gamma  F g Type_of_uncertainty   itype    Trange   Formula    Number     Number_of_(alpha, beta, gamma)      Info

    Columns:
    - "alpha, beta, gamma " are the parameters to compute the rate coefficients. The formula depends on the type of reaction. See http:// kida.obs.u-bordeaux1.fr/help
    
    - "F" is the uncertainty factor on the rate coefficient (See http://kida.obs.u-bordeaux1.fr/help)
    
    - "g" is the temperature dependence of this uncertainty factor (See http://kida.obs.u-bordeaux1.fr/help) 
    Type of uncertainty : lognormal (logn) , normal (norm) , loguniform (logu) , uniform (unif)
    
    - "Itype" is the type of reaction : See http:// kida.obs.u-bordeaux1.fr/help

    - "Trange" is the range of temperatures the rate coefficient is valid. 
    We do not recommend to make extrapolations outside this range. When we do not have information on Trange, default values are used: -9999,9999.

    - "Formula" is a number that referes to the formula needed to compute the rate coefficient of the reaction. 
    1: Cosmic-ray ionization (direct and undirect)
    2: Photo-dissociation (Draine)
    3: Kooij 
    4: ionpol1 
    5: ionpol2 
    6: Troe fall-off
    Correspondances of the names to the mathematical expression can be found at this address: http://kida.obs.u-bordeaux1.fr/help
    Note that for photorates, the type of the UV field is contained in the name fo the formula. For example, Draine means standard interstellar radiation field cf Draine (1978, ApJS, 36,595 ). 
    
    - "Number" is the number of the reaction in the downloaded network.
    
    - "Number of (alpha, beta, gamma)" is the number of (alpha, beta, gamma) in the downloaded network when several values are present in KIDA. 
    When a user selects a range of temperature and that several rate coefficients in KIDA can be in agreement with his search, all data will be included in the network. 
    We then expect the user to choose one of the values. If the reactions are particularly important, we advise the user to contact KIDA to get advises. 
    These reactions that are present more than once in the network are listed below.
    
    - "Info" is information on reaction, like literature reference or comments

================================================================================