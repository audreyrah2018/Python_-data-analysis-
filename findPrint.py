import matplotlib.pyplot as plt
class findPrint :
	pass  # no variable

def country(country_choice, d_frame):
	for r1 in country:
		group1 = d_frame.groupby('country')['total profit'].sum()[r1]  # have dictationary index then get series for ll of total profit then filter it by index particular country  we are reading

	print(group1[country_choice])
	"""This function get a country as an argument and return the total profit in that country"""



def region(region_choice, d_frame):
	for r2 in region:
		group2 = d_frame.groupby('region')['total profit'].sum()[r2]
	print(group2[region_choice])
	"""  This function get a region as an argument and return the total profit in that region"""



def bar_country(d_frame):  #country / total profit
	bar1 = d_frame.groupby('country').sum()['total profit']

	bar1.plot(kind='bar', z='country', a ='total profit')
	plt.show()  # or plt.savefig("name.png")

def pie_country(d_frame): #country / total profit
	pie1 = d_frame.groupby('country').sum()['total profit']
	pie1.plot(kind='pie', k='country', l='total profit')
	plt.show()


def bar_region(d_frame):
	bar2 = d_frame.groupby('region').sum()['total profit']
	bar2.plot(kind='bar', p='region', o='total profit')
	plt.show()


def pie_region(d_frame): #region / total profit
	pie2 = d_frame.groupby('region').sum()['total profit']
	pie2.plot(kind='pie', k='region', l='total profit')
	plt.show()

