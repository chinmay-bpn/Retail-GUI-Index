from functions import *
import operator
from math import ceil

SLOTS = [2, 4, 6, 8, 10]
#LIMITS = [100, 500, 1000, 2000, 4000]
LIMITS = [5, 10, 20, 40, 80]
SELECT_SLOT = SLOTS[4]

#------------------------DSET 1---------------------------#
pathDSET1 = 'DSET1/Intermediate/GUI/'
DSET1_TRANS_D1 = 'DSET1/trans_level1_O.txt'
DSET1_TRANS_D2 = 'DSET1/trans_level2_O.txt'

d1prod_util_file = '_prod_UL.txt'
d1prod_sup_file = '_prod_SUP.txt'

#------------------------DSET 2---------------------------#
pathDSET2 = 'DSET2/Intermediate/GUI/'
'''
DSET2_TRANS_D1 = 'DSET2/trans_tst_level1_O.txt'
DSET2_TRANS_D2 = 'DSET2/trans_tst_level2_O.txt'
'''
d2prod_util_file = '_prod_UL.txt'
#d2prod_sup_file = '_prod_tst_SUP.txt'

DSET2_TRANS_D1 = 'DSET2/trans_level1_O.txt'
DSET2_TRANS_D2 = 'DSET2/trans_level2_O.txt'
d2prod_sup_file = '_prod_SUP.txt'

GUIindex = {}
d1IndexFile = 'DSET1/Intermediate/GUI/GUI_'
logFile1 = 'DSET1/Intermediate/GUI/log'

#d2IndexFile = 'DSET2/Intermediate/GUI/GUI_tst_'
d2IndexFile = 'DSET2/Intermediate/GUI/GUIfinal_'
logFile2 = 'DSET2/Intermediate/GUI/log_v2trial'

TRANS_LIMIT = 'trans_prod_LIMIT_'
TRANS_TST_LIMIT = 'trans_prod_tst_LIMIT_'

TRANS_DICT = {}

#MIN_SUP = [0.03, 0.028, 0.025, 0.02, 0.012, 0.007, 0.0028, 0.0016, 0.0]

def checkValid(dset, candy, slist):
	if dset == 1:
		return True
	if dset == 2:
		for s in slist:
			ss = s.split(';')
			sup = MIN_SUP[len(ss)-1]
			ksup = kUIindex['sup'][len(ss)-1][s]/DSET2_TRANS_CNT
			print s, candy, ksup, sup
				
			if ksup - sup < 0.000001:
				print 'Rejected'
				return False			

		return True

def gen_trans(dset, ilist, degree, limit):
	if dset == 1:
		if degree == 1:
			trans_org = DSET1_TRANS_D1
		else:
			trans_org = DSET1_TRANS_D2
		trans_path = pathDSET1 + TRANS_LIMIT + str(limit) + '_deg' + str(degree) + '.txt'
	else:
		if degree == 1:
			trans_org = DSET2_TRANS_D1
		else:
			trans_org = DSET2_TRANS_D2
		trans_path = pathDSET2 + TRANS_LIMIT + str(limit) + '_deg' + str(degree) + '.txt'
	
	fr = open(trans_org, 'r')
	fw = open(trans_path, 'w')
	
	wline = ''
	line = fr.readline()
	while line != "":
		line = line.strip()
		trans = line.split(';')
		new_line = ''
		for item in trans:
			if item in ilist:
				if len(new_line) == 0:
					new_line += item
				else:
					new_line += ';' + item
		if len(new_line) != 0:
			if not TRANS_DICT.has_key(new_line):
				TRANS_DICT[new_line] = 1
			else:
				TRANS_DICT[new_line] += 1
		line = fr.readline()
	
	wline = ''
	for new_line in TRANS_DICT.keys():
		wline += new_line + ':' + str(TRANS_DICT[new_line]) + '\n'
		if len(wline) > 5000:
			fw.write(wline)
			wline = ""	
	if len(wline) > 0:
		fw.write(wline)
	fw.close()
	TRANS_DICT.clear()

def calcGUIindex(dset, degree, limit, slot):
	hui = {}
	lprod = {}
	GUIindex['list'] = []
	GUIindex['util'] = [{}]
	GUIindex['sup'] = [{}]

	if dset == 1:
		file = pathDSET1 + TRANS_LIMIT + str(limit) + '_deg' + str(degree) + '.txt'			
		if degree == 1:
			pref = pathDSET1 + 'deg1'
		else:
			pref = pathDSET1 + 'deg2'
		uldict = D1PROD_UTIL
		load_var(pref+d1prod_util_file, 'dict')
		itemset = D1PROD_SUP
		load_var(pref+d1prod_sup_file, 'dict')
		log_file = logFile1
		dIndexFile = d1IndexFile

	else:
		file = pathDSET2 + TRANS_LIMIT + str(limit) + '_deg' + str(degree) + '.txt'			
		if degree == 1:
			pref = pathDSET2 + 'deg1'
		else:
			pref = pathDSET2 + 'deg2'

		uldict = D2PROD_UTIL
		load_var(pref+d2prod_util_file, 'dict')
		itemset = D2PROD_SUP
		load_var(pref+d2prod_sup_file, 'dict')
		log_file = logFile2
		dIndexFile = d2IndexFile

	for item in itemset.keys():
		if item not in uldict:
			uldict[item] = 0.0
		util = round(uldict[item]*itemset[item], 2)
		lprod[item] = util
	sorted_hui = [pair[0] for pair in sorted(lprod.items(), key=operator.itemgetter(1), reverse=True)][:limit]
	gen_trans(dset, sorted_hui, degree, limit)
	print 'Generated Transactions'

	size = 1
	GUIindex['list'] = [[x for x in sorted_hui]]
	logFile(log_file, '----------------------Size: 1----------------------------')
	fout = open(dIndexFile + 'degree_' + str(degree) + "_" + str(limit) + '.txt', 'a')
	print dIndexFile + 'degree_' + str(degree) + "_" + str(limit) + '.txt'
	wp = ''
	candyDict = {}
	for x in sorted_hui:
		GUIindex['util'][0][x] = uldict[x]
		GUIindex['sup'][0][x] = itemset[x]
		logFile(log_file, str(x)+' '+str(uldict[x])+' '+str(itemset[x])+' '+str(uldict[x]*itemset[x]))
		candyDict[x] = (uldict[x], itemset[x])
		wp += x+'|'+json.dumps(candyDict[x]) + '\n'
		if len(wp) > 5000:
			fout.write(wp)
			wp = ""	
	if len(wp) > 0:
		fout.write(wp)
	fout.write('\n')
	fout.close()


	while size < slot:
		candidates = {}
		cand_util = {}
		logFile(log_file, "Generating candidates of size:"+str(size+1))
		for isize in range(0, size/2 + 1):
			jsize = size-(isize+1)
			if jsize < isize and size != 1:
				break
			list1 = GUIindex['list'][isize]
			list2 = GUIindex['list'][jsize]
			for i in xrange(len(list1)):
				itemList = list1[i].split(';')
				for j in xrange(len(list2)):
					ostring = list2[j]
					iset = ostring.split(';')
					nset = iset[:]
					for item in itemList:
						if item not in nset:
							nset.append(item)
					if len(nset) == size+1:
						nset.sort()
						istring = ';'.join(nset)		
						if not candidates.has_key(istring):
							#if checkValid(dset, istring, [GUIindex['list'][isize][i], GUIindex['list'][jsize][j]]):
							candidates[istring] = 0
							cand_util[istring] = 0
							for candy in nset:
								cand_util[istring] += GUIindex['util'][0][candy]
							cand_util[istring] = round(cand_util[istring], 2)
		
		file_ind = open(file, 'r')
		line = file_ind.readline()
		logFile(log_file, "Counting candidates:"+str(len(candidates))+" of size:"+str(size+1)+" = "+str(len(candidates)))
		while line != "":
			line = line.strip()
			line, cnt = line.split(':')
			for candy in candidates.keys():
				items = candy.split(';')
				flag = True
				for item in items:
					if item not in line:
						flag = False
						break
				if flag:
					candidates[candy] += int(cnt)
			line = file_ind.readline()
		hui_prev = []
		hui_util_prev = {}
		logFile(log_file,"Selecting top k candidates of size:"+str(size+1))
		for candy in candidates:
			hui_prev.append(candy)
			hui_util_prev[candy] = round(candidates[candy]*cand_util[candy], 2)

		hui_prev = [pair[0] for pair in sorted(hui_util_prev.items(), key=operator.itemgetter(1), reverse=True)][:limit]
		GUIindex['list'].append(hui_prev[:])
		GUIindex['util'].append({})
		GUIindex['sup'].append({})

		candyDict = {}
		logFile(log_file, "---------DEGREE:"+str(degree)+"-----LIMIT:"+str(limit)+" -- SIZE:"+str(size+1)+"-------------------")
		
		fout = open(dIndexFile + 'degree_' + str(degree) + "_" + str(limit) + '.txt', 'a')
		wp = ''
		for candy in hui_prev:
			GUIindex['util'][size][candy] = cand_util[candy]
			GUIindex['sup'][size][candy] = candidates[candy]
			candyDict[candy] = (cand_util[candy], candidates[candy])
			wp += candy + '|' + json.dumps(candyDict[candy]) + '\n'
			if len(wp) > 5000:
				fout.write(wp)
				wp = ''	
		if len(wp) > 0:
			fout.write(wp)
		fout.write('\n')	
		fout.close()

		logFile(log_file,"----------------------Size:"+str(size+1)+"--------------------------")
		'''
		for key in GUIindex['list'][size]:
			util = GUIindex['util'][size][key]
			sup = GUIindex['sup'][size][key]
			print key, util, sup, util*sup
		print '---------------------- FOR:', len(GUIindex['list'][size]), ' --------------------------'
		'''
		size += 1

'''
#-------------------- GUI Index for DSET 1 ---------------------#
for degree in range(1,3):
	for limit in LIMITS:
		fw = open(d1IndexFile + 'deg' + str(degree) + '_' + str(limit) + '.txt', 'w')
		wp = ""
		ksize = 1
		calcGUIindex(1, degree, limit, SELECT_SLOT)
		for utilDict in GUIindex['util']:
			candyDict = {}
			logFile(logFile1, "---------DEGREE:"+str(degree)+"-----LIMIT:"+str(limit)+" -- SIZE:"+str(ksize)+"-------------------")
			for item in utilDict.keys():
				candyDict[item] = [utilDict[item], GUIindex['sup'][ksize-1][item]]
			wp += json.dumps(candyDict) + '\n'
			if len(wp) > 5000:
				fw.write(wp)
				wp = ""
			ksize += 1
		if len(wp) > 0:
			fw.write(wp)
		fw.close()
'''

#-------------------- GUI Index for DSET 2 ---------------------#
for limit in LIMITS:
	calcGUIindex(1, 2, limit, SELECT_SLOT)
