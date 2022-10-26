
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14877"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14877"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Flashlight')
    newPart['gitRepo'].append('https://github.com/sparkfun/Flashlight')
    newPart['gitName'].append('Flashlight')
    newPart['eagleBoard'].append('/Hardware/Flashlight.brd')
    newPart['eagleSchem'].append('/Hardware/Flashlight.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

