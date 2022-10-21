
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4566"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AHT20 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AHT20-PCB')
    newPart['gitName'].append('Adafruit-AHT20-PCB')
    newPart['eagleBoard'].append('/Adafruit AHT20 Temperature & Humidity.brd')
    newPart['eagleSchem'].append('/Adafruit AHT20 Temperature & Humidity.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

