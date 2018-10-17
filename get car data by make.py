import json
from pprint import pprint
import urllib.request
import time

file = open('edmundsdata_allcars.txt')
file = json.loads(file.read())

All_Models = {}
for make in file['makes']:
    make_name = make['niceName']
    models = {}
    for model in make['models']:
        yrs = model['years']
        years = []
        for sets in yrs:
            years.append(str(sets.get('year')))
        models[model['niceName']] = years
    All_Models[make_name] = models

errors=[]
del All_Models['isuzu']
del All_Models['geo']
del All_Models['nissan']
del All_Models['mini']
del All_Models['scion']
del All_Models['spyker']
del All_Models['fisker']
del All_Models['panoz']
del All_Models['saab']
del All_Models['plymouth']
del All_Models['subaru']
del All_Models['ram']
del All_Models['maserati']
del All_Models['am-general']
del All_Models['toyota']
del All_Models['smart']
del All_Models['chrysler']
del All_Models['land-rover']
del All_Models['jeep']
del All_Models['aston-martin']
del All_Models['lamborghini']
del All_Models['dodge']
del All_Models['buick']
del All_Models['fiat']
del All_Models['ferrari']
del All_Models['eagle']
del All_Models['hummer']
del All_Models['kia']
del All_Models['genesis']
del All_Models['mitsubishi']
del All_Models['mclaren']
del All_Models['saturn']
del All_Models['daewoo']
del All_Models['alfa-romeo']
del All_Models['rolls-royce']
del All_Models['hyundai']
del All_Models['bugatti']
del All_Models['acura']
del All_Models['volkswagen']
del All_Models['suzuki']
del All_Models['mercedes-benz']
del All_Models['pontiac']
del All_Models['honda']
del All_Models['cadillac']
del All_Models['infiniti']
del All_Models['lincoln']
del All_Models['maybach']
del All_Models['lexus']
del All_Models['bmw']
del All_Models['volvo']
del All_Models['oldsmobile']
del All_Models['mercury']
del All_Models['gmc']
del All_Models['mazda']
del All_Models['jaguar']
del All_Models['audi']
del All_Models['lotus']
del All_Models['porsche']
del All_Models['ford']
del All_Models['bentley']
del All_Models['tesla']
del All_Models['chevrolet']


print(len(All_Models))

for make in All_Models.keys():
    info = All_Models[make]
    makedata = {}
    for model in info.keys():
        databyyear = {}
        print(model)
        years = info[model]
        for year in years:
            try:
                print('Making request...')
                request = urllib.request.Request('https://api.edmunds.com/api/vehicle/v2/' + make + '/' + model + '/' + year + '/styles?fmt=json&api_key=c7dbacwnp8fqb7swhb77gbrh&view=full')
                response = urllib.request.urlopen(request)
                encoding = response.info().get_content_charset('utf8')
                details = json.loads(response.read().decode(encoding))
                databyyear[year] = details
                print('Data logged for ' + year + ' ' + make + ' ' + model + '.')
            except ValueError or IncompleteRead:
                errors.append((year + ' ' + make + ' ' + model))
                continue
        makedata[model] = databyyear
    with open(make + '.json', 'w') as file:
        json.dump(makedata, file)
    print(errors)
