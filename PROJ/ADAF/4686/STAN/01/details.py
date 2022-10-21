
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4686"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4686"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TMP235 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TMP235-PCB')
    newPart['gitName'].append('Adafruit-TMP235-PCB')
    newPart['eagleBoard'].append('/TMP235 Rev A.brd')
    newPart['eagleSchem'].append('/TMP235 Rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

