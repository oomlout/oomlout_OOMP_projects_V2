
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1296"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1296"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TMP006 and TMP007 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TMP006-and-TMP007-PCB')
    newPart['gitName'].append('Adafruit-TMP006-and-TMP007-PCB')
    newPart['eagleBoard'].append('/TMP006.brd')
    newPart['eagleSchem'].append('/TMP006.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

