
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4090"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4090"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit USB C Downstream Breakout')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-USB-C-Downstream-Breakout')
    newPart['gitName'].append('Adafruit-USB-C-Downstream-Breakout')
    newPart['eagleBoard'].append('/Adafruit USB Type C Downstream Breakout rev B.brd')
    newPart['eagleSchem'].append('/Adafruit USB Type C Downstream Breakout rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

