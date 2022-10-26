
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13144"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Touch Potentiometer')
    newPart['gitRepo'].append('https://github.com/sparkfun/Touch_Potentiometer')
    newPart['gitName'].append('Touch_Potentiometer')
    newPart['eagleBoard'].append('/Hardware/touch_pot.brd')
    newPart['eagleSchem'].append('/Hardware/touch_pot.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

