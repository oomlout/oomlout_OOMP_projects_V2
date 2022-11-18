
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17984"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17984"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IOTA ARTIC R2 Module')
    newPart['gitRepo'].append('https://github.com/sparkfun/IOTA-ARTIC-R2-Module')
    newPart['gitName'].append('IOTA-ARTIC-R2-Module')
    newPart['eagleBoard'].append('/Hardware/ARTIC_R2_Module.brd')
    newPart['eagleSchem'].append('/Hardware/ARTIC_R2_Module.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

