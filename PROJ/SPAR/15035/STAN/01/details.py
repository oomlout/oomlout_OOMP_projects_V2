
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15035"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15035"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ATX Power Connector Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ATX_Power_Connector_Breakout')
    newPart['gitName'].append('ATX_Power_Connector_Breakout')
    newPart['eagleBoard'].append('/Hardware/ATX_Power_Connector_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/ATX_Power_Connector_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

