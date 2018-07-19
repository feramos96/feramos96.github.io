import json
import requests
from bs4 import BeautifulSoup

#url_to_scrape = 'https://www.kbb.com/cars-for-sale/cars/used-cars/ford/mustang/?distance=500&year=2016-2016'
original_url = 'https://www.kbb.com/cars-for-sale/cars/used-cars/ford/mustang/?vehicleid=410716&year=2016&distance=500#survey'
url_to_scrape = 'https://www.kbb.com/cars-for-sale/cars/used-cars/ford/mustang/?vehicleid=410716&year=2016&distance=500'
#r = requests.get('https://www.kbb.com/cars-for-sale/cars/used-cars/ford/mustang/?vehicleid=410716&year=2016&distance=500#survey')
#soup = BeautifulSoup(r.content,'html.parser')
#data = soup.find_all('div',{"class":"listing"})

def json_data_to_scrape(url:str,number_pages:int) -> None:
	r = requests.get(original_url)
	soup = BeautifulSoup(r.content,'html.parser')
	data = soup.find_all('div',{"class":"listing"})
	outfile = open('KBBjsondata3.csv','w')
	outfile.write('model,price,mileage,transmission\n')
	for item in data:
		json_data = json.loads(item.contents[-2].text)
		model = json_data['name']
		price = json_data['offers']['price']
		transmission = json_data['vehicleTransmission']
		mileage = json_data['mileageFromOdometer']['value']
		attribute = [model,price,mileage,transmission]
		for i in range(len(attribute)):
			if attribute[i] == '':
				attribute[i] = 'NA'
			else:
				attribute[i] = attribute[i]
		outfile.write(attribute[0] + ',' + attribute[1] + ',' + attribute[2] + ',' +  attribute[3] + '\n')
	for i in range(2,number_pages+1):
		url_page = url + '&p={}'.format(i)
		r2 = requests.get(url_page)
		soup2 = BeautifulSoup(r2.content,'html.parser')
		data2 = soup2.find_all('div',{"class":"listing"})
		for item in data2:
			json_data = json.loads(item.contents[-2].text)
			model = json_data['name']
			price = json_data['offers']['price']
			transmission = json_data['vehicleTransmission']
			mileage = json_data['mileageFromOdometer']['value']
			attribute = [model,price,mileage,transmission]
			for i in range(len(attribute)):
				if attribute[i] == '':
					attribute[i] = 'NA'
				else:
					attribute[i] = attribute[i]
			outfile.write(attribute[0] + ',' + attribute[1] + ',' + attribute[2] + ',' +  attribute[3] + '\n')
	outfile.close()
json_data_to_scrape(url_to_scrape,20)

''' 
----------------- KEYS ------------------------
#json_data
dict_keys(['@context', '@type', 'name', 'image', 'offers', 'description', 'vehicleIdentificationNumber', 'brand', 'mileageFromOdometer', 'color', 'vehicleInteriorColor', 'vehicleTransmission', 'vehicleEngine', 'bodyType'])

#offers
dict_keys(['@type', 'priceCurrency', 'price', 'itemCondition', 'availability'])

for item in data:
	model = item.contents[1].find_all("a",{"class":"js-vehicle-name"})[0].text.strip()
	price = item.contents[3].find_all("div",{"class":"price-info"})[0].find_all('span',{"title-four"})[0].text.strip().replace(",","")
	mileage = item.contents[3].find_all("div",{"class":"specs-wrapper"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip("Mileage: ").replace(",","")
	exterior = item.contents[3].find_all("div",{"class":"specs-wrapper"})[0].find_all("p",{"class":"paragraph-two"})[1].text.replace("Exterior: ","")
	engine = item["data-engine"]
	#transmission = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip('Trans.: ')
	print(model)
	print(engine)
	print(price)
	print(mileage)
	print(exterior)
	print()
'''

def data_to_scrape(url:str,number_pages:int) -> None:
	'''
	This function scrapes vehicle data for 2016 Mustang within 500 miles from 92612 from Kelley Blue Book and then writes it to a csv file.
	'''
	r = requests.get('https://www.kbb.com/cars-for-sale/cars/used-cars/ford/mustang/?vehicleid=410716&year=2016&distance=500#survey')
	soup = BeautifulSoup(r.content,'html.parser')
	data = soup.find_all('div',{"class":"listing"})
	outfile = open('KBBdata.csv','w')
	outfile.write('model,price,mileage,transmission,engine,doors\n')
	for item in data:
		model = item.contents[1].find_all("a",{"class":"js-vehicle-name"})[0].text.strip()
		price = item.contents[3].find_all("div",{"class":"price-info"})[0].find_all('span',{"title-four"})[0].text.strip().replace(",","")
		mileage = item.contents[3].find_all("div",{"class":"specs-wrapper"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip("Mileage: ").replace(",","")
		transmission = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip('Trans.: ')
		if "Engine" in str(transmission):
			transmission = 'NA'
		else:
			transmission = transmission
		engine = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[-2].text.strip("Engine: ")[0]
		doors = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[-1].text.strip("Doors: ")
		outfile.write(model + ',' + str(price) + ',' + str(mileage) + ',' + transmission + ',' + str(engine) + ',' + doors + '\n')
	for i in range(2,number_pages+1):
		url_page = url + '&p={}'.format(i)
		r2 = requests.get(url_page)
		soup2 = BeautifulSoup(r2.content,'html.parser')
		data2 = soup2.find_all('div',{"class":"listing"})
		for item in data2:
				model = item.contents[1].find_all("a",{"class":"js-vehicle-name"})[0].text.strip()
				price = item.contents[3].find_all("div",{"class":"price-info"})[0].find_all('span',{"title-four"})[0].text.strip().replace(",","")
				mileage = item.contents[3].find_all("div",{"class":"specs-wrapper"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip("Mileage: ").replace(",","")
				if "Engine" in str(item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip('Trans.: ')):
					transmission = 'NA'
				else:
					transmission = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[0].text.strip('Trans.: ')
				engine = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[-2].text.strip("Engine: ")[0]
				doors = item.contents[3].find_all("div",{"class":"specs-right"})[0].find_all("p",{"class":"paragraph-two"})[-1].text.strip("Doors: ")
				outfile.write(model + ',' + str(price) + ',' + str(mileage) + ',' + transmission + ',' + str(engine) + ',' + doors + '\n')
	outfile.close()
#data_to_scrape(url_to_scrape,10)

def number_of_rows(filename:'str') -> int:
    '''
    #This function returns the number of rows in the dataset created by get_data_from_url(url,number_pages)
    '''
    number_of_lines = 0
    infile = open(filename,'r')
    for line in infile:
        number_of_lines += 1
    return number_of_lines
print(number_of_rows('KBBjsondata3.csv'))
