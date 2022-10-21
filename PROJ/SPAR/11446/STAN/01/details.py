
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11446"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11446"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL362 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL362_Breakout')
    newPart['gitName'].append('ADXL362_Breakout')
    newPart['eagleBoard'].append('/Hardware/ADXL362_BOB.brd')
    newPart['eagleSchem'].append('/Hardware/ADXL362_BOB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

