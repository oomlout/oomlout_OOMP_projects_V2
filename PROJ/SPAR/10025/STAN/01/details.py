
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10025"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10025"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('EiBotBoard')
    newPart['gitRepo'].append('https://github.com/sparkfun/EiBotBoard')
    newPart['gitName'].append('EiBotBoard')
    newPart['eagleBoard'].append('/Hardware/EiBotBoard-v23.brd')
    newPart['eagleSchem'].append('/Hardware/EiBotBoard-v23.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

