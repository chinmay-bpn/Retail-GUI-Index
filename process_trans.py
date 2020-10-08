import json
import random
from functions import writeToFile, mapFileToVar

DSET1_TRANS = '../RDCH/a.txt'

DSET2_TRANS_OLD = '../Instacart_2017_05_01/order_products__prior.csv'
DSET2_TRANS = '../Instacart_2017_05_01/trans_train.txt'
DSET2_TRANS_OLD_TST = '../Instacart_2017_05_01/order_products__train.csv'
DSET2_TRANS_TST = '../Instacart_2017_05_01/trans_test.txt'


DSET1_TRANS_NEW = 'DSET1/trans_prod_sort.txt'
DSET2_TRANS_NEW = 'DSET2/trans_prod_sort.txt'
DSET2_TRANS_NEW_TST = 'DSET2/trans_prod_tst_sort.txt'

DSET1_TRANS_CNT = 9835
#DSET2_TRANS_CNT = 131209
DSET2_TRANS_CNT = 3214874
RPERC = [0.7, 0.3]

def csvTotxt(dset, new_dset):
	f = open(dset, 'r')
	fw = open(new_dset, 'w')
	line = f.readline()
	line = f.readline()
	prev = 0
	prod_list = []
	wp = ""
	while line != "":
		trans = line.split(',')
		oid = trans[0]
		pid = trans[1]
		if len(pid) != 5:
			pid = '0'*(5-len(pid)) + pid
		if prev == 0:
			prev = oid
			prod_list.append(pid)
		elif prev == oid:	
			prod_list.append(pid)
		else:
			if len(prod_list) > 0:
				sp = ';'.join(prod_list)
				sp += '\n'
				wp += sp
			if len(wp) > 5000:
				fw.write(wp)
				wp = ""
			prev = oid	
			prod_list = [pid]
		line = f.readline()
	
	if len(wp) > 0:
		fw.write(wp)	
	fw.close()

def sort_trans(dset, new_file_name, file):
	f = open(file, 'r')
	fw = open(new_file_name, 'w')
	fw_tst = open(new_file_name+'test', 'w')
	wp = ""
	wp_tst = ""
	total_trans = DSET1_TRANS_CNT
	bucket_list = [0, 0]
	line = f.readline()
	if dset == 2:
		line = f.readline()
		total_trans = DSET2_TRANS_CNT
	prod_sup = {}
	trans_small = RPERC[1]*total_trans
	trans_big = RPERC[0]*total_trans
	while line != "":
		line = line.strip()
		trans = line.split(';')
		trans.sort()

		if bucket_list[1] < trans_small:
			if bucket_list[0] >= trans_big:
				bucket = 1
			else:
				bucket = random.randint(0,1)	
		else:
			bucket = 0

		if bucket == 0:
			for item in trans:
				if not prod_sup.has_key(item):
					prod_sup[item] = 1
				else:
					prod_sup[item] += 1	
		
			sp = ';'.join(trans)
			wp += sp + '\n'
			if len(wp) > 5000:
				fw.write(wp)
				wp = ""
		else:
			for item in trans:
				if not prod_sup.has_key(item):
					prod_sup[item] = 0
			sp_tst = ';'.join(trans)
			wp_tst += sp_tst + '\n'
			if len(wp_tst) > 5000:	
				fw_tst.write(wp_tst)
				wp_tst = ""

		bucket_list[bucket] += 1

		line = f.readline()
		
	if len(wp) > 0:
		fw.write(wp)
	if len(wp_tst) > 0:
		fw_tst.write(wp_tst)	
	
	fw.close()
	fw_tst.close()

	prod_list = prod_sup.keys()
	prod_list.sort()
	if dset == 1:
		writeToFile('DSET1/prod_list.txt', prod_list, [])
		writeToFile('DSET1/prod_sup.txt', prod_sup, [])
	else:
		if new_file_name == 'DSET2/trans_prod_sort.txt':
			writeToFile('DSET2/prod_list.txt', prod_list, [])
			writeToFile('DSET2/prod_sup.txt', prod_sup, [])
		else:
			writeToFile('DSET2/prod_sup_tst.txt', prod_sup, [])	


'''
sort_trans(1, DSET1_TRANS_NEW, DSET1_TRANS)
'''

csvTotxt(DSET2_TRANS_OLD, DSET2_TRANS)
sort_trans(2, DSET2_TRANS_NEW, DSET2_TRANS)		

'''
csvTotxt(DSET2_TRANS_OLD_TST, DSET2_TRANS_TST)
sort_trans(2, DSET2_TRANS_NEW_TST, DSET2_TRANS_TST)
'''