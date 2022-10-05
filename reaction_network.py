import networkx as nx
import pandas as pd
import numpy as np

with open(path_to_molecules_database,"r") as data:
    df_info_mol = pd.read_csv(data, delimiter = '\t')
#with open(path_to_network,"r") as data:
#    df_net = pd.read_csv(data, delimiter = '\t')
df_net = FromNetworkKidaDATtoCSV(path_to_network,save=False)
df_net_tmp = df_net.copy()
df_mol_new = ExtractMolFromNetwork(df_net)
df_info_mol['In_Network'] = df_info_mol['species'].isin(df_mol_new['species'])
df_mol_new['In_database']  = df_mol_new['species'].isin(df_info_mol['species'])
df_mol_new = df_mol_new[(~df_mol_new['species'].isin(nan)) | (~df_mol_new['species'].isin(ph_list))]
df_info_mol = df_info_mol[df_info_mol['In_Network'] == True]
print("Species not prensent in Database:")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(df_mol_new[(df_mol_new['In_database']==False) & (~ df_mol_new['species'].isin(nan + ph_list))])
del df_mol_new

net_g   = nx.DiGraph()
mol_vec = df_info_mol['species'].to_numpy()
mol_ene = (df_info_mol['Energy'] + df_info_mol['ZPE']).to_numpy()
net_id  = df_net_tmp['Number'].to_numpy()
net_rec = df_net_tmp['enthalpy'].to_numpy()
#create nodes and add attribute
for i,mol in enumerate(mol_vec):
    net_g.add_node(mol)
    tmp_attr = {'type': 'species','energy': mol_ene[i]}
    net_g.nodes[mol].update(tmp_attr.copy())
for i,mol in enumerate(ph_list):
    net_g.add_node(mol)
    tmp_attr = {'type': 'species','energy': np.nan}
    net_g.nodes[mol].update(tmp_attr.copy())
#create edges and attribute
for i,rec in enumerate(net):
    net_g.add_node(net_id[i])
    tmp_attr = {'type': 'reaction','enthalpy': net_rec[i]}
    net_g.nodes[net_id[i]].update(tmp_attr.copy())
    for j,item_j in enumerate(set(net[i].reactants)):
        if item_j not in nan:
            net_g.add_edge(item_j,net_id[i])
    for k,item_k in enumerate(set(net[i].products)):
        if item_k not in nan:
            net_g.add_edge(net_id[i],item_k)

#elimination species and reaction loop
tmp_n = net_g.copy()
#delete endothemric/erroneus reactions
del_ent = tmp_endo['Number'].to_list()
tmp_n.remove_nodes_from(del_ent)
print('tot reactions endo: ' + str(len(del_ent)))
print('Reaction number: ')
print(del_ent)
#delete consequence species and reactions not produce and destroyed 
del_species  = []
del_reaction = []
while True:
    tmp_rem = [node for node in tmp_n.nodes if tmp_n.out_degree(node) == 0]
    tmp_rem = tmp_rem + [node for node in tmp_n.nodes if tmp_n.in_degree(node) == 0]
    for i,item in enumerate(ph_list):
        if item in tmp_rem:
            tmp_rem.remove(item)
    tmp = []
    for i,item in enumerate(tmp_rem):
        try:
            if tmp_n.nodes[item]['type']=='species':
                del_species.append(item)
                tmp.append(item)
                tmp_r = [n for n in nx.all_neighbors(tmp_n,item)]
                del_reaction = del_reaction + tmp_r
                tmp = tmp + tmp_r
        except:
            print(item)
    if len(tmp) == 0:
        break
    else:
        tmp_n.remove_nodes_from(tmp)
print('Tot endo del: ' + str(len(del_ent)))
print('Tot species del: ' + str(len(del_species)))
print('Species deleted: ')
print(del_species)
print('Tot reactions del by Domino Effect: ' + str(len(del_reaction)))
print(del_reaction)