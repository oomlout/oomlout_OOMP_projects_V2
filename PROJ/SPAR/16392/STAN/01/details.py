
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16392"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16392"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Configurable RC Filter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Configurable_RC_Filter')
    newPart['gitName'].append('Configurable_RC_Filter')
    newPart['eagleBoard'].append('/Hardware/Configurable_RC_Filter.brd')
    newPart['eagleSchem'].append('/Hardware/Configurable_RC_Filter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

