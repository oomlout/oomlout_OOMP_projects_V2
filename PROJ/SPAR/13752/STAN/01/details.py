
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13752"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13752"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('L6470 AutoDriver')
    newPart['gitRepo'].append('https://github.com/sparkfun/L6470-AutoDriver')
    newPart['gitName'].append('L6470-AutoDriver')
    newPart['eagleBoard'].append('/Hardware/L6470 AutoDriver.brd')
    newPart['eagleSchem'].append('/Hardware/L6470 AutoDriver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

