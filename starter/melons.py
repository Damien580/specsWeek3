import csv
from pprint import pprint

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id,
        self.common_name = common_name,
        self.price = price,
        self.image_url = image_url,
        self.color = color,
        self.seedless = seedless
        

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row)
            
