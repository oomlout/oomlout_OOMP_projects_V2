
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12069"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12069"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('H2OhNo')
    newPart['gitRepo'].append('https://github.com/sparkfun/H2OhNo')
    newPart['gitName'].append('H2OhNo')
    newPart['eagleBoard'].append('/hardware/H2OhNo.brd')
    newPart['eagleSchem'].append('/hardware/H2OhNo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

