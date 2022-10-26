
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13067"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13067"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MiP Proto Pack')
    newPart['gitRepo'].append('https://github.com/sparkfun/MiP_Proto-Pack')
    newPart['gitName'].append('MiP_Proto-Pack')
    newPart['eagleBoard'].append('/Hardware/MiP_Proto-Pack.brd')
    newPart['eagleSchem'].append('/Hardware/MiP_Proto-Pack.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

