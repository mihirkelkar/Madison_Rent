from selenium import webdriver
import time
import sys
import json

class CraigsList(object):
  
  def __init__(self):
    self.browser = webdriver.Chrome()
    self.base_url = "https://madison.craigslist.org/apa"
  def search_apt(self):
    listings = list()
    self.browser.get(self.base_url)
    time.sleep(4)
    while True:
      temp_list = list()
      temp_list = self.browser.find_elements_by_class_name("row")
      for ii in temp_list:
        if ii.get_attribute("data-repost-of") == None:
          continue
        temp = ii.find_element_by_class_name("hdrlnk")
        json_data = {}
        place = ii.find_element_by_class_name("pnr")
        if place != None:
          try:
            address = place.find_element_by_tag_name("small").text[1:-1].lower()
            address = address.replace('(','')
            address = address.replace(')','')
            json_data['address'] = address
            sourcetag = ii.find_element_by_class_name("i").get_attribute("href")
            json_data['url'] = sourcetag
            listings.append(json_data)
          except:
            pass
      try:
        button_next = self.browser.find_element_by_class_name("next")
        if button_next != None:
          button_next.click()
          time.sleep(3)
        else:
          break
      except:
        print "Reached the end of the search my lady"
        break
    json_objects = list()
    for listing in listings:
      self.browser.get(listing['url'])
      info = self.browser.find_element_by_class_name("attrgroup").find_elements_by_tag_name("b")
      info = [ii.text for ii in info]
      if len(info) != 3:
        continue
      else:
        listing['beds'] = info[0]
        listing['bath'] = info[1]
        listing['price'] = info[2]
      json_objects.append(listing)
    print json_objects
    with open('madison_sanitized.json', 'w') as outfile:
      json.dump(json_objects, outfile)

  def tear_down(self):
    self.browser.close()
    self.browser.quit()

def main():
  session = CraigsList()
  session.search_apt()
  #session.tear_down()

if __name__ == "__main__":
  main()
