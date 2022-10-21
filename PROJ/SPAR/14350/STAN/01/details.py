
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14350"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14350"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('APDS 9301 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/APDS-9301_Breakout')
    newPart['gitName'].append('APDS-9301_Breakout')
    newPart['eagleBoard'].append('/Hardware/APDS-9301_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/APDS-9301_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

