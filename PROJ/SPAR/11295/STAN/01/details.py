
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11295"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11295"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('HIH6130 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/HIH6130_Breakout')
    newPart['gitName'].append('HIH6130_Breakout')
    newPart['eagleBoard'].append('/Hardware/HIH6130_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/HIH6130_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

