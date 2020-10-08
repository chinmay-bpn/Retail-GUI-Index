import json
#------------------------DSET 1---------------------------#

d1TaxL1 = {}
d1TaxL2 = {}
d1TaxL3 = {}

d1L2UTIL = {}
d1L2CNT = {}
d1L3UTIL = {}
d1L3CNT = {}

D1PROD_LIST = {}
D1PROD_UTIL = {}
D1PROD_SUP = {}
D11PROD_SUP = {}
D12PROD_SUP = {}

d1InvTaxL1 = {}
d1InvTaxL2 = {}
d1InvTaxL3 = {}

#------------------------DSET 2---------------------------#

d2TaxL2 = {}
d2TaxL3 = {}

d2L2UTIL = {}
d2L2CNT = {}
d2L3UTIL = {}
d2L3CNT = {}

D2PROD_LIST = {}
D2PROD_UTIL = {}
D2PROD_SUP = {}
D21PROD_SUP = {}
D22PROD_SUP = {}

d2InvTaxL2 = {}
d2InvTaxL3 = {}

#----------------------------------------------------------#

EUCS = {}
TWU = {}
ULIST = {}
SUM = {}
Y = {}

pathGUI_DSET1 = 'DSET1/Intermediate/GUI/'
pathGUI_DSET2 = 'DSET2/Intermediate/GUI/'

pathMLHUI_DSET1 = 'DSET1/Intermediate/MLHUI/'
pathMLHUI_DSET2 = 'DSET2/Intermediate/MLHUI/'

pathMinFHM_DSET1 = 'DSET1/Intermediate/MinFHM/'
pathMinFHM_DSET2 = 'DSET2/Intermediate/MinFHM/'

mapFileToVar = {}
mapFileToVar['DSET1/prod_list.txt'] = D1PROD_LIST
mapFileToVar['DSET2/prod_list.txt'] = D2PROD_LIST

mapFileToVar['DSET1/prod_util.txt'] = D1PROD_UTIL
mapFileToVar['DSET2/prod_util.txt'] = D2PROD_UTIL

mapFileToVar[pathGUI_DSET1+'deg1_prod_UL.txt'] = D1PROD_UTIL
mapFileToVar[pathGUI_DSET1+'deg2_prod_UL.txt'] = D1PROD_UTIL
mapFileToVar[pathGUI_DSET2+'deg1_prod_UL.txt'] = D2PROD_UTIL
mapFileToVar[pathGUI_DSET2+'deg2_prod_UL.txt'] = D2PROD_UTIL

mapFileToVar[pathMLHUI_DSET1+'deg1_prod_UL.txt'] = D1PROD_UTIL
mapFileToVar[pathMLHUI_DSET1+'deg2_prod_UL.txt'] = D1PROD_UTIL
mapFileToVar[pathMLHUI_DSET2+'deg1_prod_UL.txt'] = D2PROD_UTIL
mapFileToVar[pathMLHUI_DSET2+'deg2_prod_UL.txt'] = D2PROD_UTIL

mapFileToVar['DSET1/prod_sup.txt'] = D1PROD_SUP
mapFileToVar['DSET2/prod_sup.txt'] = D2PROD_SUP
mapFileToVar['DSET2/prod_sup_tst.txt'] = D2PROD_SUP

mapFileToVar[pathGUI_DSET1+'deg1_prod_SUP.txt'] = D1PROD_SUP
mapFileToVar[pathGUI_DSET1+'deg2_prod_SUP.txt'] = D1PROD_SUP

mapFileToVar[pathGUI_DSET2+'deg1_prod_SUP.txt'] = D2PROD_SUP
mapFileToVar[pathGUI_DSET2+'deg2_prod_SUP.txt'] = D2PROD_SUP
mapFileToVar[pathGUI_DSET2+'deg1_prod_tst_SUP.txt'] = D2PROD_SUP
mapFileToVar[pathGUI_DSET2+'deg2_prod_tst_SUP.txt'] = D2PROD_SUP

mapFileToVar[pathMinFHM_DSET2+'prod_TWU_2000.0.txt'] = TWU
mapFileToVar[pathMinFHM_DSET2+'prod_EUCS_2000.0.txt'] = EUCS
mapFileToVar[pathMinFHM_DSET2+'prod_ULIST_SUM_2000.0.txt'] = SUM

mapFileToVar[pathMinFHM_DSET2+'prod_TWU_10000.0.txt'] = TWU
mapFileToVar[pathMinFHM_DSET2+'prod_EUCS_10000.0.txt'] = EUCS
mapFileToVar[pathMinFHM_DSET2+'prod_ULIST_SUM_10000.0.txt'] = SUM

mapFileToVar[pathMLHUI_DSET1+'deg1_prod_dict.txt'] = d1TaxL2
mapFileToVar[pathMLHUI_DSET1+'deg2_prod_dict.txt'] = d1TaxL3

mapFileToVar[pathMLHUI_DSET2+'deg1_prod_dict.txt'] = d2TaxL2
mapFileToVar[pathMLHUI_DSET2+'deg2_prod_dict.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET1+'deg1_childs.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'deg2_childs.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_0.7.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_0.7.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_0.8.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_0.8.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_0.9.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_0.9.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_1.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_1.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_1.1.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_1.1.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_1.2.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_1.2.txt'] = d1TaxL3

mapFileToVar[pathGUI_DSET1+'rxdeg1_childs_1.3.txt'] = d1TaxL2
mapFileToVar[pathGUI_DSET1+'rxdeg2_childs_1.3.txt'] = d1TaxL3


mapFileToVar[pathGUI_DSET2+'deg1_childs.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'deg2_childs.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_0.7.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_0.7.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_0.8.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_0.8.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_0.9.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_0.9.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_1.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_1.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_1.1.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_1.1.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_1.2.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_1.2.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET2+'rxdeg1_childs_1.3.txt'] = d2TaxL2
mapFileToVar[pathGUI_DSET2+'rxdeg2_childs_1.3.txt'] = d2TaxL3

mapFileToVar[pathGUI_DSET1+'deg1_inv_prod_dict.txt'] = d1InvTaxL2
mapFileToVar[pathGUI_DSET1+'deg2_inv_prod_dict.txt'] = d1InvTaxL3

mapFileToVar[pathGUI_DSET2+'deg1_inv_prod_dict.txt'] = d2InvTaxL2
mapFileToVar[pathGUI_DSET2+'deg2_inv_prod_dict.txt'] = d2InvTaxL3

def writeToFile(file_name, var, order):
	wf = open(file_name, 'w')
	#print file_name, len(var)
	if isinstance(var, list):
		svar = json.dumps(var)
		wf.write(svar)
	else:
		svar = ""
		if len(order) == 0:
			order = var.keys()	
		for key in order:
			svar += key + '|' + json.dumps(var[key]) + '\n'
			if len(svar) > 5000:
				wf.write(svar)
				svar = ""
		if len(svar) > 0:
			wf.write(svar)
	wf.close()

def bsearch(beg, end, arr, x):
	while beg <= end:
		mid = (beg + end)/2
		if mid < 0 or mid >= len(arr):
			return (False, mid)
		if x in arr[mid]:
			return (True, mid)
		elif x > arr[mid]:
			beg = mid+1
		else:
			end = mid-1
	return (False, mid)	

def read_util(dset, fname):
	store = mapFileToVar[fname]
	
	f = open(fname, 'r')
	line = f.readline()	
	if dset == 1:
		while line != "":
			line = line.strip()
			prod, util = line.split(':')
			D1PROD_UTIL[prod] = float(util)
			line = f.readline()				
	else:
		while line != "":
			line = line.strip()
			prod, util = line.split(':')
			D2PROD_UTIL[prod] = float(util)
			line = f.readline()

def load_var(file_name, vtype):
	file = open(file_name, 'r')
	line = file.readline()
	store = mapFileToVar[file_name]
	if vtype == 'list':
		store['prods'] = json.loads(line)
	else:
		while len(line) > 1:
			line = line.strip()
			key, var = line.split('|')
			store[key] = json.loads(var)
			line = file.readline()

def logFile(file_name, var):
	file = open(file_name, 'a')
	file.write(var)
	file.write('\n')
	file.close()

def load_var_cust(file_name):
	var = {}
	try:
		file = open(file_name, 'r')
		line = file.readline()
		while len(line) > 1:
			line = line.strip()
			key, val = line.split('|')
			var[key] = json.loads(val)
			line = file.readline()
	except:
		pass		
	return var	

def appendToFile(file_name, var):
	wf = open(file_name, 'a')
	wf.write(json.dumps(var)+'\n')
	wf.close()

def writeToFile2(file_name, var):
	wf = open(file_name, 'w')
	wf.write(json.dumps(var)+'\n')
	wf.close()	