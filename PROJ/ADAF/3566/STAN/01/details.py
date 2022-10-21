
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3566"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CCS811 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CCS811-Breakout-PCB')
    newPart['gitName'].append('Adafruit-CCS811-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit CCS811 STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit CCS811 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

