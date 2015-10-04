"""
The purpose of this script is to build better addresses and remove the rental 
places listed that are obviously outside what will be percieved as the grater madison area. 
"""
import json
from geopy.geocoders import Nominatim

#THIS IS GOING TO BE OUR JSON DATA GLOBAL
data = None
final_list = list()

global geolocator
geolocator = Nominatim()

def get_json_data():
  with open('madison_sanitized.json', 'r') as infile:
    data = json.load(infile)
    print len(data)
    return data

def sanitize_address():
  for ii in data:
    address = ii['address'].lower()
    for city in ['madison', 'fitchburg', 'monona', 'middleton', 'verona', 'mcfarlnad', 'sun praire']:
      if city in address:
        if 'wi' not in address:
          ii['address'] += ' wi'
        final_list.append(ii)
      
        break
    else:
      flag = 0
      for city in ['beleville','milwaukee', 'baraboo', 'janesville', 'monroe', 'juneau']:
        if city in address:
          flag = 1
          break
      else:
        if flag == 0:
          ii['address'] += ' madison, wi' 
          final_list.append(ii)
  return final_list


def build_address(final_list):
  final_data = []
  for ii in final_list:
    #print ii['address']
    try:
      location = geolocator.geocode(ii['address'])
      if 'Dane County' in location.address:
        ii['address'] = location.address
        ii['coords'] = [location.latitude, location.longitude]
        final_data.append(ii)
    except:
      pass
  with open('clean_data.json', 'w') as outfile:
    json.dump(final_data, outfile, indent = 4)
  
        

data = get_json_data()
final_list = sanitize_address()
build_address(final_list)
#print list(set([ii['address'] for ii in final_list]))

      
      
      
