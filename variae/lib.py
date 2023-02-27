import numpy as np
import networkx as nx
import pandas as pd
import os

def FromHeToKJmol(Eh):
    tmp = Eh *  6.02214076 * 100 * 4.359748199
    return(tmp)

def ExtractMolFromNetwork(df_network):
	network = FromNetworkDataFrameToNetworkClassList(df_network)
	mol = []
	for j,item in enumerate(network):
		for i,rec in enumerate(network[j].reactants):
			if network[j].reactants[i] not in mol:
				mol.append(network[j].reactants[i])
		for k,prd in enumerate(network[j].products):        
			if network[j].products[k] not in mol:
				mol.append(network[j].products[k])
	df = pd.DataFrame(mol, columns=["species"])
	return(df)

class reaction:
	def __init__(self,rct):
		#Reactants rct[0:3] deleting empty element
		if type(rct[0]) != list:
			if rct[1] == 'nan' and rct[2] == 'nan':
				self.reactants    = [rct[0]]
			elif rct[1] != 'nan' and rct[2] == 'nan':
				self.reactants    = rct[0:2]
			else:
				self.reactants    = rct[0:3]

			if   rct[4] == 'nan' and rct[5] == 'nan' and rct[6] == 'nan':
				self.products     = [rct[3]]
			elif rct[4] != 'nan' and rct[5] == 'nan' and rct[6] == 'nan':
				self.products     = rct[3:5]
			elif rct[4] != 'nan' and rct[5] != 'nan' and rct[6] == 'nan':
				self.products     = rct[3:6]
			else:
				self.products     = rct[3:7]
		else:
			self.reactants    = rct[0]
			self.products     = rct[1]

def FromNetworkCSVtoKidaDAT(pwd_csv,pwd_dat):
	if type(pwd_csv) == str: 
		with open(pwd_csv,"r") as data:
			df_net = pd.read_csv(data, delimiter = '\t')
	else:
		df_net = pwd_csv.copy()
		with open(pwd_dat, "w+") as data:
			data.write('React1     React2    React3       Prod1      Prod2      Prod3      Prod4      Prod5       A          B          C          errA     errB     errC ty  Tmin   Tmax  fr   num n  n !comment ' + '\n')
			for index, rows in df_net.iterrows():
				tmp_line = ''
				tmp = str(rows.R1)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.R2)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.R3)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' ' * 2
				else:
					tmp_line += tmp + ' ' * 2
				tmp = str(rows.P1)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.P2)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.P3)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.P4)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' '
				else:
					tmp_line += tmp + ' '
				tmp = str(rows.P5)
				if tmp == 'nan': 
					tmp = ''
				if len(tmp) <  10:
					tmp_line += tmp + (10 - len(tmp)) * ' ' + ' ' * 3
				else:
					tmp_line += tmp + ' ' * 3
				tmp_line += str("{:.3e}".format(rows.A)) + ' '
				tmp = str("{:.3e}".format(rows.B))
				if tmp[0] == '-':
					tmp_line += tmp + ' '
				else:
					tmp_line += ' ' + tmp + ' '
				tmp = str("{:.3e}".format(rows.C))
				if tmp[0] == '-':
					tmp_line += tmp + ' '
				else:
					tmp_line += ' ' + tmp + ' '
				tmp_line += str("{:.2e}".format(rows.D)) + ' '
				tmp_line += str("{:.2e}".format(rows.E)) + ' '
				if len(str(rows.Distr)) <  4:
					tmp_line += str(rows.Distr) + (4 - len(str(rows.Distr))) * ' ' + ' '
				else:
					tmp_line += str(rows.Distr) + ' '
				if len(str(rows.Type)) <  2:
					tmp_line += (2 - len(str(rows.Type))) * ' ' + str(rows.Type) + ' '
				else:
					tmp_line += str(rows.Type) + ' '
				if len(str(int(rows.T_min))) <  6:
					tmp_line += (6 - len(str(int(rows.T_min)))) * ' ' + str(int(rows.T_min)) + ' '
				else:
					tmp_line += str(int(rows.T_min)) + ' '
				if len(str(int(rows.T_max))) <  6:
					tmp_line += (6 - len(str(int(rows.T_max)))) * ' ' + str(int(rows.T_max)) + ' '
				else:
					tmp_line += str(int(rows.T_max)) + ' '
				if len(str(rows.Formula)) <  2:
					tmp_line += (2 - len(str(rows.Formula))) * ' ' + str(rows.Formula) + ' '
				else:
					tmp_line += str(rows.Formula) + ' '
				if len(str(rows.Number)) <  5:
					tmp_line += (5 - len(str(rows.Number))) * ' ' + str(rows.Number) + ' '
				else:
					tmp_line += str(rows.Number) + ' '
				tmp_line += str(rows.n3) + ' '
				if len(str(rows.n4)) <  2:
					tmp_line += (2 - len(str(rows.n4))) * ' ' + str(rows.n4) + ' '
				else:
					tmp_line += str(rows.n4) + ' '
				tmp = str(rows.comment)
				if tmp == 'nan': 
					tmp = ''
				tmp_line += tmp
				data.write(tmp_line + '\n')
	return()

def FromNetworkKidaDATtoCSV(pwd_dat,save):
	pwd_csv = pwd_dat[:-3] + 'csv'		
	with open(pwd_dat, "r") as database:
		net = []                                                          #list of reactions
		for j,line in enumerate(database):
			if j == 0:
				continue
			try: 
				line_floats = line[90:140]                                    #line parameters
				if 'D' in line_floats:                                        #D instead of e   
					line_float = line_floats.replace('D','e')
				else:
					line_float = line_floats
				A = line_float[0:10]
				B = line_float[11:21]
				C = line_float[22:32]
				D = line_float[33:41]                                         #D and E have len() smaller then A,B,C,D
				E = line_float[42:50]                                       
				if A[7:8] != 'e+' or A[7:8] != 'e-':                          #0+ or 0- instaed e+ or e- for all parameters
					A = A[0:6] + 'e' + A[7:10]
				if B[7:8] != 'e+' or B[7:8] != 'e-':
					B = B[0:6] + 'e' + B[7:10]
				if C[7:8] != 'e+' or C[7:8] != 'e-':
					C = C[0:6] + 'e' + C[7:10]        
				if D[4:6] != 'e+' or D[4:6] != 'e-':                          
					D = D[0:4] + 'e' + D[5:9]
				if E[4:6] != 'e+' or E[4:6] != 'e-':
					E = E[0:4] + 'e' + E[5:9]    
				rct = []                                                      #list info attributes of one reaction, single line in input
				rct.append(str(line[0:10]).replace(" ", ""))                  #R1
				rct.append(str(line[11:21]).replace(" ", ""))                 #R2
				rct.append(str(line[22:33]).replace(" ", ""))                 #R3 one space more because it is empty
				rct.append(str(line[34:44]).replace(" ", ""))                 #P1
				rct.append(str(line[45:55]).replace(" ", ""))                 #P2
				rct.append(str(line[56:66]).replace(" ", ""))                 #P3
				rct.append(str(line[67:77]).replace(" ", ""))                 #P4
				rct.append(str(line[78:89]).replace(" ", ""))                 #P5 one space more because it is empty           
				rct.append(float(A))                                          #A in line[90:100]
				rct.append(float(B))                                          #B in line[101:111]
				rct.append(float(C))                                          #C in line[112:122]
				rct.append(float(D))                                          #D boh in line[123:131]
				rct.append(float(E))                                          #E boh in line[132:140]
				rct.append(str(line[141:146]).replace(" ", ""))               #Distribuction
				rct.append(int(line[147:148]))                                #Type  
				rct.append(float(line[149:155]))                              #T_min
				rct.append(float(line[156:162]))                              #T_max
				rct.append(int(line[163:165]))                                #Formula 
				rct.append(int(line[166:171]))                                #Number
				rct.append(int(line[172:174]))                                #n3
				rct.append(int(line[175:176]))                                #n4
				rct.append(str(line[177:-1]))                                 #comment
				net.append(rct[:])
			except:
				print("*** Reading File input, Type error in line: %d ***" % j)
	df = pd.DataFrame(net, columns=["R1","R2","R3","P1","P2","P3","P4","P5","A","B","C","D","E","Distr","Type","T_min","T_max","Formula","Number","n3","n4","comment"])
	if save == True:	
		with open(pwd_csv, "w+") as output:
			output.write(df.to_csv(sep="\t", index=False))
		with open(pwd_csv,"r") as data:
		    df = pd.read_csv(data, delimiter = '\t')
	elif save == False:
		with open(pwd_csv, "w+") as output:
			output.write(df.to_csv(sep="\t", index=False))
		with open(pwd_csv,"r") as data:
		    df = pd.read_csv(data, delimiter = '\t')
		os.system('rm ' + pwd_csv)
	return(df)

def ReactionEnthalpyCalculation(net,df_tmp):
	col = df_tmp.shape[1] - 1 
	ent = []
	for i,items in enumerate(net):
		tmp_r = 0
		for j,item in enumerate(net[i].reactants):
			tmp = df_tmp.loc[df_tmp['species'] == net[i].reactants[j]]
			if tmp.shape[0] != 0:
				if tmp.iloc[0,col] != np.nan:
					tmp_r +=  float(tmp.iloc[0,col])
				else:
					print(tmp.iloc[0,1],tmp.iloc[0,col])
					tmp_r = None
					break
			else:
				tmp_r = None
				break
		tmp_p = 0    
		for j,item in enumerate(net[i].products):
			tmp = df_tmp.loc[df_tmp['species'] == net[i].products[j]]
			if tmp.shape[0] != 0:
				if tmp.iloc[0,col] != np.nan:
					tmp_p +=  float(tmp.iloc[0,col])
				else:
					tmp_p = None
					break
			else:
				tmp_p = None
				break
		if tmp_r is None or tmp_p is None:
			ent.append(np.nan)
		else:
			tmp_e = tmp_p - tmp_r
			ent.append(tmp_e)
	return(ent)

def FromNetworkDataFrameToNetworkClassList(df_net):
    df_net = df_net.astype('str')
    net_list = []
    for index, rows in df_net.iterrows():
        my_list =[rows.R1, rows.R2, rows.R3, rows.P1, rows.P2, rows.P3, rows.P4, rows.P5]
        net_list.append(my_list)
    network = []
    for j,item in enumerate(net_list):
        network.append(reaction(item))
    return(network)

