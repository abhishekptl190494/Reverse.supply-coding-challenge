import json

class Address:

    def __init__(self,address):
        self.address = address

    def Street(self):

        AddressText = self.address.replace(',',' ')
        Characters = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
        return " ".join(Characters[:-1])

    def HouseNumber(self):

        global Housenumber
        AddressText=self.address.replace(',','')
        Characters=[]
        Numbers = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
            else:
                Numbers.append(item)

        for number in Numbers:
            if len(number)==5:
                postcode=number
            else:
                HouseNumber = number

        return HouseNumber

    def postcode(self):

        global postcode
        AddressText=self.address.replace(',','')
        Characters=[]
        Numbers = []
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
            else:
                Numbers.append(item)

        for number in Numbers:
            if len(number)==5:
                postcode=number
            else:
                HouseNumber = Numbers
        return postcode

    def cityname(self):


        AddressText=self.address.replace(',','')
        Characters=[]
        for item in AddressText.split():
            if item.isalpha():
                Characters.append(item)
        return Characters[-1]

if __name__=='__main__':
    AddressDict = {}

    AddressObject= Address("Unter den Linden 10a, 10178 Berlin")
    AddressDict['Street'] = AddressObject.Street()
    AddressDict['HouseNumber'] = AddressObject.HouseNumber()
    AddressDict['postcode'] = AddressObject.postcode()
    AddressDict['city'] = AddressObject.cityname()

    json_object = json.dumps(AddressDict, indent=4)

with open ("output.json", "w") as outfile:
    outfile.write (json_object)
