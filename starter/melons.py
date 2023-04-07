import csv
from pprint import pprint


class Melon: #this function creates melon class objects.
    def __init__(self, melon_id, common_name, price, image_url, color, seedless): #these are the attributes of the class
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless
   
        
    
    def __repr__(self): #this defines the __repr__ method for printing individual melons.
        return (f"<Melon: {self.melon_id}, {self.common_name}>") #this __repr__ will print the melon_id and common_name of each melon.
    
    def price_str(self): #this method will return the price as a string
        return (f"${self.price}")
    
def read_csv(file): #this function pulls the melon info from the .csv file and prints it in the console.
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
            
        for row in reader:
            pprint(row) 


melon_dict = {}

def melon_obj(file): #this func creates melon objects, and stores them in the global dictionary melon_dict to be used later.
    with open("melons.csv") as csvfile:
        rows = csv.DictReader(csvfile) #this reads each row in the melons.csv file
        
        for row in rows: #this loop creates a melon dictionary for each melon fromm each row in melons.csv, to be stored in the variable.
            melon_id = row['melon_id']
            melon = Melon(melon_id, row['common_name'], float(row['price']), row['image_url'], row['color'], eval(row['seedless']))
            melon_dict[melon_id] = melon

def get_by_id(melon_id): #this function returns individual melon dictionaries by id from the melons list.
   return melon_dict[melon_id]
    
def get_melons(): #this function returns melon dictionaries in a list.
    return list(melon_dict.values())


melon_obj("melons.csv")
