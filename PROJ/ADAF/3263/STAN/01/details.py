
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3263"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX31856 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX31856-PCB')
    newPart['gitName'].append('Adafruit-MAX31856-PCB')
    newPart['eagleBoard'].append('/Adafruit MAX31856.brd')
    newPart['eagleSchem'].append('/Adafruit MAX31856.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

