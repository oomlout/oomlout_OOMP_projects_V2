
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13712"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13712"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('OpenLog')
    newPart['gitRepo'].append('https://github.com/sparkfun/OpenLog')
    newPart['gitName'].append('OpenLog')
    newPart['eagleBoard'].append('/hardware/OpenLog.brd')
    newPart['eagleSchem'].append('/hardware/OpenLog.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

