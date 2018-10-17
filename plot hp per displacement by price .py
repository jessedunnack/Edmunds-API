import json
import matplotlib.pyplot as pyplot
import os
import json

fig = pyplot.figure()
ax = pyplot.axes()

points_w_annotation=[]
makedata = input('Choose a make to plot:')
makedata = makedata + '.json'
'''
for makedata in os.listdir('C:\\Users\\Jesse Dunnack\\Dropbox\\Edmunds\\CarData'):
'''
for i in range(0,1):
    with open('C:\\Users\\Jesse Dunnack\\Dropbox\\Edmunds\\CarData\\' + makedata) as rawfile:
        file = json.load(rawfile)
        for modelname in file.keys():
            model = file[modelname]
            for yearname in model.keys():
                year = model[yearname]
                for trimname in year.keys():
                    trim = year[trimname]
                    makename = trim['make']
                    makename = makename['name']
                    modelname = trim['model']
                    modelname = modelname['name']
                    yr = trim['year']
                    yr = str(yr['year'])
                    if 'price' in trim.keys():
                        pricedict = trim['price']
                        if 'usedPrivateParty' in pricedict.keys():
                            price = pricedict['usedPrivateParty']
                        elif 'baseMSRP' in pricedict.keys():
                            price = pricedict['baseMSRP']
                        else:
                            print('ERROR: NO PRICE')
                            continue
                        enginedict = trim['engine']
                        if 'horsepower' in enginedict.keys():
                            power = enginedict['horsepower']
                            carname = (yr + ' ' + makename + ' ' + modelname + ' ' + trimname)
                            point, = pyplot.plot(price, power, 'ro', markersize=5, alpha=0.5)
                            annotation = ax.annotate((carname + '\n$'+ str(price)+'0\n'+str(power)+' hp') , (price,power), xycoords='data', xytext=(price,power), textcoords='data')
                            annotation.set_visible(False)
                            points_w_annotation.append([point, annotation])

                        else:
                            continue
                    else:
                        continue

def hovershow(event):
    visibility_changed = False
    for point, annotation in points_w_annotation:
        should_be_visible = (point.contains(event)[0]==True)

        if should_be_visible != annotation.get_visible():
            visibility_changed=True
            annotation.set_visible(should_be_visible)
    if visibility_changed:
        pyplot.draw()

hovershow_id = fig.canvas.mpl_connect('motion_notify_event', hovershow)
pyplot.show()
