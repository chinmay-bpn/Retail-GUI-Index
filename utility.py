from functions import *
import random
import json

RUTIL = [(0.01,0.2), (0.21,0.4), (0.41,0.6), (0.61,0.8), (0.81,1.0)]
RPERC = [0.1, 0.25, 0.3, 0.25, 0.1]

D1PRODS = 169

d1_Util = 'DSET1/prod_util.txt'
d1_Prod = 'DSET1/prod_list.txt'

D2PRODS = 49688

d2_Util = 'DSET2/prod_util.txt'
d2_Prod = 'DSET2/prod_list.txt'


def gen_util(dset):
	bucket_list = [0.0,0.0,0.0,0.0,0.0]
	if dset == 1:
		f = open(d1_Util, 'w')
		for prod in D1PROD_LIST:
			flag = True
			while flag:
				bucket = random.randint(0,4)
				if bucket_list[bucket] < RPERC[bucket]*D1PRODS:
					min_util, max_util = RUTIL[bucket]
					util = round(random.uniform(min_util, max_util), 2)
					prod_write = prod + ':' + str(util) + '\n'
					f.write(prod_write)
					bucket_list[bucket] += 1
					flag = False
		f.close()
	else:
		f = open(d2_Util, 'w')
		for prod in D2PROD_LIST:
			flag = True
			while flag:
				bucket = random.randint(0,4)
				if bucket_list[bucket] < RPERC[bucket]*D2PRODS:
					min_util, max_util = RUTIL[bucket]
					util = round(random.uniform(min_util, max_util), 2)
					prod_write = prod + ':' + str(util) + '\n'
					f.write(prod_write)
					bucket_list[bucket] += 1
					flag = False
		f.close()
					
		'''
		for buck in xrange(len(bucket_list)):
			print bucket_list[buck], RPERC[buck]*D2PRODS			
		'''


'''
load_var('DSET1/prod_list.txt', 'list')
D1PROD_LIST = D1PROD_LIST['prods']
gen_util(1)
'''

load_var('DSET2/prod_list.txt', 'list')
D2PROD_LIST = D2PROD_LIST['prods']
gen_util(2)
