
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3147"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3147"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FONA SIMCOM 3G Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FONA-SIMCOM-3G-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FONA-SIMCOM-3G-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit FONA SIM5320 3G Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit FONA SIM5320 3G Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

