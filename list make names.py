import os
a=[]
for make in os.listdir(r'C:\Users\Jesse Dunnack\Dropbox\Edmunds\CarData'):
    print(make[:-5])
    a.append(make[:-5])

print(a)
