
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12803"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12803"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL377 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL377_Breakout')
    newPart['gitName'].append('ADXL377_Breakout')
    newPart['eagleBoard'].append('/hardware/ADXL377 Breakout.brd')
    newPart['eagleSchem'].append('/hardware/ADXL377 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

