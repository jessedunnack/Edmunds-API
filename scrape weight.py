from bs4 import BeautifulSoup
from urllib import request
from pprint import pprint
import re

makes=[]
edmundsmakes= ['acura', 'alfa-romeo', 'am-general', 'aston-martin', 'audi', 'bentley', 'bmw', 'bugatti', 'buick', 'cadillac', 'chevrolet', 'chrysler', 'daewoo', 'dodge', 'eagle', 'ferrari', 'fiat', 'fisker', 'ford', 'genesis', 'geo', 'gmc', 'honda', 'hummer', 'hyundai', 'isuzu', 'jaguar', 'jeep', 'kia', 'lamborghini', 'land-rover', 'lexus', 'lincoln', 'lotus', 'maserati', 'maybach', 'mazda', 'mclaren', 'mercedes-benz', 'mercury', 'mini', 'mitsubishi', 'nissan', 'oldsmobile', 'panoz', 'plymouth', 'pontiac', 'porsche', 'ram', 'rolls-royce', 'saab', 'saturn', 'scion', 'smart', 'spyker', 'subaru', 'suzuki', 'tesla', 'toyota', 'volkswagen', 'volvo']
for make in edmundsmakes:
    try:
        remake = ' '.join(make.split('-'))
        makes.append(remake)
    except:
        TypeError

    
inboth = []

def listmakes(givenlist):
    webpage = request.urlopen('http://www.auto-data.net/en/?f=brands').read()
    soup = BeautifulSoup(webpage, "html.parser")
    for make in makes:
        a = soup.find_all('a', string = make.title())
        print(make)
        print(a)
listmakes(makes)
