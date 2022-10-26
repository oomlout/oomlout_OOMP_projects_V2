
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12670"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12670"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MAG3110 Breakout Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MAG3110_Breakout_Board')
    newPart['gitName'].append('MAG3110_Breakout_Board')
    newPart['eagleBoard'].append('/Hardware/MAG3110_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/MAG3110_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

