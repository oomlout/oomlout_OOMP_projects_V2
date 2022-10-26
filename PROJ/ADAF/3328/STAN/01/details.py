
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3328"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3328"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX31865 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX31865-PCB')
    newPart['gitName'].append('Adafruit-MAX31865-PCB')
    newPart['eagleBoard'].append('/Adafruit MAX31865.brd')
    newPart['eagleSchem'].append('/Adafruit MAX31865.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

