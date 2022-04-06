import json
import re


class Address:

    def __init__(self,address):
        self.address=address

    def street(self):

        return re.findall("\D+[A-z]+",self.address)[0]

    def houseNumber(self):

        return re.findall("[0-9]+[a-z]",self.address)[0]

    def postcode(self):

        return re.findall("\d{5}",self.address)[0]

    def cityname(self):

        return re.findall("\D+[A-z]+",self.address)[1]

    
if __name__=='__main__':

    AddressDict = {}

    AddressObject= Address('Am teltowkanal 7, 14513 teltow')

    AddressDict['street'] = AddressObject.street()
    AddressDict['houseNumber'] = AddressObject.houseNumber()
    AddressDict['postcode'] = AddressObject.postcode()
    AddressDict['city'] = AddressObject.cityname()

    print(AddressDict)
    json_object = json.dumps(AddressDict, indent=4)

with open ("output.json", "w") as outfile:
    outfile.write (json_object)
