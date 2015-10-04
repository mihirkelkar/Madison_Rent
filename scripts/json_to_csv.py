import json

def read_json():
  with open('../data/clean_data.json', 'r') as infile:
    data = json.load(infile)
  return data

def create_csv(data):
  keys=  ['price', 'bath', 'beds','lat','long']
  file = open('../data/house_rent.csv', 'w')
  file.write(",".join(keys) + "\n")
  print len(data)
  for ii in data:
    temp = list()
    temp+=[str(ii['price']),str(ii['bath']),str(ii['beds']),str(ii['coords'][0]),str(ii['coords'][1])]
    print temp
    file.write(",".join(temp) + "\n")
  file.close()  

data = read_json() 
create_csv(data) 
