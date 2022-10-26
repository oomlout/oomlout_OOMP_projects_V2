
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9565"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9565"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Through Hole Christmas Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Through-Hole_Christmas_Kit')
    newPart['gitName'].append('Through-Hole_Christmas_Kit')
    newPart['eagleBoard'].append('/Hardware/Christmas_Kit.brd')
    newPart['eagleSchem'].append('/Hardware/Christmas_Kit.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

