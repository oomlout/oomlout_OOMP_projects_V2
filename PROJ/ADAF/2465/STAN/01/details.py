
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2465"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2465"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PowerBoost 1000C')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PowerBoost-1000C')
    newPart['gitName'].append('Adafruit-PowerBoost-1000C')
    newPart['eagleBoard'].append('/Adafruit PowerBoost 1000C Rev B.brd')
    newPart['eagleSchem'].append('/Adafruit PowerBoost 1000C Rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

