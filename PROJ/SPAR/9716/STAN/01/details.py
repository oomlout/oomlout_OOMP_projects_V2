
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FTDI Basic Breakout 5V')
    newPart['gitRepo'].append('https://github.com/sparkfun/FTDI_Basic_Breakout-5V')
    newPart['gitName'].append('FTDI_Basic_Breakout-5V')
    newPart['eagleBoard'].append('/Hardware/FTDI Basic-5V.brd')
    newPart['eagleSchem'].append('/Hardware/FTDI Basic-5V.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

