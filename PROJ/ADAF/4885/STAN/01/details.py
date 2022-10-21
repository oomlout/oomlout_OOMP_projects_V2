
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4885"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4885"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SHT40 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SHT40-PCB')
    newPart['gitName'].append('Adafruit-SHT40-PCB')
    newPart['eagleBoard'].append('/Adafruit SHT40.brd')
    newPart['eagleSchem'].append('/Adafruit SHT40.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

