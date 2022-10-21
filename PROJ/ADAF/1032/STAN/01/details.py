
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1032"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1032"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit L3GD20 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-L3GD20-Breakout-PCB')
    newPart['gitName'].append('Adafruit-L3GD20-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit L3GD20H Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit L3GD20H Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

