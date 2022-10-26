
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15269"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15269"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator environment')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_environment')
    newPart['gitName'].append('gator_environment')
    newPart['eagleBoard'].append('/Hardware/Gator_Environment.brd')
    newPart['eagleSchem'].append('/Hardware/Gator_Environment.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

