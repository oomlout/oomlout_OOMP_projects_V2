
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11645"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11645"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpenSegment')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpenSegment')
    newPart['gitName'].append('OpenSegment')
    newPart['eagleBoard'].append('/Hardware/OpenSegment.brd')
    newPart['eagleSchem'].append('/Hardware/OpenSegment.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

