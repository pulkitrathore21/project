import csv
import json
fp=open('fetchdata.txt',"r")

r=fp.read()
dict1=json.dumps(r,indent=4)
dict2=dict #i dnt know how to
'''
the type of str is showing the string so that i try to do in json format so that i will convert that into dict 

i know how to write in the csv file 

'''
intocsv=csv.writerow("id","email","firstname","lastname","avatar") # i am writing heading in csv file
'''
here i want to use one for loop and the same process i will repeat

'''
for i in intocsv.items():
    




# frea=open('one.csv','w')



