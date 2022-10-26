
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13321"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon RedBoard')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_RedBoard')
    newPart['gitName'].append('Photon_RedBoard')
    newPart['eagleBoard'].append('/Hardware/sparkfun-photon-redboard.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-photon-redboard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

