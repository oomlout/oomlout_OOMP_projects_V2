
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4570"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4570"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DS1841 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DS1841-PCB')
    newPart['gitName'].append('Adafruit-DS1841-PCB')
    newPart['eagleBoard'].append('/DS1841 rev A.brd')
    newPart['eagleSchem'].append('/DS1841 rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

