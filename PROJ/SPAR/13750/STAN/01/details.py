
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13750"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13750"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GPS Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/GPS_Shield')
    newPart['gitName'].append('GPS_Shield')
    newPart['eagleBoard'].append('/Hardware/GPS_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/GPS_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

