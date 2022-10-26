
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13990"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13990"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('nRF52832 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/nRF52832_Breakout')
    newPart['gitName'].append('nRF52832_Breakout')
    newPart['eagleBoard'].append('/Hardware/sparkfun-nrf52832-breakout.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-nrf52832-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

