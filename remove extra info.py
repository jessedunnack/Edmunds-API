import os
import json
from pprint import pprint
'''
for file in os.listdir():
    with open(file) as file:
'''
file = open('lexus.json')
file = json.load(file)
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
for model in file.keys():
    openmodel = file[model]
    for year in openmodel.keys():
        modelyear = openmodel[year]
        stylelist = modelyear['styles']
        for i in range(0,len(stylelist)):
            alpha[i] = stylelist[i]

            
'''            
newfile = open('lexus.json', 'w')
json.dump(file, newfile)
'''
# THINGS TO DELETE:#
# 'colors' #
# 'options' #
# PATH is {model:{year:{styles:[list of styles]}}} #
