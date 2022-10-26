
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11850"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11850"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('PicoBuck')
    newPart['gitRepo'].append('https://github.com/sparkfun/PicoBuck')
    newPart['gitName'].append('PicoBuck')
    newPart['eagleBoard'].append('/hardware/picoBuck.brd')
    newPart['eagleSchem'].append('/hardware/picoBuck.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

