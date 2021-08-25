from pandas.io.parsers import read_csv 
import os

for f_name in os.listdir('.//'):
	if f_name.endswith('.csv'):
		data = read_csv(f_name)
		filtered_data = data.dropna(axis='columns', how='all')
		filtered_data.to_csv('formatted_' + f_name, index=False)
		os.remove(f_name)


