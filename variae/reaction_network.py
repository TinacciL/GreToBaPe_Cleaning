import pandas as pd
import numpy as np
import networkx as nx
#The following function can be found in https://github.com/TinacciL/GreToBaPe_Cleaning Github repository 
from lib import FromNetworkDataFrameToNetworkClassList, ExtractMolFromNetwork, FromNetworkKidaDATtoCSV
#Encode KIDA .dat format into pandas dataframe
df_net = FromNetworkKidaDATtoCSV(path_to_network,save=False)
#Extract all the molecules inside the Network inside a dataframe and then to a vector
df_mol = ExtractMolFromNetwork(df_net)
mol_vec  = df_mol['species'].to_numpy()
mol_prop = np.zeros(len(mol_vec),dtype=float)
#Add properties to species (EXAMPLE)
for i in range(len(mol_vec)):
    mol_prop[i] = len(mol_vec[i])
df_mol['properties'] = mol_prop
#Network information and adding fake energy to Network (EXAMPLE)
net_id  = df_net['Number'].to_numpy()
net_rec = np.zeros(len(net_id),dtype=float)
net  = FromNetworkDataFrameToNetworkClassList(df_net)
#Define the network type
net_g   = nx.DiGraph()
#create nodes and add attribute
for i,mol in enumerate(mol_vec):
    net_g.add_node(mol)
    tmp_attr = {'type': 'species','energy': mol_prop[i]}
    net_g.nodes[mol].update(tmp_attr.copy())
#create edges and attribute
for i,rec in enumerate(net):
    net_g.add_node(net_id[i])
    tmp_attr = {'type': 'reaction','energy': net_rec[i]}
    net_g.nodes[net_id[i]].update(tmp_attr.copy())
    for j,item_j in enumerate(set(net[i].reactants)):
        net_g.add_edge(item_j,net_id[i])
    for k,item_k in enumerate(set(net[i].products)):
        net_g.add_edge(net_id[i],item_k)