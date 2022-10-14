import csv
import os

"""Region class."""
class Region(object):
    def __init__(self, filename=None):
    
        self.fields = []
        self.records = {}
        
        if filename is not None:
            if os.path.isfile(filename) == False:
                raise ValueError("The CSV file " + filename + " is not found.")
        
        if filename:
            line = 1
            with open(filename, "r", encoding = "utf-8") as f:
                mycsv = csv.reader(f)
                for row in mycsv:
                    if type(row) == list :
                        if row[0] not in self.records.keys():
                            self.records[row[0]] = []
                        if (line == 1) :
                            if row[1] != "subdivision_name":
                                raise ValueError("Invalid region information CSV file.")
                            self.fields = row
                        else:
                            
                            self.records[row[0]].append({"code": row[2], 
                                                       "name": row[1]})
                    line = line + 1
    
    def get_region_code(self, country_code, region_name):
        """Get region code by country code and region name."""
        is_not_empty = (self.records and True) or False
        if (is_not_empty == False):
            raise ValueError("No record available.")
        if country_code in self.records:
            print(self.records[country_code])
            for i in range(0,len(self.records[country_code])):
                if (region_name.upper() == 
                    self.records[country_code][i]["name"].upper()):
                    return self.records[country_code][i]["code"]
        else:
            return