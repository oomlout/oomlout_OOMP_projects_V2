
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14048"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14048"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TeensyView')
    newPart['gitRepo'].append('https://github.com/sparkfun/TeensyView')
    newPart['gitName'].append('TeensyView')
    newPart['eagleBoard'].append('/Hardware/TeensyView.brd')
    newPart['eagleSchem'].append('/Hardware/TeensyView.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

