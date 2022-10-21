
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12941"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12941"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SD MMC Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SD-MMC_Breakout')
    newPart['gitName'].append('SD-MMC_Breakout')
    newPart['eagleBoard'].append('/Hardware/SD_MMC Breakout-v20.brd')
    newPart['eagleSchem'].append('/Hardware/SD_MMC Breakout-v20.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

