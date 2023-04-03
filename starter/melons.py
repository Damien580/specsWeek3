import csv
from pprint import pprint

class Melon: #this function creates melon class objects.
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id,
        self.common_name = common_name,
        self.price = price,
        self.image_url = image_url,
        self.color = color,
        self.seedless = seedless
    
    def __repr__(self): #this defines the __repr__ method for printing individual melons.
        return (f"<Melon: {self.melon_id}, {self.common_name}>") #this __repr__ will print the melon_id and common_name of each melon.
    
    def price_str(self): #this method will return the price as a string
        return f"${self.price:.2f}"
    
def read_csv(file): #this function pulls the melon info from the .csv file and prints it in the console.
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row) 
            


def melon_obj(file): #this func creates melon objects, and stores them in the global dictionary melon_dict to be used later.
    melon_dict = {}
    with open("melons.csv") as csvfile:
        rows = csv.DictReader(csvfile)
        
        for row in rows:
            melon_id = row['melon_id']
            melon = Melon(melon_id, row['common_name'], float(row['price']), row['image_url'], row['color'], eval(row['seedless']))
            melon_dict[melon_id] = melon

    print(melon_dict)

def get_by_id(melon_id): #this function returns individual melon dictionaries by id.
   return melon_obj[melon_id]
    
def get_melons(): #this function returns individual melon dictionaries by id.
    return list(melon_obj.values())



