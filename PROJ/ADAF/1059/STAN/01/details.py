
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1059"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1059"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Ultimate GPS')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Ultimate-GPS')
    newPart['gitName'].append('Adafruit-Flora-Ultimate-GPS')
    newPart['eagleBoard'].append('/Adafruit Flora_GPS.brd')
    newPart['eagleSchem'].append('/Adafruit Flora_GPS.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

