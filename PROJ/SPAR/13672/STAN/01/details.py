
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13672"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13672"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SAMD21 Dev Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SAMD21_Dev_Breakout')
    newPart['gitName'].append('SAMD21_Dev_Breakout')
    newPart['eagleBoard'].append('/Hardware/sparkfun-samd21-pro-breakout.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-samd21-pro-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

