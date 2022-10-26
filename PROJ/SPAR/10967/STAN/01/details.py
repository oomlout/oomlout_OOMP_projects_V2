
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10967"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10967"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('NCP1402 3.3V')
    newPart['gitRepo'].append('https://github.com/sparkfun/NCP1402-3.3V')
    newPart['gitName'].append('NCP1402-3.3V')
    newPart['eagleBoard'].append('/Hardware/NCP1402_3.3V_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/NCP1402_3.3V_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

