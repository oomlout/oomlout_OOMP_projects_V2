
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12779"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12779"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Easy Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Easy_Driver')
    newPart['gitName'].append('Easy_Driver')
    newPart['eagleBoard'].append('/Hardware/EasyDriver_v45.brd')
    newPart['eagleSchem'].append('/Hardware/EasyDriver_v45.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

