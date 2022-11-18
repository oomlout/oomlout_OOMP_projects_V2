
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14892"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14892"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ePaper')
    newPart['gitRepo'].append('https://github.com/sparkfun/ePaper')
    newPart['gitName'].append('ePaper')
    newPart['eagleBoard'].append('/1.54in display/hardware/1.54in.brd')
    newPart['eagleSchem'].append('/1.54in display/hardware/1.54in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

