"""
Code > reverse.supply coding challenge
Authour > Abhishek Patel
Date > 07.04.2022
Location > Am Teltowkanal 7, 14513 Teltow 

"""

import json
import re

class Address:
    """
     Return > Working with different address formats and their elements

    """

    def __init__(self,address):
         """
         :type address: String

         """
         self.address=address

    def parse(self):
        print(self.address)
        parsed = re.findall(r'(\D*)(\w{2})(,?)(\s*)(\d{5})(\s*)(\D*)', self.address)
        print(parsed)
        return {
            "street": parsed[0][0],
            "housenumber": parsed[0][1],
            "postalcode": parsed[0][4],
            "city": parsed[0][6]
        }

    
if __name__=='__main__':
    # Add address dictionary
    AddressDict = {}

    AddressObject= Address('Süthen 16 29482 Küsten') # insert address

    json_object = json.dumps(AddressObject.parse(), ensure_ascii=False,indent=4)
 
 # writing to output json

    with open ("output.json", "w", encoding='utf8') as outfile:
        outfile.write (json_object)
