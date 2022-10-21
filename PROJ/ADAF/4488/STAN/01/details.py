
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4488"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4488"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LIS2MDL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LIS2MDL-PCB')
    newPart['gitName'].append('Adafruit-LIS2MDL-PCB')
    newPart['eagleBoard'].append('/Adafruit LIS2MDL.brd')
    newPart['eagleSchem'].append('/Adafruit LIS2MDL.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

