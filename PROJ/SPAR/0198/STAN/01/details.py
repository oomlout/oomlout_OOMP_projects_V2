
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0198"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0198"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('CP2102 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/CP2102_Breakout')
    newPart['gitName'].append('CP2102_Breakout')
    newPart['eagleBoard'].append('/Hardware/CP2102 USB to Serial Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/CP2102 USB to Serial Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

