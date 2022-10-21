
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4711"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4711"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AP3429A PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AP3429A-PCB')
    newPart['gitName'].append('Adafruit-AP3429A-PCB')
    newPart['eagleBoard'].append('/AP3429 3.3 Buck rev A.brd')
    newPart['eagleSchem'].append('/AP3429 3.3 Buck rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

