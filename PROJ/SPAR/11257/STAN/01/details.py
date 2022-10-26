
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11257"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11257"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mr.Roboto')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mr.Roboto')
    newPart['gitName'].append('Mr.Roboto')
    newPart['eagleBoard'].append('/Hardware/MrRoboto.brd')
    newPart['eagleSchem'].append('/Hardware/MrRoboto.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

