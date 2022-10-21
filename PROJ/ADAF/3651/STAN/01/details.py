
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3651"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3651"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 3.5in TFT Featherwing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-3.5in-TFT-Featherwing-PCB')
    newPart['gitName'].append('Adafruit-3.5in-TFT-Featherwing-PCB')
    newPart['eagleBoard'].append('/Adafruit 3.5in 480x320 FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit 3.5in 480x320 FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

