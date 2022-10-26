
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12859"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12859"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Big Easy Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Big_Easy_Driver')
    newPart['gitName'].append('Big_Easy_Driver')
    newPart['eagleBoard'].append('/Hardware/BigEasyDriver.brd')
    newPart['eagleSchem'].append('/Hardware/BigEasyDriver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

