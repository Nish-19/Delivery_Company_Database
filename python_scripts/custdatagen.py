import pandas as pd
from faker import Faker
import csv 

customer_df = pd.DataFrame()
recipient_df = pd.DataFrame()
#customer_df.columns = ['cid', 'cname', 'street address', 'city', 'country', 'phone number', 'number of deliveries', 'is_company']
#recipient_df.columns = ['rid', 'rname', 'street address', 'city', 'country', 'phone number', 'number of deliveries']
faker = Faker()
data_lst = []
# for people
for i in range(300):
	address = faker.address()[:30].replace(',', '')
	address = address.replace('\n', ' ')
	data_lst.append([i+1, faker.name()[:18].replace(',', ' '), address, faker.city()[:20].replace(',', ''), faker.country()[:20].replace(',', ''), faker.phone_number()[:15], 0, 0])
# for companies
for i in range(100):
	address = faker.address()[:30].replace(',', '')
	address = address.replace('\n', ' ')
	data_lst.append([i+301, faker.company()[:18].replace(',', ' '), address, faker.city()[:20].replace(',', ''), faker.country()[:20].replace(',', ''), faker.phone_number()[:15], 0, 1])

# For recipients
rec_lst = []
for i in range(300):
	address = faker.address()[:30].replace(',', '')
	address = address.replace('\n', ' ')
	rec_lst.append([i+1, faker.name()[:18].replace(',', ''), address, faker.city()[:20].replace(',', ''), faker.country()[:20].replace(',', ''), faker.phone_number()[:15], 0])

# customer_df = data_lst
# customer_df.to_csv('customer_data.csv', index = False)
# recipient_df = rec_lst
# recipient_df.to_csv('recepient_data.csv', index = False)
# Convert to files accordingly
with open('customer_data.csv', 'w', newline= '\n') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',')
	for obj in data_lst:
		csv_writer.writerow(obj)

with open('recepient_data.csv', 'w', newline= '\n') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',')
	for obj in rec_lst:
		csv_writer.writerow(obj)
