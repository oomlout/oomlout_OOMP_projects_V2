
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13041"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13041"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Edison Micro SD Block')
    newPart['gitRepo'].append('https://github.com/sparkfun/Edison_Micro_SD_Block')
    newPart['gitName'].append('Edison_Micro_SD_Block')
    newPart['eagleBoard'].append('/Hardware/Micro_SD_Block.brd')
    newPart['eagleSchem'].append('/Hardware/Micro_SD_Block.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

