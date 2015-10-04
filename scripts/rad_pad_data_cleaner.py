import json

def sanitize_rad_data():
  with open('../data/madison_rad.json', 'r') as outfile:
    data = json.load(outfile)
    final_clean_list = list()
    for ii in data['listings']:
     try:
      for jj in ii['listings']:
        if 'listings' in jj:
          print "In fucking ception"
        temp_data_var = {}
        temp_data_var['url'] = jj['full_url']
        temp_data_var['beds'] = jj['bedrooms']
        temp_data_var['bath'] = jj['bathrooms']
        temp_data_var['price'] = jj['price']
        temp_data_var['coords'] = [jj['latitude'], jj['longitude']]
        temp_data_var['address'] = jj['street_address'] + ' Madison, WI'
      final_clean_list.append(temp_data_var)
     except:
      pass
  with open('../data/temp_file.json', 'w') as infile:
    json.dump(final_clean_list, infile, indent = 4) 


sanitize_rad_data()  
