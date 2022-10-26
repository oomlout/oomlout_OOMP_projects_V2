
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11007"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11007"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mega Pro')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mega_Pro')
    newPart['gitName'].append('Mega_Pro')
    newPart['eagleBoard'].append('/Hardware/mega_pro-v13.brd')
    newPart['eagleSchem'].append('/Hardware/mega_pro-v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

