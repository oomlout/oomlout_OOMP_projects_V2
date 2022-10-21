
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9170"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9170"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Touch Screen Connector Breakout Nintendo DS')
    newPart['gitRepo'].append('https://github.com/sparkfun/Touch_Screen_Connector_Breakout-Nintendo_DS')
    newPart['gitName'].append('Touch_Screen_Connector_Breakout-Nintendo_DS')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Touch_Screen_Connector_Breakout_DS.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Touch_Screen_Connector_Breakout_DS.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

