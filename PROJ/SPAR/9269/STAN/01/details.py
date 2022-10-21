
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9269"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9269"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL335 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL335_Breakout')
    newPart['gitName'].append('ADXL335_Breakout')
    newPart['eagleBoard'].append('/Hardware/ADXL335_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/ADXL335_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

