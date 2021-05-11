import pandas as pd
import random
from datetime import date
import random
import csv

start_dt = date.today().replace(day=1, month=1).toordinal()
end_dt = date.today().toordinal()

data_lst = []
choice_lst = ['international', 'regular', 'hazardous']
for i in range(200):
	cid = random.randint(1,400)
	rid = random.randint(1,300)
	choice = random.randint(0,2)
	random_day = date.fromordinal(random.randint(start_dt, end_dt))
	data_lst.append([i+1, cid, rid, choice_lst[choice], random_day])

with open('delivery_data.csv', 'w', newline= '\n') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',')
	for obj in data_lst:
		csv_writer.writerow(obj)
