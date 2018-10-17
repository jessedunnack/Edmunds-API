import os
import json
from pprint import pprint
import time

for filename in os.listdir():
    print(filename)
    with open(filename, encoding='utf-8') as file:
        file = json.load(file)
        alldata = {}
        for model in file.keys():
            openmodel = file[model]
            yearlist = {}
            for year in openmodel.keys():
                newstyledict = {}
                modelyear = openmodel[year]
                stylelist = modelyear['styles']
                for style in stylelist:
                    newstyle={}
                    trim = style['trim']
                    for param in style.keys():
                            a =style[param]
                            newstyle[param] = a
                    del newstyle['colors']
                    del newstyle['options']
                    del newstyle['trim']
                    del newstyle['squishVins']
                    newstyledict[trim] = newstyle
                yearlist[year] = newstyledict
            alldata[model] = yearlist
    with open(filename, 'w') as dump:
        json.dump(alldata, dump)
    time.sleep(0.5)
# THINGS TO DELETE:#
# 'colors' #
# 'options' #
# PATH is {model:{year:{styles:[list of styles]}}} #
