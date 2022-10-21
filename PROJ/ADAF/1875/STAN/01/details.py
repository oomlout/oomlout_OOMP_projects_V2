
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1875"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1875"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TXB0104 Level Shifter Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TXB0104-Level-Shifter-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TXB0104-Level-Shifter-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit TXB0104.brd')
    newPart['eagleSchem'].append('/Adafruit TXB0104.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

