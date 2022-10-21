
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12935"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12935"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FTDI SmartBasic')
    newPart['gitRepo'].append('https://github.com/sparkfun/FTDI_SmartBasic')
    newPart['gitName'].append('FTDI_SmartBasic')
    newPart['eagleBoard'].append('/Hardware/FTDI_SmartBasic.brd')
    newPart['eagleSchem'].append('/Hardware/FTDI_SmartBasic.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

