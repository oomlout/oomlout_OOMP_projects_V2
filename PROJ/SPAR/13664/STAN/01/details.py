
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13664"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13664"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SAMD21 Mini Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SAMD21_Mini_Breakout')
    newPart['gitName'].append('SAMD21_Mini_Breakout')
    newPart['eagleBoard'].append('/Hardware/sparkfun-samd21-mini-breakout.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-samd21-mini-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

