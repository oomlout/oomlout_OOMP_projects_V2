
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2019"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2019"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MMA8451 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MMA8451-Breakout-PCB')
    newPart['gitName'].append('Adafruit-MMA8451-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit MMA8451.brd')
    newPart['eagleSchem'].append('/Adafruit MMA8451.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

