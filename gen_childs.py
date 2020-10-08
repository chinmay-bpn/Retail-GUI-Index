from functions import *
import json
import operator

dset1_level1_dict = 'DSET1/Intermediate/GUI/deg1_prod_dict.txt'
dset1_level2_dict = 'DSET1/Intermediate/GUI/deg2_prod_dict.txt'
dset1_level1_sup = 'DSET1/Intermediate/GUI/deg1_prod_SUP.txt'
dset1_level2_sup = 'DSET1/Intermediate/GUI/deg2_prod_SUP.txt'
dset1_UTIL = 'DSET1/prod_util.txt'
dset1_SUP = 'DSET1/prod_sup.txt'
path1 = 'DSET1/Intermediate/GUI/'

dset2_level1_dict = 'DSET2/Intermediate/GUI/deg1_prod_dict.txt'
dset2_level2_dict = 'DSET2/Intermediate/GUI/deg2_prod_dict.txt'
dset2_level1_sup = 'DSET2/Intermediate/GUI/deg1_prod_SUP.txt'
dset2_level2_sup = 'DSET2/Intermediate/GUI/deg2_prod_SUP.txt'
dset2_UTIL = 'DSET2/prod_util.txt'
dset2_SUP = 'DSET2/prod_sup.txt'
path2 = 'DSET2/Intermediate/GUI/'

#thresh2 = [0.0002, 0.0005, 0.001, 0.005, 0.01, 0.02, 0.05]
#thresh1 = [0.005, 0.01, 0.02, 0.05, 0.15, 0.2, 0.25]
thresh = [0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]

def gen_sort(dset, degree):
	if dset == 1:
		util = dset1_UTIL
		sup = dset1_SUP
		util_dict = D1PROD_UTIL
		sup_dict = D1PROD_SUP
		if degree == 1:
			file_in = dset1_level1_dict
			file_lsup = dset1_level1_sup
			lsup = D11PROD_SUP
			file_out = path1 + 'rxdeg1_childs_'
		else:
			file_in = dset1_level2_dict
			file_lsup = dset1_level2_sup
			lsup = D12PROD_SUP
			file_out = path1 + 'rxdeg2_childs_'
	else:
		util = dset2_UTIL
		sup = dset2_SUP
		util_dict = D2PROD_UTIL
		sup_dict = D2PROD_SUP
		if degree == 1:
			file_in = dset2_level1_dict
			file_lsup = dset2_level1_sup
			lsup = D21PROD_SUP
			file_out = path2 + 'rxdeg1_childs_'
		else:
			file_in = dset2_level2_dict
			file_lsup = dset2_level2_sup
			lsup = D22PROD_SUP	
			file_out = path2 + 'rxdeg2_childs_'

	read_util(dset, util)
	load_var(sup, 'dict')
	load_var(file_lsup, 'dict')
	

	for th in thresh:
		fin = open(file_in, 'r')
		fout = open(file_out+str(th)+'.txt', 'w')
		line = fin.readline()
		while line != "":
			line = line.strip()
			key, vlist = line.split('|')
			vlist = json.loads(vlist)
			ndict = {}
			lrev = 0.0
			print vlist
			for vkey in vlist:
				try:
					lrev += util_dict[vkey]*sup_dict[vkey]
				except:
					pass	
		
			lrev_av = round(lrev/len(vlist), 2)
			lrev = 0.0
			print '+++++++++++++++++++++++', key, lrev_av, '++++++++++++++++++++++++++++'
			for vkey in vlist:
				try:
					print sup_dict[vkey]*util_dict[vkey], lrev_av*th
					if sup_dict[vkey]*util_dict[vkey] >= lrev_av*th:
						ndict[vkey] = util_dict[vkey]*sup_dict[vkey]
						lrev += ndict[vkey]
				except:
					pass			
			vlist_sort = [pair[0] for pair in sorted(ndict.items(), key=operator.itemgetter(1), reverse=True)]
			send_list = []
			for v in vlist_sort:
				if lrev == 0:
					send_list.append((v, 0))
				else:
					send_list.append((v, round(ndict[v]/lrev, 2)))
			print '+++++++++++++++++++++++', key, len(send_list), '+++++++++++++++++++++++++++'
			new_line = key + '|' + json.dumps(send_list) + '\n'
			fout.write(new_line)
			line = fin.readline()

		fout.close()

gen_sort(2, 1)