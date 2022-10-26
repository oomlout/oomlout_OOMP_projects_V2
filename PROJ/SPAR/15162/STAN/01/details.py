
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15162"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15162"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator bit')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_bit')
    newPart['gitName'].append('gator_bit')
    newPart['eagleBoard'].append('/Hardware/gator-bit.brd')
    newPart['eagleSchem'].append('/Hardware/gator-bit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

