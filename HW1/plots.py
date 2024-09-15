import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Breast_Cancer.csv')
values = []

def a():
	for variable in list(data.columns):
		
		for i in data[variable]:
			if i not in values:
				values.append(i)

		plt.hist(data[variable], bins=len(values), color='blue', edgecolor='black')
		plt.title(f'{variable} distribution')
		plt.xlabel(f'{variable}')
		plt.ylabel('Number of individuals')
		plt.savefig(f'{variable} plot.png')
		# plot.show()
	return 

	
def b():
	# Age, Regional node examined, regional nodde +ve, survival months, tumour size are the continuous variables
	# variables = ['Age', 'Regional Node Examined', 'Regional Node Positive', 'Tumor Size']
	# for var in variables:
	# 	plot.scatter(data[var], data['Survival Months'])
	# 	plot.savefig(f'{var} vs Surival Months')

	plt.scatter(data['Age'], data['Survival Months'], color='blue')
	plt.xlabel('Age')
	plt.ylabel('Survivial Months')
	# plot.show()
	plt.savefig('Age vs Survival Months')

	plt.scatter(data['Regional Node Examined'], data['Survival Months'], color='blue')
	plt.xlabel('Regional Node Examined')
	plt.ylabel('Survivial Months')
	# plt.show()
	plt.savefig('Regional Node Examined vs Survival Months')

	plt.scatter(data['Tumor Size'], data['Survival Months'], color='blue')
	plt.xlabel('Tumor Size')
	plt.ylabel('Survivial Months')
	# plt.show()
	plt.savefig('Tumor Size vs Survival Months')


	plt.scatter(data['Regional Node Positive'], data['Survival Months'], color='blue')
	plt.xlabel('Regional Node Positive')
	plt.ylabel('Survivial Months')
	plt.savefig('Regional Node Positive vs Survival Months')
	# plt.show()

	


	return 

def bPearsons():
	print("===============")
	print("Pearsons coefficient against Survival Months:")
	print("Age: ", data['Age'].corr(data['Survival Months']))
	print("Regional Node Examined", data['Regional Node Examined'].corr(data['Survival Months']))
	print("Regional Node Positive", data['Regional Node Positive'].corr(data['Survival Months']))
	print("Tumor Size", data['Tumor Size'].corr(data['Survival Months']))
	print("===============")
	print()
	return 

def variable_type(data, column_name, threshold=2):
	# print(data[column_name])
	unique_values = []
	for point in data[column_name]:
		if point not in unique_values:
			unique_values.append(point)
	if len(unique_values) > 10:
		return 0
	return 1

def c():
	status = ['Alive', 'Dead']
	vars_x = []
	for variable in list(data.columns):
		if variable_type(data, variable):
			vars_x.append(variable)

	categories = {}
	for var in vars_x:
		categories[var] = []
		for i in data[var]:
			if i not in categories[var]:
				categories[var].append(i)
	

	for category in categories.keys():
		miniDF = data.groupby([f'{category}', 'Status']).size().reset_index(name='count')
		finalDF = miniDF.pivot(index=f'{category}', columns='Status', values='count')
		finalDF.plot(kind='bar', stacked=False)
		plt.xlabel(f'{category}')
		plt.ylabel('Status')
		plt.xticks(rotation=45, ha='right')
		plt.savefig(f'{category} vs Status.png')
		plt.show()
	

		


		
c()



# print(data.columns)
# a()
# b()
# for item in data['Status']:
# 	if(item!='Alive'):
# 		print(item)


# print(data['Status'])