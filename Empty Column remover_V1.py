from pandas.io.parsers import read_csv
filename = input("Enter the Filename(No extension):")
data = read_csv(filename + '.csv')
filtered_data = data.dropna(axis='columns', how='all')
filtered_data.to_csv(filename + '_formatted.csv', index=False)