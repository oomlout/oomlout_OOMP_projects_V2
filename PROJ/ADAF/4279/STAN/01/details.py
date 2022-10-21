
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4279"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4279"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Ultimate GPS')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Ultimate-GPS')
    newPart['gitName'].append('Adafruit-Ultimate-GPS')
    newPart['eagleBoard'].append('/Adafruit Ultimate GPS Featherwing.brd')
    newPart['eagleSchem'].append('/Adafruit Ultimate GPS Featherwing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

