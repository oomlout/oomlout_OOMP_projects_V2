
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10914"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10914"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Arduino Pro 328')
    newPart['gitRepo'].append('https://github.com/sparkfun/Arduino_Pro_328')
    newPart['gitName'].append('Arduino_Pro_328')
    newPart['eagleBoard'].append('/Hardware/Arduino-Pro-v16.brd')
    newPart['eagleSchem'].append('/Hardware/Arduino-Pro-v16.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

