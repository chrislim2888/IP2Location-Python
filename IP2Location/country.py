import csv
import os

"""Country class."""
class Country(object):

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
                        if (line == 1) :
                            if row[0] != "country_code":
                                raise ValueError("Invalid country information CSV file.")
                            self.fields = row
                        else:
                            self.records[row[0]] = row
                    line = line + 1
    
    def get_country_info(self, country_code=None):
        """Get the country information."""
        results = []
        is_not_empty = (self.records and True) or False
        if (is_not_empty == False):
            raise ValueError("No record available.")
        if (country_code):
            results = {}
            if country_code in self.records:
                for i in range(0,len(self.fields)):
                    results[self.fields[i]] = self.records[country_code][i]
                return results
            else:
                return {}
        
        for key in self.records.keys():
            # print (key)
            data = {}
            for i in range(0,len(self.fields)):
                data[self.fields[i]] = self.records[key][i]
            results.append(data)
        return results