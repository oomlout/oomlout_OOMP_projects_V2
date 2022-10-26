
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11703"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11703"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('UDB5')
    newPart['gitRepo'].append('https://github.com/sparkfun/UDB5')
    newPart['gitName'].append('UDB5')
    newPart['eagleBoard'].append('/hardware/UDB5.brd')
    newPart['eagleSchem'].append('/hardware/UDB5.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

