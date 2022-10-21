
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4821"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TMP117 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TMP117-PCB')
    newPart['gitName'].append('Adafruit-TMP117-PCB')
    newPart['eagleBoard'].append('/Adafruit_TMP117.brd')
    newPart['eagleSchem'].append('/Adafruit_TMP117.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

