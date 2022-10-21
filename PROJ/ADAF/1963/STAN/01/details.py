
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1963"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1963"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FONA 800 GSM Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FONA-800-GSM-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FONA-800-GSM-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit-FONA-800-GSM-Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit-FONA-800-GSM-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

