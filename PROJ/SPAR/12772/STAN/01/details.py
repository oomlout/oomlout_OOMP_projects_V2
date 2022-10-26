
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12772"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12772"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Logomatic')
    newPart['gitRepo'].append('https://github.com/sparkfun/Logomatic')
    newPart['gitName'].append('Logomatic')
    newPart['eagleBoard'].append('/Hardware/Logomatic.brd')
    newPart['eagleSchem'].append('/Hardware/Logomatic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

