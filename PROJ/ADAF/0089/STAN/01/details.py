
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0089"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0089"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Conway Game of Life Kit')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_Conway-Game-of-Life-Kit')
    newPart['gitName'].append('Adafruit_Conway-Game-of-Life-Kit')
    newPart['eagleBoard'].append('/pcb/GoL 1.3.brd')
    newPart['eagleSchem'].append('/pcb/GoL 1.3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

