
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2305"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2305"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DRV2605 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DRV2605-PCB')
    newPart['gitName'].append('Adafruit-DRV2605-PCB')
    newPart['eagleBoard'].append('/Adafruit DRV2605L STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit DRV2605L STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

