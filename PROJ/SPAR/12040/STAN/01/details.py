
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12040"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12040"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('INA169 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/INA169_Breakout')
    newPart['gitName'].append('INA169_Breakout')
    newPart['eagleBoard'].append('/Hardware/INA169_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/INA169_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

