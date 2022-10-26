
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13684"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13684"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MyoWare Power Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/MyoWare_Power_Shield')
    newPart['gitName'].append('MyoWare_Power_Shield')
    newPart['eagleBoard'].append('/Hardware/MyoWare_Power_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/MyoWare_Power_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

