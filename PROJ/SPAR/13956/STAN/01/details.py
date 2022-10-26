
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13956"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13956"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Weather Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Weather_Shield')
    newPart['gitName'].append('Weather_Shield')
    newPart['eagleBoard'].append('/Hardware/Weather Shield_V12.brd')
    newPart['eagleSchem'].append('/Hardware/Weather Shield_V12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

