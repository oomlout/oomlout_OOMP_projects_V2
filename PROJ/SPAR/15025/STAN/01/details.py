
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15025"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15025"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('nRF52840 Breakout MDBT50Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/nRF52840_Breakout_MDBT50Q')
    newPart['gitName'].append('nRF52840_Breakout_MDBT50Q')
    newPart['eagleBoard'].append('/Hardware/nrf52840-breakout-mdbt50q.brd')
    newPart['eagleSchem'].append('/Hardware/nrf52840-breakout-mdbt50q.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

