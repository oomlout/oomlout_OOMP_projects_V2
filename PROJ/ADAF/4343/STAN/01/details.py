
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4343"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MONSTER M4SK PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MONSTER-M4SK-PCB')
    newPart['gitName'].append('Adafruit-MONSTER-M4SK-PCB')
    newPart['eagleBoard'].append('/Adafruit MONSTER M4SK.brd')
    newPart['eagleSchem'].append('/Adafruit MONSTER M4SK.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

