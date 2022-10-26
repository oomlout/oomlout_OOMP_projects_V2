
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14002"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14002"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('THAT 1206 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/THAT_1206_Breakout')
    newPart['gitName'].append('THAT_1206_Breakout')
    newPart['eagleBoard'].append('/Hardware/THAT_1206_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/THAT_1206_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

