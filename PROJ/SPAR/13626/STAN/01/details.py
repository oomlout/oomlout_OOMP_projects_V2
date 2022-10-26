
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13626"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13626"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon Battery Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_Battery_Shield')
    newPart['gitName'].append('Photon_Battery_Shield')
    newPart['eagleBoard'].append('/Hardware/Photon Battery Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Photon Battery Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

