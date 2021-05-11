import pandas as pd
import random
from datetime import timedelta
from datetime import date
from datetime import datetime
import random
import csv

tids_chosen = [i for i in range(1,300, 2)]
customer_df = pd.read_csv('csvfiles/customer_data.csv')
recepient_df = pd.read_csv('csvfiles/recepient_data.csv')
delivery_df = pd.read_csv('delivery_data.csv')

def getDate(tid_t, delivery_df):
	date = ''
	rid = 0
	type_t = ''
	for i, row in delivery_df.iterrows():
		if row['tid'] == tid_t:
			date = row['ini_date']
			rid = row['rid']
			type_t = row['type']
			break
	return date, rid, type_t

def getLocation(rid_t, recepient_df):
	location = ''
	for i, row in recepient_df.iterrows():
		if row['rid'] == rid_t:
			location = row['city']
			break
	return location

numbs = ["0010", "0011", "0110"]
data_lst = []
dates = []
# Making dispatch here
for i in tids_chosen:
	date_here, cid, type_t = getDate(i, delivery_df)
	try:
		new_date = datetime.strptime(date_here, "%d-%m-%Y") + timedelta(days=1)
	except ValueError:
		continue
	print(i, new_date, cid, type_t)
	choice = numbs[random.randint(0,2)]
	prefix = ''
	mode = ''
	if type_t == 'international':
		prefix = 'F'
		mode = 'Flight'
	else:
		prefix = 'T'
		mode = 'Truck'
	transport_num = prefix + choice
	data_lst.append([i, new_date, 'Dispatched', mode, transport_num, 'transit'])
# Making delivering here
deliv_chosen = [i for i in tids_chosen if i % 3 ==0 or i % 5 ==0]

for i in deliv_chosen:
	date_here, rid, type_t = getDate(i, delivery_df)
	if type_t == 'international':
		new_date = datetime.strptime(date_here, "%d-%m-%Y") + timedelta(days=2)
	else:
		try:
			new_date = datetime.strptime(date_here, "%d-%m-%Y") + timedelta(days=1)
		except ValueError:
			continue
	choice = numbs[random.randint(0,2)]
	transport_num = 'T' + choice
	location = getLocation(rid, recepient_df)
	data_lst.append([i, new_date, 'Delivering', "Truck", transport_num, location])

	# For delivered
	if (i%9==0 or i % 5 == 0):
		data_lst.append([i, new_date, 'Delivered', "Truck", transport_num, location])

print(len(data_lst))

with open('delivery_status_data.csv', 'w', newline= '\n') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',')
	for obj in data_lst:
		csv_writer.writerow(obj)