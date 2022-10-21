
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8276"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8276"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('XBee Module Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/XBee_Module_Breakout_Board')
    newPart['gitName'].append('XBee_Module_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_XBee-Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_XBee-Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

