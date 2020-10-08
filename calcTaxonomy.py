import json 
from functions import *

SupL1 = 'deg1_prod_SUP.txt'
SupL2 = 'deg2_prod_SUP.txt'
TransL1 = 'trans_level1.txt'
TransL2 = 'trans_level2.txt'
TransL1_O = 'trans_level1_O.txt'
TransL2_O = 'trans_level2_O.txt'

#------------------------DSET 1---------------------------#
DSET1_TRANS = 'DSET1/trans_prod_sort.txt'
DSET1_TAXO = '../RDCH/paths_5.txt'
DSET1_VARS = ['Home/', '/']

#------------------------DSET 2---------------------------#
DSET2_TRANS = 'DSET2/trans_prod_sort.txt'
DSET2_TAXO = '../Instacart_2017_05_01/products.csv'


#--------------------------TEST---------------------------#

DSET2_TRANS = 'DSET2/trans_prod_sort.txt'
DSET2_TAXO = '../Instacart_2017_05_01/products.csv'
TransL1 = 'trans_level1.txt'
TransL2 = 'trans_level2.txt'
TransL1_O = 'trans_level1_O.txt'
TransL2_O = 'trans_level2_O.txt'
#SupL1 = 'deg1_prod_tst_SUP.txt'
#SupL2 = 'deg2_prod_tst_SUP.txt'


#-------------------  Paths for Storing  -----------------#

pathApproach1 = 'Intermediate/GUI/'
pathApproach2 = 'Intermediate/MLHUI/'

pathDSET1 = 'DSET1/'
pathDSET2 = 'DSET2/'

def getLevel(dset, level):
	if level == 0:
		return (d1TaxL3, d1InvTaxL3)
		
	elif level == 1:
		return (d1TaxL2, d1InvTaxL2)
		
	elif level == 2:
		return (d1TaxL1, d1InvTaxL1)

def taxDSET(dset, approach_path):
	if dset == 1:
		f1 = open(DSET1_TAXO, 'r')
		i = 0
		line = f1.readline()
		while line != '':
			line = line.strip()
			if i%2 == 0:
				prod_name = line.split('.')[1]
			else:
				taxo = line.split(DSET1_VARS[0])[1]
				levels = taxo.split('/')
				j = 0
				for level in levels:
					if j == 3:
						break
					taxDict, taxInvDict = getLevel(dset, j)
					if level not in taxDict.keys():
						taxDict[level] = [prod_name]
					else:
						taxDict[level].append(prod_name)
					
					taxInvDict[prod_name] = level
					j += 1
			i += 1
			line = f1.readline()	
		writeToFile(pathDSET1+approach_path+'deg1_prod_dict.txt', d1TaxL1, [])
		writeToFile(pathDSET1+approach_path+'deg1_inv_prod_dict.txt', d1InvTaxL1, [])
		writeToFile(pathDSET1+approach_path+'deg2_prod_dict.txt', d1TaxL2, [])
		writeToFile(pathDSET1+approach_path+'deg2_inv_prod_dict.txt', d1InvTaxL2, [])			
	else:
		f1 = open(DSET2_TAXO, 'r')
		i = 0
		line = f1.readline()
		line = f1.readline()
		while line != '':
			line = line.strip()
			data = line.split(',')
			ind = len(data) - 1
			pid = data[0]
			pid = (5-len(pid))*'0' + pid
			aid = data[ind-1]
			aid = (3-len(aid))*'0' + aid
			did = data[ind]
			did = (2-len(did))*'0' + did
						
			d2InvTaxL2[pid] = aid
			if aid in d2TaxL2.keys():
				d2TaxL2[aid].append(pid)
			else:
				d2TaxL2[aid] = [pid]	
			
			d2InvTaxL3[pid]= did
			if did in d2TaxL3.keys():
				d2TaxL3[did].append(pid)
			else:
				d2TaxL3[did] = [pid]
			
			line = f1.readline()
		writeToFile(pathDSET2+approach_path+'deg1_prod_dict.txt', d2TaxL2, [])
		writeToFile(pathDSET2+approach_path+'deg1_inv_prod_dict.txt', d2InvTaxL2, [])
		writeToFile(pathDSET2+approach_path+'deg2_prod_dict.txt', d2TaxL3, [])
		writeToFile(pathDSET2+approach_path+'deg2_inv_prod_dict.txt', d2InvTaxL3, [])

def gen_util(dset, approach_path):
	deg1Dict = {}
	deg2Dict = {}
	
	if dset == 1:
		utilDict = D1PROD_UTIL
		invTax1 = d1TaxL1
		invTax2 = d1TaxL2
		pathDSET = pathDSET1
		fname = 'DSET1/prod_util.txt'
	else:
		utilDict = D2PROD_UTIL
		invTax1 = d2TaxL2
		invTax2 = d2TaxL3
		cntDict2 = d2L2CNT
		pathDSET = pathDSET2
		fname = 'DSET2/prod_util.txt'

	read_util(dset, fname)
		
	for key in invTax1:
		x = 0.0
		for item in invTax1[key]:
			try:
				x += utilDict[item]
			except:
				utilDict[item] = 0.0
		'''
		if dset == 2:
			x /= 1000
		'''
		x /= len(invTax1[key])
		deg1Dict[key] = round(x, 2)	

	writeToFile(pathDSET+approach_path+'deg1_prod_UL.txt', deg1Dict, [])	

	for key in invTax2:
		x = 0.0
		for item in invTax2[key]:
			x += utilDict[item]
		'''
		if dset == 2:
			x /= 100000
		'''
		x /= len(invTax2[key])
		deg2Dict[key] = round(x, 2)	

	writeToFile(pathDSET+approach_path+'deg2_prod_UL.txt', deg2Dict, [])	

def genTrans(dset, approach_path):
	if dset == 1:
		pathDSET = pathDSET1
		transDB = DSET1_TRANS
		DBL2 = pathDSET1 + TransL2
		DBL1 = pathDSET1 + TransL1
		DBL2O = pathDSET1 + TransL2_O
		DBL1O = pathDSET1 + TransL1_O
		cntDict1 = d1L2CNT
		cntDict2 = d1L3CNT
		deg2Dict = d1InvTaxL2
		deg1Dict = d1InvTaxL1
		
	else:
		pathDSET = pathDSET2
		transDB = DSET2_TRANS
		DBL2 = pathDSET2 + TransL2
		DBL1 = pathDSET2 + TransL1
		DBL2O = pathDSET2 + TransL2_O
		DBL1O = pathDSET2 + TransL1_O
		cntDict1 = d2L2CNT
		cntDict2 = d2L3CNT
		deg2Dict = d2InvTaxL3
		deg1Dict = d2InvTaxL2

	rfile = open(transDB, 'r')
	wfile1 = open(DBL1, 'w')
	wfile1O = open(DBL1O, 'w')
	wp1 = ""
	wp1O = ""

	'''
	wfile2 = open(DBL2, 'w')
	wfile2O = open(DBL2O, 'w')	
	wp2 = ""
	wp2O = ""
	'''
	line = rfile.readline()
	while line != "":
		line = line.strip()
		trans = line.split(';')
		tmp_deg1Dict = {}
		tmp_deg2Dict = {}
		tns1 = {}
		tns2 = {}
		for item in trans:
			tns1[deg1Dict[item]] = True
			tns2[deg2Dict[item]] = True

		for item in tns1.keys():	
			if cntDict1.has_key(item):
				cntDict1[item] += 1
			else:
				cntDict1[item] = 1

		for item in tns2.keys():		
			if cntDict2.has_key(item):
				cntDict2[item] += 1
			else:
				cntDict2[item] = 1
		'''		
		if tmp_deg1Dict.has_key(deg1Dict[item]):
			tmp_deg1Dict[deg1Dict[item]] += 1
		else:
			tmp_deg1Dict[deg1Dict[item]] = 1

		if tmp_deg2Dict.has_key(deg2Dict[item]):
			tmp_deg2Dict[deg2Dict[item]] += 1
		else:
			tmp_deg2Dict[deg2Dict[item]] = 1
		
		sp1 = tmp_deg1Dict.keys()[:]
		sp1.sort()
		tp1 = ";".join(sp1)
		kp1 = ""
		for x in xrange(len(sp1)):
			if x != 0:
				kp1 += ';' + sp1[x] + ':' + str(tmp_deg1Dict[sp1[x]])
			else:
				kp1 += sp1[x] + ':' + str(tmp_deg1Dict[sp1[x]])	
		
		wp1 += kp1 + '\n'

		if len(wp1) > 5000:
			wfile1.write(wp1)
			wp1 = ""

		wp1O += tp1 + '\n'
		if len(wp1O) > 5000:
			wfile1O.write(wp1O)
			wp1O = ""
		sp2 = tmp_deg2Dict.keys()[:]
		sp2.sort()
		tp2 = ";".join(sp2)
		kp2 = ""
		for x in xrange(len(sp2)):
			if x != 0:
				kp2 += ';' + sp2[x] + ':' + str(tmp_deg2Dict[sp2[x]])
			else:
				kp2 += sp2[x] + ':' + str(tmp_deg2Dict[sp2[x]])	
		
		wp2 += kp2 + '\n'
		if len(wp2) > 5000:
			wfile2.write(wp2)
			wp2 = ""

		wp2O += tp2 + '\n'	
		if len(wp2O) > 5000:
			wfile2O.write(wp2O)
			wp2O = ""
		'''
		line = rfile.readline()
	
	'''
	if len(wp1) > 0:
		wfile1.write(wp1)
	if len(wp1O) > 0:
		wfile1O.write(wp1O)	

	if len(wp2) > 0:
		wfile2.write(wp2)
	if len(wp2O) > 0:
		wfile2O.write(wp2O)
	
	wfile1.close()
	wfile1O.close()		
	wfile2.close()
	wfile2O.close()
	'''
	writeToFile(pathDSET+approach_path+SupL1, cntDict1, [])
	writeToFile(pathDSET+approach_path+SupL2, cntDict2, [])



taxDSET(2, pathApproach1)
#genTrans(2, pathApproach1)
#gen_util(2, pathApproach1)
